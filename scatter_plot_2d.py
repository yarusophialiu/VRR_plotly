import matplotlib.pyplot as plt
import numpy as np
from utils import *
from analyze_plotly_velocity import *


# Example data
resolutions = [360, 480, 720, 1080, 360, 480, 720, 1080]  # x-axis: resolution
framerates = [30, 30, 60, 60, 120, 120, 240, 240]  # y-axis: framerate (Hz)
velocities = [10, 20, 30, 40, 50, 60, 70, 80]  # Size of dots



# scenes = ['Scene1', 'Scene2', 'Scene1', 'Scene2', 'Scene1', 'Scene2', 'Scene1', 'Scene2']  # Color of dots
scenes = ['bistro']
scene_colors = {'Scene1': 'blue', 'Scene2': 'red'}

dfs_by_bitrate = create_df_all_sequence(SCENES)
print(f'dfs_by_bitrate \n {dfs_by_bitrate[500]}')

# for scene in scenes:
#     print(f'scene {scene}')
#     velocities = get_velocities_by_scene(scene)

# Map scenes to unique colors
colors = [scene_colors[scene] for scene in scenes]

# Normalize velocities for better visualization of dot sizes
dot_sizes = np.array(velocities) * 10  # Scale for better visibility

# Create the scatter plot
plt.figure(figsize=(10, 6))
scatter = plt.scatter(resolutions, framerates, s=dot_sizes, c=colors, alpha=0.7, edgecolor='k')

# Customize the plot
plt.xlabel('Resolution (p)')
plt.ylabel('Framerate (Hz)')
plt.title('Scatter Plot: Resolution vs. Framerate')
plt.grid(True)

# Add a legend for scenes
for scene, color in scene_colors.items():
    plt.scatter([], [], c=color, alpha=0.7, s=100, label=scene)  # Add dummy scatter for legend
plt.legend(title='Scene')

# Show the plot
plt.tight_layout()
plt.show()
