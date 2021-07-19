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