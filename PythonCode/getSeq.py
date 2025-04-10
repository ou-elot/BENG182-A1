def getSeq(data_seq, data_in):
    query = input("Enter your query sequence: ").strip()
    with open(data_seq, "r") as file:
        sequence = file.read()
    
    query_index = sequence.find(query)

    if query_index == -1:
        return "this query is not found"

    splits = sequence[:query_index].count("@")
    gi_nums = []
    with open(data_in, 'r') as file:
        for line in file:
            gi_nums.append(line.split()[0])
        
    gi_found = gi_nums[splits]

    return "the query was found at gi number " + str(gi_found)
    
toPrint = getSeq('data.seq', 'data.in')

print (toPrint)





    
