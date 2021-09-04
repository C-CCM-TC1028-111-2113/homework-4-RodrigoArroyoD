def main():
    #escribe tu código abajo de esta línea
    j=1
n=int(input())
while j<=n:
    print(str(j)+'.-#')
    if j==n:
        break
    j=j+1
    print(str(j)+'.-%')
    if j==n:
        break
    j=j+1
    

    pass

if __name__=='__main__':   
    main()
