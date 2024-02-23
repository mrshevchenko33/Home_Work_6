my_list = [1, 2, 3, 4, 5, 6, 7, 8]

if len(my_list) > 1:
    last_num = my_list.pop()
    my_list.insert(0, last_num)

print(my_list)