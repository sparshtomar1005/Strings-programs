#Count the frequency of words in a string using dictionary
str=input("Enter the string:")
print("The string is :",str)
str2=str.lower().split()
count={}
for x in str2:
    if x in count:
        count[x]+=1
    else:
        count[x]=1
        
print("The Frequency of words is ",count)        
  