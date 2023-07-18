from typing import List
from collections import defaultdict, deque
import string

#interview solution
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_list = set(wordList)
        word_list.add(beginWord)

        if endWord not in word_list:
            return []

        queue = deque()
        queue.append([beginWord])
        sequences = list()
        current_level = 0
        words_used_on_current_level = set()
        words_used_on_current_level.add(beginWord)

        while queue:
            sequence_list = queue.popleft()

            if len(sequence_list) > current_level:
                current_level += 1
                for word_ in words_used_on_current_level:
                    word_list.remove(word_)

            word = sequence_list[-1]

            if word == endWord:
                if not sequences:
                    sequences.append(sequence_list)
                else:
                    if len(sequence_list) <= len(sequences[-1]):
                        sequences.append(sequence_list)

            for i in range(0, len(word)):
                word_as_list = list(word)
                for alpha in string.ascii_lowercase:
                    word_as_list[i] = alpha
                    new_word = "".join(word_as_list)
                    if new_word in word_list:
                        sequence_list.append(new_word)
                        words_used_on_current_level.add(new_word)
                        queue.append(sequence_list)
                        sequence_list.pop()

        return sequences
    
#competitive programming solution
class Solution:
    def bfs(self, word_list, beginWord):
        sequence_map = dict()
        queue = deque()
        queue.append([beginWord, 0])

        while queue:
            word, count = queue.popleft()

            sequence_map[word] = count

            for i in range(0, len(word)):
                word_as_list = list(word)
                for alpha in string.ascii_lowercase:
                    word_as_list[i] = alpha
                    new_word = "".join(word_as_list)
                    if new_word in word_list:
                        queue.append([new_word, count+1])
                        word_list.remove(new_word)
        
        return sequence_map

    def dfs(self, word, sequence_list, sequence_map, beginWord, sequences):
        if word == beginWord:
            sequences.append(sequence_list[:])
            return
        
        for i in range(0, len(word)):
            word_as_list = list(word)
            for alpha in string.ascii_lowercase:
                word_as_list[i] = alpha
                new_word = "".join(word_as_list)
                if new_word in sequence_map and sequence_map[new_word] == sequence_map[word]-1:
                    sequence_list.append(new_word)
                    self.dfs(new_word, sequence_list, sequence_map, beginWord, sequences)
                    #dont forget to backtrack!!
                    sequence_list.pop()
        

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_list = set(wordList)

        if beginWord in word_list:
            word_list.remove(beginWord)

        if endWord not in word_list:
            return []

        sequences = list()

        sequence_map = self.bfs(word_list, beginWord)

        self.dfs(endWord, [endWord], sequence_map, beginWord, sequences)

        for seq in sequences:
            seq.reverse()

        return sequences
    
