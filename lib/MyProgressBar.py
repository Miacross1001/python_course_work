import os
import time

class MyProgressBar:
    def __init__(self, list):
        self.list = list
        self.global_count = 0

    def _oper_text(self, string: str):
        self.string = string
        print(f'{string}...:')

    def Bar(self):
        os.system('CLS||clear')
        print('Process uploading...')
        if self.global_count <= len(self.list):
            print('|' + '#' * 2 * self.global_count, end = ' ')
            print(f'({self.global_count/len(self.list)*100}% / 100%)' + '|')
            self.global_count += 1

    def oper_text(self, string: str):
        print(f'{string}...:')



