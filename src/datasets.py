f = '../datasets/D_Y_100K_V1/attr_triples_1'
output = '../datasets/D_Y_100K_V1/attr_triples_1_output'
fo = open(output , "w", encoding='utf-8')
for line in open(f, 'r', encoding = "utf-8"):
    if(line.find("^^") != -1):
        fo.write(line)
