def DNA_strand(dna):
    return dna.translate(str.maketrans("ATCG", "TAGC"))

test1 = DNA_strand('AAAA')
test2 = DNA_strand('ATTGC')
test3 = DNA_strand('GTAT')

print(test3)
