import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("🎬 Movie Recommendation System")
st.markdown("Search movies by **Title**, **Genre**, or combine both!")


@st.cache_data
def load_and_merge_data():
    movies_df = pd.read_csv('tmdb_5000_movies.csv')
    credits_df = pd.read_csv('tmdb_5000_credits.csv')
    
    merged_df = movies_df.merge(credits_df, left_on='id', right_on='movie_id')
    movies = merged_df[['id', 'title_x', 'genres', 'vote_average', 'popularity']]
    movies.rename(columns={'title_x': 'title'}, inplace=True)
    
    return movies

# Load data
movies_df = load_and_merge_data()

selected_genres = st.multiselect(
    "🎭 Select genres:", 
    ['Action','Adventure','Comedy','Crime','Drama','Horror','Romance']
)

movie_name = st.text_input("🔍 Enter movie title (optional):")

if st.button("Search Movies"):
    results = movies_df.copy()

    if selected_genres:
        results = results[results['genres'].apply(lambda x: any(g in x for g in selected_genres))]

    if movie_name:
        results = results[results['title'].str.contains(movie_name, case=False, na=False)]

    if not results.empty:
        results = results.sort_values(by=['vote_average','popularity'], ascending=False).head(20)
        st.subheader("Top Movies Found:")
        st.dataframe(results[['title','genres','vote_average','popularity']])
    else:
        st.warning("No movies found. Try another title or genre.")
