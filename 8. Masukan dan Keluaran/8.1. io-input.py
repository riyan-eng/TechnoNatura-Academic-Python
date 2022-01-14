def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

something = input("enter text: ")
if is_palindrome(something):
    print("ya, itu adalah palindrome")
else:
    print("tidak, itu bukan palindrome")