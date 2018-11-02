import pandas as pd
import numpy as np

movieTitle = input("Enter movie title: ")
print ("Your movie title is ", movieTitle)

rating_columns = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('u.data', sep='\t', names=rating_columns, usecols=range(3), encoding='ISO-8859-1')

movie_columns = ['movie_id', 'title']
movies = pd.read_csv('u.item', sep='|', names=movie_columns, usecols=range(2), encoding="ISO-8859-1")

ratings = pd.merge(movies, ratings)

movieRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')

starWarsRatings = movieRatings[movieTitle]

similarMovies = movieRatings.corrwith(starWarsRatings)
similarMovies = similarMovies.dropna()
similarMovies.sort_values(ascending=False)

movieStats = ratings.groupby('title').agg({'rating': [np.size, np.mean]})

popularMovies = movieStats['rating']['size'] >= 100
movieStats[popularMovies].sort_values([('rating', 'mean')], ascending=False)[:15]

dataframe = movieStats[popularMovies].join(pd.DataFrame(similarMovies, columns=['similarity']))
print dataframe.sort_values(['similarity'], ascending=False)[:15]
