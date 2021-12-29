def encrypted_word(st):
    if len(st) <=1:
        return st
    
    result = ""
    middle_index = len(st)//2
    if len(st)%2 == 0:
        middle_index-=1
    result+= st[middle_index] + encrypted_word(st[:middle_index]) + encrypted_word(st[middle_index+1:])
    return result



# print(encrypted_word("abc"))
# print(encrypted_word("abcxcba"))
# print(encrypted_word("facebook"))
# print(encrypted_word("ab"))

print(encrypted_word("cb"))