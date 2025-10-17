Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import matplotlib.pyplot as plt 
... import pandas as pd 
... import numpy as np 
... # Sample time-series data 
... dates = pd.to_datetime(pd.date_range(start='2024-01-01', periods=100, freq='D')) 
... sales_data = np.random.randint(100, 500, size=100) + np.sin(np.arange(100) * 0.2) * 50 
... df = pd.DataFrame({'Date': dates, 'Sales': sales_data}) 
... df = df.set_index('Date') 
... plt.figure(figsize=(12, 6)) 
... plt.plot(df.index, df['Sales']) 
... # Customize axis labels and date formats 
... plt.xlabel('Date') 
... plt.ylabel('Sales') 
... plt.title('Daily Sales Over Time')
... # Use pandas' built-in plotting for automatic date formatting 
... # This is a good practice for clean time-series plots 
... df.plot(y='Sales', figsize=(12, 6), title='Daily Sales Over Time')  
