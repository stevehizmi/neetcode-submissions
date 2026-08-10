class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hist = self._convert_to_dict(s)
        t_hist = self._convert_to_dict(t)

        return s_hist == t_hist

    def _convert_to_dict(self, input: str) -> dict:
        histogram = {}
        for letter in input:
            if letter not in histogram:
                histogram[letter] = 1
            else:
                histogram[letter] += 1
        return histogram
        