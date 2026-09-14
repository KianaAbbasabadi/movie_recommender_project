<div align="center">

# 🎬 CineMatch
### Content-Based Movie Recommendation System

A clean and beginner-friendly movie recommender built with **Python**, **scikit-learn**, and **Streamlit**.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikitlearn&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-Data-150458?logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Project-Educational-success)

</div>

---

## ✨ App Preview

<div align="center">

<img src="assets/cinematch-dashboard.svg" alt="CineMatch Streamlit Dashboard" width="100%" />

</div>

CineMatch lets the user choose a movie and instantly returns similar titles based on **genre, director, and main cast**. The Streamlit interface also displays each recommendation's year, IMDb rating, and similarity score.

---

## 🚀 Features

- 🎞️ Select a movie from the IMDb dataset
- 🎯 Choose the number of recommendations
- 🧠 Content-based recommendation approach
- 🔢 Text features converted using `CountVectorizer`
- 📐 Movie similarity calculated with cosine similarity
- ⭐ Displays IMDb rating and movie information
- 📊 Shows the similarity percentage for every recommendation
- 💻 Interactive Streamlit dashboard

---

## 🧠 How It Works

The recommendation pipeline is intentionally simple and easy to understand:

```text
Movie Dataset
     ↓
Select useful features
     ↓
Genre + Director + Main Cast
     ↓
CountVectorizer
     ↓
Numerical Feature Vectors
     ↓
Cosine Similarity
     ↓
Sort Similarity Scores
     ↓
Top-N Movie Recommendations
```

### 1. Feature Selection

The recommender uses these movie attributes:

- `Genre`
- `Director`
- `Star1`
- `Star2`
- `Star3`

### 2. Vectorization

`CountVectorizer` converts the combined text features into numerical vectors that can be compared mathematically.

### 3. Similarity Calculation

Cosine similarity measures how close each movie vector is to the selected movie. Movies with higher similarity scores are ranked first.

> This project uses **content-based filtering**, so recommendations are based on movie characteristics rather than user history or collaborative filtering.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| **Python** | Core programming language |
| **pandas** | Data loading and preprocessing |
| **NumPy** | Numerical operations |
| **scikit-learn** | Vectorization and similarity calculation |
| **Streamlit** | Interactive web dashboard |
| **Jupyter Notebook** | Development and experimentation |

---

## 📂 Project Structure

```text
movie_recommender_project/
│
├── app.py
├── recommender.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── assets/
│   └── cinematch-dashboard.svg
│
├── data/
│   ├── README.md
│   └── imdb_top_1000.csv
│
└── notebooks/
    ├── original_class_sample.ipynb
    └── movie_recommender_clean.ipynb
```

---

## ▶️ Run Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Streamlit app

```bash
streamlit run app.py
```

Streamlit will open the application in your browser, usually at:

```text
http://localhost:8501
```

---

## 📊 Dataset

The project uses the **IMDb Top 1000 Movies and TV Shows** dataset.

Place the CSV file here:

```text
data/imdb_top_1000.csv
```

Main columns used by the recommender:

```text
Series_Title
Genre
Director
Star1
Star2
Star3
```

Additional information such as release year and IMDb rating is used in the dashboard to make the recommendations easier to explore.

---

## 🎓 Project Purpose

This project was developed as an **educational and practice project** based on a classroom recommendation-system example. The original idea was cleaned, completed, and organized into a simple end-to-end application with a Streamlit interface.

The goal is to demonstrate the basic workflow of a recommendation system in a way that is easy to read, explain, and extend.

---

<div align="center">

### 🍿 Pick a movie. Find your next one.

**Built with Python + Streamlit**

</div>
