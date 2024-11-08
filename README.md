# Book-Recommendation-Engine-using-KNN
This repository contains a Book Recommendation Engine developed using the K-Nearest Neighbors (KNN) algorithm. The model is designed to recommend books based on user ratings, leveraging similarity between books to suggest titles with similar patterns of engagement.
##Overview
The engine uses the Book-Crossings dataset, which includes:

1.1 million ratings (scale of 1-10)
270,000 books
90,000 users
After data cleaning and processing, the model filters out users with fewer than 200 ratings and books with fewer than 100 ratings to ensure statistical relevance. It then constructs a user-book matrix and applies KNN with cosine similarity to determine the closest books for any given title.

##Features
Data Cleaning: Ensures data quality by filtering infrequent users and books.
Cosine Similarity: Measures the similarity between books based on ratings.
Efficient Recommendation Function: Provides a list of five similar books for any title queried.
Sparse Matrix Representation: Optimizes memory usage for large datasets.
##Usage
The get_recommends function accepts a book title as input and returns:

The queried book title
A list of 5 similar books with their calculated similarity scores

##Example
get_recommends("The Queen of the Damned (Vampire Chronicles (Paperback))")

##Expected output

[  'The Queen of the Damned (Vampire Chronicles (Paperback))',  [    ['Catch 22', 0.7939], 
    ['The Witching Hour (Lives of the Mayfair Witches)', 0.7449], 
    ['Interview with the Vampire', 0.7345],
    ['The Tale of the Body Thief (Vampire Chronicles (Paperback))', 0.5376],
    ['The Vampire Lestat (Vampire Chronicles, Book II)', 0.5178]
  ]
]

##Technologies Used
Python
scikit-learn: Nearest Neighbors
pandas: Data manipulation
scipy.sparse: Memory-efficient matrix operations
This repository serves as a practical example of using collaborative filtering and KNN for book recommendations.
