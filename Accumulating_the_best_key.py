#Accumulating_the_best_key

# pratice 1
"""Write a program that finds the key in a dictionary that has the maximum value. If two keys have the same maximum value, it’s OK to print out either one. Fill in the skeleton code"""

d = {'a': 194, 'b': 54, 'c':34, 'd': 44, 'e': 312, 'full':31}

ks = d.keys()
# initialize variable best_key_so_far to be the first key in d
best_key_so_far = list(ks)[0] #初始化 best_key_so_far為字典中的第一個鍵
for k in ks:
    # check if the value associated with the current key is
    # bigger than the value associated with the best_key_so_far
    # if so, save the current key as the best so far
    # 如果當前的key對應的值比目前最佳key的值大，就更新為最佳key
    if d[k] > d[best_key_so_far]:
        best_key_so_far = k

print("key " + best_key_so_far + " has the highest value, " + str(d[best_key_so_far]))

# ------------------------------------------------
# pratice 2
"""Create a dictionary called d that keeps track of all the characters in the string placement and notes how many times each character was seen. Then, find the key with the lowest value in this dictionary and assign that key to key_with_min_value."""
placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
d = {}
for c in placement:
    if c not in d:
        d[c] = 0
    d[c] = d[c] + 1
print(d)

key_with_min_value = list(d.keys())[0]#初始化key_with_min_value為字典中的第一個鍵
#應該初始化 key_with_min_value 為字典中的一個有效鍵，而不是 0
for k in d.keys():
    if  d[k]<d[key_with_min_value]:
        key_with_min_value = k
print(key_with_min_value)

# ------------------------------------------------
# pratice 3
"""Create a dictionary called lett_d that keeps track of all of the characters in the string product and notes how many times each character was seen. Then, find the key with the highest value in this dictionary and assign that key to key_with_max_value."""
product = "iphone and android phones"
lett_d = {}
for c in product:
    if c not in lett_d:
        lett_d[c] = 0
    lett_d[c] = lett_d[c] + 1
print(lett_d)
key_with_max_value = list(lett_d.keys())[0]#初始化key_with_max_value為字典中的第一個鍵
for k2 in lett_d.keys():
    if lett_d[k2] > lett_d[key_with_max_value]:
        key_with_max_value = k2
print(key_with_max_value)