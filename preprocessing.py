import pandas as pd
import numpy as np

#set to False for working on test dataset
training = True
url = "data/train.csv" if training else "data/test.csv"
des = "data/train_processed.csv" if training else "data/test_processed.csv"
data = pd.read_csv(url)


"""
this python program extracts values from columns 10 to 110 
by removing first 5 and last 5 characters from each cell in these columns
"""

len_rows = data.shape[0]
len_cols = data.shape[1]

cols = list(data.columns)[10:-1] if training else list(data.columns)[10:]
print("-"*50)
for col in cols:
    for i in range(len_rows):
        t = data.loc[i,col]
        if t not in ["nan",np.nan,0.0]:
            try:
                data.loc[i,col] = t[6:-6]
            except:
                print(t,col,i,"--------exception")
    print(f"col {col} done")

        
print(data)
data.to_csv(des,index=False)