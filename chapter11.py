import re

def checkMatch(m):
    if m:
        print('Match found:', m.group())
    else:
        print('No match')


p = re.compile('[a-z]+')

m = p.match("python")
checkMatch(m)

m = p.match("3 python")
checkMatch(m)

m = p.search("python")
checkMatch(m)

m = p.search("3 python")
checkMatch(m)

result = p.findall("life is too short")
print(result)

result = p.finditer("life is too short")
print(result)

for r in result:
    print(r)