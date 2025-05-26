def is_valid_square(square):
    if len(square) != 2:
        return False
    row, col = square[0], square[1]
    return row in '12345678' and col in 'abcdefgh'

def validate_chess_dict(chess_dict):
    for start, end in chess_dict.items():
        if not is_valid_square(start):
            print(f"Invalid start square: {start}")
            return False
        if not is_valid_square(end):
            print(f"Invalid end square: {end}")
            return False
    print("All moves are valid.")
    return True

chess_moves={"2b":"1c","2g":"1a","9i":"1a"}
validate_chess_dict(chess_moves)