import streamlit as st
import pandas as pd
import pickle
import requests

# Function to fetch poster
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=ab5d0b1930e5231aaa9fe34a09a56ff6&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# Function to recommend movies
def recommend(movie, movies):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from api
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters

# Set page configuration
st.set_page_config(page_title="Movie Recommender System", page_icon=None, layout='wide', initial_sidebar_state='auto', menu_items=None)

# Title
st.markdown("<h1 style='text-align: center;'>Movie Recommender System</h1>", unsafe_allow_html=True)

# Background Image
st.markdown(
    """
    <style>
    body {
        background-image: url('file:///C:/Users/HP/Downloads/dark-5u7v1sbwoi6hdzsb.jpg');
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl' , 'rb'))

# Selectbox
selected_movie_name = st.selectbox(
    'Select a movie:',
    movies['title'].values
)

# Button
if st.button('Recommend'):
    with st.spinner('LOADING..'):
        names, posters = recommend(selected_movie_name, movies)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
