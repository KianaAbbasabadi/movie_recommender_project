# 🎬 CineMatch — Content-Based Movie Recommender

A beginner-friendly movie recommendation project built from a classroom sample using **Python**, **pandas**, **scikit-learn**, and **Streamlit**.

The recommender suggests movies with similar content based on:

- Genre
- Director
- Main cast (`Star1`, `Star2`, `Star3`)

## How it works

1. The selected movie features are combined into a single text column.
2. `CountVectorizer` converts the text features into numerical vectors.
3. Cosine similarity is calculated between movies.
4. The movies with the highest similarity scores are returned as recommendations.

This is a **content-based filtering** recommender. It does not use user ratings or collaborative filtering.

## Project structure

```text
movie_recommender_project/
│
├── app.py
├── recommender.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   ├── README.md
│   └── imdb_top_1000.csv   # add the dataset here
│
└── notebooks/
    ├── original_class_sample.ipynb
    └── movie_recommender_clean.ipynb
```

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then Streamlit will open the app in your browser.

## Dataset

Use the common **IMDb Top 1000** dataset and save it as:

```text
data/imdb_top_1000.csv
```

Required columns are `Series_Title`, `Genre`, `Director`, `Star1`, `Star2`, and `Star3`.

## Main libraries

- pandas
- NumPy
- scikit-learn
- Streamlit

## Notes

This project was created for learning and practice. The original classroom notebook is included in `notebooks/original_class_sample.ipynb`, while the cleaned notebook contains a complete working version of the same idea.
