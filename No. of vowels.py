#To Count number of vowel
x=input("Enter a string:")
vowels=[]
x.lower()
list={'a','e','i','o','u'}
for i in x:
    if(i in list):
        vowels.append(i)
    else:
        continue
    
print("The number of vowels are:",len(vowels))
print("The vowels are :",vowels)    