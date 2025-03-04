import matplotlib.pyplot as plt
from analyze_plotly_velocity import *
from utils import *


# data = {
#     'path1_seg1_1': [
#         [(30, 720), (40, 720), (50, 720)],
#         [(30, 720), (30, 864), (30, 1080), (40, 720), (40, 864), (40, 1080), (50, 720), (60, 720), (70, 720), (80, 720), (90, 720)],
#         [(30, 720), (30, 864), (30, 1080), (40, 720), (40, 864), (40, 1080), (50, 720), (50, 864), (50, 1080), (60, 720), (60, 1080), (70, 720), (80, 720), (90, 720), (100, 720), (110, 720), (120, 720)],
#         [(30, 720), (30, 864), (30, 1080), (40, 720), (40, 864), (40, 1080), (50, 720), (50, 864), (50, 1080), (60, 720), (60, 864), (60, 1080), (70, 720), (70, 1080), (80, 720), (90, 720), (100, 720), (110, 720), (120, 720)]
#     ]
# }


def dropJOD(all_scenes, filename):
    for scene in all_scenes:
        print(f'scene {scene}')
        variable_name = f"{scene}_within_JOD_range"
        if variable_name in globals():
            comb_within_range = globals()[variable_name]
            print(f'comb_within_range {variable_name}')

            # Find the tuple with the minimum fps * resolution for each sublist
            min_data = {
                # key: [[min(sublist, key=lambda x: x[0] * x[1])] for sublist in value]
                key: [[*min(sublist, key=lambda x: x[0] * x[1])] for sublist in value]
                for key, value in comb_within_range.items()
            }

            # # print(min_data)
            # with open(filename, "a") as f:
            #     f.write(f"{scene}_comb_drop_JOD = {min_data}")
            #     f.write(f"\n")

            new_filename = f"cleaned_{filename}"
            print(f'hi {new_filename}')
            with open(new_filename, "a") as f:
                f.write(f"{variable_name} = {min_data}")
                f.write(f"\n")
            break

all_scenes =    [
            'bedroom', 
            'bistro', 
             'crytek_sponza', 
             'gallery', 
             'living_room', 
             'lost_empire', 
             'room', 'suntemple',
            'sibenik',
             'suntemple_statue' 
             ]

filename = "fps_res_drop_jod_THRESOLD60-2025-03-04-17_35.py"
dropJOD(all_scenes, filename)
