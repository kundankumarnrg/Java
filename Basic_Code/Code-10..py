lst=['quick', 'brown', 'jumps', 'over', 'lazy']
num=4
def word_lenth_long_num(lst):
    print(lst)
    lst2=[]
    for val in lst:
        if len(val)>num:
            lst2.append(val)
    print(lst2)

word_lenth_long_num(lst)
