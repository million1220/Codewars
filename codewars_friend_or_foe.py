def friend(names):
    #Code
    return [name for name in names if len(name) == 4 ]
print(friend(["Ryan", "Kieran", "Jason", "Yous"]))   # Output: ['Ryan', 'Yous']
print(friend(["Peter", "Stephen", "Joe"]))   
        
        