import streamlit as st # web development

# Page configuration
st.set_page_config(
    page_title = 'Help & Troubleshoot',
    page_icon = '💡',
)

st.title("💡 Help & Troubleshoot")
st.logo("DKS_logo.png", size="large")

st.header("ESP32-CSI-Tool")
st.markdown("""Github repository: [ESP32-CSI-Tool by StevenMHernandez](https://github.com/StevenMHernandez/ESP32-CSI-Tool)""")
st.markdown("""Software requirements:
- Visual Studio Code
- Python (Tested with version 3.12.7)
- ESP-IDF VSCode Extension (Tested with version 5.0.7)
""")

st.subheader("How to program the ESP32")
st.video("Videos/ESP32-CSI-Tool.mp4", format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)

st.header("Visualizer")
st.markdown("""Github repository: [ESP32-CSI-Data-Visualization by dviracachas](https://github.com/dviracachas/ESP32-CSI-Data-Visualization)""")
st.markdown("""Required Python libraries:
- streamlit
- numpy
- pandas
- plotly
- pyserial
""")

st.subheader("How to install?")
st.video("Videos/Installation.mp4", format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)

st.subheader("How to use?")

st.video("Videos/Usage.mp4", format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)

st.subheader("What do I do in case of errors?")
st.video("Videos/Troubleshooting.mp4", format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)

st.divider()
st.columns(3)[1].caption("🐱‍💻 Made with ♥ by David Viracachá")