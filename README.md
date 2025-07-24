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

Review Text Processing

6. Emoji and Special Character Removal

-Emojis, symbols, and special characters were removed using regular expressions to focus only on meaningful textual content.

7. Stop Word Removal

-Common stop words (e.g., “the”, “is”, “and”) were removed using NLTK to reduce noise and retain only informative words.

8. Lemmatization

-Words were reduced to their root forms (e.g., “running” → “run”) using WordNetLemmatizer, improving consistency across similar word forms.

9. Filtering Out Short and Long Reviews

-Reviews with fewer than 3 words or more than 100 words were removed to retain only meaningful and focused feedback.
-In imbalanced data:
Reviews < 3 words: 603
Reviews > 100 words: 31

-In balanced data:
Reviews < 3 words: 1014
Reviews > 100 words: 47

10. Conflicting Review Removal

-Reviews that did not align with their ratings (e.g., positive text with a negative rating or vice versa) were manually identified and removed.
-A total of 2,655 conflicting reviews were filtered out from the final dataset to enhance training clarity and reduce label noise.

These preprocessing steps ensured a high-quality, cleaned dataset .

# Visualizations Used
To better understand the data and guide modeling decisions, several visualizations were created during the exploratory data analysis (EDA) phase:

1. Histogram Plots of Rating Distributions

-Visualized how ratings were distributed across the dataset.
-Helped identify class imbalances (e.g., more 5-star reviews than 1-star).

2. Countplots (Per Rating Class)

-Displayed the number of reviews for each rating class using count plots.
-Useful for comparing rating frequency across different datasets.

3. Pie Charts of Overall Sentiment Distribution

-Ratings were grouped into broader sentiment categories like Positive, Neutral, and Negative.
-Pie charts helped visualize the proportion of each sentiment group in the dataset.


Before and After Cleaning/Balancing Comparisons

-Visualizations were also used to compare the dataset before and after cleaning and balancing. This helped in understanding how much the data was affected by preprocessing steps, especially in terms of class distribution. It clearly showed how the ratings became more evenly distributed after balancing, making the dataset suitable for training.


# Balancing Strategy
To ensure that the model does not become biased toward any specific rating class, a balancing strategy was applied. After combining and cleaning all the datasets, it was observed that the number of reviews across different rating levels (from 1 to 5) was slightly imbalanced. To fix this, each rating class was limited to 2700 samples. This was done by under-sampling the classes with more than 2700 reviews. As a result, the final dataset had an equal number of 2700 reviews for each rating class, helping the model learn fairly from all categories. The data was also shuffled to maintain randomness before training.


# Imbalancing Strategy
Before applying the imbalancing strategy, the cleaned combined dataset had the following rating distribution: 7,578 samples for rating 1, 3,274 for rating 2, 7,732 for rating 3, 16,930 for rating 4, and 46,124 for rating 5. To simulate a more realistic, real-world review distribution, we created an imbalanced dataset by excluding the samples used in the balanced dataset and then sampling the remaining data based on specific proportions. The new imbalanced dataset included 10% of samples for rating 1, 15% for rating 2, 25% for rating 3, 30% for rating 4, and 20% for rating 5. This helped in evaluating how the models perform under skewed data conditions.


# Train-Test Split Methodology
After cleaning, balancing, and shuffling the dataset, the next step was to split it into training and testing sets. An 80-20 split was used, where 80% of the data was used for training the model, and the remaining 20% was kept aside for testing. This ensures that the model learns from the majority of the data while still being evaluated on unseen data to assess its generalization performance. The split was done in a stratified manner to maintain the balanced class distribution across both sets.


# Notes on Decisions Taken
Several key preprocessing and modeling decisions were made during the development of this automated review rating system:

-Lemmatization over Stemming:
Lemmatization was preferred instead of stemming to ensure that the words are reduced to their proper base or dictionary form (e.g., “better” → “good”), preserving semantic meaning. Stemming, while faster, often produces non-meaningful root words (e.g., “running” → “run” vs. “runn”), which could negatively affect text understanding.

-TF-IDF Vectorizer over Count Vectorizer:
TF-IDF (Term Frequency-Inverse Document Frequency) was chosen to convert text data into numerical features. Unlike Count Vectorizer, TF-IDF not only considers how frequently a word appears but also penalizes common words across documents. This helps the model focus on more informative and distinctive words.

-Class Balancing via Sampling:
Since the original dataset was imbalanced across different rating categories, an equal number of reviews per class (2700) were sampled to ensure that the model does not become biased towards majority classes.
