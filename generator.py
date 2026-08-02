import secrets
import string
import math

def generate_password(length, upper = True, lower = True, 
                      digits = True, special = True):

    try:
        length = int(length)

    except ValueError:
       raise ValueError("Password length must be a whole number")
    
    chars = ""

    if upper:
        chars += string.ascii_uppercase

    if lower:
        chars += string.ascii_lowercase

    if digits:
        chars += string.digits

    if special:
        chars += string.punctuation

    if not chars:
        raise ValueError("Select at least one character type")

    if length < 8 or length > 128:
        raise ValueError("Password needs to be between 8 and 128 characters long")


    password = ""

    for _ in range(length):
        password += secrets.choice(chars)

    return password, chars, length
    

def calculate_entropy(chars, length):
    charset = len(chars)

    entropy = length * math.log2(charset)

    return entropy

def get_password_strength(entropy):
    progress = min(entropy / 128, 1.0)

    if entropy < 40:
        name = "Weak"

    elif entropy < 80:
        name = "Moderate"

    else:
        name = "Strong"

    return name, progress



tests = [8, 12, 16, 24, 32]

for test in tests:

    password, chars, length = generate_password(test)
    entropy = calculate_entropy(chars, length)
    strength, progress = get_password_strength(entropy)

    #print(f"Strength: {strength}")
    #print(f"Strength: {progress:.0%}")

    #print(f"Salasana: {password}")
    #print(f"Merkkijoukon koko: {len(chars)}")

    #print(f"Entropia: {entropy:.2f}")

