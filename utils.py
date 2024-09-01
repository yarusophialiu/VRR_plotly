import os
import numpy as np
from math import *


def count_files_in_subfolders(root_directory):
    # Traverse the directory tree starting from the root directory
    for root, dirs, files in os.walk(root_directory):
        print(f'dirs {dirs}')
        for dir_name in dirs:
            # Get the full path of the subfolder
            subfolder_path = os.path.join(root, dir_name)
            # Count the number of files in the subfolder
            file_count = sum([len(files) for _, _, files in os.walk(subfolder_path)])
            print(f"Subfolder: {subfolder_path}, File count: {file_count}")
            os.chdir(f'/home/yl962/rds/hpc-work/VRR/VRRMP4_CVVDP/crytek_sponza/{dirs}')
            current_directory = os.getcwd()
            print(f"Current working directory: {current_directory}")


def mapIdToPath(id):
    """
    NOTE: input id starts from 0 not 1, HPC job id starts from 1
    so should be mapIdToPath(JOBID-1)

    we run 45 jobs/tasks (allocate 13 gpus) at one time as each scene has 45 clips
    so we run 10 times as there are in total 10 scenes
    for each task id, we run videos for 1 scene, 1 seg, 1 speed, i.e. for loop 5 * 10 = 50 videos
    e.g. sbatch --array=1-10:1 -A STARS-SL3-GPU submission_script

    id is from 0-44, map id -> path, seg, speed

    e.g. id 0 -> paths[0], segs[0], speeds[0]
         id 1 -> paths[0], segs[0], speeds[1]
    Note that id in HPC starts from 1, so delete id by 1 when call the function
    mapIdToPath(0) -> (1, 1, 1) path1 seg1 speed1
    mapIdToPath(16) -> (2, 3, 2) path2 seg3 speed2
    """
    pathIdx = int(floor(id/9))
    segIdx = int(floor((id - pathIdx * 9) / 3))
    speedIdx = (id - pathIdx * 9) % 3
    paths = [1, 2, 3, 4, 5]
    segs = [1, 2, 3,]
    speeds = [1, 2, 3,]
#    print(f'pathIdx {pathIdx}, segIdx {segIdx} speedIdx {speedIdx}')
    return paths[pathIdx], segs[segIdx], speeds[speedIdx]


def mapPathToId(path, seg, speed):
    """
    NOTE: output id starts from 0 not 1, HPC job id starts from 1

    mapPathToId(1, 1, 1) -> 0, id is 0, need to add 1 to become jobid
    """
    id = (path-1) * 9 + (seg-1) * 3 + speed - 1
    print(f'id {id}')
    return id




def type1_analysis(df, label_idx, number, refresh_rate, bitrate, SAVE = False, DEBUG = False):
    """x axis is bandwidth, y axis is JOD, color is resolution"""
    bitrate_df = df.iloc[label_idx, 0] # check if bitrate is correct
    if DEBUG:
        print(f'bitrate_df {bitrate_df}, bitrate {bitrate}')

    assert bitrate_df == bitrate

    # fig, ax = plt.subplots(figsize=(8, 5))
    labels = ['360p', '480p', '720p', '864p', '1080p']

    # collect data for each resolution
    # manually skip the resolution we dont want
    resolution_not_want = ['540p']
    for i, resolution in enumerate(labels):
        # print(f'\n\n\ni resolution {i, resolution}')
        if resolution in resolution_not_want:
            continue

        jod = []
        for num in range(0, number): # e.g. first 3 fps, i.e. 30, 60, 70

            val = df.iloc[label_idx, 1+i+5*num]
            jod.append(val)
        jod = [float(v) for v in jod]        
        # print(f'resolution {resolution}, jod {jod}, label {labels[i]}')



