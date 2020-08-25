#PF-Prac-6
def list123(nums):
    return "123" in ''.join([str(x) for x in nums])

nums=[1,2,3,4,5]
print(list123(nums))
