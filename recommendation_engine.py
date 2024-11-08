import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors


# Load the dataset

books_filename = 'BX-Books.csv'
ratings_filename = 'BX-Book-Ratings.csv'
'''
books = pd.read_csv('BX-Books.csv', sep=';', encoding='ISO-8859-1', on_bad_lines='skip', low_memory=False)
ratings = pd.read_csv('BX-Book-Ratings.csv', sep=';', encoding='ISO-8859-1', on_bad_lines='skip', low_memory=False)
users = pd.read_csv('BX-Users.csv', sep=';', encoding='ISO-8859-1', on_bad_lines='skip', low_memory=False)
'''
# import csv data into dataframes
df_books = pd.read_csv(
    books_filename,
    encoding = "ISO-8859-1",
    sep=";",
    header=0,
    names=['isbn', 'title', 'author'],
    usecols=['isbn', 'title', 'author'],
    dtype={'isbn': 'str', 'title': 'str', 'author': 'str'})

df_ratings = pd.read_csv(
    ratings_filename,
    encoding = "ISO-8859-1",
    sep=";",
    header=0,
    names=['user', 'isbn', 'rating'],
    usecols=['user', 'isbn', 'rating'],
    dtype={'user': 'int32', 'isbn': 'str', 'rating': 'float32'})


# Data Cleaning and Preparation
c1 = df_ratings['user'].value_counts()
c2 = df_ratings['isbn'].value_counts()

# Remove users and books where the occurances are less than 200 and 100 respectively
df_ratings = df_ratings[~df_ratings['user'].isin(c1[c1 < 200].index)]
df_ratings = df_ratings[~df_ratings['isbn'].isin(c2[c2 < 100].index)]

# Merge the dataframes on isbn
df = pd.merge(right=df_ratings, left=df_books, on='isbn')

# Remove duplicates
df = df.drop_duplicates(['title', 'user'])

# Create a pivot
df_pivot = df.pivot(index = 'title', columns = 'user', values = 'rating').fillna(0)

df_csr = csr_matrix(df_pivot.values)

nbrs = NearestNeighbors(metric='cosine', algorithm='brute', p=2).fit(df_csr)

titles = list(df_pivot.index.values)


# function to return recommended books - this will be tested
def get_recommends(book = ""):
  if not book:
    return 'Please enter a book title'

  distances, indices = nbrs.kneighbors(df_pivot.loc[book].values.reshape(1, -1), len(titles), True)
  recommended_books = [book, sum([[[df_pivot.index[indices.flatten()[i]], distances.flatten()[i]]] for i in range(5, 0, -1)], [])]

  return recommended_books

print(get_recommends("Where the Heart Is (Oprah's Book Club (Paperback))"))