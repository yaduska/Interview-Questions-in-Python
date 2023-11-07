def find_max_min(list_of_numbers):
    if not list_of_numbers:
        print('please give non empty list')
        return
    max_no=list_of_numbers[0]
    min_no=list_of_numbers[0]
    for a in list_of_numbers:
        if max_no<a:
            max_no=a    
        if min_no>a:
            min_no=a
    print('min no is ',min_no)
    print('max no is ',max_no)

find_max_min([4,5,33,2,55,78,0,4,2,90,567,345,6,4,5])
find_max_min([])
        