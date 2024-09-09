import streamlit as st
import pandas as pd

import sys
import os

# Add the root directory to sys.path
sys.path.append(os.path.abspath('../..'))



from scripts import data_cleaning_and_preprocessing

main = data_cleaning_and_preprocessing()

missing = main.check_for_missing_values()
print(missing)

st.write(main.data_cleaning_and_preprocessing())
