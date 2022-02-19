import streamlit as st
import pickle
import pandas as pd


def recommend(book):
    book_index = df[df['title'] == book].index[0]
    distances = similarity[book_index]
    book_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])
    recommended_book_name = []
    recommended_book_poster = []

    for i in book_list[1:6]:
        recommended_book_name.append(df.iloc[i[0]].title)
        recommended_book_poster.append(df.iloc[i[0]].image_url)

    return recommended_book_name, recommended_book_poster


books_list = pickle.load(open('books_list.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Books Recommendation System')
selected_book_name = st.selectbox('Title', books_list)

if st.button('Show Recommendations'):
    recommended_book_name, recommended_book_poster = recommend(selected_book_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_book_name[0])
        st.image(recommended_book_poster[0])
    with col2:
        st.text(recommended_book_name[1])
        st.image(recommended_book_poster[1])

    with col3:
        st.text(recommended_book_name[2])
        st.image(recommended_book_poster[2])
    with col4:
        st.text(recommended_book_name[3])
        st.image(recommended_book_poster[3])
    with col5:
        st.text(recommended_book_name[4])
        st.image(recommended_book_poster[4])
