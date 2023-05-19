def modify_list(lst):
    lst = [int(i/2) for i in lst if i%2==0]
    print(lst)
modify_list([1,2,3,4,5,6])
modify_list([10,5,8,3])
modify_list([12,22,13,41,52,16])
