def is_unique(my_str):
    # if len(my_str) == len(set(my_str)):
    #     return True
    # else:
    #     return False
    return len(my_str) == len(set(my_str))

def check_permutation(str1, str2):
    return sorted(str1) == sorted(str2)


def URLify(my_str):
    my_url = ""
    for char in my_str.strip():
        if char == " ":
            my_url += "%20"
        else:
            my_url += char
    return my_url

def palindrome_permutation(my_str):
#palindrome if number of odd counts is 0 or 1
    str_dict = {}

    for char in my_str.replace(' ', ''):
        if char in str_dict:
            str_dict[char] += 1
        else:
            str_dict[char] = 1

    odd_spotted = False
    for count in str_dict.values():
        if count % 2 != 0:
            if odd_spotted is True:
                return False
            else:
                odd_spotted = True
    return True

def compress(my_str):
    compressed = ""
    i=1
    count = 1
    while i < len(my_str):
        if my_str[i] == my_str[i-1]:
            count += 1
        else:
            compressed += my_str[i-1] + str(count)
            count = 1
        i += 1
    compressed += my_str[i-1] + str(count)
    if len(compressed) >= len(my_str):
        return my_str
    return compressed


