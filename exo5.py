import re

text="er3453e-56-67-r"

def slug_match(text):
    
    pattern = (r"([a-z]|[0-9])+(-([a-z]|[0-9])+)+")
    value = re.match(pattern,text)

    if value[0]== text:
        print("this is a slug")
        print(value[0])
        text=text.replace(' ','-')
    else:
        print("enter a good slug")

slug_match(text)    