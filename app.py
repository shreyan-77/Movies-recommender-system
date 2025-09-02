import streamlit as st
import pickle
import pandas as pd

# Load data
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommendation function
def recommend(movie):
    movie_index = int(movies[movies['title'] == movie].index[0])
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# App Title and Intro
st.title("🎬 Movie Recommender System")
st.markdown("""
### Welcome to my Movie Recommender System  
Created as part of a Data Analytics & AI/ML project to enhance user experience through personalized recommendations.
""")

# Movie selection and recommendation
selected_movie_name = st.selectbox(
    'Select a movie:',
    movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    st.markdown("#### Recommended Movies:")
    for i in recommendations:
        st.write(i)

st.markdown("""
---
**Developed by V.Shreyan**  
📧 shreyansharma76@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/vshreyansharma) | [GitHub](https://github.com/shreyan-77)
""")


# Footer Section
#st.markdown("""---
#**📬 Contact**
#📧 [Email](shreyansharma76@gmail.com)
#🔗 [LinkedIn](www.linkedin.com/in/vshreyansharma)
#""")
