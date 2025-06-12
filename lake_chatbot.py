# installing streamlit in the environment (only needed once)
#!pip install streamlit

import pandas as pd
from shapely.geometry import Point, Polygon
import streamlit as st
import folium
from streamlit_folium import st_folium

# Loading and preprocessing
df = pd.read_csv("lake_polygons_decimal.csv")
df["Latitude_DD"] = df["Latitude_DD"].round(5)
df["Longitude_DD"] = df["Longitude_DD"].round(5)

# Building lake polygons
lake_polygons = {}
for lake_name, group in df.groupby("LAKE NAME"):
    coords_latlon = list(zip(group["Latitude_DD"], group["Longitude_DD"]))  # (lat, lon)
    coords_lonlat = [(lon, lat) for lat, lon in coords_latlon]  # (lon, lat)
    if coords_lonlat[0] != coords_lonlat[-1]:
        coords_lonlat.append(coords_lonlat[0])
    lake_polygons[lake_name] = {
        "polygon": Polygon(coords_lonlat),
        "coords_latlon": coords_latlon
    }

# Function to check if point in lake
def find_lake(lat, lon):
    point = Point(round(lon, 5), round(lat, 5))
    for lake_name, data in lake_polygons.items():
        if data["polygon"].buffer(1e-7).intersects(point):
            return f"✅ Point is inside or on the boundary of: **{lake_name}**"
    return "❌ Point is not inside any known lake."

# Streamlit UI
st.title("🧭 Lake Polygon Chatbot")
st.markdown("Enter a coordinate to check if it lies within a known lake boundary.")
st.markdown("Use coordinates from Google Maps or the Bhuvan Portal to check land plot status.")

# Initialize session state
if "show_map" not in st.session_state:
    st.session_state["show_map"] = False
    st.session_state["result"] = ""
    st.session_state["coords"] = (None, None)

# Input section (5 decimal places format)
lat = st.number_input("Enter Latitude", format="%.5f")
lon = st.number_input("Enter Longitude", format="%.5f")

# Button to check location
if st.button("Check"):
    result = find_lake(lat, lon)
    st.session_state["show_map"] = True
    st.session_state["result"] = result
    st.session_state["coords"] = (lat, lon)

# Use container to fix layout and prevent scroll gap
if st.session_state["show_map"] and st.session_state["coords"] != (None, None):
    with st.container():
        lat, lon = st.session_state["coords"]
        st.markdown(st.session_state["result"])

        fmap = folium.Map(location=[lat, lon], zoom_start=16)
        folium.Marker([lat, lon], icon=folium.Icon(color="red"), popup="Your Point").add_to(fmap)

        for name, data in lake_polygons.items():
            folium.Polygon(
                locations=data["coords_latlon"],
                color="blue",
                tooltip=name,
                fill=True,
                fill_opacity=0.4
            ).add_to(fmap)

        st_folium(fmap, width=700, height=500)

# Static test coordinates
st.markdown("---")
st.subheader("📌 Example Coordinates to Try")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### ✅ Inside a Lake")
    st.code("Lat: 17.44630\nLon: 78.31996  # 0_Chillukala_Kunta_lake")
    st.code("Lat: 17.15965\nLon: 78.28042  # Bodhi_Kunta")
    st.code("Lat: 17.07239\nLon: 78.15517  # Chama_Kunta")
    st.code("Lat: 17.05175\nLon: 78.35864  # Erra_Kunta")
    st.code("Lat: 17.21108\nLon: 78.27123  # Kummari_Kunta")

with col2:
    st.markdown("### ❌ Outside Any Lake")
    st.code("Lat: 17.50000\nLon: 78.00000")
    st.code("Lat: 17.30000\nLon: 78.60000")
    st.code("Lat: 17.00000\nLon: 78.20000")
