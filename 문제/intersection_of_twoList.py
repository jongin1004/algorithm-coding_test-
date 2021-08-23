list1 = [4, 9, 4]
list2 = [4, 9, 4, 9, 2]
result = []  # 결과 담을 리스트

if len(list1) >= len(list2):  # 두 리스트중에서 짧은 것을 기준으로 비교하기 위해
    standardList = list2
    restList = list1
else:
    standardList = list1
    restList = list2

for num in standardList:  # 길이가 짧은 리스트의 원소를 하나씩 꺼내어 for문
    if num in restList:  # 길이가 긴 리스트에 해당 원소가 존재 할 때
        result.append(num)  # 결과 리스트에 해당 num을 추가
        restList.remove(num)  # 리스트에서는 해당 num을 삭제(remove)

print(result)
