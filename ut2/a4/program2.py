import random

NUCLEOBASES = "ATGC"
DNA_SIZE = 100
con_a = 0
con_t = 0
con_g = 0
con_c = 0

sequence = "".join([random.choice(NUCLEOBASES) for a in range(DNA_SIZE)])
for i in range(0, DNA_SIZE):
    if sequence[i] == "A":
        con_a = con_a + 1
    elif sequence[i] == "T":
        con_t = con_t + 1
    elif sequence[i] == "G":
        con_g = con_g + 1
    elif sequence[i] == "C":
        con_c = con_c + 1
print(f"Adenine: {con_a}\nGuanine: {con_g}\nCytosine: {con_c}\nThymine: {con_t}")
