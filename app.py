import streamlit as st
import pickle
import joblib
import nltk
import pandas as pd
import sklearn
st.title("Movie Recommendation System")

with open("movies.pickle", 'rb') as m:
    movies = pickle.load(m)

similarites = joblib.load("similarity.joblib")
movie_name = movies['title'].values

def recommend(name_movies):
    movie_index = movies[movies['title'] == name_movies].index[0]
    recommendation = similarites[movie_index]
    movie_list = sorted(enumerate(recommendation),reverse=True,key = lambda x:x[1])[1:6]
    recommend_movies = []
    for i in movie_list:
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies


name_movies = st.selectbox("Enter the Movie Name",movie_name)


if st.button("Recommend"):
    r = recommend(name_movies)
    st.write("The Recommend Movies are:")
    
    for i in r:
        st.write(i)