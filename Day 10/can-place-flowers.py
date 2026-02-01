#https://leetcode.com/problems/can-place-flowers/


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        flowerbed_size = len(flowerbed)
        for i in range(flowerbed_size):
            if n <= 0:
                break
            a = i == 0 or flowerbed[i - 1] == 0
            b = i == flowerbed_size - 1 or flowerbed[i + 1] == 0
            if a and b and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0
# class Solution:
#     def canPlaceFlowers(flowerbed, n):
#       bed = [0] + flowerbed + [0]

#       count = 0
#       zeros = 0

#       for x in bed:
#           if x == 0:
#               zeros += 1
#           else:
#               if zeros > 0:
#                   count += (zeros - 1) // 2
#               zeros = 0

#       count += (zeros - 1) // 2

#       return count >= n
 #or

# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         if n == 0:
#             return True
#         for i in range(len(flowerbed)):
#             if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
#                 flowerbed[i] = 1
#                 n -= 1
#                 if n == 0:
#                     return True
#         return False
