#Adib-Vali

import string
from gtts import gTTS
import playsound
import os
from zipfile import ZipFile

key_dic={}
encrypted_data=''
printable='`1234567890-=!@#$%^&*()_+qwertyuiop[]}{POIUYTREWQasdfghjKl;LKJHGFDSA?><MNBVCXZzxcvbnm,./'
random=list(set(printable))

#zip key dic 
def zipper(key_dic):
    z = ZipFile( 'cryptography_key.zip' , 'w' )
    with open('cryptography_key.txt','w',encoding="utf-8") as file:
        file.write(str(key_dic))
    z.write('cryptography_key.txt')
    os.startfile('cryptography_key.txt')
    print('You can decrypt data using the built-in key that you see')
    tts('You can decrypt data using the built-in key that you see')
    tts('if you want to zip this file. type yes')
    if input('if you want to zip this file. type yes : ') == 'yes':
        os.remove('cryptography_key.txt')
        print('Successfully Zipped.....')
        tts('Successfully Zipped.....')
        print('you can decrypt data with cryptography key.zip')
        tts('you can decrypt data with cryptography key.zip')
    z.close()

# text to speech func
def tts(txt):
    # Language in which you want to convert
    language = 'en'    
    myobj = gTTS(text=txt, lang=language)
    # Saving the converted audio in a mp3 file named
    myobj.save("gtts.mp3")
    playsound.playsound('gtts.mp3',True)
    os.remove('gtts.mp3')
    # n+=1

def read_data(file_path):
    with open(file_path,'r',encoding="utf-8") as File:
        return File.read()

def write_data(data,file_name):
    with open(file_name,'w') as file:
        file.write(data)

#encrypt data
def encrypt(data):
    dic={}
    encrypt_data=''
    for item in list(set(data)):
        for i in set(printable):
            if i not in dic.values() and item!=' ':
                dic[item]=i
                break
    for item in list(data):
        if item==' ' or item=='\t' or item=='\n':
            encrypt_data+=item
            continue
        encrypt_data+=dic[item]
    return encrypt_data,dic

#decrypt data
def decrypt(data,key_dic):
    dic2={}
    dic=key_dic
    decrypted=''
    for x,y in dic.items():
        dic2[y]=x
    for item in list(data):
        if item==' ' or item=='\t' or item=='\n':
            decrypted+=item
            continue
        decrypted+=dic2[item]
    return decrypted


tts('encrypt your data with ease')
tts('please type your data address')
file_path=input('file address :')
data=read_data(file_path)
#data is txt file content
os.startfile(file_path)
tts('you can see your text here')
tts('type yes to encrypt your data')

if input('type yes to encrypt the data : ') == 'yes':
    encrypted_data,key_dic=encrypt(data)
    os.startfile(file_path)
    print(key_dic)
    write_data(encrypted_data,file_path)
    print(data,encrypted_data,key_dic)
    print("Successfully encrypted.....")
    tts('Successfully encrypted')
    tts('you can see your encrypted data')
    zipper(key_dic)

tts('type yes to decrypt the data')

if input('type yes to decrypt the data : ') == 'yes':
    decrypted_data=decrypt(encrypted_data,key_dic)
    print(key_dic)
    write_data(decrypted_data,file_path)
    os.startfile(file_path)
    print("Successfully decrypted.....")
    tts('Successfully decrypted')
    tts('you can see your decrypted data')