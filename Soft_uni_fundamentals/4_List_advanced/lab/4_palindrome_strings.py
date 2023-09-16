def is_palindrome(string):
    original_string = string
    reversed_string = string[::-1]
    if original_string == reversed_string:
        return True
    else:
        return False


entry_data = input().split()
palindrome_list = list(filter(is_palindrome, entry_data))

palindrome_search_word = input()
palindrome_count = palindrome_list.count(palindrome_search_word)
print(palindrome_list)
print(f"Found palindrome {palindrome_count} times")