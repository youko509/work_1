import re
text = "Jean-Baptiste Fean"
def initial():

    pattern = r"[A-Z]+"

    regex = re.findall(pattern,text)
    regex = ''.join(regex)
    print(regex)

initial()    