def type2_analysis(df, label_idx, bitrate, number, refresh_rate, max_jod, max_res, SAVE = False, DEBUG = False):
    """x axis is resolution, y axis is JOD, color is bitrate, labels are refresh rate"""
    bitrate_df = df.iloc[label_idx, 0] # check if bitrate is correct
    if DEBUG:
        print(f'bitrate_df {bitrate_df}, bitrate {bitrate}')

    x_values = np.array([1080, 864, 720, 480, 360,]) # resolution
    x_values = sorted(x_values)
    # print(f'\n\n\n')
    # fig, ax = plt.subplots(figsize=(8, 5))
    for num in range(number): # loop column
        # cvvdp jod from file1
        jod_cvvdp = df.iloc[label_idx, 1+5*num:6+5*num].values
        jod_cvvdp = [float(v) for v in jod_cvvdp]        

        # print(f'idx {num}, fps{refresh_rate[num]}, JOD {jod_cvvdp}, ') # max JOD {max(jod_cvvdp)}
        max_jod_idx = np.argmax(jod_cvvdp)
        # print(f'idx {num}, fps{refresh_rate[num]}, JOD {jod_cvvdp}, max JOD {max(jod_cvvdp)}')
        max_jod.append(max(jod_cvvdp))
        max_res.append(x_values[max_jod_idx])



colors_matplotlib = [
    'b',        # Blue
    'g',        # Green
    'r',        # Red
    'c',        # Cyan
    'm',        # Magenta
    'y',        # Yellow
    'k',        # Black
    'teal',        # teal
    'orange',   # Orange
    'purple',   # Purple
    'brown',    # Brown
    'pink',     # Pink
    'gray',     # Gray
    'olive',    # Olive
    'navy',      # Navy
    'lime',        # Lime
    'maroon',      # Maroon
    'gold',        # Gold
    'violet',      # Violet
    'indigo',      # Indigo
    'crimson',     # Crimson
    'plum',        # Plum
    'peachpuff',   # Peachpuff
    'aqua',        # Aqua
    'coral',       # Coral
    'salmon',      # Salmon
    'khaki',       # Khaki
    'turquoise',   # Turquoise
    'orchid',      # Orchid
    'sienna',      # Sienna
    'slategray',   # Slate Gray
    'steelblue',   # Steel Blue
    'peru',        # Peru
    'tomato',      # Tomato
    'chocolate',   # Chocolate
    'wheat',       # Wheat
    'dodgerblue',  # Dodger Blue
    'firebrick',   # Firebrick
    'goldenrod',   # Goldenrod
    'darkolivegreen', # Dark Olive Green
    'darkorange',  # Dark Orange
    'deeppink',    # Deep Pink
    'deepskyblue', # Deep Sky Blue
    'lavender',    # Lavender
    'midnightblue', # Midnight Blue
    'royalblue',   # Royal Blue
    'seagreen',    # Sea Green
    'skyblue',     # Sky Blue
    'springgreen', # Spring Green
    'tan',         # Tan
    'thistle',     # Thistle
]


