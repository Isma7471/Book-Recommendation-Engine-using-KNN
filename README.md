# Book-Recommendation-Engine-using-KNN
This repository contains a Book Recommendation Engine developed using the K-Nearest Neighbors (KNN) algorithm. The model is designed to recommend books based on user ratings, leveraging similarity between books to suggest titles with similar patterns of engagement.
<<<<<<< HEAD
## Overview
The engine uses the Book-Crossings dataset, which includes:

1.1 million ratings (scale of 1-10)
270,000 books
90,000 users
After data cleaning and processing, the model filters out users with fewer than 200 ratings and books with fewer than 100 ratings to ensure statistical relevance. It then constructs a user-book matrix and applies KNN with cosine similarity to determine the closest books for any given title.

## Features

Data Cleaning: Ensures data quality by filtering infrequent users and books.
Cosine Similarity: Measures the similarity between books based on ratings.
Efficient Recommendation Function: Provides a list of five similar books for any title queried.
Sparse Matrix Representation: Optimizes memory usage for large datasets.
## Usage
The get_recommends function accepts a book title as input and returns:
=======
## Overview 
The engine uses the Book-Crossings dataset, which includes:

- 1.1 million ratings (scale of 1-10)
- 270,000 books
- 90,000 users
After data cleaning and processing, the model filters out users with fewer than 200 ratings and books with fewer than 100 ratings to ensure statistical relevance. It then constructs a user-book matrix and applies KNN with cosine similarity to determine the closest books for any given title.
## Dataset 
The dataset is taken from kaggle dataset and it is published by:
Cai-Nicolas Ziegler, Sean M. McNee, Joseph A. Konstan, Georg Lausen; Proceedings of the 14th International World Wide Web Conference (WWW '05), May 10-14, 2005, Chiba, Japan.
## Format
The Book-Crossing dataset comprises 3 tables.
BX-Users
Contains the users. User IDs (User-ID) have been anonymized and map to integers.

BX-Books
Books are identified by their respective ISBN. Moreover, some content-based information is given (Book-Title, Book-Author, Year-Of-Publication, Publisher), obtained from Amazon Web Services.

BX-Book-Ratings
Contains the book rating information. Ratings (Book-Rating) are either explicit, expressed on a scale from 1-10 (higher values denoting higher appreciation), or implicit, expressed by 0.
## Features
- Data Cleaning: Ensures data quality by filtering infrequent users and books.
- Cosine Similarity: Measures the similarity between books based on ratings.
- Efficient Recommendation Function: Provides a list of five similar books for any title queried.
- Sparse Matrix Representation: Optimizes memory usage for large datasets.
## Usage
The `get_recommends` function accepts a book title as input and returns:
>>>>>>> f68aa8e (Updated README)

The queried book title
A list of 5 similar books with their calculated similarity scores

<<<<<<< HEAD
##Example
get_recommends("The Queen of the Damned (Vampire Chronicles (Paperback))")

##Expected output

=======
## Example
`get_recommends("The Queen of the Damned (Vampire Chronicles (Paperback))")`
## Expected output
```python
>>>>>>> f68aa8e (Updated README)
[  'The Queen of the Damned (Vampire Chronicles (Paperback))',  [    ['Catch 22', 0.7939], 
    ['The Witching Hour (Lives of the Mayfair Witches)', 0.7449], 
    ['Interview with the Vampire', 0.7345],
    ['The Tale of the Body Thief (Vampire Chronicles (Paperback))', 0.5376],
    ['The Vampire Lestat (Vampire Chronicles, Book II)', 0.5178]
  ]
]
<<<<<<< HEAD

##Technologies Used
Python
scikit-learn: Nearest Neighbors
pandas: Data manipulation
scipy.sparse: Memory-efficient matrix operations
This repository serves as a practical example of using collaborative filtering and KNN for book recommendations.
=======
```
## Technologies Used
Python
- scikit-learn: Nearest Neighbors
- pandas: Data manipulation
- scipy.sparse: Memory-efficient matrix operations
This repository serves as a practical example of using collaborative filtering and KNN for book recommendations.
>>>>>>> f68aa8e (Updated README)
