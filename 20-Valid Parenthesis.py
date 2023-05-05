class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        since s is supposed to just contains the characters ()[]{}, if the first
        if loop fails, no charcter will be appended to the stack list, leaving 
        us with an empty stack list.
        Then, will check if the character ) } } has a corresponding ( [ {
        """
        t = s
        stack = []
        for char in t:
            if char=='(' or char=='[' or char=='{':
                stack.append(char)
            else:
                if not stack:
                    return False
                elif char==')' and stack[-1]=='(':
                    stack.pop()
                elif char==']' and stack[-1]=='[':
                    stack.pop()
                elif char=='}' and stack[-1]=='{':
                    stack.pop()
                else:
                    return False
        return True