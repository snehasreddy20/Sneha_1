def duplicate(l):
    result = []
    for item in l:
        if item not in result:
            result.append(item)
    return result


my_lst = [1, 2, 3, 4, 2, 3, 5, 4, 4]
result = duplicate(my_lst)
print("result_lst",result)
print("oringinal lst",my_lst)
x=my_lst[0:4]
print(x)
print(my_lst[0])
