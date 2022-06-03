#+, -, *, /, (, )
a = input()
arr = []
str = ""
for i in a:
    if i == '(':                                #그냥 추가
        arr.append(i)
    elif i == ')':                              # 괄호 나올때까지 뺌
        while True:
            temp = arr.pop()
            if temp == '(':
                break
            else:
                str += temp
    elif i == '*' or i == '/':                  # 곱하기 나누기면 +-( 나올대 가지 뺌
        while True:
            if len(arr) == 0:
                arr.append(i)
                break
            temp = arr.pop()
            if temp == '+' or temp == '-' or temp == '(':
                arr.append(temp)
                arr.append(i)
                break
            else:
                str += temp
    elif i == '+' or i == '-':                  #+ - 이면 바닥이거나 괄호나올때 까지 뺌
        while True:
            if len(arr) == 0:
                arr.append(i)
                break
            temp = arr[len(arr)-1]
            if temp == '(':
                arr.append(i)
                break
            else:
                str += arr.pop()
    else:                                       #숫자이면 바로 후위식 추가
        str += i
for i in range(len(arr)):
    str += arr.pop()
    
print(str)