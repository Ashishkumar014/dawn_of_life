// Maximum subarray LC 53 :

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        s = nums[0]
        max_val = nums[0]
        for i in range(1,n):
            if s < 0:
                s = 0 
            s += nums[i]
            if s > max_val:
                max_val = s
        return max_val

// Two sum LC 1:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i,j]

// Add Binary LC 67:

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2) + int(b,2))[2:]

// Valid parenthesis LC 20:

class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for c in s:
            if c == '(' or c == '{' or c == '[':
                st.append(c)

            elif st and ((c == ')' and st[-1] == '(') or (c == '}' and st[-1] == '{') or (c ==']' and st[-1] == '[')):
                st.pop()

            else:
                return False

        return len(st) == 0

// Divide two integers LC 29:
