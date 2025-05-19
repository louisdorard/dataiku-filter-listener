import React, { useEffect } from "react";
import { Streamlit } from "streamlit-component-lib";

const FilterListener = () => {
  useEffect(() => {
    const handler = (event: MessageEvent) => {
      if (event.data?.type === "filters") {
        Streamlit.setComponentValue(event.data.filters);
      }
    };
    window.addEventListener("message", handler);
    return () => window.removeEventListener("message", handler);
  }, []);

  return <div>Listening for Dataiku Filters...</div>;
};

export default FilterListener;
