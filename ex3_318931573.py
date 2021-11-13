""" Exercise #3. Python for Engineers."""

#########################################
# Question 1 - do not delete this comment
#########################################


def sum_divisible_by_k(lst, k):
    sum1 = 0
    for num in lst:
        if num % 3 == 0:
            sum1 += num
    return (sum1)


#########################################
# Question 2 - do not delete this comment
#########################################
def mult_odd_digits(n):
    n = str(n)
    mult = 1
    for dig in n:
        if int(dig) % 2 == 1:
            mult *= int(dig)
    return (mult)


#########################################
# Question 3 - do not delete this comment
#########################################
def count_longest_repetition(s, c):
    count = 0
    max_count = 0
    i = 0
    if c not in s:
        return (count)
    else:
        while i < len(s):
            if c == s[i]:
                count += 1
            else:
                count = 0
            i += 1
            max_count = max(max_count, count)
        return max_count


#########################################
# Question 4 - do not delete this comment
#########################################
def upper_strings(lst):
    if type(lst) is not list:
        return(int(-1))
    else:
        i = 0
        while i < len(lst):
            if type(lst[i]) is str:
                lst[i] = lst[i].upper()
            i += 1
        print(lst)


#########################################
# Question 5 - do not delete this comment
#########################################
def div_mat_by_scalar(mat, alpha):
    mat1 = []
    for row in range(0, len(mat)):
        mat1.append([])
        for cul in range(0, len(mat[row])):
            mat1[row].append(mat[row][cul]//alpha)
    return (mat1)


#########################################
# Question 6 - do not delete this comment
#########################################
def mat_transpose(mat):
    cul = 0
    row = 0
    mat1 = []
    while cul < len(mat[row]):
        mat1.append([])
        while row < len(mat):
            mat1[cul].append(mat[row][cul])
            row += 1
        cul += 1
        row = 0
    return (mat1)


#########################
# main code - do not delete this comment
# Tests have been added for your convenience.
# You can add more tests below.
#########################
print(sum_divisible_by_k([3, 6, 4, 10, 9], 3) == 18)
print(sum_divisible_by_k([45.5, 60, 73, 48], 4) == 108)


print(mult_odd_digits(5638) == 15)
print(mult_odd_digits(2048) == 1)
print(mult_odd_digits(54984127) == 315)


print(count_longest_repetition('eabbaaaacccaaddd', 'a') == 4)
print(count_longest_repetition('cccccc', 'c') == 6)
print(count_longest_repetition('abcde', 'z') == 0)


vals = [11, 'TeSt', 3.14, 'cAsE']
upper_strings(vals)
print(vals == [11, 'TEST', 3.14, 'CASE'])

vals = [-5, None, True, [1, 'dont change me', 3]]
upper_strings(vals)
print(vals == [-5, None, True, [1, 'dont change me', 3]])

print(upper_strings(42) == -1)
print(upper_strings('im not a list') == -1)
print(upper_strings(False) == -1)


mat1 = [[2, 4], [6, 8]]
mat2 = div_mat_by_scalar(mat1, 2)
print(mat1 == [[2, 4], [6, 8]])
print(mat2 == [[1, 2], [3, 4]])

print(div_mat_by_scalar([[10, 15], [-3, 6]], -5) == [[-2, -3], [0, -2]])


mat = [[1, 2], [3, 4], [5, 6]]
mat_T = mat_transpose(mat)
print(mat == [[1, 2], [3, 4], [5, 6]])
print(mat_T == [[1, 3, 5], [2, 4, 6]])

mat2 = [[0, 1, 2], [10, 11, 12], [20, 21, 22]]
mat2_T = mat_transpose(mat2)
print(mat2_T == [[0, 10, 20], [1, 11, 21], [2, 12, 22]])

mat3 = [[0, 1, 2], [9, 8, 7], [10, 11, 12], [20, 21, 22], [0, 0, 0]]
mat3_T = mat_transpose(mat3)
print(mat3_T)
# ============================== END OF FILE =================================
