class Solution(object):
    def count_occurances(self, input_str):
        counts = {}
        for car in input_str:
            if car in counts.keys():
                counts[car] += 1
            else:
                counts[car] = 1
        return counts

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        counts_s = self.count_occurances(s)
        counts_t = self.count_occurances(t)
        return counts_s == counts_t