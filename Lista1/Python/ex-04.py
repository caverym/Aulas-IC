import math


def isnumber(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

a = 0
while True: 
    In = input("Insira um valor ou aperte enter com o campo vazio para parar: ")
    if(isnumber(In) == False):
        break
    a += float(In)
print (a)