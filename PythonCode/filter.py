def parse(file_path):
    results = {}
    with open(file_path, "r") as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line.startswith(">"):
                header = line
                i  = i+1
                seqs = []
                while (i < len(lines)) and (not lines[i].startswith(">")):
                    seqs.append(lines[i].strip())
                    i = i+1
                string = ""
                for seq in seqs:
                    string = string + seq
                results[header] = string
    return results

#we can use the same parse code that was written for the cat function, just rewritten to use dictionary for mappings of header to sequence

target = ['mouse', 'rat', 'mus musculus', 'rattus norvegicus']

mapping = parse("datafile.txt")
toReturn = {}

for x in mapping:
    for name in target:
        if name in x.lower():
            toReturn[x] = mapping[x]
            break

with open ("filtered_fasta.txt",'w') as output:
    for x in toReturn:
        seq = toReturn[x]
        output.write(str(x))
        output.write('\n')
        i = 0
        while i<len(seq):
            output.write(seq[i:i+60])
            i = i+60
            output.write('\n')







