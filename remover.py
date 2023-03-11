infile = "rawsource.txt"
outfile = "mainsource.txt"

delete_list = ["Rating</span>","CT rating</span>", "T rating</span>", "AWP</span>", "HS %</span>", "%</span>","Entry rounds</span>", "Clutch rounds</span>", "Support rounds</span>","Multi kill rounds</span>","Deaths per round</span>"]
with open(infile) as fin, open(outfile, "w+") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(word, "")
        fout.write(line)
