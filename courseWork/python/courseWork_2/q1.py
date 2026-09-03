# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i !=
# j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.


def threeSum(nums):
    nums.sort()
    result=[]

    for i in range(len(nums)-2):

        if i>0 and nums[i]==nums[i-1]:
            continue

        left=i+1
        right=len(nums)-1

        while left<right:
            total=nums[i]+nums[left]+nums[right]

            if total==0:
                result.append([nums[i],nums[left],nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left+=1
                right-=1

            elif total<0:
                left+=1

            else:
                right-=1

    return result

    
n=list(int(x) for x in input("enter the numbers comma separated: ").split(','))
print(threeSum(n))