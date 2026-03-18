import streamlit as st
import pickle
import joblib
import pandas as pd

st.title("Movie Recommendation System")

@st.cache_data
def load_movies():
    with open("movies.pickle", "rb") as m:
        return pickle.load(m)

@st.cache_resource
def load_similarity():
    return joblib.load("similarity.joblib")

movies = load_movies()
similarities = load_similarity()

movie_name = movies["title"].values

def recommend(name_movies):
    movie_index = movies[movies["title"] == name_movies].index[0]
    recommendation = similarities[movie_index]
    movie_list = sorted(enumerate(recommendation), key=lambda x: x[1], reverse=True)[1:6]
    
    recommend_movies = []
    for i in movie_list:
        recommend_movies.append(movies.iloc[i[0]]["title"])
    return recommend_movies

name_movies = st.selectbox("Enter the Movie Name", movie_name)

if st.button("Recommend"):
    r = recommend(name_movies)
    st.write("The Recommended Movies are:")
    
    for i in r:
        st.write(i)