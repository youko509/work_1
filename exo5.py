import re

text="er3453 e-56-67-r()"

def sluglify(text):
    text=text.replace(' ','-')
    table="[^abcdefghijklmnopkrstuvwxyz1234567890-]"
    regex = re.findall(table,text)
    print(regex)
    if len(regex) == len(text):
        print(f"your slug is: {text}")
    else:
        for val in regex:
            text = text.replace(val,'-')
        print(f"unused format for slug will be replace by - ")    
        print(text)
sluglify(text)    