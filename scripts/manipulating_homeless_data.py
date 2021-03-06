#!python3

import pandas as pd

def main():
    df_homelessness = pd.read_csv("./data/homelessness.csv")
    
    # #inspecting values
    # print(df_homelessness.head())
    # print(df_homelessness.values)
    # print(df_homelessness.columns)
    # print(df_homelessness.index)
    
    #sorting rows
    print(df_homelessness.head())
    df_homelessness = df_homelessness.sort_values('individuals')
    # print(df_homelessness.head())
    # #select individual columns
    # # df_homelessness = df_homelessness['individuals']
    # print(df_homelessness.head())
    # columns_list = ['individuals','state_pop','region']
    # df_homelessness = df_homelessness[columns_list]
    # print(df_homelessness.head())
    # #subsetting with condition individuals > 1000
    # subset_condition = df_homelessness['individuals']>1000
    # df_homelessness = df_homelessness[subset_condition]
    # # print(df_homelessness.head())
    # subset_condition = df_homelessness['region']=='Mountain'
    # df_homelessness = df_homelessness[subset_condition]
    # print(df_homelessness.head())
    # df_homelessness = df_homelessness[(df_homelessness['family_members']<1000) & (df_homelessness['region']=='Pacific')]
    # print(df_homelessness.head())
    # df_homelessness = df_homelessness[(df_homelessness['family_members']<1000) | (df_homelessness['region']=='Pacific')]
    # print(df_homelessness.head())
    # values_list = ['California','Arizona','Nevada','Utah']
    # subset_condition = df_homelessness['state'].isin(values_list)
    # df_homelessness = df_homelessness[subset_condition]
    # print(df_homelessness.head())
    
    #adding new column with arithmetical process
    # df_homelessness['total'] = df_homelessness['individuals']+df_homelessness['family_members']
    # print(df_homelessness.head())
    # df_homelessness['p_individuals'] = df_homelessness['total']/df_homelessness['individuals']
    # print(df_homelessness.head())