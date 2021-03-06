# -*- coding: utf-8 -*
##疑惑的汉字
##题目链接，http://www.shiyanbar.com/ctf/1876

def decodePawnshop(char):
    dic = {u'口': 0,
           u'由': 1,
           u'中': 2,
           u'人': 3,
           u'工': 4,
           u'大': 5,
           u'王': 6,
           u'夫': 7,
           u'井': 8,
           u'羊': 9,}
    if char in dic:        
        return dic[char]
    else:
        return char

def decrypt(text):
    return ''.join([str(decodePawnshop(char)) for char in text])  

def asciiOrderToChar(text):
    return ''.join([chr(int(char)) for char in text.split(' ')])    

def main():
    text = u'王夫 井工 夫口 由中人 井中 夫夫 由中大'
    string = decrypt(text)
    print asciiOrderToChar(string)
    
if __name__ == '__main__':
    main()
