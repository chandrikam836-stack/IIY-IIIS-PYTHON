Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np 
... arr = np.array([1, 2, 2, 3, 4, 4, 4, 5]) 
... print("Original array:", arr) 
... print("\nUsing repr():")print(repr(arr)) 
... print("\nUsing count():") 
... arr_list = arr.tolist() 
... print("Count of 4 in array:", arr_list.count(4)) 
... print("\nUsing np.bincount():") 
... print("Element counts (by index):", np.bincount(arr)) 
... print("\nUsing np.unique():") 
... unique_elements, counts = np.unique(arr, return_counts=True) 
... print("Unique elements:", unique_elements) 
