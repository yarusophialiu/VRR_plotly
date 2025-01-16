import matplotlib.pyplot as plt
import numpy as np
from analyze_plotly_velocity import *

# Example dfs_by_bitrate dictionary
# Assume dfs_by_bitrate contains DataFrames for each bitrate
# dfs_by_bitrate = {
#     500: {'resolution': [360, 480, 720, 1080],
#           'fps': [30, 60, 120, 240],
#           'velocity': [10, 20, 30, 40],
#           'path': ['Scene1', 'Scene2', 'Scene1', 'Scene2']},
#     1000: {'resolution': [360, 480, 720, 1080],
#            'fps': [30, 60, 120, 240],
#            'velocity': [15, 25, 35, 45],
#            'path': ['Scene3', 'Scene4', 'Scene3', 'Scene4']},
#     # Add 1500 and 2000 as needed
# }

dfs_by_bitrate = create_df_all_sequence(SCENES)


# Map paths (scenes) to unique colors
# for df in dfs_by_bitrate.values():
#     print(f'df \n {df["path"]}')
# print([df['path'] for df in dfs_by_bitrate.values()])
# unique_paths = set(sum([df['path'] for df in dfs_by_bitrate.values()], []))
# unique_paths = ['Bedroom', 'Bistro', 'Crytek_sponza', 'Gallery', 'Living_room', 'Lost_empire', 'Room', 'Suntemple', 'Statue', 'Sibenik']
unique_paths = [ 'bedroom',  'bistro',  'crytek_sponza', 'gallery',   'living_room',   'lost_empire',   'room',  'suntemple',   'suntemple_statue', 'sibenik']
scene_colors = {path: f'C{i}' for i, path in enumerate(unique_paths)}
scene_colors = {'bedroom': 'C0', 'bistro': 'C1', 'crytek_sponza': 'C2', 'gallery': 'C3', 
              'living_room': 'C4', 'lost_empire': 'C5', 'room': 'C6', 'suntemple': 'C7', 
              'suntemple_statue': 'C8', 'sibenik': 'C9'}
unique_paths = {'bedroom': 'Bedroom', 'bistro': 'Bistro', 'crytek_sponza': 'Crytek sponza', 'gallery': 'Gallery', 
              'living_room': 'Living room', 'lost_empire': 'Lost empire', 'room': 'Room', 'suntemple': 'Suntemple', 
              'suntemple_statue': 'Statue', 'sibenik': 'Sibenik'}
# print(f'scene_colors {scene_colors}')

# Loop over bitrates and plot scatter plots
for bitrate, data in dfs_by_bitrate.items():
    resolutions = data['resolution']
    framerates = data['fps']
    velocities = data['velocity']
    paths = data['path']

    # Normalize velocities for dot sizes
    dot_sizes = np.array(velocities) * 10000  # Adjust scale if needed

    # Map paths to colors
    colors = [scene_colors[path] for path in paths]
    plt.figure(figsize=(10, 6))
    # Create scatter plot for this bitrate
    plt.scatter(resolutions, framerates, s=dot_sizes, c=colors, alpha=0.7) # edgecolor='k'

    # Add legend for scenes
    for scene, color in scene_colors.items():
        plt.scatter([], [], c=color, alpha=0.7, s=100, label=unique_paths[scene])  # Dummy scatter for legend
    plt.legend(title='Scenes', fontsize=8)

    # Customize the plot
    plt.xlabel('Resolution',  fontsize=15)
    plt.ylabel('Framerate (Hz)',  fontsize=15)
    plt.xticks([360, 480, 720, 864, 1080])
    plt.yticks([i for i in range(30, 121, 10)])
    # plt.title('Scatter Plot: Resolution vs. Framerate by Bitrate')
    # plt.grid(True)

    # Show the plot
    plt.tight_layout()
    plt.show()
    break
