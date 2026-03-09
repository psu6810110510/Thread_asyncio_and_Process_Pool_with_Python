def count_vowels(text: str) -> int:
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

if __name__ == "__main__":
    input_text = input("Enter a string: ")
    vowel_count = count_vowels(input_text)
    print(f"The number of vowels in the input string is: {vowel_count}")