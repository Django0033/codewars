def DNA_strand(dna):
    dna_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    new_dna_strand = []

    for i in dna:
        new_dna_strand.append(dna_dict[i])

    return ''.join(new_dna_strand)

test1 = DNA_strand('AAAA')
test2 = DNA_strand('ATTGC')
test3 = DNA_strand('GTAT')

print(test3)
