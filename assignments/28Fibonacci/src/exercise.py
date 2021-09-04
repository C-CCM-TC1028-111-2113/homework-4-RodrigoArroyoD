
def main():
    #escribe tu código abajo de esta línea
    a=0
    b=1
    c=0
    print('enter a number: ')
    n=int((input()))
    r=0
    while True:
        if r==n:
            break
        c=a+b
        a=b
        b=c
        r=r+1
    print(a)

    pass

if __name__=='__main__':
    main()
