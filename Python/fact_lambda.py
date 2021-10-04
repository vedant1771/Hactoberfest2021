n=int(input('ENTER THE NUMBER: ', ))
def fact(n):
    if(n==1):
        return n
    else:
        return n*fact(n-1)
print(fact(n))
double=lambda x:((x*2)+3)*6
#here lambda is a function we use when we want a nameless function
print(double(n))
my_list=[1,2,3,4,5,6,7,8,9]
new_list=list(filter(lambda x:(x%2==0),my_list))
print(new_list)
#Here filter() is used to check the condition 
new_list1=list(map(lambda x:(x+1)**2,my_list))
print(new_list1)
#here map() is used to perform the equation

