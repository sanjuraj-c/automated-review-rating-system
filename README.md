# Automated-review-rating-system
This project aims to automatically predicts the numerical ratings of the reviews given by the user.It uses Natural Language Processing(NLP), & Machine learning techniques for it.

# Project overview and objective
This project aims to build an automated review rating system that analyzes customer reviews and predicts the rating associated with each review. In many real-world scenarios, users provide detailed textual feedback, but numeric ratings may be missing, inconsistent, or biased. The goal is to train a machine learning model that can understand the sentiment and content of a review and accurately classify it into one of the standard rating categories (e.g., 1 to 5 stars).

By processing and analyzing review text using natural language processing techniques, this system helps businesses quickly identify the sentiment of customer feedback, monitor product performance, and make data-driven decisions without manual intervention.

# Dataset description
This project combines multiple publicly available review datasets collected in two phases. Each dataset contains user-generated product reviews along with corresponding rating scores. Below is a brief description of the datasets used:
Phase 1 Datasets
1.E-commerce Product Reviews (Electronics)
Contains reviews of electronic products including features like review text, rating, review title, date, and verification status. After preprocessing, only the review text and rating columns were retained.

2.Amazon General Product Reviews
A larger collection of various product reviews. The dataset included review headers, review body, and rating fields. Null and unnecessary fields were removed before combining.

3.ChatGPT User Reviews
A small but clean set of reviews with rating and review text, requiring minimal cleaning. All columns were retained after removing irrelevant ones.

4.Amazon Product Reviews
Includes detailed Amazon reviews with fields like reviewer name, helpful votes, review summary, and rating. Only the core fields relevant to review text and rating were used after preprocessing.

After cleaning, these were merged together into a single combined dataset called Cleaned Dataset 1.

Phase 2 Datasets
1.Cosmetic Product Reviews (MakeupAlley)
This dataset contains reviews of cosmetic products with corresponding ratings and product names. Cleaned to retain only the review text and rating.

2.Women’s Clothing E-commerce Reviews
Contains user feedback on women’s clothing products, including customer age, department, and detailed reviews. After removing null values and duplicates, only essential fields like review text and rating were kept.

These were merged into Cleaned Dataset 2, and then both cleaned datasets from phase 1 and phase 2 were finally combined to form the complete dataset used for training and evaluation.

