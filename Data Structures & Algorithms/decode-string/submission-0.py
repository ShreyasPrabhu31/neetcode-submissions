class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substring = ""
                while stack[-1] != "[":
                    substring = stack.pop() + substring
                stack.pop()#To pop the opening parenthesis so that we can get the int digit.

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substring)
        
        return "".join(stack)