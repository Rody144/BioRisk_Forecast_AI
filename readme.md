[706BA01B-3A67-494E-8B0F-3A15E529557B](https://github.com/user-attachments/assets/5454d169-fc50-4b34-b6f3-d941a8f082cd)[Uploading 706BA01B-3A67-494E-8B0F-3A15E529557B.png…]()
# 🧬 BioRisk Forecast AI

[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-ff4b4b?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## Overview

**BioRisk Forecast AI** is an advanced, user-friendly web application designed for healthcare professionals, data scientists, and public health officials. It leverages artificial intelligence to detect abnormal patterns in medical waste data, providing early warnings for potential infection outbreaks. By analyzing trends in the disposal of respiratory tools, blood-related waste, and masks, the app empowers proactive decision-making and risk mitigation in healthcare environments.

---

## 🚀 Features

- **AI-Powered Anomaly Detection:**  
  Utilizes Isolation Forest to identify abnormal spikes in medical waste data that may indicate infection outbreaks.

- **Interactive Data Upload:**  
  Supports both CSV and Excel files with instant feedback on data quality and structure.

- **Customizable Sensitivity:**  
  Adjust anomaly detection sensitivity directly from the sidebar for tailored analysis.

- **Professional Data Visualization:**  
  Clean, interactive plots highlight trends and detected anomalies for rapid insight.

- **Downloadable Reports:**  
  Export results and anomaly flags as Excel files for further analysis or record-keeping.

- **Sample Data Included:**  
  Instantly explore the app’s capabilities with built-in sample data if no file is uploaded.

---

## 🏥 Use Cases

- **Hospital Infection Control**
- **Public Health Surveillance**
- **Medical Waste Management**
- **Research & Epidemiology**

---

## 📦 Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/your-org/biorisk-forecast-ai.git
    cd biorisk-forecast-ai
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the app:**
    ```sh
    streamlit run app.py
    ```

---

## 📊 Data Format

Your data file (CSV or Excel) should include the following columns:

| Date        | Respiratory_Tools | Blood_Disposal | Masks_Discarded |
|-------------|------------------|---------------|-----------------|
| 2025-01-01  | 10               | 5             | 8               |
| ...         | ...              | ...           | ...             |

- **Date:** Date of waste record (YYYY-MM-DD)
- **Respiratory_Tools:** Count of respiratory-related tools disposed
- **Blood_Disposal:** Count of blood-related waste disposed
- **Masks_Discarded:** Count of masks discarded

> **Note:** Column names are case-insensitive and can contain spaces or underscores.

---

## 🖼️ Screenshots

<p align="center">
  <img src="https://i.imgur.com/6rQwQwB.png" alt="App Screenshot" width="700"/>
</p>

---

## 🛡️ Security & Privacy

- All data is processed locally; no information is uploaded or stored externally.
- The app is intended for informational and research purposes only.

---

## 🤝 Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements, bug fixes, or new features.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Authors

- Healthcare AI Team  
- [Raghad Kafafy](https://www.linkedin.com/in/raghad-kafafy-5a079b336/)

---

## 📬 Contact

For questions, suggestions, or support, please contact:  
**Email:** raghad.ehab.kafafy@icloud.com
**phone number:** +201120412046

---

<center>
    <sub>
        Developed with ❤️ by the Healthcare AI Team | BioRisk Forecast AI © 2025
