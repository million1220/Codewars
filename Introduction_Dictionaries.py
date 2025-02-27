def square_digits(num):
    digits = list(map(int, str(num)))
    nums = []
    for i in digits:
        a = int(i)**2
        nums.append(a)
        
    return nums

square_digits(9119)
        