class Solution(object):
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        index_i, index_j = 0, 0
        result = []
        while index_i < len(nums1) and index_j < len(nums2):
        	if nums1[index_i] == nums2[index_j]:
        		result.append(nums1[index_i])
          index_i += 1
          index_j += 1
         elif nums1[index_i] > nums2[index_j]:
        		index_j += 1
         else:
        		index_i += 1
        return result
