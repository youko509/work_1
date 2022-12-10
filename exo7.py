def encrypt_text():
    table = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    text = "ahc"
    text = text.lower()
    code=""
    
    for val in text:
        index = table.index(val)
        code  = f"{index}" if len(code)==0 else code + "-" + f"{index}" 
    print(code)    

encrypt_text()    