def rail_fence_encrypt(plaintext, depth):
    if depth <= 1:
        return plaintext
    
    # Create a 2D list (rail fence) to store the pattern
    fence = [['' for _ in range(len(plaintext))] for _ in range(depth)]
    
    row, step = 0, 1
    for char in plaintext:
        fence[row].append(char)
        if row == 0:
            step = 1
        elif row == depth - 1:
            step = -1
        row += step
    
    # Concatenate the rows to get the ciphertext
    ciphertext = ''.join([''.join(r) for r in fence])
    return ciphertext

def rail_fence_decrypt(ciphertext, depth):
    if depth <= 1:
        return ciphertext
    
    # Create a 2D list (rail fence) to mark the positions
    fence = [['' for _ in range(len(ciphertext))] for _ in range(depth)]
    
    # Determine the zigzag pattern to place the markers
    row, step = 0, 1
    for i in range(len(ciphertext)):
        fence[row][i] = '*'
        if row == 0:
            step = 1
        elif row == depth - 1:
            step = -1
        row += step
    
    # Fill the fence with the ciphertext characters
    index = 0
    for r in range(depth):
        for c in range(len(ciphertext)):
            if fence[r][c] == '*':
                fence[r][c] = ciphertext[index]
                index += 1
    
    # Read the plaintext from the fence
    plaintext = ''
    row, step = 0, 1
    for i in range(len(ciphertext)):
        plaintext += fence[row][i]
        if row == 0:
            step = 1
        elif row == depth - 1:
            step = -1
        row += step
    
    return plaintext

# Example usage
plaintext = "Hello World"
depth = 3

encrypted = rail_fence_encrypt(plaintext, depth)
print(f"Encrypted: {encrypted}")

decrypted = rail_fence_decrypt(encrypted, depth)
print(f"Decrypted: {decrypted}")
