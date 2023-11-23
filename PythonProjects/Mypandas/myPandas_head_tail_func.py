import pandas as pd
import numpy as nm


data = {"name" : ["Ankit", "Prateek", "Aarav"],
        "Age" : [12, 10, 2.5],
        "Class" : ["6th", "4th", "kg"]}

df = pd.DataFrame(data)
#print(df)
#print(df.head()) #by default it will print first 5 rows, head(n)==>first n rows
#print(df.tail()) #by default it will print last 5 rows, tail(n)==>last n rows

print(df.head(2))
print(df.tail(2))
