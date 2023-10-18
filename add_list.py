n = int(input("enter size of list: "))
list=[]

for i in range(n):
    elements= input("enter the elements: ")

def add(n,list):
    if (n==0):
        return 0
    else:
        return list[n-1]+ add(list,n-1)
total = add(len(list),list)
print(total)
    