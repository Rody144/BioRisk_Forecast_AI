import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO

# --- Page Config ---
st.set_page_config(
    page_title="🧬 BioRisk Forecast AI",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS for Professional Look ---
st.markdown("""
    <style>
    .main {background-color: #f8f9fa;}
    .stButton>button {color: white; background: #0072C6;}
    .stDataFrame {background-color: #fff;}
    .css-1d391kg {background: #0072C6;}
    .stAlert {border-radius: 8px;}
    </style>
""", unsafe_allow_html=True)

# --- Logo and Title ---
col1, col2 = st.columns([1, 8])
with col1:
    st.image("https://img.icons8.com/color/96/000000/biohazard.png", width=80)
with col2:
    st.title("🧬 BioRisk Forecast AI")
    st.markdown("🔬 **Can infection outbreaks be predicted from medical waste patterns?**")

# --- Sidebar ---
st.sidebar.header("📁 Upload Data")
uploaded_file = st.sidebar.file_uploader("Upload an Excel or CSV file", type=["csv", "xlsx"])
st.sidebar.markdown("---")
st.sidebar.info("👨‍🔬 This app uses AI to detect abnormal patterns in medical waste data.")

# --- Sample Data Loader ---
def load_sample_data():
    np.random.seed(42)
    n_days = 100
    data = {
        "Date": pd.date_range(start="2025-01-01", periods=n_days),
        "Respiratory_Tools": np.random.poisson(10, n_days),
        "Blood_Disposal": np.random.poisson(5, n_days),
        "Masks_Discarded": np.random.poisson(8, n_days),
    }
    df = pd.DataFrame(data)
    df.loc[70:74, "Respiratory_Tools"] += 30
    df.loc[70:74, "Blood_Disposal"] += 15
    df.loc[70:74, "Masks_Discarded"] += 20
    return df

# --- Load Data ---
if uploaded_file:
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        st.sidebar.success("✅ Data uploaded successfully.")
    except Exception as e:
        st.sidebar.error(f"❌ Error reading file: {e}")
        df = load_sample_data()
else:
    st.sidebar.info("📌 No file uploaded, using sample data.")
    df = load_sample_data()

# --- Normalize column names ---
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

# --- Required columns in normalized form ---
required_cols = ["date", "respiratory_tools", "blood_disposal", "masks_discarded"]
missing = [col for col in required_cols if col not in df.columns]
if missing:
    st.error("❌ Uploaded file is missing required columns: " + ", ".join(missing))
    st.stop()

# --- Use only required columns ---
df = df[required_cols]

# --- Sidebar sensitivity control ---
contamination = st.sidebar.slider("Anomaly Sensitivity", 0.01, 0.2, 0.05, 0.01)

# --- Data Display ---
with st.expander("📊 Show Data (click to expand)", expanded=True):
    st.dataframe(df.head(20), use_container_width=True)

# --- Anomaly Detection ---
st.subheader("🚨 Anomaly Detection Analysis")
features = ["respiratory_tools", "blood_disposal", "masks_discarded"]
clf = IsolationForest(contamination=contamination, random_state=42)
df["anomaly"] = clf.fit_predict(df[features])
df["anomaly"] = df["anomaly"].map({1: 0, -1: 1})

# --- Plotting ---
fig, ax = plt.subplots(figsize=(14, 6))
sns.set(style="whitegrid")
for col in features:
    ax.plot(df["date"], df[col], label=col.replace("_", " ").title())
ax.scatter(
    df["date"][df["anomaly"] == 1],
    df["respiratory_tools"][df["anomaly"] == 1],
    color='red', label="Anomaly", zorder=5, s=80, marker="X"
)
ax.set_title("Medical Waste Trends with Detected Anomalies", fontsize=16)
ax.set_xlabel("Date")
ax.set_ylabel("Waste Count")
ax.legend()
st.pyplot(fig)

# --- Download Results ---
def to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False)
    return output.getvalue()

st.download_button(
    label="⬇️ Download Results (Excel)",
    data=to_excel(df),
    file_name="biorisk_results.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

# --- Warnings and Insights ---
if df["anomaly"].sum() > 0:
    st.error(f"⚠️ {df['anomaly'].sum()} abnormal patterns detected in waste data – possible infection outbreak!")
    st.info("Please review the time periods with detected anomalies for preventive action.")
else:
    st.success("✅ No abnormal patterns detected at this time.")

# --- Footer ---
st.markdown("""
---
<center>
    <small>
        Developed by the Healthcare AI Team | BioRisk Forecast AI © 2025
    </small>
</center>
  """, unsafe_allow_html=True)