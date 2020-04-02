
print("")
print("")
print("   ██████╗    ██████╗     ███████╗")
print("  ██╔════╝    ██╔══██╗    ██╔════╝")
print("  ██║         ██████╔╝    █████╗  ")
print("  ██║         ██╔═══╝     ██╔══╝  ")
print("  ╚██████╗    ██║         ███████╗")
print("   ╚═════╝    ╚═╝         ╚══════╝")


print("")



# สร้างตัวแปร
global KB
global input_fact
global BlackBoard
global StartingNode
global TherminalNode
global inThen
global FireTheRule
global ThenPart
global Concluding

# กำหนดค่า

FireTheRule = False
debug = True
input_fact = True
inThen = 0
ThenPart = []
Concluding = []
# รูปแบบตัวแปรที่เก็บ เช่น if orange and circle Then orange
# จะเก็บในรูป ["orange", "circle", "orange"]
KB = []

# ------------------------------------- ข้างงบนเป็น Code
'''

'''
Knowledge = [
  'if ส่งเสียงร้องในลำคอ and กินแมลง Then กบ',\
  'if กบ Then มีสีเขียว',\
  'if ส่งเสียงร้องสูง and กินแมลง Then นกขมิ้น',\
  'if นกขมิ้น Then มีสีเหลือง',\
  'if มีงวง and มีงา Then ช้าง'\
  'if ช้าง Then กินพืช'\
  'if มีพิษ and สัตว์เลื้อยคลาน Then งู',\
  'if งู Then กินเนื้อ'\
  'if มีสีขาวดำ and ตัวเป็นลายทาง Then ม้าลาย',\
  'if ม้าลาย Then สัตว์บก',\
  'if มีหางยาวเหมือนสัตว์เลื้อยคลาน and ตัวผู้อุ้มท้อง Then ม้าน้ำ',\
  'if ม้าน้ำ Then สัตว์น้ำ',\
  'if ส่งเสียงเห่า and สัตว์เลี้ยง Then สุนัข',\
  'if สุนัข Then สัตว์ออกลูกเป็นตัว',\
  'if ส่งเสียงขัน and มีขน Then ไก่',\
  'if ไก่ Then สัตว์ออกลูกเป็นไข่'
 ]

'''

'''
BlackBoard = []
StartingNode = []
TherminalNode = []

# แปลง if and then เป็น code
for kn in Knowledge:
    # kn = kn.lower()
    if "if" or "and" or "Then" in kn:
        kn = kn.replace("if", "")
        kn = kn.replace("and", "")
        kn = kn.replace("Then", "")
    newkn = kn.split()
    KB.append(newkn)

# Get fact From user
print("")
print("=================================================")
print("ระบบ Expert System By CPE SWU ID: 165 491 492 508")
print("=================================================")
print("")
#print("กรุณาใส่รายละเอียดที่คุณเจอ (Problem Fact): ")
#input_fact_txt = input()  # ขึ้นให้ป้อนข้อมูล เก็บไว้ในตัวแปรชื่อ input_fact_txt
print("กรุณาใส่รายละเอียดที่คุณเจอ (Problem Fact) ")
print("ตัวอย่าง: กินแมลง ส่งเสียงร้องในลำคอ")
BlackBoard = [str(BlackBoard) for BlackBoard in input(">> ").split()]

if BlackBoard != "":  # ถ้าผู้ใช้ป้อนข้อมูล
    input_fact = False
'''if input_fact_txt != "":  # ถ้าผู้ใช้ป้อนข้อมูล
    inputdata = input_fact_txt.split()
    for data in inputdata:
        BlackBoard.append(data)
else:  # ถ้าผู้ใช้ไม่ป้อนข้อมูล
    input_fact = False
'''
# เก็บ TherminalNode ไว้ในตัวแปร ปล.ยังไม่ได้แยกเอา intermidiant Node ออก
for ther in KB:
    TherminalNode.append(str(ther[len(ther) - 1]))
    ThenPart.append(ther[len(ther) - 1])
# เก็บ Starting Node ไว้ในตัวแปร
# Starting node คือ ตัวที่ไม่อยู่ใน then

for a in KB:  # นำข้อมูล array ตัวแรก ของ array ใน KB มาเก็บไว้ใน a
    # ข้อมูลที่ได้คือ a มีค่า ['orange','circle','orange']
    len_a = len(a)
    check = 0
    while check < len_a - 1:
        for b in KB:  # นำข้อมูล array ตัวแรก ของ array ใน KB มาเก็บไว้ใน b
            # ข้อมูลที่ได้คือ b มีค่า ['orange','circle','orange']
            if (str(a[check]) == str(b[len(b) - 1])):  # ถ้า a ตัวที่ check ตรงกับ b ใน then part
                inThen = inThen + 1  # เพิ่มค่าตัวแปร inThen ให้เพิ่มขึ้น 1
                TherminalNode.remove(a[check])  # ลบตัวที่เป็น intermidiant node ออกจาก therminalnode

        if inThen == 0:  # ถ้าไม่ตรงกับใน then เลย
            StartingNode.append(a[check])  # เพิ่ม a ตัวที่ check ใน starting node
        inThen = 0  # reset ค่าใหม่ แล้วก็ลูปเช็คไปเรื่อยๆ
        check = check + 1  # เช็คตัวถัดไป

StartingNode = list(set(StartingNode))  # ลบตัวซ้ำ


def premiseRemain(numpr):
    pr2 = numpr

    if (int(lengthRule) - int(pr2)) == 0:
        status = False
    else:
        status = True
    return status


numPremise = 0
notin = []
skiprule = False
# main LOOP
for rule in KB:

    lengthRule = len(rule) - 1

    numPremise = 0
    for premise in rule[0:lengthRule]:

        numPremise = numPremise + 1
        if premise in BlackBoard:
            premiseinBB = True
            if premiseRemain(numPremise) == False:
                for p1 in rule:
                    if p1 not in BlackBoard:
                        BlackBoard.append(p1)
        else:
            if premise in StartingNode:
                print(str(premise) + " ? (y = yes, n = No)")
                response = input()
                if str(response) == "y":
                    if premiseRemain(numPremise) == False:
                        for p2 in rule:
                            if p2 not in BlackBoard:
                                BlackBoard.append(p2)
                else:

                    break
            else:

                break
    #else:
     #   break

for th in TherminalNode:
    for bbb in BlackBoard:
        if str(th) == str(bbb):
            Concluding.append(th)
concludTxt = ""
Concluding = list(set(Concluding))  # ลบตัวซ้ำ
count = 0
print(" ")
print(" ")
if Concluding != []:
    if len(Concluding) > 1:
        for con in Concluding:
            if count < len(Concluding) - 1:
                concludTxt = concludTxt + con + " และ "
                count = count + 1
            else:

                concludTxt = concludTxt + con + ""
    else:
        for con in Concluding:
            concludTxt = concludTxt + con + ""
    print("มันคือ " + str(concludTxt))
else:
    print("ไม่มีคำตอบ (ปัญหานี้ใช้ไม่ได้กับ KB นี้)")

# BlackBoard = list(set(BlackBoard)) # ลบตัวซ้ำ
print(" ")

print(" ")
# Rule Teacher

# Debug
if debug == True:
    print("--------------- > DEBUG Enable <-------------- ")
    print("BlackBoard = " + str(BlackBoard))
    print("StartingNode = " + str(StartingNode))
    print("TerminalNode = " + str(TherminalNode))
    print("ThenPart = " + str(ThenPart))



