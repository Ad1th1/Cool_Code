# Just a peek into what the heck dash is...
# Brought to you from the official pages of the dash documentation `https://dash.plotly.com/layout`
# It's kinda sexy if you can excuse the crude language used...


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas","Apples", "Oranges", "Bananas"],
    "Amount": [4,1,2,2,4,5],
    "City": ["SF","SF","SF","Montreal","Montreal","Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example0graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
