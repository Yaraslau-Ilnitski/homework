dict_1 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
dict_2 = {}
string1 = list(dict_1.keys())
string2 = list(dict_1.values())
n = 0
for i in string1:
    string1[n] = string1[n] + str(len(string1[n]))
    n += 1
m = 0
for i in string1:
    dict_2[string1[m]] = string2[m]
    m += 1
print(dict_2)

dict_1 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
dict_2 = {}
string1 = list(dict_1.keys())
string2 = list(dict_1.values())
n = 0
while n < len(dict_1):
    string1[n] = string1[n] + str(len(string1[n]))
    n += 1

m = 0

while m < len(string1):
    dict_2[string1[m]] = string2[m]
    m += 1
print(dict_2)