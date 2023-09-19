import pandas as pd
import csv
import sys


##
## Create a vocabulary dictionary
##

print('=== Numerically encoding terms ===')

vocab_df = pd.read_csv ('/tmp/vocabulary.csv',header=None)
vocab_df.rename(columns = {0:'code', 1: 'term'}, inplace = True)
  
print(vocab_df)



##
## Read the training data
##

print('=== Reading training data ===')

df = pd.read_csv ('/Volumes/trash/trash/python_nlp_data_mwk_snippet_training.csv.small',header=None)
df.rename(columns = {0:'category', 1: 'snippet', 2: 'term'}, inplace = True)
training_rows = []
for ind in df.index:
	category = df['category'][ind]
	snippet = df['snippet'][ind]
	
	term = df['term'][ind]
	code = vocab_df.loc[vocab_df['term'] == term].code.values[0]
	
	new_row = {'category':category, 'snippet':snippet, 'term':term, 'code':code}
	training_rows.append(new_row)
# 	df2 = pd.concat([training_df, pd.DataFrame([new_row])], ignore_index=True)
	print(".")

training_df = pd.DataFrame(training_rows)

print(training_df)

##
## Create the neural network
##

print('=== Creating neural network ===')

##
## Sort the test data
##

print('=== Finding categories for test data ===')

csv_data = []
csv_reader = csv.DictReader(sys.stdin, fieldnames=['filepath'])
for row in csv_reader:
	print(row['filepath'])
	training_row = {'filepath' : row['filepath'] }
	for term in row[None]:
	
		result_df = df.loc[df['term'] == term]
		if len(result_df) > 0:	

			print(result_df.code.values[0]," ---- ",term)


	training_df.append(training_row)
	print("--------------------")
