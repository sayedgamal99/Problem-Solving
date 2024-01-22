# nums = [0,1,2,2,3,0,4,2]
nums = [2]
val = 3
kk = len(nums)-nums.count(2)
# nums2 = sorted(nums[:kk])
# for i,ii in enumerate(nums2):
#     if ii == val:
#         for ind, ij in enumerate(nums[kk:]):
#             if ij != val:
#                 nums2[i] = ij
#                 nums.pop(ind)
#                 break
        
# print(nums2)
# nums = nums2
# print(nums)
# print(kk)
# kk = len(nums)-nums.count(2)
ind = len(nums)-1
while(ind>=0):
    
    if nums[ind] == val:
        nums.pop(ind)
        print(ind)
        
    ind-=1
print(nums)