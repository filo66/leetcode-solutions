class Solution:
    def findMedianSortedArrays(self, nums1:list, nums2:list):
        self.nums1 = nums1
        self.nums2 = nums2

        m = len(nums1)
        n = len(nums2)

        if 0<=m<=1000 and 0<=n<=1000:
            total_lst = nums1+nums2
            total_lst.sort()

            if len(total_lst)%2 == 1:
                index_median = int(((len(total_lst)+1)/2)-1)
                return total_lst[index_median]
            else:
                st1_index = int((len(total_lst)/2)-1)
                nd2_index = int((len(total_lst)/2))

                avarage = (total_lst[st1_index]+total_lst[nd2_index])/2

                return avarage
          
