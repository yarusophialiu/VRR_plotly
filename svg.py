import plotly.io as pio
import plotly.express as px
from analyze_plotly_velocity import *



scene_name = ': all scenes'
p_width = 800
p_height = 700

dfs_by_bitrate = create_df_all_sequence(SCENES)
print(f'dfs_by_bitrate \n {dfs_by_bitrate[500].shape}')
# Generate the scatter plot
fig500 = px.scatter_3d(
    dfs_by_bitrate[500],
    x='resolution', y='fps', z='velocity',
    color='path'
)

# Update the layout
fig500.update_layout(
    # title=f'scene {scene_name} \n optimal fps + resolution for different velocity, bitrate 500kbps',
    autosize=True,
    width=p_width,
    height=p_height,
    # margin=dict(l=65, r=50, b=65, t=0),
    margin=dict(l=0, r=0, b=0, t=0),
    showlegend=False,
    # scene=scene_style,
    font=dict(
        family="Arial, sans-serif",
        size=13
    ),
    scene=dict(
        xaxis_title="Resolution",  # Update x-axis title here
        yaxis_title="Framerate (Hz)",
        zaxis_title="Velocity",
        **scene_style
    ),
    scene_camera_eye=dict(x=1.8, y=1.8, z=1)
)

# print(f"Scatter plot saved as {svg_output_path}")

fig1000 = px.scatter_3d(dfs_by_bitrate[1000], x='resolution', y='fps', z='velocity', color='path') # scatter_3d line_3d
fig1000.update_layout(
    # title=f'scene {scene_name} \n optimal fps + resolution for different velocity, bitrate 1000kbps', 
                    autosize=False,
                    width=p_width, height=p_height,
                    # margin=dict(l=65, r=50, b=65, t=0),
                    margin=dict(l=0, r=0, b=0, t=0),
                    showlegend=False,
                    # scene = scene_style,
                    font=dict(size=13),
                    scene=dict(
                        xaxis_title="Resolution",  # Update x-axis title here
                        yaxis_title="Framerate (Hz)",
                        zaxis_title="Velocity",
                        **scene_style
                    ),
                    scene_camera_eye=dict(x=1.8, y=1.8, z=1)
                )

bitrate3 = 1500
fig1500 = px.scatter_3d(dfs_by_bitrate[bitrate3], x='resolution', y='fps', z='velocity', color='path') # scatter_3d line_3d
fig1500.update_layout(
    # title=f'scene {scene_name} \n optimal fps + resolution for different velocity, bitrate {bitrate3}kbps', 
                    autosize=False,
                    width=p_width, height=p_height,
                    # margin=dict(l=65, r=50, b=65, t=0),
                    margin=dict(l=0, r=0, b=0, t=0),
                    showlegend=False,
                    # scene = scene_style,
                    font=dict(size=13),
                    scene=dict(
                        xaxis_title="Resolution",  # Update x-axis title here
                        yaxis_title="Framerate (Hz)",
                        zaxis_title="Velocity",
                        **scene_style
                    ),
                    scene_camera_eye=dict(x=1.8, y=1.8, z=1)
                )


bitrate4 = 2000
fig2000 = px.scatter_3d(dfs_by_bitrate[bitrate4], x='resolution', y='fps', z='velocity', color='path') # scatter_3d line_3d
fig2000.update_layout(
    # title=f'scene {scene_name} \n optimal fps + resolution for different velocity, bitrate {bitrate4}kbps', 
                    autosize=False,
                    width=p_width, height=p_height,
                    # margin=dict(l=65, r=50, b=65, t=0),
                    margin=dict(l=0, r=0, b=0, t=0),
                    showlegend=False,
                    # scene = scene_style,
                    font=dict(size=13),
                    scene=dict(
                        xaxis_title="Resolution",  # Update x-axis title here
                        yaxis_title="Framerate (Hz)",
                        zaxis_title="Velocity",
                        **scene_style
                    ),
                    scene_camera_eye=dict(x=1.8, y=1.8, z=1)
                )

fig500.write_image('images/fig500.svg')
# fig1000.write_image('images/fig1000.svg')
# fig1500.write_image('images/fig1500.svg')
# fig2000.write_image('images/fig2000.svg')