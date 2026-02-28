#https://leetcode.com/problems/string-to-integer-atoi/
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip() 
        if not s:
            return 0
        sign = 1
        i = 0
        if s[0] == "-":
            sign = -1
            i += 1
        elif s[0] == "+":
            i += 1

        num = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            num = num * 10 + digit
            i += 1

        return sign * num

#this does't work 
#class Solution:
#     def myAtoi(self, n: str) -> int:
#         c=n.replace(" ", "") and n.replace("0","")
#         ch="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ +-."
#         temp=""
#         for c in n:
#             if not n or not n[0].isdigit():
#                 print(0)
#             if c in ch:
#                 break
#                 temp+=c
#         return(temp)
