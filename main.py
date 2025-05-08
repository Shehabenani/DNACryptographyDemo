# dna_simple_encoding.py

# DNA base encoding scheme: 2 bits per base
binary_to_dna = {
    '00': 'A',
    '01': 'T',
    '10': 'C',
    '11': 'G'
}

dna_to_binary = {v: k for k, v in binary_to_dna.items()}


def text_to_binary(text: str) -> str:
    """Convert text to a binary string (8 bits per character)."""
    return ''.join(format(ord(char), '08b') for char in text)


def binary_to_dna_sequence(binary: str) -> str:
    """Convert a binary string to a DNA sequence using 2-bit encoding."""
    return ''.join(binary_to_dna[binary[i:i+2]] for i in range(0, len(binary), 2))


def dna_to_binary_sequence(dna: str) -> str:
    """Convert a DNA sequence back to a binary string."""
    return ''.join(dna_to_binary[base] for base in dna)


def binary_to_text(binary: str) -> str:
    """Convert a binary string (8 bits per char) back to text."""
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(b, 2)) for b in chars)


def main():
    message = "HELLO"
    print("Original Message:", message)

    
    binary = text_to_binary(message)
    print("Binary:", binary)

    dna = binary_to_dna_sequence(binary)
    print("Encoded DNA Sequence:", dna)

    
    decoded_binary = dna_to_binary_sequence(dna)
    decoded_message = binary_to_text(decoded_binary)
    print("Decoded Message:", decoded_message)


if __name__ == "__main__":
    main()