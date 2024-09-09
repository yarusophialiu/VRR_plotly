import dash
from dash import html
from dash import dcc
from utils import *
from analyze_plotly_velocity import *
import plotly.express as px


########### Define your variables
beers=['Chesapeake Stout', 'Snake Dog IPA', 'Imperial Porter', 'Double Dog IPA']
ibu_values=[35, 60, 85, 75]
abv_values=[5.4, 7.1, 9.2, 4.3]
color1='darkred'
color2='orange'
mytitle='Beer Comparison'
tabtitle='beer!'
myheading='VRR Plotly'
label1='IBU'
label2='ABV'
githublink='https://github.com/austinlasseter/flying-dog-beers'
sourceurl='https://www.flyingdog.com/beers/'

########### Set up the chart

scene_name = 'bistro'
p_width = 800
p_height = 700

with open('velocity_sequence/bistro_velocity_cleaned.txt', 'r') as file:
    lines = file.readlines()
velocities = [float(line.strip()) for line in lines]
# print(f'velocities {velocities}')
dfs_by_bitrate = create_df_per_sequence(bistro_max_comb_per_sequence, velocities)
# bitrates = [500, 1000, 1500, 2000]
# bitrates = [500, ]



########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets,use_pages=True)
server = app.server
app.title=tabtitle

app.layout = html.Div([
    html.H1('VRR Plot results'),
    html.Div([
        html.Div(
            dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
        ) for page in dash.page_registry.values()
    ]),
    dash.page_container
])

if __name__ == '__main__':
    app.run_server()
    # app.run(debug=True)