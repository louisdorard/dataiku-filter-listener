from dataiku_filter_listener import DataikuFilterListener
from dash_extensions.enrich import DashProxy, html, Input, Output

app = DashProxy()

app.layout = html.Div(
    [
        DataikuFilterListener(logging=True, id="el"),  # "el" stands for event listener
        html.Div(id="log", children="init"),
    ]
)


@app.callback(
    Output("log", "children"), Input("el", "filters"), prevent_initial_call=True
)
def filter_event(filters):
    filters = str(filters)
    print("Filters: " + filters)
    return filters


if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8050)
