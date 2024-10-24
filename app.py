import streamlit as st # web development
import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import time # to simulate a real time data, time loop 
import plotly.express as px # interactive charts 
from io import StringIO
import serial
import serial.tools.list_ports

# Page configuration
st.set_page_config(
    page_title = 'ESP32 CSI-Data Visualization',
    page_icon = '📡',
)
st.title("📡 ESP32 CSI-Data Visualization")

# Initialize dataframe
csv_header = 'type,role,mac,rssi,rate,sig_mode,mcs,bandwidth,smoothing,not_sounding,aggregation,stbc,fec_coding,sgi,rssi,ampdu_cnt,channel,secondary_channel,local_timestamp,ant,sig_len,rx_state,real_time_set,real_timestamp,len,CSI_DATA\n'
df = pd.read_csv(StringIO(csv_header))

# Dashboard
with st.sidebar:
    st.header("⚙ Settings")
    # Port configuration
    listening_port = st.selectbox("Select the port of the ESP32:", list(serial.tools.list_ports.comports()))
    baudrate = st.selectbox("Configure the baud rate:", [921600, 1152000])

    # Port usage
    st.session_state['read_data'] = False
    col1, col2 = st.columns(2)
    with col1:
        # Receive information
        if st.button("🚀 Read port"):
            # Open port
            if 'ser' not in st.session_state.keys():
                st.session_state['ser'] = serial.Serial(listening_port.name, baudrate, timeout=1)
            else:
                if not st.session_state.ser.is_open:
                    st.session_state['ser'] = serial.Serial(listening_port.name, baudrate, timeout=1)
            # Read port
            st.session_state['read_data'] = True
            st.session_state.df = df
            
    with col2:
        # Close serial port
        if st.button("✋ Close port"):
            st.session_state['read_data'] = False
            if 'ser' in st.session_state.keys():
                st.session_state.ser.close()

# Loop to retrieve data
i = 0 # Index used to provide different keys to the generated objects
placeholder = st.empty() # Space used to render the data
while st.session_state['read_data']:
    i = i+1
    line = st.session_state.ser.readline()   # Read a '\n' terminated line
    # Append every read line
    try:
        new_col = pd.read_csv(StringIO(csv_header + str(line)))
        if 'df' in st.session_state.keys():
            st.session_state['df'] = pd.concat([st.session_state.df,new_col], ignore_index=True)
        else:
            st.session_state['df'] = pd.concat([df,new_col], ignore_index=True)
    except:
        line = "Serial not readable"

    # Render the data visualization objects (during loop)
    with placeholder.container():
        if 'df' in st.session_state.keys():
            fig = px.line(data_frame=st.session_state.df, x="real_timestamp", y="rssi", title='Noise floor vs. Time')
        else:
            fig = px.line(data_frame=df, x="real_timestamp", y="rssi", title='Noise floor vs. Time')
        st.plotly_chart(fig, use_container_width=True, key=f"nf_vs_time{i}")

        st.markdown("###### Detailed Data View")
        if 'df' in st.session_state.keys():
            st.dataframe(st.session_state.df)
        else:
            st.dataframe(df) 


# Final data visualization (after reading the serial port)
if 'df' in st.session_state.keys():
    fig = px.line(data_frame=st.session_state.df, x="real_timestamp", y="rssi", title='Noise floor vs. Time')
else:
    fig = px.line(data_frame=df, x="real_timestamp", y="rssi", title='Noise floor vs. Time')
st.plotly_chart(fig, use_container_width=True, key=f"nf_vs_time{i}")

st.markdown("###### Detailed Data View")
if 'df' in st.session_state.keys():
    st.dataframe(st.session_state.df)
else:
    st.dataframe(df) 