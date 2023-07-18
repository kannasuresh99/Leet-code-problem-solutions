from typing import List
from collections import deque
import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque()
        word_list = set(wordList)
        queue.append([beginWord, 1])
        if beginWord in word_list:
            word_list.remove(beginWord)

        while queue:
            word, seq_len = queue.popleft()

            if word == endWord:
                return seq_len

            for i in range(0, len(word)):
                word_ = list(word)
                for alpha in string.ascii_lowercase:
                    word_[i] = alpha
                    new_word = "".join(word_)
                    if new_word in word_list:
                        queue.append([new_word, seq_len+1])
                        word_list.remove(new_word)

        return 0
