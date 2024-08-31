import os
import random
import numpy as np
import pandas as pd
from datetime import datetime, date
from utils import *
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px



def create_df_per_sequence(max_comb, velocities):
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

    # # Output the DataFrames with the inserted velocities
    # for bitrate, group_df in dfs_by_bitrate.items():
    #     print(f"DataFrame for bitrate {bitrate}:")
    #     group_df = group_df.drop(columns=['bitrate'])
    #     # print(group_df)
    #     print("\n")
    #     print(f'group_df {group_df.values}')

    #     x, y = np.array([360, 480, 720, 864, 1080]), np.array([30, 40, 50, 60, 70, 80, 90, 100, 110, 120])
    #     # fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
    #     # # fig = go.Figure(data=[go.Surface(z=group_df.values)])

    #     # fig.update_layout(title=f'{bitrate} kbps', 
    #     #                 #   autosize=False,
    #     #                 # width=500, height=500,
    #     #                 margin=dict(l=65, r=50, b=65, t=90))

    #     fig.show()
    #     # print(f'2000 \n {dfs_by_bitrate[2000]}')
    #     # fig = px.line_3d(df, x='resolution', y='fps', z='velocity', color='path') # scatter_3d line_3d

    #     # fig.update_layout(title=f'scene {scene_name} \n optimal fps + resolution for different velocity, bitrate {bitrate}kbps', 
    #     #                 margin=dict(l=65, r=50, b=65, t=90))
    #     # fig.show()
                    
    return dfs_by_bitrate


if __name__ == "__main__":
    scene_name = 'bistro'
    max_comb_per_sequence = {'path1_seg1_1': [[30, 1080], [40, 1080], [50, 1080], [50, 1080]], 'path1_seg1_2': [[70, 720], [80, 720], [80, 1080], [80, 1080]], 'path1_seg1_3': [[120, 480], [120, 720], [120, 720], [120, 720]], 'path1_seg2_1': [[50, 720], [70, 1080], [80, 1080], [80, 1080]], 'path1_seg2_2': [[110, 480], [120, 720], [120, 720], [120, 720]], 'path1_seg2_3': [[110, 480], [120, 720], [120, 720], [120, 720]], 'path1_seg3_1': [[50, 720], [50, 1080], [50, 1080], [60, 1080]], 'path1_seg3_2': [[80, 720], [90, 720], [110, 720], [110, 720]], 'path1_seg3_3': [[110, 720], [120, 720], [120, 720], [120, 720]], 'path2_seg1_1': [[60, 720], [80, 720], [80, 720], [80, 1080]], 'path2_seg1_2': [[90, 720], [110, 720], [120, 720], [120, 720]], 'path2_seg1_3': [[120, 480], [120, 720], [120, 720], [120, 720]], 'path2_seg2_1': [[60, 720], [80, 720], [80, 1080], [80, 1080]], 'path2_seg2_2': [[90, 480], [110, 720], [120, 720], [120, 720]], 'path2_seg2_3': [[120, 360], [120, 480], [120, 480], [120, 720]], 'path2_seg3_1': [[40, 720], [50, 1080], [60, 1080], [60, 1080]], 'path2_seg3_2': [[80, 720], [90, 720], [110, 720], [120, 720]], 'path2_seg3_3': [[110, 480], [120, 720], [120, 720], [120, 720]], 'path3_seg1_1': [[90, 720], [100, 720], [110, 720], [120, 720]], 'path3_seg1_2': [[80, 480], [110, 720], [120, 720], [120, 720]], 'path3_seg1_3': [[120, 480], [120, 720], [120, 720], [120, 720]], 'path3_seg2_1': [[80, 720], [90, 720], [110, 720], [110, 720]], 'path3_seg2_2': [[80, 720], [100, 720], [110, 720], [120, 720]], 'path3_seg2_3': [[80, 480], [110, 720], [120, 720], [120, 720]], 'path3_seg3_1': [[80, 720], [90, 720], [110, 720], [120, 1080]], 'path3_seg3_2': [[110, 480], [120, 720], [120, 720], [120, 720]], 'path3_seg3_3': [[120, 480], [120, 480], [120, 480], [120, 720]], 'path4_seg1_1': [[80, 720], [110, 720], [120, 720], [120, 720]], 'path4_seg1_2': [[110, 480], [120, 720], [120, 720], [120, 720]], 'path4_seg1_3': [[120, 720], [120, 720], [120, 720], [120, 720]], 'path4_seg2_1': [[80, 720], [110, 720], [120, 720], [120, 720]], 'path4_seg2_2': [[110, 480], [120, 720], [120, 720], [120, 720]], 'path4_seg2_3': [[110, 720], [120, 720], [120, 720], [120, 720]], 'path4_seg3_1': [[120, 480], [120, 720], [120, 720], [120, 720]], 'path4_seg3_2': [[120, 480], [120, 720], [120, 720], [120, 720]], 'path4_seg3_3': [[120, 360], [120, 480], [120, 480], [120, 480]], 'path5_seg1_1': [[80, 720], [80, 720], [110, 720], [110, 720]], 'path5_seg1_2': [[80, 720], [110, 720], [120, 720], [120, 720]], 'path5_seg1_3': [[90, 720], [120, 720], [120, 720], [120, 720]], 'path5_seg2_1': [[80, 720], [90, 720], [120, 720], [120, 720]], 'path5_seg2_2': [[80, 720], [120, 720], [120, 720], [120, 720]], 'path5_seg2_3': [[120, 480], [120, 720], [120, 720], [120, 720]], 'path5_seg3_1': [[120, 720], [120, 720], [120, 720], [120, 720]], 'path5_seg3_2': [[120, 480], [120, 720], [120, 720], [120, 720]], 'path5_seg3_3': [[120, 480], [120, 720], [120, 720], [120, 720]]}
    # max_comb_per_sequence = {'path1_seg1_1': [[30, 1080], [40, 1080], [50, 1080], [50, 1080]], 
    #                          'path1_seg1_2': [[70, 720], [80, 720], [80, 1080], [80, 1080]], 
    #                          'path1_seg2_3': [[110, 480], [120, 720], [120, 720], [120, 720]], }
    with open('velocity_sequence/bistro_velocity_cleaned.txt', 'r') as file:
        lines = file.readlines()
    velocities = [float(line.strip()) for line in lines]
    print(f'velocities {velocities}')

    dfs_by_bitrate = create_df_per_sequence(max_comb_per_sequence, velocities)
    bitrates = [500, 1000, 1500, 2000]
    bitrates = [500, ]
    for bitrate in bitrates:
        df = dfs_by_bitrate[bitrate]
        # print(f'df \n {df}')
        fig = px.scatter_3d(df, x='resolution', y='fps', z='velocity', color='path') # scatter_3d line_3d

        fig.update_layout(title=f'scene {scene_name} \n optimal fps + resolution for different velocity, bitrate {bitrate}kbps', 
                        margin=dict(l=65, r=50, b=65, t=90))
        fig.show()