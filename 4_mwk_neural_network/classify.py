import pandas as pd
import csv
import sys


df = pd.read_csv ('/tmp/vocabulary.csv',header=None)
df.rename(columns = {0:'code', 1: 'term'}, inplace = True)
  
# df = pd.DataFrame(csv_data, columns=['code','term'])

# print(csv_data)
print(df)

csv_data = []
csv_reader = csv.DictReader(sys.stdin, fieldnames=['filepath','terms'])

for row in csv_reader:
#     csv_data.append(row)
# 	r = row.values()
	print(row['filepath'])
	print(row['terms'])
# 	coderow = df['term'].eq('aaron')
	
	result_df = df.loc[df['term'] == row['terms']]
	if len(result_df) > 0:	
		print(result_df.code.values[0])
	print("--------------------")
# 	for term in row['terms']:
# 		coderow = df['term'].eq(term)
# 		print(coderow)
# 	pass
