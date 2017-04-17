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

def one_away(str1, str2):
    a = len(str1)
    b = len(str2)
    if abs(a-b) > 1:
        return False
    i = 0
    j = 0
    edit_count = 0
    while i < a and j < b:
        if str1[i] != str2[j]:
            if edit_count == 1:
                return False
            if a > b:
                i+=1
            elif a < b:
                j += 1
            else:
                i+=1
                j+=1
            edit_count += 1
        else:
            i+=1
            j+=1
    if i < a or j < b:
        edit_count += 1
    if edit_count > 1:
        return False
    return True

def zero_matrix(matrix):
    if not matrix:
        return []
    rows = len(matrix)
    cols = len(matrix[0])

    clear_rows = [False] * rows
    clear_cols = [False] * cols
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                clear_rows[i] = True
                clear_cols[j] = True
    for i in range(rows):
        for j in range(cols):
            if clear_rows[i] or clear_cols[j] is True:
                matrix[i][j] = 0
    return matrix
