# 496. Next Greater Element I pyhton
# https://leetcode.com/problems/next-greater-element-i/description/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2: 
            return []
        
        res = []
        nums2_dic = {v:i for i, v in enumerate(nums2)}
        
        for x in nums1:
            index=nums2_dic[x]+1
            while index < len(nums2) and x >= nums2[index]:
                index += 1
            if index == len(nums2):
                res.append(-1)
            else:
                res.append(nums2[index])
        return res