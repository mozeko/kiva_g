import pandas as pd 
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Kiva Egypt", page_icon=None, layout="wide", initial_sidebar_state="expanded")
# load data

kiva_eg = pd.read_csv('kiva_eg.csv')




st.sidebar.title("Kiva Egypt Dasdboard")
st.sidebar.image('loan.jpg')
st.sidebar.write("Tis is Dashboard is Using Kiva Egypt Dataset From Kaggle For Educational Purposes ")
st.sidebar.write("")
st.sidebar.write("Filter You Data :")
cat_filt = st.sidebar.selectbox("Categorical Filtering",[None,'Gender','region'])

year_filt = st.sidebar.selectbox("Year Filtering",[None,'funded_year'])



st.sidebar.write("")
st.sidebar.markdown("Made With :blush: by Analyst. Zakaria Mostafa ")

#body
# row a
a1,a2,a3, = st.columns(3)

a1.metric("Total.funded",kiva_eg['funded_amount'].sum())
a2.metric("Max.funded",kiva_eg['funded_amount'].max())
a3.metric("Min.funded",kiva_eg[kiva_eg['funded_amount']>0]['funded_amount'].min())

# row b1

st.subheader("Sectors in Egypt")
fig = px.bar(data_frame=kiva_eg,x='sector',y='funded_amount',color=cat_filt,pattern_shape=year_filt)
st.plotly_chart(fig,use_container_width=True)

#rowb2
st.subheader("Sector by Percent")
fig_2 = px.pie(data_frame=kiva_eg,names='sector',values='funded_amount')
st.plotly_chart(fig_2,use_container_width=True)



# row c
c1,c2 ,c3= st.columns((4,2,4))

with c1:
    st.text("Gender vs Funded amount")
    fig = px.bar(x='Gender',y='funded_amount',data_frame=kiva_eg,color=cat_filt)
    st.plotly_chart(fig,use_container_width=True)

with c3:
        st.text("Region vs Funded amount")
        fig = px.pie(names='region',values='funded_amount',data_frame=kiva_eg,hole=0.4,color=cat_filt)
        st.plotly_chart(fig,use_container_width=True)


sector_year = kiva_eg.pivot_table(index='funded_year',columns='sector',values='funded_amount')

st.text("Food vs Agriculture")
fig = px.scatter(data_frame=sector_year,x='Agriculture',y='Food')
st.plotly_chart(fig,use_container_width=True)


st.text("Funded amount")
fig = px.histogram(kiva_eg['funded_amount'])
st.plotly_chart(fig,use_container_width=True)






st.text("Count Female vs Male")
fig = px.bar(x='Gender',data_frame=kiva_eg,color=cat_filt)
st.plotly_chart(fig,use_container_width=True)

btn = st.button("Show Data")
if btn:
    st.dataframe(kiva_eg.sample(5))