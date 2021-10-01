class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(set(sentence)) == 26:
            return True
        else:
            return False
