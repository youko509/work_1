
def decrypt_code():
    table = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    text = "0-2-1"
    text = text.split('-')
    value=""
    
    for val in text:
        value = value+table[int(val)]
        
    print(value)

decrypt_code()
