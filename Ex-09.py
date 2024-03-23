nums = ['4, 8, 7, 4,3,6,2,1,9']
list_nums = nums[0].split(',')
int_nums = [int(num) for num in list_nums]
if int_nums.index(6) >= 0 and int_nums.index(6) < len(int_nums):
    print("Available")
else:
    print("Not Available")
