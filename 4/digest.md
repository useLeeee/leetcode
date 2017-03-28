+ 有没有更优雅的处理空输入的方式？
+ 有些输入错误有可能是一开始设计时逻辑就不清晰导致的
+ INT_MIN、INT_MAX在c语言中表示无穷大、无穷小等，python无穷大和无穷小为float('inf')和float('-inf')
+ 一般边界情况仅有0的情况，如果再有过多的边界情况有可能是逻辑不清晰
+ 二分查找的基础有问题，不是移动的尺度越来越小，而是移动的区间越来越小！




* excellent:使用调用自身的方式，避免写if判断并写重复代码
·if (N1 < N2) return findMedianSortedArrays(nums2, nums1);	// Make sure A2 is the shorter one.·

