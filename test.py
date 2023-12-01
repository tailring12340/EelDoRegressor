import numpy as np
import pandas as pd

raw_data = {'first_name' : ['Jason',np.nan,'Tina','Jake','Amy'],
            'last_name' : ['Miller', np.nan, 'Ali','milner','Cooze'],
            'age' : [42, np.nan,36, 24, 73],
            'sex' : ['m', np.nan, 'f', 'm', 'f'],
            'preTestScore' : [4, np.nan, np.nan, 2, 3],
            'postTestScore' : [25, np.nan, np.nan, 26, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'sex', 'preTestScore', 'postTestScore'])

print(df.isnull().sum())
