def generate(length, string = ""):
    if len(string) == length:
        return [ string ]
    
    return generate(length, string + 'A') + generate(length, string + 'B') + generate(length, string + 'C')

print(generate(2))