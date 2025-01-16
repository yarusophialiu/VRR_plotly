import pandas as pd
from utils import *
from analyze_plotly_velocity import *


# SCENES = ['bedroom']
# create_df_all_sequence(SCENES, COMBINE=False)
import plotly.io as pio
import plotly.express as px



scene_name = ': all scenes'
p_width = 800
p_height = 700

dfs_by_bitrate = create_df_all_sequence(SCENES)
print(f'dfs_by_bitrate \n {dfs_by_bitrate[500]}')