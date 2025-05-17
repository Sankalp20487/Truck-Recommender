# 🚛 Smart Truck Recommender WebApp

A logistics optimization web application designed to help breweries make cost-effective truck choices for outbound shipments. Built using **Streamlit**, this app recommends whether to use a **Dry Truck** or a **Temperature-Controlled Truck** based on route-level weather forecasts and shipping logic.


<img width="1019" alt="image" src="https://github.com/user-attachments/assets/8b949328-ffb9-4be6-9a19-d5316fbce3c1" />


## 🌟 Features

- **Truck Type Recommendation**  
  Suggests the most cost-efficient truck (Dry or Temperature-Controlled) based on temperature constraints:
  - **Relaxed Mode**: Average route temperature between 40–60°F
  - **Strict Mode**: All states along the route must fall within 40–60°F

- **Weather-Driven Logistics**  
  Integrates a 5-day temperature forecast for all states along the delivery route using real-time weather APIs.

- **Route Temperature Analysis**  
  Uses Google Maps API to fetch waypoints, then analyzes temperatures state-by-state for safety and cost optimization.

- **Interactive UI with Streamlit**  
  Simple, intuitive user interface for business users to:
  - Enter delivery destination
  - Select recommendation mode
  - Get truck recommendation, route breakdown, and temperature insights

## 🛠 Tech Stack

- **Frontend/Backend**: Streamlit  
- **APIs Used**:  
  - Google Maps API (for routing)  
  - OpenWeather API (for temperature forecasts)  

- **Libraries**:  
  `requests`, `pandas`, `datetime`, `streamlit`

## 🚀 How to Run

1. Clone this repository:
   
   git clone https://github.com/your-username/smart-truck-recommender.git
   cd smart-truck-recommender

2. Install required packages:
   
    pip install -r requirements.txt

3. Run the Streamlit app:

    streamlit run app.py


Built with ❤️ by Team Alpha Huskies @ Northeastern University
For Allagash Brewing Company | March 2025
