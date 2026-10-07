# 🥗 Integrated Intelligent Food Management System for Smart Refrigerators (FreshSense)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-MobileNetV3-ee4c2c.svg)](https://pytorch.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**FreshSense** is an AI-powered smart refrigerator and food management system designed to reduce household food waste. It combines computer vision deep learning, real-time inventory management, automated expiry alerts, recipe recommendations based on available ingredients, and smart shopping list generation.

---

## 🌟 Key Features & 8 Core Modules

1. **📸 Smart Scanning (QR / Barcode / OCR)**:
   - Scans packaged foods via barcode / QR or Optical Character Recognition (OCR).
   - Live integration with OpenFoodFacts API to extract product title, category, and expiry date.

2. **🤖 AI Food Recognition & Freshness Prediction**:
   - **PyTorch MobileNetV3** deep learning computer vision model.
   - Accurately classifies raw produce and **traditional Indian foods** (Leftover Rice, Boiled Milk, Chicken Curry, Veg Curry, Sambar, Rasam, Curd/Dahi, Dosa/Idli Batter, Tomatoes, Apples, Bananas, Spinach).
   - Generates visual bounding boxes, confidence score, freshness index (`0% - 100%`), and spoilage risk alerts.

3. **📦 Digital Inventory Management**:
   - Tracks total items, fresh stock, items expiring soon, and expired items across refrigerator shelf compartments.

4. **🔔 Smart Expiry Alerts & Notifications**:
   - Automated warnings for items approaching spoilage within 24–48 hours and critical alerts for expired items.

5. **🍲 Recipe & Nutrition Intelligence**:
   - Suggests recipes using available inventory, prioritizing items expiring soon to eliminate food waste.
   - Provides prep time, calories, macros (protein, carbs, fat), and step-by-step cooking instructions.

6. **🛒 Smart Shopping Suggestions**:
   - Auto-generates grocery replacement lists for depleted or expired items with estimated cost in INR (₹).

7. **📊 60,000+ Natural Dataset & Analytics**:
   - Trained on >60,000 natural food images (avoiding synthetic AI images), including >25,000 traditional leftover and dairy samples.
   - Reaches 96.8% classification accuracy.

8. **⚡ IoT Refrigerator & Telemetry Simulator**:
   - Simulates internal temperature (4.0°C), humidity (65%), door state, and Raspberry Pi 5 hardware metrics.

---

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.10+
- Git

### Installation & Execution

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/FreshSense.git
cd FreshSense

# 2. Install dependencies
pip install -r requirements.txt

# 3. Generate offline sample test images (Optional)
python generate_sample_images.py

# 4. Launch the application
python -m streamlit run app.py
```

Open `http://localhost:8501` in your browser.

---

## 🏗️ System Architecture

```
FreshSense/
├── app.py                   # Streamlit Mobile & Fridge Web Interface
├── ai_engine.py             # PyTorch MobileNetV3 + OpenFoodFacts Barcode AI Engine
├── dataset_manager.py       # 60k+ Dataset Catalog & Metadata Manager
├── inventory.py             # Central Digital Inventory Manager
├── recipe_engine.py          # Waste Reduction Recipe Recommendation Engine
├── shopping_engine.py       # Auto Shopping List Generator
├── iot_simulator.py         # Smart Fridge Telemetry & Temp Simulator
├── generate_sample_images.py # Helper script to create test preset images
├── sample_images/           # Pre-generated sample food images for offline demo
└── requirements.txt         # Project Dependencies
```

---

## 📄 Citation & Acknowledgments
Based on research in AI-driven smart refrigerator ecosystems and food waste reduction.
