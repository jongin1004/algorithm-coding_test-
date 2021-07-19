#조합 : 서로 다른 n개에서 순서와 상관없이 서로 다른 r 개를 선택하는 것 
#순서를 고려하지 않고 두개를 뽑는 경우 
from itertools import combinations

data = ['A', 'B', 'C']

result = list(combinations(data, 2))
print(result, len(result))