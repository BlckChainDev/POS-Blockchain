from ProofOfStake import ProofOfStake
from Lot import Lot
import string
import random


def getRandomString(length):
    letters = string.ascii_lowercase
    resultString = ''.join(random.choice(letters) for i in range(length))
    return resultString


if __name__ == '__main__':
    pos = ProofOfStake()
    pos.update('bob', 10)
    pos.update('alice', 100)

    bobWins = 0
    aliceWins = 0

    for i in range(100):
        forger = pos.forger(getRandomString(i))
        if forger == 'bob':
            bobWins += 1
        elif forger == 'alice':
            aliceWins += 1
        
    print('bob won: ' + str(bobWins) + ' times')
    print('alice won: ' + str(aliceWins) + ' times')
