# DES Initial and Final Permutation Tables
INITIAL_PERMUTATION = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

FINAL_PERMUTATION = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

def permute(block, permutation_table):
    """
    Permutes the input block according to the permutation table.
    
    Parameters:
    block (str): A binary string representing the block to permute.
    permutation_table (list): A list representing the permutation table.
    
    Returns:
    str: A binary string representing the permuted block.
    """
    return ''.join(block[i - 1] for i in permutation_table)

def main():
    # Example 64-bit block (in binary)
    block = '0000000100100011010001010110011110001001101010111100110111101111'
    print("Original Block:       ", block)
    
    # Perform initial permutation
    initial_permuted_block = permute(block, INITIAL_PERMUTATION)
    print("After Initial Permutation: ", initial_permuted_block)
    
    # Perform final permutation (which is the inverse of initial permutation)
    final_permuted_block = permute(initial_permuted_block, FINAL_PERMUTATION)
    print("After Final Permutation:   ", final_permuted_block)
    
    # Verify that the final permuted block matches the original block
    if final_permuted_block == block:
        print("Final permutation matches the original block.")
    else:
        print("Final permutation does not match the original block.")

if __name__ == "__main__":
    main()