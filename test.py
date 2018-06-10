import core
import ai

def test_available_ply():
    board1 = core.new_board()
    result1 = core.available_ply(board1)

    print(result1)

def test_utility():
    board1 = [1, 1, 1, -1, -1, 0, 0, 0, 0]
    result1 = ai.utility(board1)
    print(result1 == 10)

    board2 = [-1, -1, -1, 0, 1, 0, 1, 1, 0]
    result2 = ai.utility(board2)
    print(result2 == -10)

    board3 = [-1, 1, -1, 1, 1, 0, 1, 0, 1]
    result3 = ai.utility(board3)
    print(result3 == 0)

def test_max_utility():
    # game terminated, firsthand wins
    board1 = [1, 1, 1, -1, -1, 0, 0, 0, 0]
    result1 = ai.max_utility(board1)
    print(result1 == 10)

    # game terminated, secondhand wins
    board2 = [-1, -1, -1, 0, 1, 0, 1, 1, 0]
    result2 = ai.max_utility(board2)
    print(result2 == -10)

    # game terminated, tie
    board3 = [1, -1, -1, -1, 1, 1, 1, 1, -1]
    result3 = ai.max_utility(board3)
    print(result3 == 0)   

    # one-ply to terminate, firsthand will win
    board4 = [1, 1, 0, -1, -1, 0, 0, 0, 0]
    result4 = ai.max_utility(board4)
    print(result4 == 10)

    # two-plies to terminate, will tie
    board5 = [1, -1, 1, 0, -1, 0, 0, 0, 0]
    result5 = ai.max_utility(board5)
    print(result5 == 0)

def test_min_utility():
    # game terminated, firsthand wins
    board1 = [1, 1, 1, -1, -1, 0, 0, 0, 0]
    result1 = ai.min_utility(board1)
    print(result1 == 10)

    # game terminated, secondhand wins
    board2 = [-1, -1, -1, 0, 1, 0, 1, 1, 0]
    result2 = ai.min_utility(board2)
    print(result2 == -10)

    # game terminated, tie
    board3 = [1, -1, -1, -1, 1, 1, 1, 1, -1]
    result3 = ai.min_utility(board3)
    print(result3 == 0)

    # one-ply to terminate, secondhand will win
    board4 = [1, 1, 0, -1, -1, 0, 0, 0, 1]
    result4 = ai.min_utility(board4)
    print(result4 == -10)

if __name__ == '__main__':
    test_utility()
    test_max_utility()
    test_min_utility()
