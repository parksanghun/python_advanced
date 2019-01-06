import re

p = re.compile('a.b')
p = re.compile('a.b', re.DOTALL)
p = re.compile('a.b', re.S)
m = p.match('a\nb')
print(m)

import re
p = re.compile('[a-z]', re.I)
m = p.match('Python')
print(m)

import re
p = re.compile("^python\s\w+", re.MULTILINE)

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))

m = p.match("python good")
print(m)

m = p.match("pythongood")
print(m)

import re
charref = re.compile(r"""
&[#]
(
    0[0-7]+         # Octal form
    | [0-9]+        # Decimal form
    | x[0-9a-fA-F]+ # Hexadecimal form
)
;
""", re.VERBOSE)

m = charref.match("")
print(m)

p = re.compile('\\\\section')
p = re.compile(r'\\section')

import re
p = re.compile('Crow|Servo')
m = p.match('CrowHello')
m = p.match('ServoHello')
print(m)

print(re.search('^Life', 'Life is too short'))
print(re.search('^Life', 'My Life'))

print(re.search('short$', 'Life is too short'))
print(re.search('short$', 'Life is too short, you need python'))

import re
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))

import re
p = re.compile(r'\sclass\s')
print(p.search('no class at all'))

print(p.search('the declassified algorithm'))
print(p.search('one subclass is'))

p = re.compile(r'\Bclass\B')
print(p.search('no class at all'))

print(p.search('the declassified algorithm'))
print(p.search('one subclass is'))

