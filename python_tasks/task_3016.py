from collections import Counter


class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        letter_seen = 0
        count = 0
        hashmap = Counter(word)
        for _, value in hashmap.most_common():
            letter_seen += 1
            count += value * ((letter_seen // 8) + (letter_seen % 8 > 0))
        return count
