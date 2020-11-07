from itertools import combinations, combinations_with_replacement, count, repeat, chain, compress
from itertools import permutations
import math
from functools import partial

nums = list(range(10))
print(nums)
print(list(combinations(nums, 3))) # комбинации по 3 (без повторениями)
print(len(list(combinations(nums, 3))))
# по формуле сочетаний
fp = partial(math.factorial)
print(fp(10)/(fp(3)*fp(10-3)))


print("С повторами:", list(combinations_with_replacement(nums, 3))) # комбинации по 3 (с повторениями)
print(len(list(combinations_with_replacement(nums, 3))))
print('-'*30)

odds = count(start=1, step=2)
print(type(odds)) # генератор
print(next(odds))
print(list(next(odds) for _ in range(10)))

print('-'*30)

tens = repeat(10, 4)
print(type(tens)) # генератор
# print(next(tens))
print(list(next(tens) for _ in range(4)))

print('-'*30)
list_of_lists = [[1,2,3], ['a','b','c'], [4,5,6]]

print(list(compress(list_of_lists, [1,0,1])))

print('-'*30)
print("Все комбинации от 0 до 4:")
for i in list(permutations(list(range(5)))):
    print(i)
