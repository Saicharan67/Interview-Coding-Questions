def new_func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = 0
        b = 0
        lefta = n
        leftb = n
        s = list(map(int, input()))
        for i in range(1, len(s)+1):
            if i % 2 == 0:
                a += s[i]
                lefta -= 1
            else:
                b += s[i]
                leftb -= 1
            if a > b+leftb or b > a+lefta or (a == b and i == 2*n):
                break

        print(i)


new_func()

# class EngineeringProgramming:
#     def __init__(self) -> None:
#         self.quizes = []

#     def addResults(self, quiz):
#         self.quizes.append(quiz)

#     def getNoOfQuizzes(self):
#         print(len(self.quizes))


# ep = EngineeringProgramming()
# ep.addResults([5, 6, 7, 8])
# ep.addResults([5, 4, 7, 8, 3, 6])
# ep.addResults([10, 6, 8, 9, 10, 7])
# ep.addResults([9, 4, 10, 8, 3, 6])
# ep.addResults([10, 6, 8, 6, 7, 7, 10])
# ep.getNoOfQuizzes()
