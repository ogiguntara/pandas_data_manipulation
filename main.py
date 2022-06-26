#!python3

from defusedxml import DTDForbidden
import pandas as pd

if __name__ == "__main__":
    df_homelessness = pd.read_csv("./data/homelessness.csv")
    
    #inspecting values
    print(df_homelessness.head())
    print(df_homelessness.values)
    print(df_homelessness.columns)
    print(df_homelessness.index)
    