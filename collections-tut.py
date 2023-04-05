# #Counter
# from collections import Counter
# a = "aaaahjhjhffffffdfdjhfjvvvvdhfdufshf"
# mycounter = Counter(a)
# print(mycounter)
# print(mycounter.most_common(1))
# print(mycounter.most_common(3))
# print(mycounter.most_common(3)[0][0])
# print(list(mycounter.elements()))


# #namedtuple
# from collections import namedtuple
# Point = namedtuple('Point', 'x, y')
# pt = Point(1,2)
# print(pt)
# print(pt.x , pt.y)


# #ordereddict
# from collections import OrderedDict
# odict = OrderedDict()
# # odict = {}
# odict['a']=1
# odict['b']=1
# odict['c']=1
# odict['d']=1
# odict['g']=1
# print(odict)

# #defaultdict
# from collections import defaultdict
# ddict = defaultdict(int)
# ddict['a'] = 1
# ddict['b'] = 2
# print(ddict['o'])

# # deque
# from collections import deque
# dq = deque()
# dq.append(1)
# dq.append(2)
# dq.append(2)
# dq.appendleft(5)
# dq.pop()
# dq.popleft()
# dq.extendleft([1,2,3])
# print(dq)
# dq.rotate(1)
# print(dq)



