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

        self.roman_sub_prefixes = ['I', 'X', 'C']


    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        unprocessed_roman_characters = s
        answer = 0

        while unprocessed_roman_characters:
            if unprocessed_roman_characters[0] in self.roman_sub_prefixes:
                roman_sub_chunk = unprocessed_roman_characters[0:2]
                if roman_sub_chunk in self.roman_subs.keys():
                    answer += self.roman_subs[roman_sub_chunk]
                    unprocessed_roman_characters = unprocessed_roman_characters[2:]
                else:
                    answer += self.roman_base_values[unprocessed_roman_characters[0]]
                    unprocessed_roman_characters = unprocessed_roman_characters[1:]
            else:
                answer += self.roman_base_values[unprocessed_roman_characters[0]]
                unprocessed_roman_characters = unprocessed_roman_characters[1:]

        return answer


if __name__ == "__main__":
    sol = Solution()
    #answer = sol.romanToInt("MCMXCIV")
    answer = sol.romanToInt("III")
    print(answer)