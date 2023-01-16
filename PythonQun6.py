def palindrome(string):
    for i in range(int(len(string)/2)):
        if string[i] != string[len(string)-i-1]:
            return "Not a palindrome" 
        return "yes, it is palindrome"
    
string = input("Entre the string:")
print(palindrome(string))