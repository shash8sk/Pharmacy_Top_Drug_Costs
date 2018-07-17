# Pharmacy_Top_Drug_Costs
Test Project:

Python 3.6 code to estimate top drug costs using sample dataset from Centers for Medicare & Medicaid Services

The input csv file should contain the following fields in the specified order:


'''
id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost
1000000001,Smith,James,AMBIEN,100
1000000002,Garcia,Maria,AMBIEN,200
1000000003,Johnson,James,CHLORPROMAZINE,1000
1000000004,Rodriguez,Maria,CHLORPROMAZINE,2000
1000000005,Smith,David,BENZTROPINE MESYLATE,1500
'''


The output file csv will contain the drugname, number of unique prescribers and the total drug costs across all prescribers sorted in descending order of cost.
'''
drug_name,num_prescriber,total_cost
CHLORPROMAZINE,2,3000
BENZTROPINE MESYLATE,1,1500
AMBIEN,2,300
'''

You will need to have the following csv package to import the csv without any issues of commas within quotes.

The output cost will ne rounded to the nearest dollar amount.


