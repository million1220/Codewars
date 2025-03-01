eng2sp = {}
eng2sp['one'] = 'uno'
eng2sp['two'] = 'dos'
eng2sp['three'] = 'tres'
print(eng2sp)
print(eng2sp['two'])
print(len(eng2sp))
print('one' in eng2sp)   

# dictionary method 
# x.keys() returns a list of the keys used in the dictionary
inventory ={"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
for akey in inventory.keys():
    print("Got key", akey, "which maps to value", inventory[akey])
ks = list(inventory.keys()) #make a list of all of the keys
print(ks)
print(ks[0])
# 每次迴圈執行時，變數 akey都會被賦值為字典中的不同鍵。在迴圈主體內，可以使用inventoryakey]來訪問與該鍵關聯的值。不過需要注意的是，key的遍歷順序是不確定的
# 如果希望按照字母順序訪問key ，可以使用 sorted()函數來獲取排序後的key列表
for akey in sorted(inventory.keys()):
    print("Got key", akey, "which maps to value", inventory[akey])

#在dictionary中，遍歷鍵是一種非常常見的操作，因此可以省略 .keys()方法，直接使用dictionary本身
for akey in inventory:
    print("Got key", akey, "which maps to value", inventory[akey])


# x.values() returns a list of the values used in the dictionary
inventory ={"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
print(list(inventory.values()))
for v in inventory.values():
    # 每次迴圈執行時，k會獲取字典中的不同值。在迴圈主體內，可以使用v來訪問該值
    print("Got",v)
# x.items() returns a list of the key-value pairs in the dictionary返回字典中的鍵-值對列表
inventory ={"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
print(list(inventory.items()))
for k,v in inventory.items():
    print("Got",k,"that maps to",v)

# keys()、values()和items()方法返回的對象不是真正的列表，而是類似列表的對象。這意味著它們不能被修改，不能使用append()方法添加新的元素
# 但是可以使用list()函數將它們轉換為真正的列表
list(inventory.keys())[0]

# 在dictionary中，可以使用in運算符來檢查鍵是否存在
inventory ={"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
if "apples" in inventory:
    print(inventory["apples"])
else:
    print("We have no apples")

# 或者使用get()方法，與[]運算符類似，但是當鍵不存在時，get()方法不會引發異常，而是返回None
inventory ={"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
#  x.get(key) returns the value associated with the key, or None if the key is not in the dictionary
print(inventory.get("cherries"))
#或是提供自定義的預設值作為第二個參數，當key不存在時返回這個參數
# x.get(key, default) returns the value associated with the key, or default if the key is not in the dictionary
print(inventory.get("cherries",0))

# pratice
mydict = {"a":12,"b":6,"c":13}
answer = mydict.get("a")//mydict.get("b")
print(answer)# =2
mydict2 = {"a":12,"b":6,"c":13}
print("c" in mydict2)# =True
print(23 in mydict2)# =False

total = 0
mydict3 = {"aaa":12,"bbb":6,"cccc":13}
for k in mydict3:
    if len(k) > 3 :
        total = total + mydict3[k]
print(total)# 13