refresh_rate = [30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
bistro_max_comb_per_sequence = {'path1_seg1_1': [[30, 1080], [40, 1080], [50, 1080], [50, 1080]], 'path1_seg1_2': [[70, 720], [80, 720], [80, 1080], [80, 1080]], 'path1_seg1_3': [[120, 480], [120, 720], [120, 720], [120, 720]], 'path1_seg2_1': [[50, 720], [70, 1080], [80, 1080], [80, 1080]], 'path1_seg2_2': [[110, 480], [120, 720], [120, 720], [120, 720]], 'path1_seg2_3': [[110, 480], [120, 720], [120, 720], [120, 720]], 'path1_seg3_1': [[50, 720], [50, 1080], [50, 1080], [60, 1080]], 'path1_seg3_2': [[80, 720], [90, 720], [110, 720], [110, 720]], 'path1_seg3_3': [[110, 720], [120, 720], [120, 720], [120, 720]], 'path2_seg1_1': [[60, 720], [80, 720], [80, 720], [80, 1080]], 'path2_seg1_2': [[90, 720], [110, 720], [120, 720], [120, 720]], 'path2_seg1_3': [[120, 480], [120, 720], [120, 720], [120, 720]], 'path2_seg2_1': [[60, 720], [80, 720], [80, 1080], [80, 1080]], 'path2_seg2_2': [[90, 480], [110, 720], [120, 720], [120, 720]], 'path2_seg2_3': [[120, 360], [120, 480], [120, 480], [120, 720]], 'path2_seg3_1': [[40, 720], [50, 1080], [60, 1080], [60, 1080]], 'path2_seg3_2': [[80, 720], [90, 720], [110, 720], [120, 720]], 'path2_seg3_3': [[110, 480], [120, 720], [120, 720], [120, 720]], 'path3_seg1_1': [[90, 720], [100, 720], [110, 720], [120, 720]], 'path3_seg1_2': [[80, 480], [110, 720], [120, 720], [120, 720]], 'path3_seg1_3': [[120, 480], [120, 720], [120, 720], [120, 720]], 'path3_seg2_1': [[80, 720], [90, 720], [110, 720], [110, 720]], 'path3_seg2_2': [[80, 720], [100, 720], [110, 720], [120, 720]], 'path3_seg2_3': [[80, 480], [110, 720], [120, 720], [120, 720]], 'path3_seg3_1': [[80, 720], [90, 720], [110, 720], [120, 1080]], 'path3_seg3_2': [[110, 480], [120, 720], [120, 720], [120, 720]], 'path3_seg3_3': [[120, 480], [120, 480], [120, 480], [120, 720]], 'path4_seg1_1': [[80, 720], [110, 720], [120, 720], [120, 720]], 'path4_seg1_2': [[110, 480], [120, 720], [120, 720], [120, 720]], 'path4_seg1_3': [[120, 720], [120, 720], [120, 720], [120, 720]], 'path4_seg2_1': [[80, 720], [110, 720], [120, 720], [120, 720]], 'path4_seg2_2': [[110, 480], [120, 720], [120, 720], [120, 720]], 'path4_seg2_3': [[110, 720], [120, 720], [120, 720], [120, 720]], 'path4_seg3_1': [[120, 480], [120, 720], [120, 720], [120, 720]], 'path4_seg3_2': [[120, 480], [120, 720], [120, 720], [120, 720]], 'path4_seg3_3': [[120, 360], [120, 480], [120, 480], [120, 480]], 'path5_seg1_1': [[80, 720], [80, 720], [110, 720], [110, 720]], 'path5_seg1_2': [[80, 720], [110, 720], [120, 720], [120, 720]], 'path5_seg1_3': [[90, 720], [120, 720], [120, 720], [120, 720]], 'path5_seg2_1': [[80, 720], [90, 720], [120, 720], [120, 720]], 'path5_seg2_2': [[80, 720], [120, 720], [120, 720], [120, 720]], 'path5_seg2_3': [[120, 480], [120, 720], [120, 720], [120, 720]], 'path5_seg3_1': [[120, 720], [120, 720], [120, 720], [120, 720]], 'path5_seg3_2': [[120, 480], [120, 720], [120, 720], [120, 720]], 'path5_seg3_3': [[120, 480], [120, 720], [120, 720], [120, 720]]}
room_max_comb_per_sequence = {'path1_seg1_1': [[60, 720], [70, 720], [90, 720], [110, 720]], 'path1_seg1_2': [[90, 720], [110, 720], [120, 720], [120, 720]], 'path1_seg1_3': [[120, 720], [120, 720], [120, 720], [120, 720]], 'path1_seg2_1': [[80, 720], [80, 720], [110, 720], [110, 720]], 'path1_seg2_2': [[110, 720], [120, 720], [120, 720], [120, 720]], 'path1_seg2_3': [[120, 720], [120, 720], [120, 720], [120, 720]], 'path1_seg3_1': [[120, 360], [120, 360], [120, 360], [120, 360]], 'path1_seg3_2': [[120, 480], [120, 360], [120, 360], [120, 360]], 'path1_seg3_3': [[120, 360], [120, 480], [120, 360], [120, 360]], 'path2_seg1_1': [[60, 720], [110, 720], [110, 720], [110, 720]], 'path2_seg1_2': [[80, 720], [110, 720], [110, 720], [120, 720]], 'path2_seg1_3': [[110, 720], [120, 720], [120, 720], [120, 720]], 'path2_seg2_1': [[80, 720], [90, 720], [110, 720], [110, 720]], 'path2_seg2_2': [[90, 720], [120, 720], [120, 720], [120, 720]], 'path2_seg2_3': [[110, 720], [110, 720], [110, 720], [110, 720]], 'path2_seg3_1': [[60, 720], [70, 720], [80, 720], [90, 720]], 'path2_seg3_2': [[70, 720], [80, 720], [80, 720], [110, 720]], 'path2_seg3_3': [[120, 480], [120, 720], [120, 720], [120, 720]], 'path3_seg1_1': [[60, 720], [100, 720], [100, 720], [110, 720]], 'path3_seg1_2': [[80, 720], [110, 720], [110, 720], [110, 720]], 'path3_seg1_3': [[80, 720], [120, 720], [120, 720], [120, 720]], 'path3_seg2_1': [[80, 720], [80, 720], [110, 720], [110, 720]], 'path3_seg2_2': [[120, 720], [120, 720], [120, 720], [120, 720]], 'path3_seg2_3': [[120, 720], [120, 720], [120, 720], [120, 720]], 'path3_seg3_1': [[80, 720], [120, 720], [120, 720], [120, 720]], 'path3_seg3_2': [[80, 720], [90, 720], [120, 720], [120, 720]], 'path3_seg3_3': [[100, 720], [100, 720], [100, 720], [100, 720]], 'path4_seg1_1': [[110, 720], [110, 720], [110, 720], [120, 720]], 'path4_seg1_2': [[120, 480], [120, 720], [120, 720], [120, 720]], 'path4_seg1_3': [[120, 720], [120, 720], [120, 720], [120, 720]], 'path4_seg2_1': [[120, 720], [120, 720], [120, 720], [120, 720]], 'path4_seg2_2': [[120, 720], [120, 720], [120, 720], [120, 720]], 'path4_seg2_3': [[120, 720], [120, 720], [120, 720], [120, 720]], 'path4_seg3_1': [[80, 720], [90, 720], [120, 720], [120, 720]], 'path4_seg3_2': [[120, 720], [120, 720], [120, 720], [120, 720]], 'path4_seg3_3': [[120, 720], [120, 720], [120, 720], [120, 720]], 'path5_seg1_1': [[70, 720], [80, 720], [110, 720], [110, 720]], 'path5_seg1_2': [[120, 720], [120, 720], [120, 720], [120, 720]], 'path5_seg1_3': [[120, 720], [120, 720], [120, 720], [120, 720]], 'path5_seg2_1': [[120, 480], [120, 480], [120, 480], [120, 480]], 'path5_seg2_2': [[120, 480], [120, 720], [120, 720], [120, 720]], 'path5_seg2_3': [[120, 720], [120, 720], [120, 720], [120, 720]], 'path5_seg3_1': [[80, 720], [110, 720], [110, 720], [90, 1080]], 'path5_seg3_2': [[100, 720], [120, 720], [120, 720], [120, 720]], 'path5_seg3_3': [[120, 720], [120, 720], [120, 720], [120, 720]]}

scene_style = dict(
                xaxis = dict(
                    backgroundcolor="rgb(200, 200, 230)",
                    gridcolor="white",
                    showbackground=True,
                    zerolinecolor="white",),
                yaxis = dict(
                    backgroundcolor="rgb(230, 200,230)",
                    gridcolor="white",
                    showbackground=True,
                    zerolinecolor="white"),
                zaxis = dict(
                    backgroundcolor="rgb(230, 230,200)",
                    gridcolor="white",
                    showbackground=True,
                    zerolinecolor="white",),)