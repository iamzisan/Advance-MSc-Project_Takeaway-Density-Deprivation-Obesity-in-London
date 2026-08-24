# ============================================================
# Streamlit Dashboard: Takeaway Density, Deprivation and Obesity
# Student: Zisan Ahmed (24162855)
# Module: 7COM1075 - Data Science and Analytics Masters Project
# ============================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="London Takeaways & Obesity Dashboard",
    page_icon="🍔",
    layout="wide"
)

# Title
st.title("🍔 Takeaway Density, Deprivation and Obesity in London")
st.markdown("*MSc Project - Zisan Ahmed (24162855)*")
st.markdown("---")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('london_borough_final_data.csv')
    return df

try:
    df = load_data()
    st.success("✅ Data loaded successfully!")
except FileNotFoundError:
    st.error("❌ Error: 'london_borough_final_data.csv' not found.")
    st.stop()

# ---- Borough Coordinates ----
borough_coords = {
    'Barking and Dagenham': (51.540, 0.100),
    'Barnet': (51.620, -0.200),
    'Bexley': (51.440, 0.150),
    'Brent': (51.550, -0.300),
    'Bromley': (51.400, 0.020),
    'Camden': (51.540, -0.160),
    'City of London': (51.510, -0.090),
    'Croydon': (51.380, -0.100),
    'Ealing': (51.510, -0.300),
    'Enfield': (51.650, -0.080),
    'Greenwich': (51.480, 0.000),
    'Hackney': (51.550, -0.060),
    'Hammersmith and Fulham': (51.490, -0.220),
    'Haringey': (51.590, -0.100),
    'Hillingdon': (51.540, -0.450),
    'Islington': (51.540, -0.100),
    'Kingston upon Thames': (51.410, -0.300),
    'Lambeth': (51.460, -0.120),
    'Lewisham': (51.440, -0.020),
    'Merton': (51.400, -0.200),
    'Newham': (51.520, 0.040),
    'Redbridge': (51.580, 0.080),
    'Richmond upon Thames': (51.460, -0.300),
    'Southwark': (51.500, -0.080),
    'Sutton': (51.360, -0.200),
    'Tower Hamlets': (51.520, -0.040),
    'Waltham Forest': (51.590, -0.020),
    'Wandsworth': (51.460, -0.200),
    'Westminster': (51.500, -0.140)
}

# Add coordinates to dataframe
df['lat'] = df['BoroughName'].apply(lambda x: borough_coords.get(x, (51.5, -0.1))[0])
df['lon'] = df['BoroughName'].apply(lambda x: borough_coords.get(x, (51.5, -0.1))[1])

# ---- SIDEBAR ----
st.sidebar.header("🔍 Select a Borough")

borough_list = sorted(df['BoroughName'].unique())
selected_borough = st.sidebar.selectbox("Choose a London Borough:", borough_list)

st.sidebar.markdown("---")
st.sidebar.subheader("📊 Borough Metrics")

borough_data = df[df['BoroughName'] == selected_borough].iloc[0]

col1_side, col2_side = st.sidebar.columns(2)
with col1_side:
    st.metric("🏪 Takeaway Density", f"{borough_data['takeaway_density_per_1000']:.2f}")
with col2_side:
    st.metric("📉 IMD Score", f"{borough_data['IMD_Score']:.1f}")

st.sidebar.metric("⚖️ Obesity Rate", f"{borough_data['obesity_rate']:.1f}%")

st.sidebar.markdown("---")
st.sidebar.info("Data sources: FHRS, IMD 2019, PHE, ONS")

# Highlight selected borough in the map
df['selected'] = df['BoroughName'] == selected_borough
df['marker_size'] = df['selected'].apply(lambda x: 50 if x else 20)

# ---- MAIN CONTENT ----

# Row 1: Key Metrics
st.subheader("📈 London Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Average Takeaway Density", f"{df['takeaway_density_per_1000'].mean():.2f} per 1,000")
with col2:
    st.metric("Average Obesity Rate", f"{df['obesity_rate'].mean():.1f}%")
with col3:
    st.metric("Average IMD Score", f"{df['IMD_Score'].mean():.1f}")
with col4:
    st.metric("Number of Boroughs", f"{len(df)}")

st.markdown("---")

# ---- ROW 2: Map and Borough Info Side by Side ----
col_map, col_info = st.columns([2, 1])

with col_map:
    st.subheader("🗺️ Takeaway Density Map of London")
    
    fig_map = px.scatter_mapbox(
        df,
        lat='lat',
        lon='lon',
        size='marker_size',
        color='takeaway_density_per_1000',
        color_continuous_scale='RdYlGn_r',
        text='BoroughName',
        hover_data={
            'BoroughName': True,
            'takeaway_density_per_1000': ':.2f',
            'IMD_Score': ':.1f',
            'obesity_rate': ':.1f',
            'takeaway_count': True,
            'population': True,
            'lat': False,
            'lon': False,
            'marker_size': False,
            'selected': False
        },
        zoom=9.5,
        center={'lat': 51.5, 'lon': -0.1},
        title=None,
        labels={'takeaway_density_per_1000': 'Takeaway Density'}
    )
    
    # Customise the map - FIXED
    fig_map.update_traces(
        marker=dict(
            sizemode='diameter',
            sizeref=1,
            opacity=0.8
        ),
        textposition='top center',
        textfont=dict(size=10, color='black')
    )
    
    fig_map.update_layout(
        mapbox_style='open-street-map',
        height=500,
        margin=dict(l=0, r=0, t=0, b=0),
        coloraxis_colorbar=dict(
            title="Density",
            thickness=20,
            len=0.8
        ),
        hoverlabel=dict(
            bgcolor="white",
            font_size=12,
            font_family="Arial"
        )
    )
    
    st.plotly_chart(fig_map, use_container_width=True)
    st.caption("💡 Hover over a borough to see details | Click on the sidebar to select a borough")

