# sentiment-analysis-reviews

NLP project: sentiment analysis of e-commerce reviews (TF-IDF, Logistic Regression, Linear SVM, DistilBERT)

## Dataset

- **Name:** Amazon Fine Food Reviews (from Kaggle)
- **Source credit:** [add the original source and license exactly as written on the Kaggle dataset page]
- **Size:** 568,454 reviews, 10 columns
- **Columns used:** `Text` (review text) and `Score` (1 to 5 stars)
- **Labels:** 1-2 stars = negative, 3 = neutral, 4-5 = positive
- **Class balance:** positive 78.1%, negative 14.4%, neutral 7.5%
- **Note:** the raw data is not stored in this repo. Download it from Kaggle and place it at `data/reviews.csv`.

## Why accuracy alone is misleading

About 78% of reviews are positive, so a model that always predicts "positive" would reach about 78% accuracy while learning nothing. I will compare models using macro F1 and per-class recall, and use stratified splits.

## Progress

- [x] Environment setup (Python 3.12, VS Code, Git)
- [x] Data loading and class balance check
- [ ] Text cleaning and train/test split
- [ ] TF-IDF baselines (Logistic Regression, Linear SVM)
- [ ] DistilBERT fine-tuning
- [ ] Error analysis and results
- [ ] Streamlit demo
