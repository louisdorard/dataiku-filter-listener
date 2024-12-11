from dataiku_filter_listener import DataikuFilterListener
from dash_extensions.enrich import DashProxy, html, Input, Output, State
from dash.exceptions import PreventUpdate

app = DashProxy()

app.layout = html.Div([
    DataikuFilterListener(
        logging=True,
        id="el" # "el" stands for event listener
    ),
    html.Div(id="log", children="init")
])

@app.callback(
    Output("log", "children"),
    Input("el", "n_events"), # the number of events fired
    State("el", "event"), # the last event fired
    prevent_initial_call=True)
def message_event(n_events, event):
    if event is None:
        raise PreventUpdate()
    elif "data" in event:
        data = event["data"]
        if (data and "k" in data):
            print("Caught event! value is " + data["k"])
    return "callback"

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8050)
