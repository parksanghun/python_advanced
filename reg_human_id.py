import re

data = """
park 840921-1234567
kim 700101-2012313
"""

result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))


# g<1> : compile된 정보의 그룹 첫번째
pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))

