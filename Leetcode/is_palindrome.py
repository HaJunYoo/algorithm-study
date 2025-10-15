class Solution:
    def isPalindrome(self, s: str) -> bool:
        l_b = ord("a")
        u_b = ord("z")
        num_l_b = ord("0")
        num_u_b = ord("9")

        sentence = []
        for char in s:
            lower_char = char.lower()
            ord_char = ord(lower_char)
            if (l_b <= ord_char <= u_b) or (num_l_b <= ord_char <= num_u_b):
                sentence.append(lower_char)

        if sentence == sentence[::-1]:
            return True
        
        else:
            return False
        