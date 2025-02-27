def high_and_low(numbers):
    nlist =[int(num) for num in numbers.split()]
    return f"{max(nlist)} {min(nlist)}"

    