# MSME Personalized Financial Chatbot

**Preparation Project for Dalberg Data Insights – AI Engineering Fellow**

---

## 📋 Project Overview

This project demonstrates an **end-to-end AI solution** for personalizing financial advice for Micro, Small, and Medium Enterprises (MSMEs) in Kenya using **Unsupervised Machine Learning** and **Local Large Language Models**.

By combining **K-Means Clustering**, **PCA**, and **Ollama (Llama3)**, the system segments users and delivers highly relevant, context-aware financial coaching — similar to tools like **MESH Money Coach**.

---

## ✨ Key Features

- **Synthetic MSME Dataset** generation (realistic Kenyan financial data)
- **User Segmentation** using K-Means Clustering
- **Dimensionality Reduction** with Principal Component Analysis (PCA)
- **Personalized AI Chatbot** powered by local Ollama
- **Actionable financial insights** tailored to each user segment

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **scikit-learn** – Clustering & PCA
- **Ollama** – Local LLM (Llama3 / Mistral recommended)
- **pandas, numpy, matplotlib, seaborn**

---

## 📁 Project Structure

```bash
msme-chatbot-personalization/
├── src/
│   ├── data_preprocessing.py
│   ├── clustering.py
│   ├── pca_analysis.py
│   ├── chatbot.py
│   └── utils.py
├── notebooks/
│   └── view.ipynb
├── outputs/
│   └── results/
├── main.py
├── view_data.py
├── requirements.txt
└── README.md
```
```bash
git clone https://github.com/Jimmymugendi/MSME-Financial-Chatbot-Personalization-System.git
cd msme-chatbot-personalization
```
```bash
pip install -r requirements.txt
```
