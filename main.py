text = input("Enter the Text: ").lower()


def palindrome(string):
    reverse_text = string[::-1]
    if reverse_text == string:
        print("This is a palindrome.")
    else:
        print("This is not a palindrome")


palindrome(text)

