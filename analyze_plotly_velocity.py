import os
import random
import numpy as np
import pandas as pd
from datetime import datetime, date
from utils import *
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px



def create_df_per_sequence(max_comb, velocities, COMBINE=False):
    fps_list = []
    resolution_list = []
    bitrate_list = []
    path_list = []

    # Iterate through the dictionary and populate the lists
    for path, values in max_comb.items():
        for idx, (fps, resolution) in enumerate(values):
            fps_list.append(fps)
            resolution_list.append(resolution)
            bitrate_list.append((idx + 1) * 500)  # Assuming velocity is the index+1
            path_list.append(path)

    data = {
        'resolution': resolution_list,
        'fps': fps_list,
        'bitrate': bitrate_list,
        'path': path_list,
        #  'velocity': velocities
    }

    df = pd.DataFrame(data)

    bitrate_groups = df.groupby('bitrate')
    dfs_by_bitrate = {bitrate: group_df for bitrate, group_df in bitrate_groups}

    # print(f'bitrate_groups \n {bitrate_groups}')

    # Create a dictionary to store the separate DataFrames
    # dfs_by_bitrate = {bitrate: group_df for bitrate, group_df in bitrate_groups}

    for bitrate, group_df in dfs_by_bitrate.items():
        group_df['velocity'] = velocities
        # group_df = group_df.drop(columns=['bitrate'])
        dfs_by_bitrate[bitrate] = group_df  # Update the dictionary with the new DataFrame

    if COMBINE:
        combined_df = pd.concat(dfs_by_bitrate.values(), ignore_index=True)
        # combined_df['bitrate'] = combined_df['bitrate'].astype(str)
        return combined_df
    else:
        return dfs_by_bitrate


