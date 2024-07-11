def find_repeated_sequences(s, k):

    n = len(s)
    
    # Mapping of characters
    mapping = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    
    # Base value
    a = 4

    # Numeric representation of the sequence
    numbers = [0] * n
    for i in range(n):
        numbers[i] = mapping.get(s[i])

    print("\n\tConverted sequence:", numbers)


print(find_repeated_sequences('ACTCT'))