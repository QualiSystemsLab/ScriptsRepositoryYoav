import random

class horse():
    def __init__(self):
        self.speed = round(random.random()*100000)
        self.ID = 0

class riddle():
    def __init__(self):
        self.batch = []
        self.solved = 0
        self.races = 0
        for i in range(25):
            self.batch.append(horse())
            self.batch[i].ID = i

    def print_results(self):
        newlist = sorted(self.batch, key=lambda x: x.speed, reverse=True)
        for h in newlist:
            print ('horse ID {0} with speed {1} '.format(h.ID, h.speed))

    def check_guess(self, sequence):
        newlist = sorted(self.batch, key=lambda x: x.speed, reverse=True)
        answer = 'yes'
        for j in range(3):
            if newlist[j].ID != int(sequence[j]):
                answer = 'no'
        if answer == 'yes':
            print ('congrats! you got it . it took you {0} races'.format(self.races))
            self.solved = 1
        return answer

    def race(self, participants):
        if participants.__len__() != 5:
            print ('race needs to have 5 participants!')
            raise Exception('a')
        answer = []
        fastest = horse()
        while participants:
            fastest_speed = 0
            for participant in participants:
                if fastest_speed < self.batch[int(participant)].speed:
                    fastest = self.batch[int(participant)]
                    fastest_speed = self.batch[int(participant)].speed
            answer.append(fastest)
            participants.remove(str(fastest.ID))
        peckinng_order = ','.join([str(a.ID) for a in answer])
        self.races = self.races + 1
        return peckinng_order


myriddle = riddle()
while myriddle.solved == 0:
    response = raw_input("what do you want to do?\n")
    if response == 'q':
        myriddle.solved = 1
    elif response in ['race', 'r']:
        race_seq = raw_input('please enter sequence\n')
        try:
            answer = myriddle.race(race_seq.split(','))
            print answer
        except Exception as e:
            print 'sorry , could not do that'
    elif response in ['list', 'l']:
        myriddle.print_results()
    elif response in ['help', 'h']:
        print ('this is help')
    elif response in ['guess', 'g']:
        guess_seq = raw_input('please enter sequence\n')
        try:
            result = myriddle.check_guess(guess_seq.split(','))
            print result
        except Exception as e:
            print 'sorry , could not do that'
    else:
        print 'not valid. let\'s  try again\n'







pass