def obvious_sort(l):
    x = []
    while l:
        mini = l[0]
        for i in range(len(l)):
            if l[i] < mini:
                mini = l[i]
        x.append(mini)
        l.remove(mini)
    return x

l = [90, 23, 97, 88, 5, 1]
print(obvious_sort(l))





def min_list(l):
    mini=l[0]
    for i in range(len(l)):
        if l[i] < mini:
            mini = l[i]
    return mini


def obvious_sort1(l):
    x=[]
    while l:
        mini = min_list(l)
        x.append(mini)
        l.remove(mini)
    return x

l = [90, 23, 97, 88, 5, 1]
print(obvious_sort1(l))