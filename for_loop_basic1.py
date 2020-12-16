def primeros150(num):
    for i in range (num+1):
        print(i)

def de5en5(lim):
    for i in range (0,lim +1,5):
        print(i)

def contarDojoWay(num):
    for i in range (0,num+1):
        if i%10==0:
            print('Coding Dojo')
        elif i%5==0:
            print('Codificación')
        else:
            print(i)

def example4(num):
    sum=0
    for i in range (0, num+1, 1):
        if (i%2!=0):
            sum=sum+i
    print('La suma es:',sum)

def ctaRegresivaX4(num):
    while num>0:
        print(num)
        num=num-4

def flexCount():
    highNum = input('Ingrese el numero mayor')
    lowNum = input('Ingrese el numero menor')
    mult = input('Ingrese el multiplicador')
    lowNum=int(lowNum)
    highNum=int(highNum)
    mult=int(mult)

    for x in range (lowNum, highNum, 1):
        if x%mult==0:
            print(x)


if __name__ == '__main__':
    primeros150(150)
    de5en5(1000)
    contarDojoWay(100)
    example4(5000)
    ctaRegresivaX4(2018)
    flexCount()