Str=input('')
lst=[]
dic={}
S=''
lst=[i for i in Str]
lst=sorted(lst)
S=[S+i for i in lst]
lst=[]
for i in S:
    if i not in lst:
        dic[i]=S.count(i)
        lst.append(i)
dic2=sorted(dic.items(),key=lambda KV:(KV[1]),reverse=True)
#print(dic2)
x=0
for key,value in dic2:
    print(key,value)
    x+=1
    if x==3:
        break
