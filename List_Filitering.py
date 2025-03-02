def filter_list(l):
    newlist = []
    a= 1
    for i in l:
        if type(i) == type(a):
            newlist.append(i)
    return newlist
