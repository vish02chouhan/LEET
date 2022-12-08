'''
Find the sum of first n natural numbers
'''


def sumOfN(n):
    dp = [0] * (n+1)

    dp[0] = 0

    for idx in range(1,len(dp)):
        dp[idx] = dp[idx-1] + idx

    print(dp)


sumOfN(6)


#flatten linked list test case  in python
# # Definition for a Node.
# class Node:
#     def __init__(self, val=None, prev=None, next=None, child=None):
#         self.val = val
#         self.prev = prev
#         self.next = next
#         self.child = child
#   
# class Solution:
