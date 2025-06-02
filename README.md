# 📦 Logistics Optimization Suite for Allagash Brewing Company

Data-powered tools to enhance shipment planning, reduce freight costs, and weather-proof logistics decisions.

This project combines a Smart Truck Recommender WebApp with a suite of interactive Power BI dashboards to help Allagash Brewing Company optimize outbound shipments. From choosing the right truck type based on weather forecasts to analyzing freight spending, route efficiency, and pallet utilization, this solution empowers the supply chain team with actionable insights and automated recommendations.


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


# 📊 Shipment optimization Dashboards

## Dashboard 1: Freight Cost & Shipment Performance

<img width="831" alt="image" src="https://github.com/user-attachments/assets/68b9212d-f17d-4dde-994b-bc4fa19d49e4" />

[View Dashboard](https://northeastern-my.sharepoint.com/:u:/r/personal/wadekar_sh_northeastern_edu/Documents/Attachments/Alpha%20Huskies%201.pbix?csf=1&web=1&e=AzwxyA)

### Analysis:
- Shows total freight cost, weight moved, and cost per pallet over time.
- Identifies cities and routes contributing to highest costs using bar and map visuals.
- Pie chart highlights which transportation modes consume the highest freight cost share.

### How It Helps Allagash:
- Pinpoints cost-heavy cities and truck types for cost-reduction focus.
- Enables time-based tracking of freight spending trends.
- Guides optimization of shipment strategy to reduce total freight costs.

## Dashboard 2: Route & Shipment Efficiency Analysis

<img width="828" alt="image" src="https://github.com/user-attachments/assets/eb5a49ed-914d-4fdb-b25e-31347901a384" />

[View Dashboard](https://northeastern-my.sharepoint.com/:u:/r/personal/wadekar_sh_northeastern_edu/Documents/Attachments/Alpha%20Huskies%201.pbix?csf=1&web=1&e=t3yMkW)


### Analysis:
- Highlights the most frequently used and heaviest routes (e.g., Portland → Secaucus).
- Scatter chart shows relationship between shipment weight and freight cost.
- Shipment volume table provides route-level comparisons and density map by state.

### How It Helps Allagash:
- Helps consolidate or optimize high-cost routes.
- Identifies routes with inefficient cost-to-weight ratio for improvement.
- Supports planning of resource allocation based on route volume.

## Dashboard 3: Pallet Utilization Over Time

<img width="830" alt="image" src="https://github.com/user-attachments/assets/fe3e2077-fd79-4981-a1eb-a12d1ba3028e" />

[View Dashboard](https://northeastern-my.sharepoint.com/:u:/r/personal/wadekar_sh_northeastern_edu/Documents/Attachments/Alpha%20Huskies%20Dashboard1_Pallet%20Utilization.pbix?csf=1&web=1&e=c7HVYP)


### Analysis:
- Highlights average pallet utilization and most used truck types.
- Compares cost-per-pallet by truck mode to identify efficient options.
- Tree map shows drop cities with the highest pallet flow.

### How It Helps Allagash:
- Reduces underutilization of pallets and improves truck fill rates.
- Enables switching to more cost-efficient transportation modes.
- Informs drop location strategy for load balancing.

## Dashboard 4: Shipment Mode Insights by Weather

<img width="831" alt="image" src="https://github.com/user-attachments/assets/2ba76cf3-6aa6-4a27-ab62-a2345c552e9b" />

[View Dashboard](https://northeastern-my.sharepoint.com/:u:/r/personal/wadekar_sh_northeastern_edu/Documents/Attachments/Alpha_Huskies%20Dashboard2_Map.pbix?csf=1&web=1&e=ENMdtR)

### Analysis:
- Map visual shows weather conditions and load types across destinations.
- KPI cards track total, good, and bad weather shipments.
- Gauge shows the shipment success ratio in good weather.

### How It Helps Allagash:
- Improves route planning by aligning shipments with good weather conditions.
- Reduces delays and risks by avoiding extreme weather zones.
- Supports dynamic transport mode selection based on weather type.






Built with ❤️ by Team Alpha Huskies @ Northeastern University
For Allagash Brewing Company | March 2025
