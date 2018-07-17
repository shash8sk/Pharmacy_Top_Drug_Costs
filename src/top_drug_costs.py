##  python code 
"""
Created on Sat Jul 14 10:28:52 2018

@author: snaidu
"""
import io
import os
import csv
import sys


data_filename = sys.argv[1]

counter = 0
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','.']
dict_cost = {}
dict_count = {}
with open(data_filename, buffering = 20000000) as infile: 
    reader = csv.reader(infile, quotechar = '"', delimiter = ',', skipinitialspace= True)
    for line in reader:  
        if (counter > 0):
            idnum = line[0]
            lname = line[1]
            fname = line[2]
            name = fname.strip() + " " + lname.strip()
            drugname = line[3]
            cost = float(''.join(c for c in line[4] if c in digits))
            if drugname in dict_cost:
                dict_cost[drugname] += cost
            else:
                dict_cost[drugname] = cost
            if drugname in dict_count:
                dict_count[drugname].add(name)
            else:
                dict_count[drugname] = set()
                dict_count[drugname].add(name)
        #if (counter == 50):
            #break
        counter += 1
 
#print(dict_cost)
#print(dict_count)
        
cost_sort = [(k, dict_cost[k]) for k in sorted(dict_cost, key=dict_cost.get, reverse=True)]
#print(cost_sort)


out_filename = sys.argv[2]
output = open(out_filename, 'w')
output.write('drug_name,num_prescriber,total_cost\n')

for i, j in cost_sort:
    line = '"' + str(i)+ '"' + ',' + str(len(dict_count[i])) + ',' + str(j) + '\n' 
    output.write(line)
output.close()
