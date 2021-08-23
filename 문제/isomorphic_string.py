s, t = input().split()
ismorphic = {}  # dict 선언
count = 0  # 조건을 만족했을 경우 올려줄 카운터 초기화


if len(s) == len(t):  # 두 문자열의 길이가 같은지 확인
    for i in range(len(s)):  # 두 문자열중 아무거나 선택 후 for문
        if s[i] not in ismorphic:  # dict에 s[i] 문자의 key가 없을 때
            ismorphic[s[i]] = t[i]  # s[i]를 키 값으로  , t[i]를 value 값 저장
            count += 1  # ismorphic에 만족하는 조건이므로 count ++

        else:
            if ismorphic[s[i]] != t[i]:  # dict에 s[i] 문자의 key가 있는데, 그 value값이 일치하지 않을 때
                break  # ismorphic를 만족 못하므로 바로 for문을 break

            else:
                count += 1  # dict에 s[i] 문자의 key가 있는데, 그 value값이 일치할 때 count ++


if count == len(s):  # count수가 문자열의 길이와 같음면, 모든 문자가 ismorphic 조건을 만족
    result = "true"
else:
    result = "false"

print(result)
