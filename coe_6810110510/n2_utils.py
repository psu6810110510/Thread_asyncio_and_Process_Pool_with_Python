def find_second_largest(numbers: list[int]) -> int | None:
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    for i in numbers:
        if not isinstance(i, int):
            raise TypeError("All elements in the list must be integers")
        
    if len(numbers) < 2:
        return None
        
    unique_nums = list(set(numbers))
    if len(unique_nums) < 2:
        return None
        
    unique_nums.sort(reverse=True)
    return unique_nums[1]