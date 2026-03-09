def find_second_largest(numbers: list[int]) -> int | None:
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    if len(numbers) < 2:
        return None
        
    unique_nums = list(set(numbers)) # ตัดตัวซ้ำทิ้ง
    if len(unique_nums) < 2:
        return None
        
    unique_nums.sort(reverse=True)
    return unique_nums[1]