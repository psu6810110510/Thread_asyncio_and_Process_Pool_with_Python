def cat_and_mouse(x: int, y: int, z: int) -> str:
    assert 1 <= x <= 100 and 1 <= y <= 100 and 1 <= z <= 100, "x, y, z must be between 1 and 100"
    if abs(x - z) < abs(y - z):
        return "Cat A"
    elif abs(x - z) > abs(y - z):
        return "Cat B"  
    elif abs(x - z) == abs(y - z):
        return "Mouse C"
    return "Cat A"


if __name__ == "__main__":
    line_str = input("Enter A B C:")
    line = map(int, line_str.split())

    result = cat_and_mouse(*line)
    print("Result:", result)