import keyboard

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
KB = [["orange", "circle", "Orange"], \
      ["yellow", "long", "banana"], \
      ["red", "circle", "apple"], \
      ["yellow", "strong smell", "durian"]]
# ------------------------------------- ข้างงบนเป็น Code
'''
**ช่วยคิดหน่อย ใส่ and กี่ตัวก็ได้นะไม่จำเป็นต้อง 2
    ================== กฏทั้งหมด ==================
    if orange and circle Then orange *
    if yellow and long Then banana *
    if red and circle Then apple *
    if yellow and circle Then durian * ดอกจันคือ เอาไปเพิ่มในโค้ดแล้ว

    สี+ลักษณะ+เป็นพวงหรือลูกเดียว+รสชาติ
(ทำให้เป็นแพทเทิลนี้) !!!
Bitter - ขม
Sweet - หวาน
Tart - เปรี้ยว
Sweet and Sour เปรี้ยวอมหวาน
Sour - เปรี้ยว (ในแง่ลบ)
Mild - รสไม่จัด 
Bland / Tasteless - จืด (ในแง่ลบ)
Bunch -พวง
Acerbic คือรสชาติที่มีความเปรี้ยวอมฝาด คำนี้น่าจะเหมาะกับผลไม้ไทยหลายชนิดนะคะ อย่างเช่นมะยม หรือมะขามป้อมเป็นต้นค่ะ
Mature ส่วนมากที่เคยได้ยินกันจะแปลว่าเป็นผู้ใหญ่ใช่ไหมคะ แต่พอมาใช้กับรสชาติ Mature แปลว่า รสชาติที่สุกงอม พร้อมรับประทานแล้ว เหมือนกับ ผลไม้ที่สุกเต็มที่พร้อมรับประทานแล้วนั่นเองค่ะ
stone fruit ผลไม้ที่มีเปลือกแข็ง เช่นลูกพลัมหรือลูกพีช


    if purple and circle and Bunch and Sweet Then grape
    if brown and Hairy and Single and Sweet and Sour Then kiwi
    if yellow and Oval and Single and Sour Then lemon
    if and Then lychee
    if and Then mango
    if and Then melon
    if and Then peach
    if and Then Pear
    if yellow and Then pineapple
    if red and Then strawberry
    if and Then tomato
    if and Then taro
    if and Then cherry
    if and Then coconut
    if and Then corn
    if and Then avocado
    if and Then blackberry
    if and Then blueberry
    if and Then Chestnut
    if and Then Chinese pear
    if and Then Dragon fruit
    if and Then goji berry
    if and Then guava
    if and Then jackfruit
    if and Then mangosteen
    if and Then papaya
    if and Then rambutan
    if and Then raspberry
    if and Then Acorn
    if and Then Alder berry
    if and Then Cantaloupe
    if and Then Custard apple
    if and Then Jujube
    if and Then Lime
    if and Then Longan 
    if and Then Longong
    if and Then Ma Fai 
    if and Then Madan
    if and Then Manila tamarind
    if and Then Mariam plum
    if and Then Mulberry
    if and Then muskmelon
    if and Then langsat
    if and Then pomegranate
    if and Then pomelo
    if and Then prune
    if and Then raisins
    if and Then rose apple
    if and Then salak
    if and Then Star gooseberry
    if and Then Waive
    if and Then Watermelon
    if and Then tamarind
    if and Then Alder berry
    if and Then Breadfruit
    if and Then potato
    if and Then taro
    if and Then Quince
    if and Then
    if and Then
    if and Then
    if and Then
    if and Then
    if and Then
    if and Then
    if and Then
    if and Then

สี+ลักษณะ+รสชาติ+เป็นพวงหรือลูก+
(ทำให้เป็นแพทเทิลนี้)
'''
BlackBoard = []
StartingNode = []
TherminalNode = []


def add_fact_to_BB(fact):
    BlackBoard.append(fact)


# Get fact From user
while input_fact:
    print('Enter fact:')
    input_fact_txt = input()  # ขึ้นให้ป้อนข้อมูล เก็บไว้ในตัวแปรชื่อ input_fact_txt

    if input_fact_txt != "":  # ถ้าผู้ใช้ป้อนข้อมูล

        print('Have another fact ? (Y = yes,N = no)')
        # if keyboard.is_pressed('y'): # เช็คว่ากด Y ไหม ต้องเทสใน Pycharm !!
        #  input_fact = True
        # else:
        #  input_fact = False
        if input() == "y":
            input_fact = True
        else:
            input_fact = False

        add_fact_to_BB(input_fact_txt)
    else:  # ถ้าผู้ใช้ไม่ป้อนข้อมูล
        input_fact = False

# เก็บ TherminalNode ไว้ในตัวแปร ปล.ยังไม่ได้แยกเอา intermidiant Node ออก
for ther in KB:
    TherminalNode.append(ther[len(ther) - 1])
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
                TherminalNode.remove(str(a[check]))  # ลบตัวที่เป็น intermidiant node ออกจาก therminalnode

        if inThen == 0:  # ถ้าไม่ตรงกับใน then เลย
            StartingNode.append(a[check])  # เพิ่ม a ตัวที่ check ใน starting node
        inThen = 0  # reset ค่าใหม่ แล้วก็ลูปเช็คไปเรื่อยๆ
        check = check + 1  # เช็คตัวถัดไป


StartingNode = list(set(StartingNode)) # ลบตัวซ้ำ



def premiseRemain(numpr):
    pr2 = numpr

    if (int(lengthRule) - int(pr2)) == 0:
        status = False
    else:
        status = True
    return  status
numPremise = 0
# main LOOP
for rule in KB:
    lengthRule = len(rule)-1
    numPremise = 0
    for premise in rule[0:lengthRule]:
        numPremise = numPremise +1
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
                    break

for th in TherminalNode:
    for bbb in BlackBoard:
        if str(th) == str(bbb):
            Concluding.append(th)
if Concluding != []:
    print("It is "+str(Concluding))
else:
    print("No Answer")





#Rule Teacher

# Debug
if debug == True:
    print("BlackBoard = " + str(BlackBoard))
    print("StartingNode = " + str(StartingNode))
    print("TherminalNode = " + str(TherminalNode))
    print("ThenPart = " + str(ThenPart))



