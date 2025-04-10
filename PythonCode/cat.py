def parse(file_path):
    results = []
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
                results.append((header, len(string)))
    return results

cat = parse('datafile.txt')

with open ("sequence_lengths.txt", 'w') as output:
    for x in cat:
        output.write(str(x))
        output.write("\n")