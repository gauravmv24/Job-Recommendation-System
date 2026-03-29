# Job-Recommendation-System
Developed during internship at Nova Nector Service Pvt. Ltd.
NLP-based Job Recommendation System using TF-IDF and Cosine Similarity
Project Timeline

 Week 1–3: Problem understanding and research on job recommendation systems  
 Week 4-6: Designed approach using NLP techniques (TF-IDF)  
Week 6-9: Implemented similarity model using cosine similarity  

Job Recommendation System
Overview
This project is an NLP-based Job Recommendation System developed during internship. It recommends relevant job roles to candidates by analyzing their skills, resume content, and experience, and matching them with job descriptions.


 Problem Statement
Job seekers often struggle to find relevant job roles due to large volumes of job postings. Traditional keyword matching systems are inefficient and fail to capture context. This project aims to build a system that intelligently recommends jobs based on semantic similarity.


Approach / Methodology
1. Input candidate resume or skills  
2. Collect job descriptions  
3. Text preprocessing (cleaning, removing stopwords)  
4. Feature extraction using TF-IDF  
5. Compute similarity using cosine similarity  
6. Rank jobs based on similarity score  



Tech Stack
- Python  
- Scikit-learn  
- Natural Language Processing (NLP)  
- TF-IDF Vectorizer  
- Cosine Similarity  


Dataset
- Sample job descriptions created manually  
- Candidate skills provided as input  
- Future scope includes using real-world datasets from job portals  

---

 Model Details
- TF-IDF is used to convert text data into numerical vectors  
- Cosine similarity is used to measure similarity between resume and job descriptions  
- Higher similarity score indicates better job match  


Results / Accuracy
Sample Output:

Data Scientist with Python and Machine Learning - Match Score: 0.82  
Data Analyst with SQL and Excel - Match Score: 0.75  
AI Engineer with NLP - Match Score: 0.68  

The system successfully recommends jobs based on skill similarity.

  
 Future Work

Integrate advanced NLP models like BERT for better understanding
 Use real-time job data from job portals
 Build a web interface for user interaction
 Improve accuracy using larger datasets
