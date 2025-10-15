import streamlit as st
import pandas as pd
import pickle
import os

st.set_page_config(
    page_title="Cell Phone Price Prediction",
    layout="wide",
)

st.sidebar.header("About This Project")
st.sidebar.markdown("""
This project predicts the **price range of a mobile phone** based on its technical specifications.  
It helps manufacturers and customers understand how hardware features affect pricing trends.
""")

st.sidebar.subheader("Technical Details")
st.sidebar.markdown("""
- **Core Algorithm:** Logistic Regression  
- **Preprocessing:** StandardScaler for numeric features  
- **Dataset:** Mobile Price Classification Dataset (Kaggle)  
- **Best Model Accuracy:** **94.75%**
""")

st.sidebar.subheader("Impact")
st.sidebar.markdown("""
This model assists users and companies in identifying **feature-price relationships** and helps in  
**market positioning** and **product planning**.
""")

st.sidebar.markdown("---")
st.sidebar.write("Made by Karthikeyan")

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")
PREPROCESSOR_PATH = os.path.join(BASE_DIR, "preprocessor.pkl")
STYLE_PATH = os.path.join(BASE_DIR, "style.css")

try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    with open(PREPROCESSOR_PATH, "rb") as f:
        preprocessor = pickle.load(f)
except Exception as e:
    st.error(f"Error loading model or preprocessor: {e}")
    st.stop()

if os.path.exists(STYLE_PATH):
    with open(STYLE_PATH) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("<h1 class='title'>Cell Phone Price Range Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Select the phone specifications below to predict its price category.</p>", unsafe_allow_html=True)

with st.form("cellphone_form"):
    st.markdown("<div class='section-header'>General Information</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        thickness = st.selectbox("Phone Thickness", ["Slim", "Average", "Thick"])
        thickness_map = {"Slim": 0.1, "Average": 0.5, "Thick": 1.0}
        m_dep = thickness_map[thickness]

        mobile_wt_map = {"Slim": 80, "Average": 140, "Thick": 200}
        mobile_wt = mobile_wt_map[thickness]
    with col2:
        processor_perf = st.selectbox("Processor Performance", ["Low", "Normal", "High"])
        n_cores_map = {"Low": 1, "Normal": 4, "High": 8}
        n_cores = n_cores_map[processor_perf]

        clock_speed_map = {"Low": 0.5, "Normal": 1.5, "High": 3.0}
        clock_speed = clock_speed_map[processor_perf]

    st.markdown("<div class='section-header'>Hardware Specifications</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        ram_cat = st.selectbox("RAM Size", ["Low", "Medium", "High", "Very High"])
        int_memory_cat = st.selectbox("Internal Storage", ["Low", "Medium", "High", "Very High"])
        battery_cat = st.selectbox("Battery Capacity", ["Low", "Medium", "High", "Very High"])
    with col2:
        fc_cat = st.selectbox("Front Camera Megapixels", ["Low", "Medium", "High"])
        pc_cat = st.selectbox("Rear Camera Megapixels", ["Low", "Medium", "High", "Very High"])
        screen_size = st.selectbox("Screen Size", ["Small", "Medium", "Large", "Very Large"])
        touch_screen = st.radio("Touchscreen?", ["Yes", "No"])

    st.markdown("<div class='section-header'>Connectivity & Features</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        three_g = st.radio("3G Support?", ["Yes", "No"])
        four_g = st.radio("4G Support?", ["Yes", "No"])
        wifi = st.radio("Wi-Fi Support?", ["Yes", "No"])
    with col2:
        bluetooth = st.radio("Bluetooth Support?", ["Yes", "No"])
        dual_sim = st.radio("Dual SIM Support?", ["Yes", "No"])

    submitted = st.form_submit_button("Predict Price Range")

if submitted:

    map_4 = {"Low": 0.25, "Medium": 0.5, "High": 0.75, "Very High": 1.0}
    map_3 = {"Low": 0.33, "Medium": 0.66, "High": 1.0}
    map_bin = {"Yes": 1, "No": 0}
    map_ram = {"Low": 256, "Medium": 2146, "High": 3064, "Very High": 3998}
    map_int_memory = {"Low": 2, "Medium": 32, "High": 48, "Very High": 64}
    map_fc = {"Low": 0, "Medium": 4, "High": 19}
    map_pc = {"Low": 0, "Medium": 10, "High": 15, "Very High": 20}
    map_battery = {"Low": 501, "Medium": 1226, "High": 1615, "Very High": 1998}
    talk_time_map = {"Low": 2, "Medium": 11, "High": 16, "Very High": 20}

    screen_map = {
        "Small": {"px_height": 282, "px_width": 874, "sc_h": 9, "sc_w": 2},
        "Medium": {"px_height": 564, "px_width": 1247, "sc_h": 12, "sc_w": 5},
        "Large": {"px_height": 947, "px_width": 1633, "sc_h": 16, "sc_w": 9},
        "Very Large": {"px_height": 1960, "px_width": 1998, "sc_h": 19, "sc_w": 18},
    }
    px_height = screen_map[screen_size]["px_height"]
    px_width = screen_map[screen_size]["px_width"]
    sc_h = screen_map[screen_size]["sc_h"]
    sc_w = screen_map[screen_size]["sc_w"]

    talk_time = talk_time_map[battery_cat]

    input_data = pd.DataFrame([{
        "battery_power": map_battery[battery_cat],
        "blue": map_bin[bluetooth],
        "clock_speed": clock_speed,
        "dual_sim": map_bin[dual_sim],
        "fc": map_fc[fc_cat],
        "four_g": map_bin[four_g],
        "int_memory": map_int_memory[int_memory_cat],
        "m_dep": m_dep,
        "mobile_wt": mobile_wt,
        "n_cores": n_cores,
        "pc": map_pc[pc_cat],
        "px_height": px_height,
        "px_width": px_width,
        "ram": map_ram[ram_cat],
        "sc_h": sc_h,
        "sc_w": sc_w,
        "talk_time": talk_time,
        "three_g": map_bin[three_g],
        "touch_screen": map_bin[touch_screen],
        "wifi": map_bin[wifi],
    }])

    expected_cols = preprocessor.feature_names_in_
    for col in expected_cols:
        if col not in input_data.columns:
            input_data[col] = 0

    try:
        X_transformed = preprocessor.transform(input_data)
        prediction = model.predict(X_transformed)[0]

        if prediction == 0:
            st.markdown("<div class='prediction-card low'>Price Range: Low</div>", unsafe_allow_html=True)
        elif prediction == 1:
            st.markdown("<div class='prediction-card medium'>Price Range: Medium</div>", unsafe_allow_html=True)
        elif prediction == 2:
            st.markdown("<div class='prediction-card high'>Price Range: High</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='prediction-card very-high'>Price Range: Very High</div>", unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error during prediction: {e}")