with col_info:
    st.subheader("📍 Selected Borough")
    st.markdown(f"### {selected_borough}")
    
    st.markdown(f"""
    <div style="background-color:#f0f2f6; padding:15px; border-radius:10px;">
        <p><strong>🏪 Takeaway Density:</strong> {borough_data['takeaway_density_per_1000']:.2f} per 1,000</p>
        <p><strong>📊 IMD Score:</strong> {borough_data['IMD_Score']:.2f}</p>
        <p><strong>⚖️ Obesity Rate:</strong> {borough_data['obesity_rate']:.1f}%</p>
        <p><strong>🏢 Takeaways:</strong> {borough_data['takeaway_count']}</p>
        <p><strong>👥 Population:</strong> {borough_data['population']:,}</p>
    </div>
    """, unsafe_allow_html=True)
    
    rank_density = df['takeaway_density_per_1000'].rank(ascending=False)
    rank_obesity = df['obesity_rate'].rank(ascending=False)
    
    st.markdown(f"""
    <div style="background-color:#e8f4f8; padding:15px; border-radius:10px; margin-top:10px;">
        <p><strong>📈 Rankings:</strong></p>
        <p>🏪 Density Rank: #{int(rank_density[df['BoroughName'] == selected_borough].values[0])} of {len(df)}</p>
        <p>⚖️ Obesity Rank: #{int(rank_obesity[df['BoroughName'] == selected_borough].values[0])} of {len(df)}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ---- ROW 3: Two Scatter Plots ----
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏪 Takeaway Density vs Obesity Rate")
    
    fig1 = px.scatter(
        df,
        x='takeaway_density_per_1000',
        y='obesity_rate',
        text='BoroughName',
        size='population',
        color='IMD_Score',
        color_continuous_scale='RdYlGn_r',
        labels={
            'takeaway_density_per_1000': 'Takeaway Density (per 1,000)',
            'obesity_rate': 'Obesity Rate (%)',
            'IMD_Score': 'Deprivation Score'
        },
        hover_data=['BoroughName', 'takeaway_count']
    )
    
    fig1.add_trace(
        go.Scatter(
            x=[borough_data['takeaway_density_per_1000']],
            y=[borough_data['obesity_rate']],
            mode='markers+text',
            marker=dict(size=20, color='red', symbol='star'),
            text=['★ Selected'],
            textposition='top center',
            name='Selected Borough',
            hoverinfo='skip'
        )
    )
    
    fig1.update_traces(textposition='top center', marker=dict(size=12, opacity=0.7))
    fig1.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("📉 Deprivation vs Obesity Rate")
    
    fig2 = px.scatter(
        df,
        x='IMD_Score',
        y='obesity_rate',
        text='BoroughName',
        size='takeaway_density_per_1000',
        color='takeaway_density_per_1000',
        color_continuous_scale='Blues',
        labels={
            'IMD_Score': 'IMD Score (Deprivation)',
            'obesity_rate': 'Obesity Rate (%)',
            'takeaway_density_per_1000': 'Takeaway Density'
        },
        hover_data=['BoroughName']
    )
    
    fig2.add_trace(
        go.Scatter(
            x=[borough_data['IMD_Score']],
            y=[borough_data['obesity_rate']],
            mode='markers+text',
            marker=dict(size=20, color='red', symbol='star'),
            text=['★ Selected'],
            textposition='top center',
            name='Selected Borough',
            hoverinfo='skip'
        )
    )
    
    fig2.update_traces(textposition='top center', marker=dict(size=12, opacity=0.7))
    fig2.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# ---- ROW 4: Bar Chart ----
st.subheader("📊 Takeaway Density by Borough")

df_sorted = df.sort_values('takeaway_density_per_1000', ascending=True)
df_sorted['color'] = df_sorted['BoroughName'].apply(
    lambda x: '#FF4444' if x == selected_borough else '#4682B4'
)

fig3 = px.bar(
    df_sorted,
    x='takeaway_density_per_1000',
    y='BoroughName',
    orientation='h',
    color='color',
    color_discrete_map={'#FF4444': '#FF4444', '#4682B4': '#4682B4'},
    labels={
        'takeaway_density_per_1000': 'Takeaway Density (per 1,000)',
        'BoroughName': ''
    },
    hover_data=['takeaway_count', 'population', 'obesity_rate']
)

fig3.update_layout(
    height=500,
    showlegend=False,
    xaxis=dict(gridcolor='lightgray'),
    yaxis=dict(gridcolor='lightgray')
)

st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")

# ---- ROW 5: Correlation Matrix ----
st.subheader("📈 Correlation Matrix")

corr_df = df[['takeaway_density_per_1000', 'IMD_Score', 'obesity_rate']].corr()

fig4 = px.imshow(
    corr_df,
    text_auto='.3f',
    color_continuous_scale='RdBu_r',
    zmin=-1,
    zmax=1,
    labels=dict(x='', y='', color='Correlation')
)

fig4.update_layout(height=350)
st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")

# ---- Footer ----
st.markdown("""
**Data Sources:**
- Food Hygiene Rating Scheme (FHRS) - Food Standards Agency
- Index of Multiple Deprivation (IMD) 2019 - MHCLG
- ONS Postcode Directory (ONSPD) - Office for National Statistics
- Obesity Data - Public Health England
- Population Estimates - Office for National Statistics
""")

st.caption(f"Dashboard created for MSc Project - Zisan Ahmed (24162855) - {pd.Timestamp.now().strftime('%B %Y')}")