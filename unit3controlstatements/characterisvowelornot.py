#Entered character is a vowel or not
ch = input("Enter a character : " )
ch = ch[0]
if(ch=='a' or ch=='e'or ch=='i' or ch=='0' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U') :
    print("Enterd character is a vowel")
else:
    print("Entered character is not a vowel")
ch = input("Enter a character : ")
ch = ch[0]
count=0
for i in ['a','e','i','o','u','A','E','I','O','U']:
    if ch == i :
        count += 1
if count == 1 :
    print("Entered character is a vowel")
        
else :
    print("Entered character is not a vowel")
    
