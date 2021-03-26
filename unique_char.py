def unique_string(string):
    temp_list = []
    for char in string:
        if char in temp_list:
            return False
        if char == ' ':
            continue
        char.append(temp_list)
    return True