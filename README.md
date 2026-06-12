# Hybrid Learning-to-Rank Search Engine

A full-stack AI-powered search engine that combines Semantic Search, BM25 Ranking, Click Feedback Signals, and Machine Learning-based Learning-to-Rank (LTR) to improve search relevance.

This project demonstrates how modern search engines rank results using multiple signals instead of relying on keyword matching alone. The system combines:

* Semantic Search using Sentence Transformers
* BM25 Keyword Ranking
* User Click Feedback
* Machine Learning Ranking Model
* Query Autocomplete
* Analytics Dashboard

The final ranking score is generated using a hybrid approach that combines all signals.

## Features

### Search Engine

* Semantic Search using embeddings
* BM25 keyword matching
* Hybrid ranking
* Query autocomplete
* Search result ranking
* Top-ranked result highlighting

### Learning-to-Rank

* Click feedback collection
* Positive and negative training samples
* ML ranking model using Scikit-Learn
* Ranking score prediction

### Analytics Dashboard

* Top search queries
* Most clicked documents
* Interactive charts
* Search statistics

## 📷 Screenshots

### Home Page with Search Interface and Autocomplete Suggestions
<img width="1440" height="900" alt="Screenshot 2026-06-13 at 2 19 34 AM" src="https://github.com/user-attachments/assets/5b6965a4-19ba-4563-bbbb-a9de514c0518" />


### Hybrid Ranking Results
<img width="1440" height="900" alt="Screenshot 2026-06-13 at 2 19 54 AM" src="https://github.com/user-attachments/assets/6c20ed9d-b008-4e8c-b608-c9030bad0ada" />

### Analytics Dashboard
<img width="1440" height="900" alt="Screenshot 2026-06-13 at 2 20 10 AM" src="https://github.com/user-attachments/assets/591c900d-f6fb-4b68-8d07-900ea4358f6b" />

<img width="1440" height="900" alt="Screenshot 2026-06-13 at 2 20 26 AM" src="https://github.com/user-attachments/assets/1f718b31-cda8-4764-af3e-fea87d39668d" />

### FastAPI API Documentation
<img src="screenshots/api.png" width="900"/>

## Hybrid Ranking Formula

The final ranking score combines:

```text
Hybrid Score =
0.4 × Semantic Score
+ 0.2 × BM25 Score
+ 0.2 × Click Score
+ 0.2 × ML Rank Score
```

## Machine Learning Ranking

Training features:

* Query Length
* Title Length
* Click Labels

Model:

* Random Forest Classifier

Output:

* Ranking Probability Score

## Analytics

The dashboard provides:

* Top Queries
* Most Clicked Documents
* User Interaction Insights
* Search Performance Monitoring
