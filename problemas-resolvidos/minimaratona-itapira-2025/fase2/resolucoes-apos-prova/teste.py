from collections import defaultdict

keys = ['a', 'b', 'c']

myDict = defaultdict(set)
myDict['a'] = set([1,2,3])
myDict['b'] = set([4,5,6])

for elm in myDict['C']:
    print(elm)