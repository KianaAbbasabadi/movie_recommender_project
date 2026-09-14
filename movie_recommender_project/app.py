from pathlib import Path

import streamlit as st

from recommender import build_similarity_matrix, load_movies, recommend_movies

st.set_page_config(
    page_title="CineMatch | Movie Recommender",
    page_icon="🎬",
    layout="wide",
)

st.markdown(
    """
    <style>
        .block-container {padding-top: 2rem; padding-bottom: 3rem; max-width: 1200px;}
        .hero {
            padding: 2rem;
            border-radius: 24px;
            background: linear-gradient(135deg, rgba(124,58,237,.18), rgba(236,72,153,.12));
            border: 1px solid rgba(148,163,184,.2);
            margin-bottom: 1.5rem;
        }
        .hero h1 {margin: 0; font-size: 2.5rem;}
        .hero p {margin: .6rem 0 0 0; opacity: .82; font-size: 1.05rem;}
        .movie-card {
            border: 1px solid rgba(148,163,184,.18);
            border-radius: 18px;
            padding: 1rem;
            min-height: 185px;
            background: rgba(255,255,255,.03);
        }
        .movie-title {font-size: 1.1rem; font-weight: 700; margin-bottom: .35rem;}
        .muted {opacity: .72; font-size: .9rem;}
        .score {font-weight: 700; margin-top: .5rem;}
        div.stButton > button {
            width: 100%; border-radius: 12px; font-weight: 700; height: 3rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero">
      <h1>🎬 CineMatch</h1>
      <p>A simple content-based movie recommender built with CountVectorizer and cosine similarity.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

DATA_PATH = Path(__file__).parent / "data" / "imdb_top_1000.csv"

if not DATA_PATH.exists():
    st.error("Dataset not found. Put `imdb_top_1000.csv` inside the `data/` folder.")
    st.stop()


@st.cache_data
def get_data():
    return load_movies(DATA_PATH)


@st.cache_resource
def get_model(df_signature: tuple, combined_features: tuple):
    # Arguments make Streamlit invalidate cache if the data changes.
    import pandas as pd
    temp_df = pd.DataFrame({"Combined_Features": combined_features})
    return build_similarity_matrix(temp_df)[1]


try:
    df = get_data()
    similarity_matrix = get_model(tuple(df["Series_Title"]), tuple(df["Combined_Features"]))
except Exception as exc:
    st.error(f"Could not prepare the recommender: {exc}")
    st.stop()

left, right = st.columns([2.2, 1])
with left:
    selected_movie = st.selectbox(
        "Choose a movie you like",
        options=sorted(df["Series_Title"].dropna().unique()),
        index=None,
        placeholder="Search for a movie...",
    )
with right:
    n_recommendations = st.slider("Number of recommendations", 3, 10, 6)

if st.button("✨ Recommend movies", type="primary"):
    if not selected_movie:
        st.warning("Please choose a movie first.")
    else:
        results = recommend_movies(selected_movie, df, similarity_matrix, n_recommendations)
        st.subheader(f"Because you liked “{selected_movie}”")
        st.caption("Recommendations are based on genre, director, and main cast similarity.")

        for start in range(0, len(results), 3):
            cols = st.columns(3)
            for col, (_, row) in zip(cols, results.iloc[start:start+3].iterrows()):
                with col:
                    title = row.get("Series_Title", "Unknown")
                    year = row.get("Released_Year", "")
                    genre = row.get("Genre", "")
                    director = row.get("Director", "")
                    rating = row.get("IMDB_Rating", "")
                    score = float(row.get("Similarity", 0)) * 100

                    st.markdown(
                        f"""
                        <div class="movie-card">
                          <div class="movie-title">{title}</div>
                          <div class="muted">{year} &nbsp; • &nbsp; {genre}</div>
                          <div class="muted">Director: {director}</div>
                          <div class="muted">IMDb: {rating if rating != '' else 'N/A'}</div>
                          <div class="score">Similarity: {score:.1f}%</div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

with st.expander("How does it work?"):
    st.write(
        "The app combines each movie's genre, director, and main actors into one text field. "
        "CountVectorizer converts those words into numeric vectors, and cosine similarity "
        "measures how close movies are to each other."
    )
