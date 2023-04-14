import dash
from dash import html
import dash_daq as daq

# Define o layout do aplicativo
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Dashboard em Python'),

    html.Div([
        html.Div([
            daq.Gauge(
                id='my-gauge-3',
                label='Pressão',
                min=0,
                max=100,
                value=20,
                showCurrentValue=True,
                units="BAR",
                color={"gradient":True,"ranges":{"green":[0,50],"yellow":[50,80],"red":[80,100]}}
            ),
        ], className='inline-block'),
        
        html.Div([
            daq.Gauge(
                id='my-gauge',
                label='Velocidade',
                min=0,
                max=200,
                value=100
            ),
        ], className='inline-block'),

        html.Div([
            daq.Gauge(
                id='my-gauge-2',
                label='Temperatura',
                min=-20,
                max=50,
                value=25,
                color={"gradient":True,"ranges":{"green":[0,20],"yellow":[20,35],"red":[35,50]}}
            ),
        ], className='inline-block'),      
        
    ], className='row')
])

if __name__ == '__main__':
    app.run_server(debug=True)
