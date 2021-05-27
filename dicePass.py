from os import replace
import random

def read_pws(file):
    with open(file, 'r') as f:
        data = f.read()
        data = ' '.join(data.split())
        data = data.split(' ')
        dict = {data[i]:data[i+1] for i in range(0, len(data), 2)}
        
    return dict

 

def roll_dice():
    return random.randrange(1,7776)

if __name__ == '__main__':
    data = read_pws('word_list.txt')
    word_amt = int(input())
    combos = list(data.keys())
    c = 0
    pw = ''
    while c < word_amt:
        dice = combos[roll_dice()]
        pw = pw + data[dice]
        c = c + 1
    print(pw)
