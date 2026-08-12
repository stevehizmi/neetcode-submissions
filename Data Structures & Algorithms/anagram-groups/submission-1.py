class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            key = tuple(sorted(self._convert_to_dict(s).items()))
            res[key].append(s)
        return list(res.values())

    def _convert_to_dict(self, string: str) -> dict:
        if not string:
            return {}

        hist = {}
        for letter in string:
            if letter not in hist:
                hist[letter] = 1
            else:
                hist[letter] += 1
        return hist