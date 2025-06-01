import time
import json
import pandas as pd
import numpy as np
from datetime import datetime
import streamlit as st
import streamlit.components.v1 as components
from utils import (
    load_route_data, get_available_dates, calculate_avg_temp,
    recommend_truck_type
)

# Google Maps API Key (replace with your key)
GOOGLE_MAPS_API_KEY = "GOOGLE_API_KEY"

# Page configuration
st.set_page_config(
    page_title="Logistics Route Planner",
    page_icon="🚛",
    layout="wide"
)

# Title and description
st.title("🚛 Logistics Route Planner")
st.markdown("Plan your route from Portland, Maine and get truck recommendations based on temperature.")

try:
    # Load route data
    df = load_route_data()

    # Debug info
    st.sidebar.write("Debug Info:")
    st.sidebar.write("Available columns:", df.columns.tolist())

    # Create two columns for input
    col1, col2 = st.columns(2)

    with col1:
        # Simple text input for DROP CITY
        search_city = st.text_input(
            "Enter DROP CITY",
            help="Type your delivery city name"
        )

        if search_city:
            # Filter destinations based on the entered city
            matches = df[df['Drop City'].str.contains(search_city, case=False)]
            if matches.empty:
                st.error("No matching cities found. Please try a different city name.")
                selected_destination = None
            else:
                selected_destination = matches.iloc[0]
                st.success(f"Found destination: {selected_destination['Drop City']}, {selected_destination['Drop State']}")
        else:
            selected_destination = None

    with col2:
        # Date selection
        available_dates = get_available_dates()
        selected_date = st.date_input(
            "Select Delivery Date",
            min_value=available_dates[0],
            max_value=available_dates[-1],
            value=available_dates[0],
            help="Choose a delivery date (up to 5 days from today)"
        )

    if selected_destination is not None and st.button("Calculate Route", type="primary"):
        with st.spinner("Processing route information..."):
            # Get route information
            states = selected_destination['States Along Route'].split(', ')

            # Calculate temperatures
            state_temps = calculate_avg_temp(states)
            avg_temp = np.mean(list(state_temps.values()))

            # Create columns for results
            result_col1, result_col2 = st.columns([1, 1])

            with result_col1:
                # Route Information in a styled container
                with st.container():
                    st.markdown("### 📍 Route Details")
                    st.markdown("""
                    <style>
                    .route-info {
                        padding: 20px;
                        border-radius: 10px;
                        background-color: #f0f2f6;
                        margin: 10px 0;
                    }
                    </style>
                    """, unsafe_allow_html=True)

                    st.markdown('<div class="route-info">', unsafe_allow_html=True)
                    st.markdown(f"""
                    🏁 **Origin:** Portland, Maine  
                    🎯 **Destination:** {selected_destination['Drop City']}, {selected_destination['Drop State']}  
                    📅 **Delivery Date:** {selected_date.strftime('%B %d, %Y')}
                    """)
                    st.markdown('</div>', unsafe_allow_html=True)

                # Temperature Analysis
                st.markdown("### 🌡️ Temperature Analysis")
                with st.container():
                    for state, temp in state_temps.items():
                        st.markdown(f"**{state}:** {temp:.1f}°F")
                    st.markdown(f"**Overall Average:** {avg_temp:.1f}°F")

                # Truck Recommendation
                truck_type = recommend_truck_type(avg_temp)
                st.markdown("### 🚚 Recommendation")

                recommendation_color = "#28a745" if "Dry Truck" in truck_type else "#dc3545"
                st.markdown(
                    f"""
                    <div style='padding: 15px; border-radius: 5px; background-color: {recommendation_color}; color: white;'>
                        <strong>Recommended Truck Type:</strong><br>{truck_type}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with result_col2:
                st.markdown("### 🗺️ Route Visualization")

                # ✅ Generate Google Maps URL using Pickup and Drop City
                def generate_google_maps_url(pickup_city, drop_city):
                    return f"""
                    <iframe
                        width="100%"
                        height="500"
                        frameborder="0"
                        style="border:0"
                        src="https://www.google.com/maps/embed/v1/directions?key={GOOGLE_MAPS_API_KEY}
                        &origin={pickup_city}
                        &destination={drop_city}
                        &mode=driving"
                        allowfullscreen>
                    </iframe>
                    """

                pickup_city = "Portland, Maine"
                drop_city = f"{selected_destination['Drop City']}, {selected_destination['Drop State']}"

                try:
                    google_maps_html = generate_google_maps_url(pickup_city, drop_city)
                    components.html(google_maps_html, height=500)
                except Exception as e:
                    st.error(f"Unable to display route map: {str(e)}")
                    st.write("Please try a different destination or contact support if the issue persists.")

except Exception as e:
    st.error(f"An error occurred: {str(e)}")
    st.error("Please try again later or contact support if the problem persists.")

# Footer
st.markdown("---")
st.markdown("🚚 Logistics Route Planner - Helping you choose the right truck for your delivery")
