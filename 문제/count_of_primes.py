def isPrimes(x):  # 소수인지 검증하는 함수 선언
    for i in range(2, x):  # 2부터 x보다 작은 값까지 for문
        if x % i == 0:  # i값으로 x를 나눴을 때 딱 나뉘어 떨어지면, 소수가 아니므로 False 리턴
            return False

    return True


num = int(input())  # n을 입력 받음
primesList = []  # 소수를 넣을 리스트

for i in range(num-1, 1, -1):  # num이 2이하 일 때에는 for문이 0번 돌기 때문에 알아서, 소수 카운트는 0
    if isPrimes(i) == True:  # 소수일 떄
        primesList.append(i)  # 소수 리스트에추가

print(len(primesList))  # len함수로 리스트 count
