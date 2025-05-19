import streamlit.components.v1 as components
from pathlib import Path

_filter_listener = components.declare_component(
    "filter_listener",
    path=str(Path(__file__).parent / "frontend" / "build"),
)

def filter_listener():
    return _filter_listener() or []
