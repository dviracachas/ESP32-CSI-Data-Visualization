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
## Two headers are joined this way so that it is easier to concatenate the dataframe later
## given that the CSI_DATA is separated using spaces
csv_header = 'type,role,mac,rssi,rate,sig_mode,mcs,bandwidth,smoothing,not_sounding,aggregation,stbc,fec_coding,sgi,noise_floor,ampdu_cnt,channel,secondary_channel,local_timestamp,ant,sig_len,rx_state,real_time_set,real_timestamp,len,CSI_DATA\n'
df = pd.read_csv(StringIO(csv_header))
csi_header = 'CSI0 CSI1 CSI2 CSI3 CSI4 CSI5 CSI6 CSI7 CSI8 CSI9 CSI10 CSI11 CSI12 CSI13 CSI14 CSI15 CSI16 CSI17 CSI18 CSI19 CSI20 CSI21 CSI22 CSI23 CSI24 CSI25 CSI26 CSI27 CSI28 CSI29 CSI30 CSI31 CSI32 CSI33 CSI34 CSI35 CSI36 CSI37 CSI38 CSI39 CSI40 CSI41 CSI42 CSI43 CSI44 CSI45 CSI46 CSI47 CSI48 CSI49 CSI50 CSI51 CSI52 CSI53 CSI54 CSI55 CSI56 CSI57 CSI58 CSI59 CSI60 CSI61 CSI62 CSI63 CSI64 CSI65 CSI66 CSI67 CSI68 CSI69 CSI70 CSI71 CSI72 CSI73 CSI74 CSI75 CSI76 CSI77 CSI78 CSI79 CSI80 CSI81 CSI82 CSI83 CSI84 CSI85 CSI86 CSI87 CSI88 CSI89 CSI90 CSI91 CSI92 CSI93 CSI94 CSI95 CSI96 CSI97 CSI98 CSI99 CSI100 CSI101 CSI102 CSI103 CSI104 CSI105 CSI106 CSI107 CSI108 CSI109 CSI110 CSI111 CSI112 CSI113 CSI114 CSI115 CSI116 CSI117 CSI118 CSI119 CSI120 CSI121 CSI122 CSI123 CSI124 CSI125 CSI126 CSI127\n'
df_csi = pd.read_csv(StringIO(csi_header), sep=' ')
df = pd.concat([df, df_csi], axis=1)

# Dashboard
with st.sidebar:
    st.header("⚙ Settings")

    # Port configuration
    listening_port = st.selectbox("Select the port of the ESP32:", list(serial.tools.list_ports.comports()))
    baudrate = st.selectbox("Configure the baud rate:", [921600, 1152000])
    st.divider()
    
    # Variable selection
    graph_var_x = st.selectbox("Select the variable of the x-axis:", df.columns, index=23)
    graph_var_y = st.selectbox("Select the variable of the y-axis:", df.columns, index=3)

    st.divider()

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
            # Refresh data
            st.session_state.df = df
            st.session_state.csi = None
            # Read port
            st.session_state['read_data'] = True
            
    with col2:
        # Close serial port
        if st.button("✋ Close port"):
            st.session_state['read_data'] = False
            if 'ser' in st.session_state.keys():
                st.session_state.ser.close()

    st.caption("🐱‍💻 Made with ♥ by David Viracachá")

# Loop to retrieve data
i = 0 # Index used to provide different keys to the generated objects
placeholder = st.empty() # Space used to render the data
while st.session_state['read_data']:
    # Return to the top of the page to prevent confussion with old data
    if i == 0:
        st.components.v1.html("""<script>window.parent.document.querySelector('section.main').scrollTo(0, 0);</script>""", height=0)

    # Append every read line
    recieved_line = str(st.session_state.ser.readline())[2:]   # Read a '\n' terminated line, ignore "b'" at the beggining
    try:
        # Join the original dataframe with the separated CSI-Data, ignore '[' character for the separation
        new_col = pd.read_csv(StringIO(csv_header + recieved_line))
        csi_data_separated = pd.read_csv(StringIO(csi_header + new_col['CSI_DATA'][0][1:]), sep=' ', usecols=range(128))
        joint_new_col = pd.concat([new_col, csi_data_separated], axis=1)
        if 'df' in st.session_state.keys():
            st.session_state['df'] = pd.concat([st.session_state.df,joint_new_col], ignore_index=True)
        else:
            st.session_state['df'] = pd.concat([df,joint_new_col], ignore_index=True)    
    except:
        line = "Serial not readable"

    # Render the data visualization objects (during loop)
    with placeholder.container():
        if 'df' in st.session_state.keys():
            fig = px.line(data_frame=st.session_state.df, x=graph_var_x, y=graph_var_y, title=f'{graph_var_y} vs. {graph_var_x}')
        else:
            fig = px.line(data_frame=df, x=graph_var_x, y=graph_var_y, title=f'{graph_var_y} vs. {graph_var_x}')
        st.plotly_chart(fig, use_container_width=True, key=f"nf_vs_time{i}")

        st.markdown("###### Detailed Data View")
        if 'df' in st.session_state.keys():
            st.dataframe(st.session_state.df)
        else:
            st.dataframe(df)

    i = i+1

# Final data visualization (after reading the serial port)
if 'df' in st.session_state.keys():
    fig = px.line(data_frame=st.session_state.df, x=graph_var_x, y=graph_var_y, title=f'{graph_var_y} vs. {graph_var_x}')
else:
    fig = px.line(data_frame=df, x=graph_var_x, y=graph_var_y, title=f'{graph_var_y} vs. {graph_var_x}')
st.plotly_chart(fig, use_container_width=True, key=f"nf_vs_time{i}")

st.markdown("###### Detailed Data View")
if 'df' in st.session_state.keys():
    st.dataframe(st.session_state.df)
else:
    st.dataframe(df)