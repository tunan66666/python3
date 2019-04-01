# by tunan
# download: https://github.com/tunan66666/python3

import operator
import pprint

test1 = []
test_dict1 = {'id':1, 'name':'d'}
test_dict2 = {'id':2, 'name':'b'}
test_dict3 = {'id':2, 'name':'c'}
test_dict4 = {'id':3, 'name':'a'}
test1.append(test_dict1)
test1.append(test_dict2)
test1.append(test_dict3)
test1.append(test_dict4)

# order by id, name
cmpfun = operator.itemgetter('id', 'name')
test1.sort(key=cmpfun)
print('\norder by id, name')
pprint.pprint(test1)

# first order by id, name then reverse
cmpfun = operator.itemgetter('id', 'name')
test1.sort(key=cmpfun, reverse=True)
print('\nfirst order by id, name then reverse')
pprint.pprint(test1)

# order by id desc, name
test1 = sorted(test1, key=lambda x:(-x['id'], x['name']))
print('\norder by id desc, name')
pprint.pprint(test1)

