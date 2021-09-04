

def main():
    #Escribe tu código debajo de esta línea
    n=int(input())
    s=0
    while True:
        if s*s>n:
            break
        s=s+1
    print(s)

    pass

if __name__=='__main__':
    main()
