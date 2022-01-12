from dataclasses import dataclass
from collections import defaultdict


@dataclass(frozen=True)
class GameState:
    p1pos: int
    p2pos: int
    p1score: int = 0
    p2score: int = 0


def turn(state, copies, roll1, roll2):
    p1pos = (state.p1pos + roll1[0]) % 10
    if not p1pos:
        p1pos = 10
    p1score = state.p1score + p1pos
    copies = copies * roll1[1]

    p2pos = (state.p2pos + roll2[0]) % 10
    if not p2pos:
        p2pos = 10
    p2score = state.p2score + p2pos
    if p1score < 21:
        copies *= roll2[1]

    return GameState(p1pos, p2pos, p1score, p2score), copies


def main():
    rolls = ((3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1))
    wins = [0, 0]
    states = {GameState(7, 6): 1}
    loops = 0
    while states:
        loops += 1
        print(f"Loop {loops}: {len(states)} states.")
        newStates = defaultdict(lambda: 0)
        for state, copies in states.items():
            for roll1 in rolls:
                halfState, halfCopies = turn(state, copies, roll1, (0, 1))
                if halfState.p1score >= 21:
                    wins[0] += halfCopies
                else:
                    for roll2 in rolls:
                        newState, newCopies = turn(state, copies, roll1, roll2)
                        if newState.p2score >= 21:
                            wins[1] += newCopies
                        else:
                            newStates[newState] += newCopies
        states = newStates
    print(wins)
    print(max(wins))


if __name__ == "__main__":
    main()
