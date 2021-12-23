from collections import defaultdict
state = [defaultdict(int), defaultdict(int)]
state[0][(0, pos1)] = 1   # this is player 1's initial state
state[1][(0, pos2)] = 1   # this is player 2's initial state

r, other_ct, wins = 0, 1, [0, 0]
while other_ct:
    new_state = defaultdict(int)
    for score in range(21):
        for pos in range(1, 11):
            for die, ct in ((3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)):
                new_pos = (pos + die - 1) % 10 + 1
                new_score = score + new_pos
                if new_score < 21:
                    new_state[(new_score, new_pos)] += ct*state[r%2][(score, pos)]
                else:
                    wins[r%2]+= ct*other_ct*state[r%2][(score, pos)]
    state[r%2] = new_state
    r += 1
    other_ct = sum(state[(r+1)%2].values())
print("2:", max(wins))