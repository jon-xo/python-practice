# loop_challenge.py

# Divisble by Ten

def divisible_by_ten(nums):
    count = 0
    for num in nums:
        if num % 10 == 0:
            count += 1
    return count

print(divisible_by_ten([20, 25, 30, 35, 40]))

# Greetings

def add_greetings(names):
    new_list = []
    for name in names:
        new_list.append("Hello, " + name)
    return new_list


# Delete Starting Even Numbers

def delete_starting_evens(lst):
    for num in lst:
        if lst[0] % 2 == 0:
            lst.pop(0)
    if len(lst) == 1:        
        if lst[0] % 2 == 0:
            return []
    else:
        return lst

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([2, 10, 6]))

# Odd Indices

def odd_indices(lst):
    new_lst = []
    for item in lst:
        if lst.index(item) % 2 == 1:
            new_lst.append(item)
    return new_lst

print(odd_indices([4, 3, 7, 10, 11, -2]))

# Exponents

def exponents(bases, powers):
    answers = []
    for num in bases:
        for exp in powers:
            answers.append(num ** exp)
    return answers

print(exponents([2, 3, 4], [1, 2, 3]))

# ------------------
# Advanced Loops

# Larger Sum
def larger_sum(lst1, lst2):
    sum1 = sum(lst1)
    sum2 = sum(lst2)

    if sum1 >= sum2:
        return lst1
    else:
        return lst2

print(larger_sum([1, 9, 5], [2, 3, 10]))

# Over 9k

def over_nine_thousand(lst):
    tally = 0
    if len(lst) == 0:
        return tally
    else:
        for num in lst:
            if(tally <= 9000):
                tally += num
        return tally

print(over_nine_thousand([8000, 900, 120, 5000]))

# Max Num

def max_num(nums):
    default = nums[0]
    for value in nums:
        if value > default:
            default = value
    return default

print(max_num([50, -10, 0, 75, 20]))

# Same Values

# def same_values(lst1, lst2):
#     new_list = []

#     for x in lst1:
#         for y in lst2:
#             if lst2.index(y) == lst1.index(x):
#                 if y == x:
#                     new_list.append(lst1.index(x))
#                 break
#     return new_list

def same_values(lst1, lst2):
    new_list = []

    for x in range(len(lst1)):
        for y in lst2:
            if lst1[x] == lst2[x]:
                new_list.append(x)
                break
    return new_list
    

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

# Reversed List

def reversed_list(lst1, lst2):
    for x in range(len(lst1)):
        if lst1[x] != lst2[(-1-x)]:
            return False
    return True

print(reversed_list([1, 2, 3], [3, 2, 1]))