#write functions here, don't add input('') statements here!
def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    indices = []
    for i in range(len(dna_string1) - len(dna_string2) + 1):
        if dna_string1[i:i+len(dna_string2)] == dna_string2:
            indices.append(i + 1)
    return indices
