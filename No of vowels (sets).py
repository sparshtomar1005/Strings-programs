#To count no of vowels using sets

def vowel_count(str):
    count=0
    vowel=set("aeiouAEIOU")
    for alphabet in str:
        if alphabet in vowel:
            count = count+1
    print("No. of Vowels :",count)            


str=input("Enter the string:")
print("Your string is:",str)
vowel_count(str)





