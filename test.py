def palindrome(input):
    return input == "".join(input[::-1])


def palindrome_new(input):
    reverse = [e for e in input]
    start, end = 0, len(input) - 1
    while start < end:
        reverse[start], reverse[end] = reverse[end], reverse[start]
        start += 1
        end -= 1
    return input == "".join(reverse)


if __name__ == '__main__':
    print(palindrome("aba"))
    print(palindrome("abc"))
    print(palindrome("abba"))
    print(palindrome("abab"))
    print(palindrome_new("aba"))
    print(palindrome_new("abc"))
    print(palindrome_new("abba"))
    print(palindrome_new("abab"))
