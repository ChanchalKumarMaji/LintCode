class Solution:
    """
    @param nums: a sorted array
    @param a: 
    @param b: 
    @param c: 
    @return: a sorted array
    """
    def sortTransformedArray(self, nums, a, b, c):
        # Write your code here
        if a == 0 and b >= 0:
            return [a*num*num + b*num + c for num in nums]
        if a == 0 and b < 0:
            return [a*num*num + b*num + c for num in nums][::-1]
        n = len(nums)
        nums1 = []
        nums2 = []
        x = -1 * b / (2 * a)
        for num in nums:
            if num <= x:
                nums1.append(a*num*num + b*num + c)
            else:
                nums2.append(a*num*num + b*num + c)
        if a >= 0:
            nums1 = nums1[::-1]
        else:
            nums2 = nums2[::-1]
        print(nums1, nums2)
        i, j, k = 0, 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                nums[k] = nums1[i]
                i += 1
            else:
                nums[k] = nums2[j]
                j += 1
            k += 1
        while i < len(nums1):
            nums[k] = nums1[i]
            i += 1
            k += 1
        while j < len(nums2):
            nums[k] = nums2[j]
            j += 1
            k += 1
        
        return nums
