class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        stat = { }
        for i, character in enumerate(s):
            if character in stat:
                stat[character] = i
            else:
                stat[character] = i - stat[character] - 1
                if stat[character] != distance[ord[character] - ord('a')]:
                    return False
        return True