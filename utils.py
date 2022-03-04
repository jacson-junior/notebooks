import pandas as pd

def symbol_dict_to_df(symbol_dict):
    tmp_df_list = list()
    for k, v in symbol_dict.items():
        tmp_df = pd.DataFrame(v)
        tmp_df = tmp_df.assign(symbol=k)
        tmp_df_list.append(tmp_df)
    df = pd.concat(tmp_df_list)
    return df
