#Calculate Upper case and lower case letters in a string
x=input("Enter the string :")
upper=0
lower=0
for i in x:
        if i.isupper():
            upper=upper+1
        if i.islower():
            lower=lower+1
            
print("The Upper case letters are:",upper)          
print("The lower case letters are:",lower) 