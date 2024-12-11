# Inspired from https://www.dash-extensions.com/components/event_listener

from dash_extensions.enrich import DashProxy, html, Input, Output, State
from dash_extensions import EventListener
from dash.exceptions import PreventUpdate

# JavaScript event(s) that we want to listen to and what properties to collect.
event = {"event": "message", "props": ["k"]}

app = DashProxy()

app.layout = html.Div([
    EventListener(logging=True, id="el"),
    html.Div(id="log")
])

@app.callback(
    Output("log", "children"),
    Input("el", "n_events"), # the number of events fired
    State("el", "event")) # the last event fired
def message_event(n_events, event):
    print(n_events)
    print(event)
    if event is None:
        raise PreventUpdate()
    return "callback"

if __name__ == "__main__":
    app.run_server()
