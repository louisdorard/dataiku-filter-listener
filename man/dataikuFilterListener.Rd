% Auto-generated: do not edit by hand
\name{dataikuFilterListener}

\alias{dataikuFilterListener}

\title{DataikuFilterListener component}

\description{
The DataikuFilterListener component listens for events from the document object or children if provided.
}

\usage{
dataikuFilterListener(children=NULL, id=NULL, className=NULL, events=NULL,
filters=NULL, logging=NULL, style=NULL, useCapture=NULL)
}

\arguments{
\item{children}{A list of or a singular dash component, string or number. The children of this component. If any children are provided, the component will listen for events from these
     components. If no children are specified, the component will listen for events from the document object.}

\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{className}{Character. A custom class name.}

\item{events}{List of lists containing elements 'event', 'props'.
those elements have the following types:
  - event (character; optional)
  - props (list of characters; optional)s. The event entry specifies which event to listen to, e.g. "click" for click events. The "props" entry specifies
     what event properties to record, e.g. ["x", "y"] to get the cursor position.}

\item{filters}{Unnamed list. Values from the latest event fired by the Dataiku Dashboard Filters.}

\item{logging}{Logical. If true, event information is logged to the javascript console. Useful if you can't remember events props.}

\item{style}{Named list. The CSS style of the component.}

\item{useCapture}{Logical. Value of useCapture used when registering event listeners.}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

