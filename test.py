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
    board1 = [1, 1, 1, -1, -1, 0, 0, 0, 0]
    result1 = ai.max_utility(board1, 1)
    print(result1 == 10)

    board2 = [-1, -1, -1, 0, 1, 0, 1, 1, 0]
    result2 = ai.max_utility(board2, 1)
    print(result2 == -10)

    board3 = [-1, 1, -1, 1, 1, 0, 1, 0, 1]
    result3 = ai.max_utility(board3, 1)
    print(result3 == 0)   

    board4 = [1, 1, 0, 0, -1, 0, 0, 0, -1]
    result4 = ai.max_utility(board4, 1)
    print(result4 == 10)

def test_min_utility():
    pass

if __name__ == '__main__':
    test_utility()
    test_max_utility()
    test_min_utility()
