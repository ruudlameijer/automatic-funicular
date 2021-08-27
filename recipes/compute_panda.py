# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu


car_brands = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
            'Price': [22000,25000,27000,35000]
            }

panda_df = pd.DataFrame(car_brands, columns = ['Brand', 'Price'])

# Write recipe outputs
cars = dataiku.Dataset("car_brands")
cars.write_with_schema(panda_df)
