import secrets
import string
import math

def generate_password(length, upper = True, lower = True, 
                      digits = True, special = True):

    required_chars = []

    try:
        length = int(length)

    except ValueError:
       raise ValueError("Password length must be a whole number")
    
    chars = ""

    if upper:
        chars += string.ascii_uppercase
        required_chars.append(secrets.choice(string.ascii_uppercase))

    if lower:
        chars += string.ascii_lowercase
        required_chars.append(secrets.choice(string.ascii_lowercase))
    if digits:
        chars += string.digits
        required_chars.append(secrets.choice(string.digits))

    if special:
        chars += string.punctuation
        required_chars.append(secrets.choice(string.punctuation))

    if not chars:
        raise ValueError("Select at least one character type")

    if length < 8 or length > 128:
        raise ValueError("Password needs to be between 8 and 128 characters long")


    password = required_chars[:]

    while len(password) < length:
        password.append(secrets.choice(chars))

    secrets.SystemRandom().shuffle(password)

    password = "".join(password)

    print(len(password))

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



#tests = [8, 12, 16, 24, 32]

#for test in tests:

    password, chars, length = generate_password(test)
    entropy = calculate_entropy(chars, length)
    strength, progress = get_password_strength(entropy)

    #print(f"Strength: {strength}")
    #print(f"Strength: {progress:.0%}")

    #print(f"Salasana: {password}")
    #print(f"Merkkijoukon koko: {len(chars)}")

    #print(f"Entropia: {entropy:.2f}")

