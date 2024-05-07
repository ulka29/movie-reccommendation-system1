import streamlit as st
import pickle
import pandas as pd
# import requests
#
#
# def fetch_poster(movie_id):
#     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=f42344c61062784ac2e25c66e7c895a1'.format(movie_id))
#     data = response.json()
#     return  data['poster_path']



movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    for i in movies_list:
        movie_id = i[0]
        #fetch poster from API

        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

st.title('Movie Recommender System')

selected_movie_name = st.selectbox('hello',movies['title'].values)
if st.button('Recommend'):
    recomendation = recommend(selected_movie_name)
    for i in recomendation:

        st.write(i)