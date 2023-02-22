import re

pattern = re.compile(r"[a-zA-Z]")

string = 'Search this inside this text please!'

a = pattern.search(string)
b = pattern.findall(string)
print(a.string)
