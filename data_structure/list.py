# ["a","b","c","d"]
# order collection of items
# changable
# allows dublicates

# ============ creating list =============
empty_list = []
print(empty_list)
print(type(empty_list))

list = ["a", "b", "c", "d"]
print(list)
print(type(list))

list2 = [1, 2, 3, 4]
print(list2)
print(type(list2))

mix = [1, "nomi", True, None]
print(mix)
print(type(mix))

#=============== Nested list ============
matrix = [
    ["a","b"],
    ["c","d"],
    ["e","f"],
    ["g","h"],
]
print(matrix)
print(type(matrix))

mix_matric = [
    ["a","b"],
    [1,2,3],
    [True]
]
print(mix_matric)
print(type(mix_matric))

#=========== Read & Access ==============
# can access and read through index number which start from zero
lst = ["a", "b", "c", "d"]
print(lst[0])
print(lst[2])
print(lst[-1])
print(lst[1])

# how to access and read nested list
matrix = [
    ["a","b"],
    ["c","d"],
    ["e","f"],
    ["g","h"],
]
print(matrix[0]) # if i need first full row 
print(matrix[1]) # if i need second full row 
print(matrix[1][0]) #output c because first i access the second row which is c and d then i target the 0 index which is c
print(matrix[-1][0])
print(matrix[0][1])
print(matrix[2][1])
print(matrix[3][1])

# =========== slicing =============


