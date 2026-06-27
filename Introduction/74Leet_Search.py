
# ============== Leet code problem 74 Search a 2D matrix =================
# 
# Problem====


# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.
 
# example :
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# ==========  normal Brute force approach ================ in normal python

# ======== main class==================

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            for col in row:
                if target == col:
                    return True
        return False

# Take matrix input ================
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter the matrix values row by row:")

for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Take target input
target = int(input("Enter target value: "))

# Use your solution
obj = Solution()
result = obj.searchMatrix(matrix, target)

print("Found:", result)


    
