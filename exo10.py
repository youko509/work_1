import re
text = "Jean-Baptiste Jean"

pattern = r"[A-Z]+"

regex = re.findall(pattern,text)
regex = ''.join(regex)
print(regex)