import re

text="er3453 e-56-67-r"

def sluglify(text):
    
    table="abcdefghijklmnopkrstuvwxyz1234567890-"
    text=text.replace(' ','-')
    print(text)
sluglify(text)    