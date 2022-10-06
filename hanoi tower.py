class Hanoi_Tower:
    def __init__(self, numberOfRings):
        self.numberOfRings = numberOfRings
        self.towers = [[],[],[]]

        for i in range(numberOfRings):
            self.towers[0].append(i + 1)
        print(self.towers)

    def play(self):
        accessednumber = None
        movetonumber = None
        towerToAccess = input('Choice a tower between 1-3 to access ')
        if '1' in towerToAccess and not(len(self.towers[0]) == 0):
            accessednumber = 0
        elif '2' in towerToAccess and not(len(self.towers[1]) == 0):
            accessednumber = 1
        elif '3' in towerToAccess and not(len(self.towers[2]) == 0):
            accessednumber = 2
        else:
            print('Not a valid input')
        if not(accessednumber == None):
            moveto = input('Choice a tower between 1-3 to move disk ' + str(self.towers[accessednumber][0]) + ' to. ')
            if '1' in moveto:
                movetonumber = 0
            elif '2' in moveto:
                movetonumber = 1
            elif '3' in moveto:
                movetonumber = 2
            else:
                print('Not a valid input')
        if not(accessednumber == None) and not(movetonumber == None):
            if len(self.towers[movetonumber]) == 0:
                self.towers[movetonumber].insert(0, self.towers[accessednumber].pop(0))
            elif self.towers[accessednumber][0] < self.towers[movetonumber][0]:
                self.towers[movetonumber].insert(0, self.towers[accessednumber].pop(0))
            else:
                print('number in that slot is to big')

        print(accessednumber)
        print(movetonumber)
        print(self.towers)
    'Extra Credit'
    def autoSolve(self):
        n = 0
        passednum = 0
        while not(len(self.towers[1]) == self.numberOfRings):
        #for a in range(100):
            moved = False
            for b in range(1,3):
                if len(self.towers[n%3]) > 0:
                    if not (passednum == self.towers[n % 3][0]):
                        if len(self.towers[(n+b)%3]) == 0:
                            passednum = self.towers[n % 3].pop(0)
                            self.towers[(n+b)%3].insert(0, passednum)
                            moved = True
                        elif self.towers[n%3][0] < self.towers[(n+b)%3][0]:
                            passednum = self.towers[n % 3].pop(0)
                            self.towers[(n+b)%3].insert(0, passednum)
                            moved = True
            print(passednum)
            if len(self.towers[2]) == self.numberOfRings:
                passednum = 0
                n = 2
            elif not moved:
                n += 1
            else:
                n= 0
            print(a, ')', self.towers)

ringNumber = int(input('Enter hpw many rings you will like? '))
a = Hanoi_Tower(ringNumber)
answer = input('Do you want to play the hanoi tower or have it solved? ')

if 'play' in answer.lower():
    while not(len(a.towers[1]) == a.numberOfRings):
        a.play()
elif 'solve' in answer.lower():
    a.autoSolve()
else:
    'Not Valid'


