import streamlit as st # web development
import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import time # to simulate a real time data, time loop 
import plotly.express as px # interactive charts 
from io import StringIO

# read csv from a github repo
df = pd.read_csv("CSIDataExample.csv")
csv_header = 'type,role,mac,rssi,rate,sig_mode,mcs,bandwidth,smoothing,not_sounding,aggregation,stbc,fec_coding,sgi,noise_floor,ampdu_cnt,channel,secondary_channel,local_timestamp,ant,sig_len,rx_state,real_time_set,real_timestamp,len,CSI_DATA\n'



st.set_page_config(
    page_title = 'ESP32 CSI-Data Visualization',
    page_icon = '📡',
    layout = 'wide'
)

# dashboard title

st.title("📡 ESP32 CSI-Data Visualization")

# top-level filters 

role_filter = st.selectbox("Select the role", pd.unique(df['role']))

columns_added = 0
# creating a single-element container.
placeholder = st.empty()

# dataframe filter 

df = df[df['role']==role_filter]


with placeholder.container():
    

    fig_col1, fig_col2 = st.columns(2)
    with fig_col1:
        st.markdown("### First Chart")
        fig = px.line(data_frame=df, x="real_timestamp", y="noise_floor", title='Noise floor vs. Time')
        st.plotly_chart(fig, use_container_width=True, key=f"nf_vs_time")

    with fig_col2:
        st.markdown("### Second Chart")
        fig2 = px.histogram(data_frame = df, x = 'noise_floor')
        st.plotly_chart(fig2, use_container_width=True, key=f"histogram_2")
    

    #if 'df' not in st.session_state:
     #   st.session_state.newData = df


    if st.button("Add row"):
            if 'columns_added' in st.session_state.keys():
                st.session_state['columns_added'] += 1
            else:
                st.session_state['columns_added'] = 1
            
            st.write(f"Added Columns: {st.session_state.columns_added}")


            new_col = pd.read_csv(StringIO(csv_header + "CSI_DATA,STA,08:3A:F2:B7:88:01,-62,11,1,7,1,1,1,1,0,0,1,-95,6,6,2,3165573,0,110,0,0,3.32647,384,[110 96 6 0 0 0 0 0 0 0 0 0 7 -11 6 -11 6 -11 6 -12 6 -12 5 -11 5 -12 5 -12 5 -12 4 -13 4 -13 4 -13 4 -13 4 -13 4 -13 3 -14 2 -14 2 -14 2 -14 2 -14 2 -15 2 -15 1 -15 1 -16 1 -16 1 -16 0 0 0 -16 0 -17 0 -17 -1 -17 0 -17 0 -18 1 -18 0 -18 0 -18 0 -18 0 -19 0 -19 0 -20 1 -20 1 -19 1 -19 1 -20 2 -19 2 -19 3 -19 3 -19 5 -20 5 -20 4 -20 6 -18 6 -18 0 0 0 0 0 0 0 0 0 0 ]"))
            if 'df' in st.session_state.keys():
                st.session_state['df'] = pd.concat([st.session_state.df,new_col], ignore_index=True)
            else:
                st.session_state['df'] = df
            #st.dataframe(df)
            st.dataframe(new_col)
            #df.loc[len(df)] = f"hola_{columns_added}"

    st.markdown("### Detailed Data View")
    if 'df' in st.session_state.keys():
        st.dataframe(st.session_state.df)
    else:
        st.dataframe(df)
    

# near real-time / live feed simulation 

#for seconds in range(200):
#while True: 


    
   
"""     
    df['age_new'] = df['age'] * np.random.choice(range(1,5))
    df['balance_new'] = df['balance'] * np.random.choice(range(1,5))

    # creating KPIs 
    avg_age = np.mean(df['age_new']) 

    count_married = int(df[(df["marital"]=='married')]['marital'].count() + np.random.choice(range(1,30)))
    
    balance = np.mean(df['balance_new']) 
    

    with placeholder.container():
        
        # create three columns
        kpi1, kpi2, kpi3 = st.columns(3)

        # fill in those three columns with respective metrics or KPIs 
        kpi1.metric(label="Age ⏳", value=round(avg_age), delta= round(avg_age) - 10)
        kpi2.metric(label="Married Count 💍", value= int(count_married), delta= - 10 + count_married)
        kpi3.metric(label="A/C Balance ＄", value= f"$ {round(balance,2)} ", delta= - round(balance/count_married) * 100)
        
        # create two columns for charts 

        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown("### First Chart")
            fig = px.density_heatmap(data_frame=df, y = 'age_new', x = 'marital')
            st.plotly_chart(fig, use_container_width=True, key=f"heatmap_{seconds}")
            #st.write(fig, key=f'1_{seconds}')
        with fig_col2:
            st.markdown("### Second Chart")
            fig2 = px.histogram(data_frame = df, x = 'age_new')
            #st.write(fig2)
            st.plotly_chart(fig2, use_container_width=True, key=f"histogram_2{seconds}")
        st.markdown("### Detailed Data View")
        st.dataframe(df)
        time.sleep(0.1)
    #placeholder.empty()
    """

