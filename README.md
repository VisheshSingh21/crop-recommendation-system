<h1 align="center">🌱 Crop Recommendation System using Machine Learning</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Machine%20Learning-Random%20Forest-success" />
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen" />
  <img src="https://img.shields.io/badge/Python-3.8+-blue" />
  <img src="https://img.shields.io/badge/Streamlit-Web%20App-red" />
</p>

<p align="center">
  An end-to-end Machine Learning project that recommends the most suitable crop based on soil nutrients and climatic conditions.
</p>

<hr>

<h2>🌾 Project Overview</h2>

<p>
Agriculture plays a vital role in the economy. Selecting the right crop based on soil composition and environmental conditions is crucial for maximizing yield and minimizing losses.
</p>

<p>
This project uses <b>Machine Learning classification techniques</b> to recommend the most suitable crop by analyzing soil nutrients and climate parameters.
</p>

<hr>

<h2>🎯 Problem Statement</h2>

<p>
Farmers often rely on traditional knowledge and intuition to decide which crop to grow. However, incorrect crop selection can result in poor yield, financial loss, and soil degradation.
</p>

<p>
The objective of this project is to develop a <b>data-driven crop recommendation system</b> using Machine Learning that suggests the best crop based on soil nutrients and climatic conditions.
</p>

<hr>

<h2>🧠 Machine Learning Approach</h2>

<ul>
  <li>Supervised Learning</li>
  <li>Multi-class Classification</li>
  <li>Model Comparison & Selection</li>
</ul>

<b>Algorithms Implemented:</b>
<ul>
  <li>Logistic Regression</li>
  <li>K-Nearest Neighbors (KNN)</li>
  <li>Decision Tree</li>
  <li><b>Random Forest (Best Performing Model)</b></li>
  <li>Support Vector Machine (SVM)</li>
</ul>
<hr>

<h2>📈 Model Performance</h2>
<ul>
  <li>Multiple ML models were trained and evaluated</li>
  <li><b>Random Forest achieved the highest accuracy</b></li>
</ul>
<b>Random Forest achieved the highest accuracy</b>





<hr>

<h2>📊 Dataset Description</h2>

<table>
<tr><th>Feature</th><th>Description</th></tr>
<tr><td>N</td><td>Nitrogen content in soil</td></tr>
<tr><td>P</td><td>Phosphorus content in soil</td></tr>
<tr><td>K</td><td>Potassium content in soil</td></tr>
<tr><td>Temperature</td><td>Temperature (°C)</td></tr>
<tr><td>Humidity</td><td>Relative humidity (%)</td></tr>
<tr><td>pH</td><td>Soil pH value</td></tr>
<tr><td>Rainfall</td><td>Rainfall (mm)</td></tr>
</table>

<p><b>Target Variable:</b> Crop Label</p>

<hr>

<h2>⚙️ Project Structure</h2>

<pre>
Crop_Recommendation_System/
│
├── Crop_recommendation.csv
├── notebook.ipynb
├── model.pkl
├── scaler.pkl
├── app.py
├── requirements.txt
└── README.md
</pre>

<hr>

<h2>🚀 Streamlit Web Application</h2>

<p>
The trained Random Forest model is deployed using <b>Streamlit</b> with an interactive and user-friendly interface.
</p>

<b>Key Features:</b>
<ul>
  <li>Clean and simple agricultural-themed UI</li>
  <li>User-friendly sliders and input fields</li>
  <li>Real-time crop prediction</li>
</ul>

<hr>
<p align="center">⭐ If you find this project useful, don’t forget to star the repository!</p>


<h2>▶️ How to Run the Project</h2>

<h4>1️⃣ Clone the Repository</h4>

```bash
git clone https://github.com/your-username/Crop_Recommendation_System.git
cd Crop_Recommendation_System
