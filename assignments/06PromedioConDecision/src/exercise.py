def main():
    #escribe tu código abajo de esta línea
    print('to stop the average, type a negative number')
    n=0
    total=0
    c=0
    while True:
        n=float(input())
        if n<0:
            break
    
        total=total+n
        c=c+1
        p=total/c
        print('you added :'+str(n))
    print('the average until now is:'+str(p))

        

print ('the final average was:'+str(p))

    pass
if __name__=='__main__':
    main()
