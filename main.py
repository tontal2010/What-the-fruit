import keyboard

# สร้างตัวแปร
global KB
global not_END
global input_fact
global BlackBoard
global StartingNode
global inThen
# กำหนดค่า
not_END = True
input_fact = True
inThen = 0

# รูปแบบตัวแปรที่เก็บ เช่น if orange and circle Then orange
# จะเก็บในรูป ["orange", "circle", "orange"]
KB = [["orange", "circle", "Orange"], ["yellow", "long", "banana"], ["test", "oval", "yellow"]]

'''
**ช่วยคิดหน่อย
    ================== กฏทั้งหมด ==================
    if orange and circle Then orange
    if yellow and long Then banana
    if 

'''
BlackBoard = []
StartingNode = []


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

# เก็บ Starting Node ไว้ในตัวแปร
# Starting node คือ ตัวที่ไม่อยู่ใน then
for a in KB:  # นำข้อมูล array ตัวแรก ของ array ใน KB มาเก็บไว้ใน a
    # ข้อมูลที่ได้คือ a มีค่า ['orange','circle','orange']
    len_a = len(a)
    check = 0
    while check < len_a - 1:
        for b in KB:  # นำข้อมูล array ตัวแรก ของ array ใน KB มาเก็บไว้ใน b
            # ข้อมูลที่ได้คือ b มีค่า ['orange','circle','orange']
            print(str(a[check]) + " " + str(b[len(b) - 1]))  # แสดงข้อความเอาไว้ดู a[0] กับ b ตัวสุดท้าย
            if (str(a[check]) == str(b[len(b) - 1])):  # ถ้า a ตัวที่ check ตรงกับ b ใน then part
                inThen = inThen + 1  # เพิ่มค่าตัวแปร inThen ให้เพิ่มขึ้น 1
        if inThen == 0:  # ถ้าไม่ตรงกับใน then เลย
            StartingNode.append(a[check])  # เพิ่ม a ตัวที่ check ใน starting node
        inThen = 0  # reset ค่าใหม่ แล้วก็ลูปเช็คไปเรื่อยๆ
        check = check + 1  # เช็คตัวถัดไป

print(str(StartingNode))

print(len(KB))

# while not_END:
