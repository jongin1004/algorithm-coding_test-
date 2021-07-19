data = input()
num_sum = 0
string = ""

for i in data :
    if ord(i) >= 48 and ord(i) <= 57 :
        num_sum += int(i)
        continue

    string += i

string = sorted(string)
string = "".join(string)
print(string+str(num_sum))


#=================================

data = input()
result = []
value = 0

for x in data :
    if x.isalpha():
        result.append(x)

    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))