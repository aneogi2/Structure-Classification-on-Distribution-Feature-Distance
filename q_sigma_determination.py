import numpy as np
data = {}
ids_of_interest = [155186,156004,139930,139620,147795,59730,60097,41815,68880,59521]
with open("Q.dat") as q:
     lines = q.readlines()
     for count,line in enumerate(lines):
         clean_line = line.strip().split()
         if len(clean_line) != 3:
             continue
         if int(clean_line[0]) in ids_of_interest:
             if clean_line[0] in data.keys():
                 data[clean_line[0]].append(float(clean_line[1])+ float(clean_line[2]))
             else:
                  data[clean_line[0]] = [float(clean_line[1])+ float(clean_line[2])] 

for key in data.keys():
    Average = np.mean(data[key])
    std_dev = np.std(data[key])
    print(key, Average, std_dev)
