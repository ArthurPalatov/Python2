
def is_palindrome(s):
    cleaned = ""
    for char in s:
        if char.isalnum():
            cleaned += char.lower()
    if cleaned == cleaned[::-1]:
        return "Yes"
    else:
        return "No"
input_string = input("Введите строку: ")
print(is_palindrome(input_string))