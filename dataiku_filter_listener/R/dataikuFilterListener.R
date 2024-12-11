# AUTO GENERATED FILE - DO NOT EDIT

#' @export
dataikuFilterListener <- function(children=NULL, id=NULL, className=NULL, event=NULL, events=NULL, logging=NULL, n_events=NULL, style=NULL, useCapture=NULL) {
    
    props <- list(children=children, id=id, className=className, event=event, events=events, logging=logging, n_events=n_events, style=style, useCapture=useCapture)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DataikuFilterListener',
        namespace = 'dataiku_filter_listener',
        propNames = c('children', 'id', 'className', 'event', 'events', 'logging', 'n_events', 'style', 'useCapture'),
        package = 'dataikuFilterListener'
        )

    structure(component, class = c('dash_component', 'list'))
}
