from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat
import operator

# # product
# a= [1,2]
# b = [4,5]
# prod= product(a,b)
# print(list(prod))

# # permutations
# a= [1,2,3]
# per = permutations(a)
# per = permutations(a, 1)
# print(list(per))

# # combinations
# a = [1,2,3,4,5,]
# comb = combinations(a, 3)
# print(list(comb))


# # combinations_with_replacements
# a = [1,2,3,4,5,]
# comb = combinations_with_replacement(a, 3)
# print(list(comb))


# # accumulate
# a = [1,2,3,4,5]
# acc = accumulate(a)
# print(a)
# print(list(acc))
# a = [1,2,3,4,5]
# acc = accumulate(a, func=operator.mul)
# acc = accumulate(a, func=max)
# print(a)
# print(list(acc))


# groupy
# def grt3(x):
#     return x >3
# a = [1,2,3,4,5,6,7]
# grp = groupby(a, key= lambda x: x>3)
# # print(grp)
# for k, v in grp:
#     print(k , list(v))


# # count
# for i in count(1):
#     print(i)
#     if i == 1000:
#         break

# #cycle
# a=[1,2,3]
# for i in cycle(a):
#     print(i)

# repeat
# a = [1,2,3]
# for i in repeat(a, 5):
#     print(i)



