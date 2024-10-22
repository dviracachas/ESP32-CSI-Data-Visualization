import streamlit as st # web development
import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import time # to simulate a real time data, time loop 
import plotly.express as px # interactive charts 


# read csv from a github repo
df = pd.read_csv("CSIDataExample.csv")


st.set_page_config(
    page_title = 'ESP32 CSI-Data Visualization',
    page_icon = '📡',
    layout = 'wide'
)

# dashboard title

st.title("📡 ESP32 CSI-Data Visualization")

# top-level filters 

role_filter = st.selectbox("Select the role", pd.unique(df['role']))


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
    st.markdown("### Detailed Data View")
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

