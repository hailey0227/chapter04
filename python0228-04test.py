#-*-coding:utf-8

# 연습문제 1
# def fib(n):
#     if n == 0
#     return 0
#     if n == 1
#     return 1

#     return fib

# for i 


# 연습문제 2
f = open("sample.txt", "r", encoding="utf8") # encoding="utf8" 쓰는 이유 : 현재 sample 파일은 숫자라서 필요없지만, 글자라면 필요할 수도 있다.
lines = f.readlines() # 파일을 한 줄 씩 모든
f.close()

total = 0
for line in lines:
    score = int(line) # 문자열 타입을 숫자형 타입으로 
    total += score

average = total / len(lines)

f = open("result.txt", "w")
f.write(str(average))
f.close()


# 연습문제3
# 파일을 열고, 메뉴에 따라서 파일의 내용을 확인하고 파일의 내용을 입력하는 형태의 프로그램을 작성하세요
# 파일명 : memory.txt
# 메뉴 | 1. 내용 입력 | 2. 내용 출력 | 3. 종료
# 내용 입력 시 기존 내용을 덮어쓰기하는 형태로 작성

while True:
    print("문제3) 메뉴 | 1. 내용 입력 | 2. 내용 출력 | 3. 종료")
    menu = input("몇 번? ")
    
    if menu == "1":
        f = open("result.txt", "w", encoding="utf8")
        content = input("내용을 입력하세요 : ")
        f.write(str(content))
        f.close()
    
    elif menu == "2":
        f = open("result.txt", "r", encoding="utf8")
        lines = f.readline()
        print(lines)
        f.close()
    
    elif menu == "3":
        print("종료")
        break
print()
# 연습문제4
# 위의 문제 3번을 함수를 이용하여 프로그램을 작성하세요
# 내용 입력 함수명 memoryWrite
# 내용 출력 함수명 memoryRead
# 다른 사항은 문제 3번과 동일

def memoryWrite():
    f = open("result.txt", "w", encoding="utf8")
    content = input("내용을 입력하세요 : ")
    f.write(str(content))
    f.close()

def memoryRead():
    f = open("result.txt", "r", encoding="utf8")
    lines = f.readline()
    print(lines)

while True:
    print("문제 4) 메뉴 | 1. 내용 입력 | 2. 내용 출력 | 3. 종료")
    menu = input("몇 번? ")
    
    if menu == "1":
        memoryWrite()
    elif menu == "2":
        memoryRead()
    elif menu == "3":
        print("종료")
        break


# 함수 (메서드)
# 입력을 받아 기능을 수행하고 결과값을 출력하는 것
# 매개변수 - 청소 작업 (필요도구) / 청소 수행
# 리턴값 - 작업 결과 보고

# 성적표 출력 함수를 사용하여 프로그램 제작
# 5점에 한단계식 낮아짐
# 95점 이상 A+, 90점 이상 A, ...
# 60점 미만은 F

  
