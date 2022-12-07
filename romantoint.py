class Solution(object):
    def __init__(self) -> None:

        self.roman_base_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        self.roman_subs = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

        self.roman_sub_prefixes = ['i', 'X', 'C']


    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman_chunk_index = 0

if __name__ == "__main__":
    sol = Solution()
    answer = sol.romanToInt("MCMXCIV")
    print(f"answer: {answer}")