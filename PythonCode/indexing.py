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

sequences = parse("datafile.txt")

big_string = ""

for x in sequences:
    big_string = big_string + sequences[x] + "@"

big_string = big_string[:-1] # we will have one extra @ at end, cut it out

with open ("data.seq", "w") as output:
    output.write(big_string)

gi_nums = {}
for x in sequences:
    gi_number = x.split("|")[1]
    gi_nums[x] = gi_number

offset = 0
with open("data.in", "w") as output:
    for header in sequences:
        sequence = sequences[header]
        gi_number = gi_nums[header]
        toWrite = str(gi_number) + "    " + str(offset)
        output.write(toWrite)
        output.write('\n')
        offset = offset + len(sequence) + 1  # +1 for the '@' symbol in long sequence



