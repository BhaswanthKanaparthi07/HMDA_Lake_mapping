# HMDA Lake Mapping & Verification Chatbot
"A Chatbot that maps HMDA lake boundaries and verifies whether user-entered coordinates fall within official lake layouts using geospatial polygon detection."


This project helps users verify whether a given latitude and longitude point falls inside the boundary of any officially digitized HMDA lake layout (Full Tank Level/FTL lakes) in Hyderabad. It uses polygon mapping techniques powered by Shapely and Folium, and provides an easy-to-use chatbot-like interface built with Streamlit.
Whether you're a land buyer, civic-tech researcher, or just curious — you can instantly test any coordinate against mapped lake boundaries and visualize the result on an interactive map.

# How to Set Up and Run the Project (Step-by-Step)
1. Clone the Repository

    git clone https://github.com/your-username/hmda-lake-mapping.git
    cd hmda-lake-mapping
   
2. Install Required Libraries
     pip install -r requirements.txt

3. Run the Streamlit Chatbot App
     streamlit run lake_chatbot.py

# How to Use the App
Once the app is running:
You'll see a form asking for latitude and longitude.
You can get these coordinates from Google Maps by right-clicking a location and copying the numbers.
Paste the latitude and longitude into the app and click the "Check" button.

# The app will:
Tell you whether your point is inside any lake layout.
Show the lake name (if matched).
Plot both your point and the lake boundary on an interactive map.
If your point doesn’t fall within any known lake polygon, the app will clearly let you know that it lies outside the digitized layouts.



# Want to Explore the Backend Logic? 
You’ll find a few Jupyter notebooks in the project which explain how each part of the pipeline works:

1. HMDA_lake_retrieve.ipynb – Shows how lake coordinates were collected or parsed.

2. HMDA_lake_shapely.ipynb – Demonstrates how we construct polygon shapes from CSV data using shapely.

3. HMDA_lake_folium.ipynb – Visualizes all mapped lakes using folium in a standalone map view.

4. hmda_lake_chatbot.ipynb – A simplified chatbot simulation inside a notebook (without needing Streamlit).


# Notes and Best Practices
Make sure coordinates are always in decimal degree format (e.g., 17.44629, 78.32012).

This tool is specifically designed for FTL lake layouts under the HMDA region in Telangana.

The core data file (lake_polygons_decimal.csv) contains pre-cleaned lake boundary points and must not be altered unless you're updating all polygons carefully.

The polygon detection logic uses small geometric buffers to account for boundary inaccuracies — so it’s sensitive and accurate to around 1 meter.

Ideal for use cases like land verification, civic-tech dashboards, or spatial analysis in urban planning



# Contributing
If you'd like to extend this project — maybe by integrating satellite overlays, supporting multi-point checks, or visual comparison with real-time maps — feel free to fork, build, and submit a pull request.
This project is open for collaboration and learning. Let’s make spatial intelligence accessible for all.
