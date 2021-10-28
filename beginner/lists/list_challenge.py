# list_challenge.py

# Append size

def append_size(lst):
    lst.append(len(lst))
    return lst


print(append_size([23, 42, 108]))

# Append sum


def append_sum(lst):
    x = 0
    while(x < 3):
        lst.append(lst[-1] + lst[-2])
        x += 1
    return lst


print(append_sum([1, 1, 2]))

# Larger list


def larger_list(lst1, lst2):
    len1 = len(lst1)
    len2 = len(lst2)

    if(len1 >= len2):
        return lst1[-1]
    else:
        return lst2[-1]


print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

# More than N


def more_than_n(lst, item, n):
    matched_snacks = []
    for snack in lst:
        if(snack == item):
            matched_snacks.append(snack)
    if(len(matched_snacks) > n):
        return True
    else:
        return False


print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))


# Combine Sort

def combine_sort(lst1, list2):
    new_list = lst1 + list2
    return sorted(new_list)

# Advanced Lists
# --------------

# Every three numbers


def every_three_nums(start):
    if int(start) > 100:
        return []
    else:
        return list(range(start, 101, 3))


print(every_three_nums(91))

test_list = every_three_nums(93)
# try:
# print(test_list[3])

# Remove Middle


def remove_middle(lst, start, end):
    final_list = lst[0:start] + lst[end+1:]
    return final_list
    # print(lst[0:start])
    # print(lst[end+1:])


remove_middle([4, 8, 15, 16, 23, 42], 1, 3)

# More Frequent Item

def more_frequent_item(lst, item1, item2):
    x = lst.count(item1)
    y = lst.count(item2)

    if x > y or x == y:
        return item1
    else:
        return item2

# Double Index

def double_index(lst, index):
    try:
        new_list = lst[0:index]
        new_list.append(lst[index] * 2)
        new_list.extend(lst[index+1:])
        return new_list
    except IndexError:
        return lst

print("double i")
print(double_index([1, 2, 3, 4], 2))

# Middle Item

def middle_element(lst):
    if len(lst) % 2 == 0:        
        x = round(len(lst) / 2)
        # print(x)
        # print(lst[x])
        # print(lst[x-1])
        return (int(lst[x-1]) + int(lst[x])) / 2
    else:
        return lst[round(len(lst) / 2)]
        # print(x)
        # print("value 1: {0} + value2: {1} / 2").format(lst[x], lst[x+1])

# print(middle_element([5, 2, -10, -4, 4, 5]))
# print(middle_element([1, 3, 5, 15, 30]))
print(middle_element([4, 3, 8, 2]))
