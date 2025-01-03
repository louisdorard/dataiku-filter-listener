# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DataikuFilterListener(Component):
    """A DataikuFilterListener component.
The DataikuFilterListener component listens for events from the document object or children if provided.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The children of this component. If any children are provided, the
    component will listen for events from these      components. If no
    children are specified, the component will listen for events from
    the document object.

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- className (string; optional):
    A custom class name.

- events (list of dicts; default [{ "event": "message", "props": ["data"] }]):
    The event entry specifies which event to listen to, e.g. \"click\"
    for click events. The \"props\" entry specifies      what event
    properties to record, e.g. [\"x\", \"y\"] to get the cursor
    position.

    `events` is a list of dicts with keys:

    - event (string; optional)

    - props (list of strings; optional)

- filters (list; optional):
    Values from the latest event fired by the Dataiku Dashboard
    Filters.

- logging (boolean; default False):
    If True, event information is logged to the javascript console.
    Useful if you can't remember events props.

- style (dict; optional):
    The CSS style of the component.

- useCapture (boolean; default False):
    Value of useCapture used when registering event listeners."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dataiku_filter_listener'
    _type = 'DataikuFilterListener'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, events=Component.UNDEFINED, logging=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, filters=Component.UNDEFINED, useCapture=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'events', 'filters', 'logging', 'style', 'useCapture']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'events', 'filters', 'logging', 'style', 'useCapture']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(DataikuFilterListener, self).__init__(children=children, **args)
