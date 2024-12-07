#add import
from question_d import get_most_likely_ancestor_consensus

if __name__ == "__main__":
    while True:
        dna_string1 = input("Enter a DNA string (8-16 characters): ").strip()
        if len(dna_string1) < 8 or len(dna_string1) > 16:
            print("Invalid DNA string length.")
            continue

        dna_string2 = input("Enter a DNA substring (4 characters): ").strip()
        if len(dna_string2) != 4:
            print("DNA substring must be exactly 4 characters.")
            continue

        result = get_most_likely_ancestor_consensus(dna_string1, dna_string2)
        print("Substring found at positions:", " ".join(map(str, result)))

        choice = input("Do you want to continue? (yes/no): ").strip().lower()
        if choice != 'yes':
            break
