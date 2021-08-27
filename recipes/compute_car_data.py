# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Generate some data
cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
        'Price': [22000,25000,27000,35000]
        }

# Convert to dataframe
car_data_df = pd.DataFrame(cars, columns = ['Brand', 'Price'])

# Write recipe outputs
car_data = dataiku.Dataset("car_data")
car_data.write_with_schema(car_data_df)

# This is the bugfix on Release 1
