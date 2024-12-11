# AUTO GENERATED FILE - DO NOT EDIT

export dataikufilterlistener

"""
    dataikufilterlistener(;kwargs...)
    dataikufilterlistener(children::Any;kwargs...)
    dataikufilterlistener(children_maker::Function;kwargs...)


A DataikuFilterListener component.
The DataikuFilterListener component listens for events from the document object or children if provided.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The children of this component. If any children are provided, the component will listen for events from these
     components. If no children are specified, the component will listen for events from the document object.
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): A custom class name.
- `event` (Dict; optional): The latest event fired.
- `events` (optional): The event entry specifies which event to listen to, e.g. "click" for click events. The "props" entry specifies
     what event properties to record, e.g. ["x", "y"] to get the cursor position.. events has the following type: Array of lists containing elements 'event', 'props'.
Those elements have the following types:
  - `event` (String; optional)
  - `props` (Array of Strings; optional)s
- `logging` (Bool; optional): If true, event information is logged to the javascript console. Useful if you can't remember events props.
- `n_events` (Real; optional): The number of events fired.
- `style` (Dict; optional): The CSS style of the component.
- `useCapture` (Bool; optional): Value of useCapture used when registering event listeners.
"""
function dataikufilterlistener(; kwargs...)
        available_props = Symbol[:children, :id, :className, :event, :events, :logging, :n_events, :style, :useCapture]
        wild_props = Symbol[]
        return Component("dataikufilterlistener", "DataikuFilterListener", "dataiku_filter_listener", available_props, wild_props; kwargs...)
end

dataikufilterlistener(children::Any; kwargs...) = dataikufilterlistener(;kwargs..., children = children)
dataikufilterlistener(children_maker::Function; kwargs...) = dataikufilterlistener(children_maker(); kwargs...)

