class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp_s = s.replace(" ", "").lower()
        clean_s = "".join(char for char in temp_s if char.isalnum())
        print(clean_s)
        if len(s) == 1:
            return True

        i = 0
        j = len(clean_s)-1

        while i <= j:
            if clean_s[i] != clean_s[j]:
                return False
            print(clean_s[i]+", "+clean_s[j])
            i += 1
            j -= 1
        return True

        