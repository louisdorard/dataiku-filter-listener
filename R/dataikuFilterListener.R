# AUTO GENERATED FILE - DO NOT EDIT

#' @export
dataikuFilterListener <- function(children=NULL, id=NULL, className=NULL, events=NULL, filters=NULL, logging=NULL, style=NULL, useCapture=NULL) {
    
    props <- list(children=children, id=id, className=className, events=events, filters=filters, logging=logging, style=style, useCapture=useCapture)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DataikuFilterListener',
        namespace = 'dataiku_filter_listener',
        propNames = c('children', 'id', 'className', 'events', 'filters', 'logging', 'style', 'useCapture'),
        package = 'dataikuFilterListener'
        )

    structure(component, class = c('dash_component', 'list'))
}
