import streamlit as st # web development

# Page configuration
st.set_page_config(
    page_title = 'Help & Troubleshoot',
    page_icon = '💡',
)

st.title("💡 Help & Troubleshoot")
st.logo("DKS_logo.png", size="large")

st.subheader("How to install this tool?")
st.video("Videos/Installation.mp4", format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)

st.subheader("How to use this tool?")
st.markdown("""This tool works by connecting an ESP32 programmed with the [ESP32-CSI-Tool by StevenMHernandez](https://github.com/StevenMHernandez/ESP32-CSI-Tool)
            to an available USB port and reading it.""")
st.video("Videos/Usage.mp4", format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)

st.subheader("What do I do in case of errors?")
st.video("Videos/Troubleshooting.mp4", format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)

st.divider()
st.columns(3)[1].caption("🐱‍💻 Made with ♥ by David Viracachá")