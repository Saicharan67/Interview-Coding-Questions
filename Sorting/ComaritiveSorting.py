#Comparators are used to compare two objects. In this challenge, we'll create a comparator and use
#it to sort an array. The Player class is provided in the editor below. It has two fields:

# hackerrank question 

from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name=name
        self.score=score
    def __repr__(self):
        
        return [self.name,self.score]
        
    def comparator(a, b):
        if a.score>b.score:
            return -1 
        elif a.score<b.score:
            return 1
        else:
            if a.name>b.name:
                return 1
            else:
                return -1

n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)