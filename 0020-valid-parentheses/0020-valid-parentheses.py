class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return False

        stack = []

        for ele in s:
            if ele == "(" or ele == "{" or ele == '[':
                stack.append(ele)
            else:
                if len(stack) > 0:
                    if(ele == ")" and stack[-1] == "(") or (ele == "}" and stack[-1] == "{") or (ele == "]" and stack[-1] == "["):
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        
        return True if not len(stack) else False
        