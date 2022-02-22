import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

app = dash.Dash()

df = pd.read_csv(
    "./df.csv"
)

fig = px.scatter(
    df,
    x="intensity",
    y="time"
)

app.layout = html.Div([dcc.Graph(id="life-exp-vs-gdp", figure=fig)])

if __name__ == "__main__":
    app.run_server(debug=True)