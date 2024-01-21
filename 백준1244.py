'''
여러줄 프린트시 print( ,end = " ")
'''
def men_simulation(number : int) :
    global switches
    global N

    numbers = []
    for i in range(1, N + 1)  :
        if i % number == 0 :
            numbers.append(i)

    change_switch(numbers)

def woemn_simulation(number : int) :
    global switches
    global N

    left_index = number
    right_index = number

    while True :
        if left_index - 1 < 1 :
            break
        if right_index + 1> N :
            break

        if switches[left_index - 1] != switches[right_index + 1] :
            break

        left_index -= 1
        right_index += 1

    numbers = []
    for number in range(left_index, right_index + 1) :
        numbers.append(number)
    
    change_switch(numbers)

def change_switch(numbers) :
    global switches

    for number in numbers :
        if switches[number] == 1 :
            switches[number] = 0
            continue
        if switches[number] == 0 :
            switches[number] = 1

# 1 <= 스위치 개수 <= 100
N = int(input())
# 켜짐 : 1, 꺼짐 : 0
switches = list(map(int, input().split(" ")))
switches.insert(0, -1)
# 1 <= 학생수 <= 100
M = int(input())
students = []
# 성별, 학생이 받은 수
for i in range(M) :
    students.append(list(map(int, input().split(" "))))

# 남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꿈
# 여학생은
for student in students :
    sex = student[0]
    number = student[1]
    # 남자의 경우
    if sex == 1 :
        men_simulation(number)
        continue
    if sex == 2 :
        woemn_simulation(number)

# 출력
for i in range(1 , N + 1) :
    print(switches[i], end = " ")
    if i % 20 == 0 :
        print()