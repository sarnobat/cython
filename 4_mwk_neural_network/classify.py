import pandas as pd
import csv
import sys


df = pd.read_csv ('/tmp/vocabulary.csv',header=None)
df.rename(columns = {0:'code', 1: 'term'}, inplace = True)
  
print(df)

csv_data = []
csv_reader = csv.DictReader(sys.stdin, fieldnames=['filepath'])

for row in csv_reader:
	print(row['filepath'])
	for term in row[None]:
	
		result_df = df.loc[df['term'] == term]
		if len(result_df) > 0:	

			print(result_df.code.values[0]," ---- ",term)
	print("--------------------")
