"""
A presentation is occurs for n hours and has a starting time and ending time.
A person can attend only one presentation at a given hour. 
There is no delay between changing to another presentation.

Given 2 0-indexed arrays scheduleStart and scheduleEnd which 
represents a presentation as an index, determine the maximum 
number of presentations a person can go to.
"""


from pprint import pprint

class Presentation:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.diff = end - start
    
    def conflicts(self, other):
        '''The boundaries of each presentation can overlap.'''
        isSafe = self.start < other.end and other.start < self.end
        return isSafe

    def __repr__(self):
        return f"{self.start} {self.end} {self.diff}"

    def __lt__(self, other):
        return self.diff < other.diff

    def __str__(self):
        return f"{self.start} {self.end} {self.diff}"

def main(sStart, sEnd):
    # group start and ends together and sort by length ascending
    diffs = []
    for i in range(len(sStart)):
        new = Presentation(sStart[i], sEnd[i])
        diffs.append(new)
    
    diffs.sort()
    
    # from the shortest presentation onwards, fill schedule up.
    efficient = [diffs[0]]
    for diff in diffs[1:]:
        conflicts = False
        for s in efficient:
            if s.conflicts(diff):
                conflicts = True
                break
        
        if not conflicts:
            efficient.append(diff)

    return len(efficient)  


if __name__ == '__main__':
    sStart = [0, 1, 2, 3, 4]
    sEnd = [1, 2, 3, 5, 5]
    ret = main(sStart, sEnd)
    print(ret)