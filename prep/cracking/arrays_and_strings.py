class Dice():
    from random import randrange

    @classmethod
    def roll(cls):
        return cls.randrange(1, 7, 1)

class Error(Exception):
    pass

class TabAlreadyClosedError(Error):
    def __init__(self, tab):
        self.tab = tab

class SelectionNotEqualToDiceTotalError(Error):
    pass

class Box():
    def __init__(self):
        self.status = range(1,13)

    def move_is_possible(self, dice_total):
        return self.combinations_exist(dice_total, self.status)

    def combinations_exist(self, n, tabs, combos=False):
        if sum(tabs) == n:
            return True
        else:
            for i in range(len(tabs)):
                temp_tabs = tabs[:i] + tabs[i+1:]
                combos = self.combinations_exist(n, temp_tabs, combos)
                if combos == True:
                    break

        return combos

    def prepare_move(self, chosen_tabs, dice_total):
        status = list(self.status)
        for i in chosen_tabs:
            if i not in status:
                raise TabAlreadyClosedError(i)
            else:
                status.remove(i)
        if sum(chosen_tabs) != dice_total:
            raise SelectionNotEqualToDiceTotalError()
        return status

    def move(self, chosen_tabs, dice_total):
        self.status = self.prepare_move(chosen_tabs, dice_total)

    def score(self):
        return sum(self.status)

def play():
    box = Box()
    while True: # game not over yet
        first = Dice.roll()
        second = Dice.roll()
        dice_total = first + second
        print box.status
        print "Your roll was", first, second, "for a total of:", dice_total
        if box.move_is_possible(dice_total):
            while True:
                try:
                    selection = raw_input("Provide your selected integers separated by spaces:")
                    chosen_tabs = map(int, selection.split())
                    box.move(chosen_tabs, dice_total)
                    break
                except TabAlreadyClosedError as e:
                    print "Sorry. Tab:", e.tab, "is already closed. Try again."
                except SelectionNotEqualToDiceTotalError:
                    print "Sorry. Your selection does not equal the dice total. Try again."
        else:
            print "Game over. Your final score was:", box.score()
            break

if __name__ == '__main__':
    play()
