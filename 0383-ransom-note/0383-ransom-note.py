class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteMap = Counter(ransomNote)
        magazineMap = Counter(magazine)
        
        for key, val in ransomNoteMap.items():
            if key not in magazineMap:
                return False
            if magazineMap[key] < val:
                return False
        return True