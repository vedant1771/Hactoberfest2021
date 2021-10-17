def print_rangoli(size):
    row= 4*size - 3
    n= 97 + size-1
    st=""
    store=[]
    for i in range(size):
        temp=[]
        for j in range(i+1):
            temp.append(chr(n-j))
        if(len(temp)>1):    
            x= ("-".join(temp)) +"-"+ ("-".join(temp[-2::-1]))
        else:
            x=temp[0]
        store.append(x.center(row,"-"))
    res =  ('\n'.join(store)) +"\n"+ ('\n'.join(store[-2::-1]))
    print(res)




#a=97

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
