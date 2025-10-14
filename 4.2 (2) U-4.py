Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd 
... import numpy as np 
... # Given dictionary data 
... exam_data = { 
... 'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 
... 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19], 
... 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 
... 'qualify': ['yes', 'no', 'yes', 'no', 'no', 
... 'yes', 'yes', 'no', 'no', 'yes'] 
... } 
... # Custom labels 
... labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] 
... # Create DataFrame with index labels 
... df = pd.DataFrame(exam_data, index=labels) 
... # Display DataFrame 
... print("Original dataframe") 
... print(df) 
... df.loc[df['name']== 'James','name']='Suresh' 
... print("\nDataframe after changing 'James' to 'suresh:") 
... print(df) 
