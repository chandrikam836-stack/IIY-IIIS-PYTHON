Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd 
... import numpy as np 
... # Original Data 
... exam_data = { 
... 'name': ['Anastasia', 'Dima', 'Katherine', 'Suresh', 'Emily', 
... 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'], 
... 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19], 
... 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 
... 'qualify': ['yes', 'no', 'yes', 'no', 'no', 
... 'yes', 'yes', 'no', 'no', 'yes'] 
... } 
... labels = ['a','b','c','d','e','f','g','h','i','j'] 
... df = pd.DataFrame(exam_data, index=labels) 
... col_list =df.columns.tolist() 
... print("List of column headers:") 
