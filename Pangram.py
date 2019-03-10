#Check wheter a string is a pangram or not
x=input("Enter a Sting:")
y=set(x)
if(len(x)==26):
    print("It is a pangram")
else:
    print("Its is not a pangram")