def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    result = ''.join([char for char in input_string if char not in vowels])
    return result

