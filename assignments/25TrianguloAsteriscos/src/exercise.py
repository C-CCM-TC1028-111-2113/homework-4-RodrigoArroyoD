
def main():
    #Escribe tu código debajo de esta línea
    n=int(input())
    h=0
       t=n
    while True:
        if h==n:
        break
        h=h+1
        t=t-1
        print(' '*(t)+'*'*(h))
    pass


if __name__=='__main__':
    main()
