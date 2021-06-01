from collections import OrderedDict
key_value = {}

key_value[2] = 56
key_value[1] = 2
key_value[5] = 12
key_value[4] = 24
key_value[6] = 18
key_value[3] = 323

# alpha order
print(sorted(key_value.items(), key=lambda x: x[1]))
for i in sorted(key_value):
    print(i)

# lexi order
dict2 = {'ravi': '10', 'rajnish': '9',
         'sanjeev': '15', 'yash': '2', 'suraj': '32'}
dict1 = OrderedDict(sorted(dict2.items()))
print(sorted(dict2.items()), dict1)

# Dict merging can be done in 3 ways

# 1 using update poerator => dict1.update(dict2)
# 2 using ** operator => {**dict1,**dict2}
# 3 using "|" operator => dict1 | dict2
