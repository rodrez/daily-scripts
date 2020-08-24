def encrypt(message):
    """Converts a string to an number-encrypted message

    Args:
        message (str): Any string messae

    Returns:
        str: Encoded message as a string of number pairs
    """

    # Generate a public key
    p = 3
    q = 11
    n = p * q 

    # Selection of exponent e:
    # e is an integer that is not factor n. We take e = 9
    # Public key is made up of n in this case it should be n as = (3*11) = 33 and e as 9

    e = 9

    # Generate Private Key
    # Calculation of ⏀(n)
    n_o = (p - 1) * (q - 1)
    # print(n_o)

    # Calculation of (k**⏀(n) + 1)/e for some integer k
    k = 4

    d = (k*n_o+1)/e
        
    alpha_code = {'a': '01', 'b': '02', 'c': '03', 'd': '04', 
    'e': '05', 'f': '06', 'g': '07', 'h': '08', 'i': '09', 
    'j': '10', 'k': '11', 'l': '12', 'm': '13', 'n': '14', 
    'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19', 
    't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 
    'y': '25', 'z': '26', ' ': '27', '.': '28', ',': '29'}

    encrypted_message = []

    for letter in message:
        encrypted_letter = (int(alpha_code[letter]) ** e) % n
        encrypted_message.append(str(encrypted_letter))
    return " ".join(encrypted_message)

print(encrypt("this is an encrypted message"))


def decryption(encrypted_message, e):
    """Decrypts a message using RSA and the integer e. 

    Args:
        encrypted_message (list, string): A list of number or string - encrypted message.
        For better usability, pass pairs of numbers or strings into the list.
        e (int): an integer that is not factor n.
        

    Returns:
        (str): Decrypted message
    """
    # Generate a public key
    p = 3
    q = 11
    n = p * q 

    # Selection of exponent e:
    # e is an integer that is not factor n. We take e = 9
    # Public key is made up of n and e in this case it should be 33 and 9

    e = 9

    # Generate Private Key
    # Calculation of ⏀(n)
    n_o = (p - 1) * (q - 1)
    # print(n_o)

    # Calculation of (k**⏀(n) + 1)/e for some integer k
    k = 4

    d = (k*n_o+1)/e

    alpha_code_num = {'01': 'a', '02': 'b', '03': 'c', '04': 'd', '05': 'e',
                      '06': 'f', '07': 'g', '08': 'h', '09': 'i', '10': 'j',
                      '11': 'k', '12': 'l', '13': 'm', '14': 'n', '15': 'o',
                      '16': 'p', '17': 'q', '18': 'r', '19': 's', '20': 't',
                      '21': 'u', '22': 'v', '23': 'w', '24': 'x', '25': 'y',
                      '26': 'z', '27': ' ', '28': '.', '29': ','}

    decrypted_message = []

    message_length = len(encrypted_message)

    if type(encrypted_message) == str:
        encrypted_message = encrypted_message.split(" ")

    for pair in encrypted_message:

        em_to_num = int(pair) ** d % n 
        num_converted = '%02d' % em_to_num
        letter_to_number = alpha_code_num[num_converted]

        decrypted_message.append(str(letter_to_number))
        
    return "".join(decrypted_message)

print(decryption())
