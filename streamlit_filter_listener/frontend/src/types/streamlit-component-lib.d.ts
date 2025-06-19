declare module 'streamlit-component-lib' {
  export interface Streamlit {
    setComponentValue: (value: any) => void;
    getComponentValue: () => any;
    setFrameHeight: (height: number) => void;
    RENDER_EVENT: string;
    COMPONENT_READY_EVENT: string;
  }

  export const Streamlit: Streamlit;
} 