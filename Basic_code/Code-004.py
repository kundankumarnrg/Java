lst=[7,110,21,5,4,8,9,600,3,25,69,48,20,11]
'''
#Type-1:-----------------------------------#

def find_min_ele(lst):
    print("Min values: ",min(lst))
find_min_ele(lst)


#Type-2:-----------------------------------#

def find_min_val(lst):
    lst1=sorted(lst)
    print("min val: ",lst1[0])
find_min_val(lst)
'''

#Type-3:-----------------------------------#
'''
def find_min_values(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i]<lst[j]:
                lst[i],lst[j]=lst[j],lst[i]
    print("min values: ",lst[0])
find_min_values(lst)
'''
#Type-4:-----------------------------------#
def find_min_val(lst):
    tem=lst[0]
    for val in lst:
        if tem>val:
            tem=val
    print(tem)
find_min_val(lst)
