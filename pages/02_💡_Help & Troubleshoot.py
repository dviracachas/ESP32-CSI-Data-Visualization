import streamlit as st # web development

# Page configuration
st.set_page_config(
    page_title = 'Help & Troubleshoot',
    page_icon = '💡',
)

st.title("💡 Help & Troubleshoot")
st.logo("DKS_logo.png", size="large")

st.subheader("How to use this tool?")
st.markdown("""This tool works by connecting an ESP32 programmed with the [ESP32-CSI-Tool by StevenMHernandez](https://github.com/StevenMHernandez/ESP32-CSI-Tool)
            to an available USB port """)


st.divider()
st.columns(3)[1].caption("🐱‍💻 Made with ♥ by David Viracachá")