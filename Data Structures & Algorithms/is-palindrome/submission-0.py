class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        ptr1, ptr2 = 0, len(s) -1

        while ptr1 < ptr2:
            if (not s[ptr1].isalnum()):
                ptr1 += 1
            elif (not s[ptr2].isalnum()):
                ptr2 -= 1
            else:
                if((s[ptr1].lower()) != (s[ptr2].lower())):
                    return False
                else:
                    ptr1 += 1
                    ptr2 -= 1
        
        return True
            
        