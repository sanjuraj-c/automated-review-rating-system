# Automated-review-rating-system
This project aims to automatically predicts the numerical ratings of the reviews given by the user.It uses Natural Language Processing(NLP), & Machine learning techniques for it.

# Project overview and objective
This project aims to build an automated review rating system that analyzes customer reviews and predicts the rating associated with each review. In many real-world scenarios, users provide detailed textual feedback, but numeric ratings may be missing, inconsistent, or biased. The goal is to train a machine learning model that can understand the sentiment and content of a review and accurately classify it into one of the standard rating categories (e.g., 1 to 5 stars).

By processing and analyzing review text using natural language processing techniques, this system helps businesses quickly identify the sentiment of customer feedback, monitor product performance, and make data-driven decisions without manual intervention.

# Dataset description
To build the automated review rating system, data was gathered in two phases from various sources containing customer reviews along with corresponding ratings. The objective was to retain only the review text and rating fields after cleaning and preprocessing.

Phase 1 Datasets:
1. Amazon Echo Product Reviews

-Columns included metadata such as page URL, title, review color, review date, and more.

-After inspection, unnecessary and mostly null-filled columns were dropped.

-Only the review text and rating columns were retained.

-Null values and duplicates were removed.

2. Amazon Product Reviews

-Contained product categories and user review details.

-Similar cleaning steps were applied: dropped unneeded columns and removed rows with missing review text.

-No duplicates were found.

3. ChatGPT Product Reviews

-A small set of reviews with rating and review date.

-No missing or duplicate values were present.

-Cleaned to keep only necessary fields.

4. Amazon General Reviews

-Included fields like reviewer ID, helpfulness votes, review summary, and time.

-Columns with missing or irrelevant data were removed.

-Ensured that all reviews were valid and unique.

These cleaned datasets were combined to form Cleaned Dataset 1.


Phase 2 Datasets:
1. MakeupAlley Cosmetic Product Reviews

-Each entry included product review, rating, and date.

-All entries were clean with no missing or duplicate records.

-Retained only the review text and rating columns.

2. Women’s Clothing E-commerce Reviews

-Included customer demographics and feedback information.

-After cleaning, only the review text and rating were kept.

-Null values and a single duplicate were removed.

These cleaned datasets were combined to form Cleaned Dataset 2.

Finally, both Cleaned Dataset 1 and Cleaned Dataset 2 were merged into a single dataset used for model training. Only reviews with meaningful content and valid rating labels were preserved.


# Preprocessing Steps
After collecting and cleaning the datasets, the following initial preprocessing steps were applied to prepare the review text and rating data for model training:

1. Data Loading and Inspection

Each dataset was loaded using pandas and inspected using functions like .head(), .tail(), .sample(), .shape, .columns, .info(), and .describe() to understand structure and content.

2. Handling Missing Values

-Columns that had a large number of missing values or were irrelevant to the analysis were dropped.

-Rows with missing entries in the review text or rating columns were removed to maintain data quality.

3. Dropping Irrelevant Columns

-Only the review text and rating columns were retained from each dataset.

-Other metadata like dates, user details, product configuration, etc., were considered unnecessary and discarded.

4. Duplicate Removal

-All datasets were checked for duplicate rows using .duplicated().

-Any duplicate records found (if any) were removed to avoid data redundancy.

5. Data Merging

-Cleaned datasets from Phase 1 were combined into a single dataset.

-Similarly, Phase 2 datasets were cleaned and merged.

-Finally, both cleaned datasets were concatenated to form one unified dataset.
