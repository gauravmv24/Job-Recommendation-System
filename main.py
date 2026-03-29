from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Candidate Resume
candidate_profile = ["Python, Data Analysis, Machine Learning, NLP, Pandas"]

# Job Descriptions
job_list = [
    "Looking for Data Scientist with Python and Machine Learning skills",
    "Frontend Developer required with React and JavaScript",
    "Data Analyst with SQL, Excel, and Python knowledge",
    "AI Engineer with NLP and Deep Learning experience",
    "Software Engineer with Java and Spring Boot"
]

# Convert text to vectors
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(candidate_profile + job_list)

# Compute similarity
similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])

print("Top Job Recommendations:\n")

# Rank jobs
for i, score in enumerate(similarity_scores[0]):
    print(f"{job_list[i]} --> Match Score: {score:.2f}")
