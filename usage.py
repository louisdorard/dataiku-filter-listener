from dataiku_filter_listener import DataikuFilterListener
from dash_extensions.enrich import DashProxy, html, Input, Output

"""
Initialize the Dash app
Remove this line if you are creating a Dash app within Dataiku
"""
app = DashProxy()

"""
Add the DataikuFilterListener component to the layout
We also add a placeholder to show filter values, for demo purposes
"""
app.layout = html.Div(
    [
        DataikuFilterListener(logging=True, id="dfl"),
        html.H1("Dataiku Dashboard Filters"),
        html.P("Filters will be displayed in the log below"),
        html.Div(id="log", children="")
    ]
)

"""
Callback that will be triggered when the filters change and will display the filter values in the placeholder

Args:
    filters: array with the filter values for each dataset column used in the Dataiku Dashboard Filters

Returns:
    string representation of the filters
"""
@app.callback(
    Output("log", "children"), Input("dfl", "filters"), prevent_initial_call=True
)
def filter_event(filters):
    filters_str = str(filters)
    print("Filters: " + filters_str)
    return filters_str

"""
Run the Dash app
Remove this block if you are creating a Dash app within Dataiku
"""
if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8050)
