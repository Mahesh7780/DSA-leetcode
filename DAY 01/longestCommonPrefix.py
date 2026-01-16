#  https://leetcode.com/problems/longest-common-prefix/?roomId=lwCIGB


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        # Take the shortest string (prefix can't be longer than this)
        shortest = min(strs, key=len) # flow

        for i in range(len(shortest)): # 3
            for s in strs: #flower #flow
                if s[i] != shortest[i]: #S[f] sh[f] 
                    return shortest[:i]

        return shortest



# class Solution:
#     def longestCommonPrefix(self, strs):
#         if not strs:
#             return ""
            
#             short=min(strs)
#             n=len(short)
#             for i in range (n):
#                 for s in strs:
#                     if s[i] != short[i]:
#                         return short[:i]
#             return short
            
# class Solution:
#     def longestCommonPrefix(self, strs):
#         if not strs:
#             return ""

#         shortest = min(strs, key=len)
#         l=len(shortest) #3
#         for i in range(l):
#             for s in strs:
#                 if s[i] != shortest[i]:
#                     return shortest[:i]

#         return shortest


# # -------- driver code (THIS PART IS IMPORTANT) --------
# if __name__ == "__main__":
#     sol = Solution()

#     # Test cases
#     print(sol.longestCommonPrefix(["flower", "flow", "flight"]))  # fl
#     print(sol.longestCommonPrefix(["dog", "racecar", "car"]))     # ""
#     print(sol.longestCommonPrefix(["interview", "internet", "internal"]))  # inte
