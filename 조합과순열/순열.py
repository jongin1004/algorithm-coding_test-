#순열 : 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것 
from itertools import permutations

data = ['A', 'B', 'C'] 

result = list(permutations(data, 3 ))
print(result, len(result))