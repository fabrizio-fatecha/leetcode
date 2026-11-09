"""
118. Pascal's Triangle
Easy
Topics
premium lock icon
Companies
You are given an integer numRows.

Return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it and the first and last number on each row must be equal to 1, as shown below:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30

1-  1
2-  1   1
3-  1   2   1
4-  13      31
5-  14  6   41
6-  1510    1051

index
always 2 ones on each side


"""

# NOT FINISHED YET


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        o = []
        for row in range(numRows):
            if row == 0:
                o.append([1])
            elif row > 1:
                inserts = []
                for _ in range(row):
                    inserts.append(1)
                o.append(inserts)

        for i in range(len(o)):

            length = i
            length_required = i/2
            is_even = i % 2 == 0
            value = o[i]

            print(f"length = {length} , length_required = {length_required} ,  is_even = {is_even} , value = {value}")
            
            for j in range(length_required):

            # i believe the solution is into iterating previous elements 2 by two to create the new arrays

i = Solution()
i.generate(30)