l=[[1,[2]],[3,4,[5,6],7],8,[2+4j,"psit",[11,22]],'python']
f=[]
def check(l):
  for i in l:
    if type(i)==list:
      check(i)
    else:
      f.append(i)
  return f
print(check(l))
