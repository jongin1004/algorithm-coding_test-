rest_money = int(input())
count = 0
money_unit = [500, 100, 50, 10]

for unit in money_unit :
    count += rest_money // unit 
    rest_money %= unit

print(count)
