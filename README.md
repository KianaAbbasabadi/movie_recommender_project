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

<img src="assets/cinematch-dashboard.jpg" alt="CineMatch Streamlit Dashboard" width="100%" />

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

The recommender uses `Genre`, `Director`, `Star1`, `Star2`, and `Star3` as the main content features. `CountVectorizer` converts the combined text into numerical vectors, then cosine similarity measures how close each movie is to the selected title.

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
├── README.md
├── assets/
│   └── cinematch-dashboard.jpg
│
└── movie_recommender_project/
    ├── app.py
    ├── recommender.py
    ├── requirements.txt
    ├── .gitignore
    │
    ├── data/
    │   └── imdb_top_1000.csv
    │
    └── notebooks/
        └── movie_recommender_clean.ipynb
```

---

## ▶️ Run Locally

```bash
cd movie_recommender_project
pip install -r requirements.txt
streamlit run app.py
```

Streamlit will usually open the app at:

```text
http://localhost:8501
```

---

## 📊 Dataset

The project uses the **IMDb Top 1000 Movies and TV Shows** dataset.

The CSV file is stored at:

```text
movie_recommender_project/data/imdb_top_1000.csv
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

---

## 🎓 Project Purpose

This project was developed as an **educational and practice project** based on a classroom recommendation-system example. The original idea was cleaned, completed, and organized into a simple end-to-end application with a Streamlit interface.

The goal is to demonstrate the basic workflow of a recommendation system in a way that is easy to read, explain, and extend.

---

<div align="center">

### 🍿 Pick a movie. Find your next one.

**Built with Python + Streamlit**

</div>
