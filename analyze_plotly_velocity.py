import pandas as pd
from utils import *


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
        combined_df = pd.concat(dfs_by_bitrate.values(), ignore_index=True) # concatenates them into a single DataFrame
        # combined_df['bitrate'] = combined_df['bitrate'].astype(str)
        return combined_df
    else:
        return dfs_by_bitrate
    



def create_df_all_sequence(all_scenes, COMBINE=False):
    # SCENES = ['bistro', 'room']
    all_scenes_dfs_by_bitrate = []
    for scene in all_scenes:
        variable_name = f"{scene}_max_comb_per_sequence"
        fps_list = []
        resolution_list = []
        bitrate_list = []
        path_list = []
            
        # Use globals() to access the variable content
        if variable_name in globals():
            max_comb = globals()[variable_name]
            print(f"Content of {variable_name}")
            # print(f"Content of {variable_name}: {variable_name['path1_seg1_1']}")
            # Iterate through the dictionary and populate the lists
            for path, values in max_comb.items():
                # print(f'values {values}')
                # count += 1
                for idx, (fps, resolution) in enumerate(values):
                    fps_list.append(fps)
                    resolution_list.append(resolution)
                    bitrate_list.append((idx + 1) * 500)  # Assuming velocity is the index+1
                    path_list.append(path)
        else:
            print(f"Variable {variable_name} does not exist.\n")

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
        with open(f'reference_velocity/{scene}_cleaned.txt', 'r') as file:
            lines = file.readlines()
            velocities = [float(line.strip()) for line in lines]
            velocities = np.array(velocities)
            velocities /= 51
            frame_limit = frame_per_fps_video(166)
            velocities /= (frame_limit + 1)
            # print(f'velocities {velocities}')


            for bitrate, group_df in dfs_by_bitrate.items():
                group_df['velocity'] = velocities
                # group_df = group_df.drop(columns=['bitrate'])
                dfs_by_bitrate[bitrate] = group_df  # Update the dictionary with the new DataFrame
        all_scenes_dfs_by_bitrate.append(dfs_by_bitrate)
        # print(f'dfs_by_bitrate[bitrate] \n {dfs_by_bitrate[500]}')

    combined_dfs_by_bitrate = {}  
    # Loop through each scene's dfs_by_bitrate
    for scene_dfs in all_scenes_dfs_by_bitrate:
        for bitrate, df in scene_dfs.items():
            if bitrate not in combined_dfs_by_bitrate:
                # If bitrate not present, create a new entry
                combined_dfs_by_bitrate[bitrate] = df
            else:
                # If bitrate exists, concatenate the DataFrames
                combined_dfs_by_bitrate[bitrate] = pd.concat([combined_dfs_by_bitrate[bitrate], df])
    # print(f'dfs_by_bitrate[bitrate] \n {len(all_scenes_dfs_by_bitrate)}')

    if COMBINE:
        combined_df = pd.concat(dfs_by_bitrate.values(), ignore_index=True) # concatenates them into a single DataFrame
        # combined_df['bitrate'] = combined_df['bitrate'].astype(str)
        return combined_df
    else:
        return combined_dfs_by_bitrate
