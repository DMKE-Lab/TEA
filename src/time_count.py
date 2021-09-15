f = '../datasets/D_Y_100K_V2/attr_triples_2_output'
output = '../datasets/D_Y_100K_V2/attr_triples_2_time'
fo = open(output , "w", encoding='utf-8')
for line in open(f, 'r', encoding = "utf-8"):
    # if((line.find("<http://www.w3.org/2001/XMLSchema#gYear>") != -1) or
    #     (line.find("<http://www.w3.org/2001/XMLSchema#date>") != -1)or
    #     (line.find("<http://www.w3.org/2001/XMLSchema#gYearMonth>")!= -1)):#DW
    if (line.find("xsd:date") != -1):#YAGO
        fo.write(line)