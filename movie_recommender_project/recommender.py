from pathlib import Path
from typing import Tuple

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

FEATURE_COLUMNS = ["Genre", "Director", "Star1", "Star2", "Star3"]
REQUIRED_COLUMNS = ["Series_Title", *FEATURE_COLUMNS]


def _clean_token_series(series: pd.Series, replace_spaces: bool = True) -> pd.Series:
    series = series.fillna("").astype(str).str.strip()
    if replace_spaces:
        series = series.str.replace(" ", "_", regex=False)
    return series


def load_movies(csv_path: str | Path) -> pd.DataFrame:
    """Load and prepare the IMDb dataset used by the recommender."""
    df = pd.read_csv(csv_path)

    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Dataset is missing required columns: {', '.join(missing)}")

    # Keep useful display columns when available.
    display_columns = [
        "Series_Title", "Genre", "Director", "Star1", "Star2", "Star3",
        "Star4", "Released_Year", "Runtime", "IMDB_Rating", "Overview", "Poster_Link"
    ]
    keep = [col for col in display_columns if col in df.columns]
    df = df[keep].copy()

    # Build one text field from content features.
    genre = df["Genre"].fillna("").astype(str).str.replace(",", " ", regex=False)
    director = _clean_token_series(df["Director"])
    star1 = _clean_token_series(df["Star1"])
    star2 = _clean_token_series(df["Star2"])
    star3 = _clean_token_series(df["Star3"])

    df["Combined_Features"] = (
        genre + " " + director + " " + star1 + " " + star2 + " " + star3
    ).str.replace(r"\s+", " ", regex=True).str.strip()

    return df.reset_index(drop=True)


def build_similarity_matrix(df: pd.DataFrame) -> Tuple[CountVectorizer, np.ndarray]:
    """Vectorize combined movie features and calculate cosine similarity."""
    vectorizer = CountVectorizer()
    feature_matrix = vectorizer.fit_transform(df["Combined_Features"])
    similarity_matrix = cosine_similarity(feature_matrix)
    return vectorizer, similarity_matrix


def recommend_movies(
    movie_title: str,
    df: pd.DataFrame,
    similarity_matrix: np.ndarray,
    n_recommendations: int = 6,
) -> pd.DataFrame:
    """Return the most similar movies for the selected title."""
    matches = df.index[df["Series_Title"] == movie_title].tolist()
    if not matches:
        raise ValueError(f"Movie not found: {movie_title}")

    movie_index = matches[0]
    scores = list(enumerate(similarity_matrix[movie_index]))
    scores = sorted(scores, key=lambda item: item[1], reverse=True)

    # The first item is the movie itself, so skip it.
    recommended = scores[1 : n_recommendations + 1]
    indices = [idx for idx, _ in recommended]
    similarities = [score for _, score in recommended]

    result = df.iloc[indices].copy()
    result["Similarity"] = similarities
    return result.reset_index(drop=True)
