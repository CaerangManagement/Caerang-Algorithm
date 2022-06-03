N = int(input())

card = []

abandon = []
index = 0
for i in range(1, N+1):
    card.append(i)

while len(card) != 1:


    abandon.append(card[0]) #제일 위에 있는 카드 리스트에서 삭제전 abandon 에 저장
    card.remove(abandon[index]) # 제일 위에 있는 카드 리스트에서 삭제
    index = index + 1 # 버린 카드 리스트 abandon 인덱스를 증가
    card.append(card[0]) # 카드 리스트의 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
    card.remove(card[0])# 카드 리스트의 제일 위에 있는 카드를 삭제

for i in abandon: #출력 
    print(i, end=" ")
print(card[0],end='')