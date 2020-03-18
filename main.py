# import keyboard

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
**ช่วยคิดหน่อย ใส่ and กี่ตัวก็ได้นะไม่จำเป็นต้อง 2
    ================== กฏทั้งหมด ==================
    if orange and circle Then orange *
    if yellow and long Then banana *
    if red and circle Then apple *
    if yellow and circle Then durian * ดอกจันคือ เอาไปเพิ่มในโค้ดแล้ว

************ Code น่าจะเสร็จแล้ว กำลังคิดอยู่ว่ามันเก็บค่าที่ซ้ำไว้ใน BlackBoard ไหม

    สี+ลักษณะ+เป็นพวงหรือลูกเดียว+รสชาติ
(ทำให้เป็นแพทเทิลนี้) !!!
Bitter - ขม
Sweet - หวาน
Tart - เปรี้ยว
Sweet Sour เปรี้ยวอมหวาน
Sour - เปรี้ยว (ในแง่ลบ)
Mild - รสไม่จัด 
Bland / Tasteless - จืด (ในแง่ลบ)
Bunch -พวง
Acerbic คือรสชาติที่มีความเปรี้ยวอมฝาด คำนี้น่าจะเหมาะกับผลไม้ไทยหลายชนิดนะคะ อย่างเช่นมะยม หรือมะขามป้อมเป็นต้นค่ะ
Mature ส่วนมากที่เคยได้ยินกันจะแปลว่าเป็นผู้ใหญ่ใช่ไหมคะ แต่พอมาใช้กับรสชาติ Mature แปลว่า รสชาติที่สุกงอม พร้อมรับประทานแล้ว เหมือนกับ ผลไม้ที่สุกเต็มที่พร้อมรับประทานแล้วนั่นเองค่ะ
Stone fruit ผลไม้ที่มีเปลือกแข็ง เช่นลูกพลัมหรือลูกพีช
SphereSphere = ทรงกลม
'''
Knowledge = [
    'if orange and Sphere and Single and Sour Then OrangeFruit', \
    'if yellow and long and Bland and Sweet Then banana', \
    'if red and Sphere and Single and Sweet Then apple', \
    'if yellow and Barbed and Single and Sweet Then durian', \
    'if purple and Sphere and Bunch and Sweet Then grape', \
    'if brown and Hairy and Single and SweetSour Then kiwi', \
    'if yellow and Oval and Single and Sour Then lemon', \
    'if PinkToRed and Oval and Bunch and Sweet Then lychee', \
    'if green and Oval and Single and Sweet Then mango', \
    'if green and PatternedSphere and Single and sweet Then melon', \
    'if pink and Sphere and Single and Sweet Sour Then peach', \
    'if yellow and Oval and Single and Sweet Then Pear', \
    'if yellow and Oval and Single and SweetSour Then pineapple', \
    'if red and Triangle and Single and SweetSour Then strawberry', \
    'if red and Sphere and Single and Sour Then tomato', \
    'if red and Sphere and Bunch and Sour Then cherry', \
    'if while and Sphere and Single and Bland Then coconut', \
    'if yellow and Long and Single and Sweet Then corn', \
    'if green and Oval and Single and Bland Then avocado', \
    'if blue and Sphere and Bunch and Sour Then blueberry', \
    'if brown and Sphere and Single and  Bunch Then Chestnut', \
    'if yellow and Sphere and Single and Sweet Then ChinesePear', \
    'if pink and Sphere and Single and Sweet Then DragonFruit', \
    'if red and Oval and Bunch and Sour Then GojiBerry', \
    'if green and Sphere and Single and Bland Then guava', \
    'if yellow and Oval and Single and Sweet Then jackfruit', \
    'if purple and Sphere and Single and SweetSour Then mangosteen', \
    'if orange and long and Single and Sweet Then papaya', \
    'if red and Hairy and Bunch and Sweet Then rambutan', \
    'if red and Small and Bunch and Sour Then raspberry', \
    'if brown and HardShell and Single and Bunch Then Acorn', \
    'if orange and Sphere and Single and Sweet Then Cantaloupe', \
    'if Green and Rough and Single and Sweet Then CustardApple', \
    'if red and Oval and Bunch and Sweet Then Jujube', \
    'if yellow and Sphere and Single and Sour Then Lime', \
    'if brown and circle and Bunch and Sweet Then Longan', \
    'if brown and circle and Bunch and SweetSour Then Longong', \
    'if Sour and circle and Bunch and Sour Then MaFai', \
    'if Green and Oval and Single and Sour Then Madan', \
    'if purple and Sphere and Single and Sweet Then MariamPlum', \
    'if purple and Rugged and Bunch and SweetSour Then Mulberry', \
    'if yellow and Oval and Single and Sweet Then muskmelon', \
    'if yellow and Sphere and Bunch and Sweet Then langsat', \
    'if red and Sphere and Single and SweetSour Then pomegranate', \
    'if green and Sphere and Single and SweetSour Then pomelo', \
    'if purple and Sphere and Bunch and Sour Then prune', \
    'if black and Granular and Bunch and SweetSour Then raisins', \
    'if red and BellShape and Bunch and Sweet Then rose apple', \
    'if redbrown and Barbed and Bunch and SweetSour Then salak', \
    'if green and Translucent and Single and SweetSour Then StarGooseberry', \
    'if red and Sphere and Single and Sweet Then Watermelon', \
    'if brown and StoneFruit and Bunch and SweetSour Then tamarind', \
    'if green and Sphere and Single and Bland Then Breadfruit', \
    'if yellow and Oval and Single and Bland Then potato', \
    'if purple and Oval and Single and Bland Then taro', \
    'if yellow and Sphere and Single and Sweet Then Quince']

'''
สี+ลักษณะ+รสชาติ+เป็นพวงหรือลูก+
(ทำให้เป็นแพทเทิลนี้)
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

print("Enter fact (ex. yellow long): ")
input_fact_txt = input()  # ขึ้นให้ป้อนข้อมูล เก็บไว้ในตัวแปรชื่อ input_fact_txt

if input_fact_txt != "":  # ถ้าผู้ใช้ป้อนข้อมูล
    inputdata = input_fact_txt.split()
    for data in inputdata:
        BlackBoard.append(data)
else:  # ถ้าผู้ใช้ไม่ป้อนข้อมูล
    input_fact = False

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
# main LOOP
for rule in KB:
    lengthRule = len(rule) - 1
    numPremise = 0
    for premise in rule[0:lengthRule]:
        if premise not in notin:
            numPremise = numPremise + 1
            if premise in BlackBoard:
                premiseinBB = True
                if premiseRemain(numPremise) == False:
                    for p1 in rule:
                        BlackBoard.append(p1)
            else:
                if premise in StartingNode:
                    print(str(premise) + " ? (y = yes, n = No)")
                    response = input()
                    if str(response) == "y":
                        if premiseRemain(numPremise) == False:
                            for p2 in rule:
                                BlackBoard.append(p2)
                    else:
                        notin.append(premise)
                        break
        else:
            break

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
                concludTxt = concludTxt + con + " and "
                count = count + 1
            else:

                concludTxt = concludTxt + con + "."
    else:
        for con in Concluding:
            concludTxt = concludTxt + con + "."
    print("It's " + str(concludTxt))
else:
    print("No Answer")

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



