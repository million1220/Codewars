def hello2(s,n):
    greeting = "hello {}".format(s)
    print(greeting*n)

hello2("World",5)

'''
test---------------------------------------
'''
def print_many(x,y):
    for i in range(y):
        print(x)

z= 3
print_many("hello",z)

'''
- 函數 function 是一段可以重複使用的程式碼，用來完成特定任務
- 透過 def 關鍵字來定義函數，後面接函數名稱和參數列表
- 函數可以有參數 inputs, 也可以回傳值 outputs
'''

def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# 帶回傳值的函數
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 輸出: 8

a = '-----next code------'
print(a)

#12.8 A function that accumulates
def mylen(seq):
    c = 0 # initialize count varable to 0
    for _ in seq: 
        c=c+1 # increment count for each item in the sequence
    return c # return the count
print(mylen("hello"))  # 輸出: 5
print(mylen([1, 2, 3, 4]))  # 輸出: 4


