import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide",
                   page_title='Premier League Dashboard',
                   page_icon="⚽️")  # Changed soccer ball icon!

@st.cache
def load():  
    return pd.read_csv('PremierLeague.csv')

# Load the data once per app session. This function gets called only when
# the module is loaded, and not at every rerun. It's ideal for large datasets that don't change often.

# main load starts here
df = load()

st.image('banner.jpeg', width=500)  # Adjust width as needed
st.title("Premier League Dashboard")
with st.expander('View raw Premier League data'):  # Corrected title
    st.dataframe(df.sample(1000))

rows, cols = df.shape
c1, c2 = st.columns(2)
c1.markdown(f'### total Records : {rows}')
c1.markdown(f'### total columns : {cols}')

numeric_df = df.select_dtypes(include='number')
cat_df = df.select_dtypes(exclude=['number'])
with st.expander("Columns names"):
    st.markdown(f'Columns with numbers : {",".join(numeric_df)}')
    st.markdown(f'Columns without numbers : {",".join(cat_df)}')

# visualization 

c1, c2 = st.columns([1, 3])
xcol = c1.selectbox("choose a column for x-axis", numeric_df.columns)
ycol = c1.selectbox("choose a column for y-axis", numeric_df.columns)
zcol = c1.selectbox("choose a column for z-axis", numeric_df.columns)
color = c1.selectbox("choose a column for color", cat_df.columns)
fig = px.scatter_3d(df, x=xcol, y=ycol, z=zcol, color=color, height=600)
c2.plotly_chart(fig, use_container_width=True)

st.title("What is Premier League")
c1, c2 = st.columns(2)
c1.video("https://youtu.be/X8R9cQAdLts?si=UxScXdBsN-8BGQmH")
c2.markdown(''' The Premier League is the highest level of the English football league system. Contested by 20 clubs, it operates on a system of promotion and relegation with the English Football League (EFL). Seasons typically run from August to May, with each team playing 38 matches against all other teams, both home and away.[1] Most games are played on Saturday and Sunday afternoons, with occasional weekday evening fixtures.[2]

The competition was founded as the FA Premier League on 20 February 1992 following the decision of First Division (top-tier league from 1888 until 1992) clubs to break away from the English Football League. However, teams may still be relegated to and promoted from the EFL Championship. The Premier League takes advantage of a £5 billion television rights deal, with Sky and BT Group securing the domestic rights to broadcast 128 and 32 games, respectively.[3][4] This deal will rise to £6.7 billion for the four seasons from 2025 to 2029.[5] The league is projected to earn $7.2bn in overseas TV rights from 2022 to 2025.[6] The Premier League is a corporation managed by a chief executive, with member clubs acting as shareholders.[7] Clubs were apportioned central payment revenues of £2.4 billion in 2016–17, with a further £343 million in solidarity payments to EFL clubs.''')

st.title("Premier League Clubs")
clubs = df['HomeTeam'].unique().tolist() + df['AwayTeam'].unique().tolist()
clubs = sorted(set(clubs))
st.info(", ".join(clubs))
