# # vc_count: int = int(input())
# # vc_m = []
# # p_m = []
# # count = 0

# # if (vc_count > 0):
# #     vc_m.append(input())

# # for x in vc_m:
# #     print(x)
# inp = [1, 5, 7, 8, 15]
# target = 20
# arr = []

# for x in range(len(inp)):
#     for y in range(x, len(inp)):
#         if (inp[x] + inp[y] == target) and (inp[x]/2 != inp[y]/2):

#             # arr.append(inp.index(inp[x]))
#             # arr.append(inp.index(inp[y]))
#         else:
#             pass

# # print(arr)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        list_n = []
        for x in range(len(nums)):
            for y in range(x, len(nums)):
                if (nums[x] + nums[y] == target) and (nums[x]/2 != nums[y]/2):
                    list_n.append(nums.index(nums[x]))
                    list_n.append(nums.index(nums[y]))
        return list_n


if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], 9))
