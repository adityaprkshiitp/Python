from ast import If
from re import X


text = "Hello Hi Hola amigos"
count=0
for x in text:
    if(x == 'H'): 
        count +=1
print(count)
