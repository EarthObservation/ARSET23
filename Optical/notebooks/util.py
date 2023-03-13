# Once StatAPI reaches maturity, these functions will be available in sh-py.

from collections import defaultdict
from sentinelhub  import parse_time
import pandas as pd

def stat_to_df(stat_data):
    """ transform response from StatAPI into dataframe"""
    df_data = defaultdict(list)

    for single_data in stat_data['data']:
        df_data['interval_from'].append(parse_time(single_data['interval']['from']).date())
        df_data['interval_to'].append(parse_time(single_data['interval']['to']).date())
        
        for output_data in single_data['outputs'].keys():
            single_band = len(single_data['outputs'][output_data]['bands']) == 1
            for band_name, band_values in single_data['outputs'][output_data]['bands'].items():
                for stat_name, value in band_values['stats'].items():
                    col_name = f'{output_data}_{band_name}_{stat_name}'
                    if stat_name == 'percentiles':
                        for perc, perc_val in value.items():
                            perc_col_name = f'{col_name}_{perc}'
                            df_data[perc_col_name].append(perc_val)
                    else:
                        df_data[col_name].append(value)
    
    df = pd.DataFrame(df_data)
    # df = df.astype({c:'float' for c in df.columns if any(n in c for n in ['mean','min','max','stDev','percentil'])})
    return df