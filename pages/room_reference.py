import dash
import numpy as np
from dash import html, dcc
from utils import *
from analyze_plotly_velocity import *
import plotly.express as px


dash.register_page(__name__)

scene_name = 'room'
p_width = 800
p_height = 700

with open(f'reference_velocity/{scene_name}_cleaned.txt', 'r') as file:
    lines = file.readlines()
velocities = [float(line.strip()) for line in lines]
# print(f'velocities {velocities}')
velocities = np.array(velocities)
velocities /= 51
frame_limit = frame_per_fps_video(166)
velocities /= (frame_limit + 1)
# print(f'velocities {velocities}')

dfs_by_bitrate = create_df_per_sequence(room_max_comb_per_sequence, velocities)
# bitrates = [500, 1000, 1500, 2000]
# bitrates = [500, ]
fig500 = px.scatter_3d(dfs_by_bitrate[500], x='resolution', y='fps', z='velocity', color='path') # scatter_3d line_3d
fig500.update_layout(title=f'scene {scene_name} \n optimal fps + resolution for different velocity, bitrate 500kbps', 
                    autosize=False,
                    width=p_width, height=p_height,
                    margin=dict(l=65, r=50, b=65, t=90),
                    showlegend=False,
                    scene = scene_style
                )

fig1000 = px.scatter_3d(dfs_by_bitrate[1000], x='resolution', y='fps', z='velocity', color='path') # scatter_3d line_3d
fig1000.update_layout(title=f'scene {scene_name} \n optimal fps + resolution for different velocity, bitrate 1000kbps', 
                    autosize=False,
                    width=p_width, height=p_height,
                    margin=dict(l=65, r=50, b=65, t=90),
                    showlegend=False,
                    scene = scene_style
                )

bitrate3 = 1500
fig1500 = px.scatter_3d(dfs_by_bitrate[bitrate3], x='resolution', y='fps', z='velocity', color='path') # scatter_3d line_3d
fig1500.update_layout(title=f'scene {scene_name} \n optimal fps + resolution for different velocity, bitrate {bitrate3}kbps', 
                    autosize=False,
                    width=p_width, height=p_height,
                    margin=dict(l=65, r=50, b=65, t=90),
                    showlegend=False,
                    scene = scene_style,
                )


bitrate4 = 2000
fig2000 = px.scatter_3d(dfs_by_bitrate[bitrate4], x='resolution', y='fps', z='velocity', color='path') # scatter_3d line_3d
fig2000.update_layout(title=f'scene {scene_name} \n optimal fps + resolution for different velocity, bitrate {bitrate4}kbps', 
                    autosize=False,
                    width=p_width, height=p_height,
                    margin=dict(l=65, r=50, b=65, t=90),
                    showlegend=False,
                    scene = scene_style,
                )



df = create_df_per_sequence(room_max_comb_per_sequence, velocities, COMBINE=True)
# print(f'df \n {df}')
fig_all_bitrates = px.scatter_3d(df, x='resolution', y='fps', z='velocity', color='bitrate') # scatter_3d line_3d

fig_all_bitrates.update_layout(title=f'scene {scene_name} \n optimal fps + resolution for different bitrate, color indicates bitrate', 
                                autosize=False,
                                width=p_width+200, height=p_height+200,
                                scene = scene_style, margin=dict(l=65, r=50, b=65, t=90))


layout = html.Div([
                html.H1(f'Complex scene {scene_name}'),
                html.Div([
                    html.Div([
                        # html.H3('Column 1'),
                        dcc.Graph(id=f'{scene_name}500', figure=fig500),
                        dcc.Graph(id=f'{scene_name}1500', figure=fig1500)
                    ], className="six columns"),

                    html.Div([
                        # html.H3('Column 2'),
                        dcc.Graph(id=f'{scene_name}1000', figure=fig1000),
                        dcc.Graph(id=f'{scene_name}2000', figure=fig2000),
                    ], className="six columns"),
                ], className="row"),
                html.Div([dcc.Graph(id=f'{scene_name}allbitrates', figure=fig_all_bitrates),], className="row"),
])


