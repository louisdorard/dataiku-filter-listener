# Inspired from https://www.dash-extensions.com/components/event_listener

from dash_extensions.enrich import DashProxy, html, Input, Output, State
from dash_extensions import EventListener
from dash.exceptions import PreventUpdate

app = DashProxy()

app.layout = html.Div([
    EventListener(
        # events=[{"event": "message", "props": ["k"]}], # JavaScript event(s) that we want to listen to and what properties to collect.
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
    print(event)
    if event is None:
        raise PreventUpdate()
    data = event.data
    if (data and data.k):
        print("Caught event! value is " + data.k)
    return "callback"

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8050)
