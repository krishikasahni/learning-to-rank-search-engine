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

### Home Page

<img width="1440" height="900" alt="screenshots:home" src="https://github.com/user-attachments/assets/d90e1b30-8e85-420d-9ed9-fd774b08ee62" />

### Search Results

<img width="1440" height="900" alt="screenshots:search-results" src="https://github.com/user-attachments/assets/79b8c512-3590-4db5-8d07-b69ee90b356e" />

<img width="1440" height="900" alt="Screenshot 2026-06-04 at 7 38 46 PM" src="https://github.com/user-attachments/assets/afa171cd-3fb9-4a43-9dcd-7a86c72c2370" />

### Analytics Dashboard

<img width="1440" height="900" alt="screenshots:analytics" src="https://github.com/user-attachments/assets/c68f9f18-86bd-49d5-9b6e-de1649de99be" />

<img width="1440" height="900" alt="Screenshot 2026-06-04 at 7 39 44 PM" src="https://github.com/user-attachments/assets/78703f5c-0480-446e-91fc-4ba1fb0f30b9" />

### API Documentation

<img width="1440" height="900" alt="screenshots:api-docs" src="https://github.com/user-attachments/assets/1205546b-1f4e-4fe5-ab56-a196368f71a7" />

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
