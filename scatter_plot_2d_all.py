import matplotlib.pyplot as plt
import numpy as np
from analyze_plotly_velocity import *
from datetime import datetime


dfs_by_bitrate = create_df_all_sequence(SCENES)

# Map paths (scenes) to unique colors
unique_paths = [ 'bedroom',  'bistro',  'crytek_sponza', 'gallery',   'living_room',   'lost_empire',   'room',  'suntemple',   'suntemple_statue', 'sibenik']
scene_colors = {path: f'C{i}' for i, path in enumerate(unique_paths)}
scene_colors = {'bedroom': 'dodgerblue', # C0', 
                'bistro': 'C1', 'crytek_sponza': 'C2', 
                'gallery': 'orangered', # 'C3', 
                'living_room': 'C4', 'lost_empire': 'C5', 'room': 'C6', 'suntemple': 'C7', 
                'suntemple_statue': 'gold', #'C8', 
                'sibenik': 'C9'}
unique_paths = {'bedroom': 'Bedroom', 'bistro': 'Bistro', 'crytek_sponza': 'Crytek sponza', 'gallery': 'Gallery', 'living_room': 'Living room', 'lost_empire': 'Lost empire', 'room': 'Room', 'suntemple': 'Suntemple', 'suntemple_statue': 'Statue', 'sibenik': 'Sibenik'}
# print(f'scene_colors {scene_colors}')
res_mapping = {360:0, 480:1, 720:2, 864:3, 1080:4}

SAVE = True
SHOW = False # True False
# Loop over bitrates and plot scatter plots
for bitrate, data in dfs_by_bitrate.items():
    resolutions = data['resolution']
    framerates = data['fps']
    velocities = data['velocity']
    paths = data['path']
    converted_resolutions = resolutions.replace(res_mapping)


    # Normalize velocities for dot sizes
    dot_sizes = np.array(velocities) * 10000  # Adjust scale if needed

    # Map paths to colors
    colors = [scene_colors[path] for path in paths]
    plt.figure(figsize=(10, 6))
    # Create scatter plot for this bitrate
    plt.scatter(converted_resolutions, framerates, s=dot_sizes, c=colors, alpha=0.7) # edgecolor='k'

    # Add legend for scenes
    for scene, color in scene_colors.items():
        plt.scatter([], [], c=color, alpha=0.7, s=100, label=unique_paths[scene])  # Dummy scatter for legend
    plt.legend(title='Scenes', fontsize=8)
    plt.legend(title="Marker Size ~ Velocity", loc='upper right')

    # Customize the plot
    plt.xlabel('Resolution (height in px)',  fontsize=15)
    plt.ylabel('Framerate (Hz)',  fontsize=15)
    x_values = [360, 480, 720, 864, 1080]
    evenly_spaced_x = range(len(x_values))

    # Set the x-ticks to the evenly spaced positions
    plt.xticks(evenly_spaced_x, x_values)
    # plt.xticks([360, 480, 720, 864, 1080])
    plt.yticks([i for i in range(30, 131, 10)])
    # plt.title('Scatter Plot: Resolution vs. Framerate by Bitrate')
    plt.grid(True, c='lightgrey', linestyle='--')

    # Show the plot
    plt.tight_layout()
    plt.text(0.08, 0.11, "0.5 Mbps", fontsize=15, color='darkgrey', transform=plt.gcf().transFigure,  # Transform coordinates to figure-relative
             ha="left", va="bottom")

    now = datetime.now()
    time_path = now.strftime("%Y-%m-%d-%H_%M")
    img_path = f"{bitrate}-{time_path}.svg"
    if SAVE:
        plt.savefig(img_path, bbox_inches='tight', pad_inches=0)
    if SHOW:
        plt.show()
    # break
