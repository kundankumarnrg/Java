
sample_list=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#removing 0th,4th, 5th possition element

def remove_spefic_element(sample_list):
    print(sample_list)
    rem_ele=[5,4,0]
    for val in rem_ele:
        sample_list.remove(sample_list[val])
        
    print(sample_list)
remove_spefic_element(sample_list)

