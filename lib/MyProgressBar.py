
class MyProgressBar:
    def __init__(self, lenth, count):
        self.lenth = lenth
        self.count = count

        for i in range(count):
            count_ = 0
            for j in range(lenth):
                count_ += 1
                print('-' * 20)
                print('|' + '#' * count + f'{i (count)}')
                print('-' * 20)