#연습 90번
#+123, -2같은 걸 입력했을 때, 정수인지 아닌지 판별하는 함수를 입력하는 것이 문제의 목적
#그럼 0번째 부분은 생략하자. 나머지는 int로 바꿔서 판별하면 되는거 아닌가?
#그리고 type으로 다시 확인을 굳이 해야하나 싶기도 한데.

def isIntger(text):
    string=text
    fact=True
    if string[0]=="+" or string[0]=="-":
        for i in range(1,len(string)): 
            print(i)
            if string[i] !=int(i):
                fact=False
                break
            fact=True
    return fact
text=input()
fact=isIntger(text)
if fact=="True":
    print("{}는 정수가 맞습니다.".format(text))
else:
    print("{}는 정수가 아닙니다.".format(text))


#연습 91번