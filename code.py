num=input() #entering the input 
mi=100000000
input_set=len(set(num))   #getting the total number of distinct letters of the given input  
i=0
j=0
while i<=len(num):    #iterating all possible substring and checking if it is equal to number to distinct elements
    if len(set(num[j:i+1]))==input_set:  
        mi=min(i+1-j,mi)
        j+=1
    else:
        i+=1       #if condition not satisfied increasing the substring
print(mi)
