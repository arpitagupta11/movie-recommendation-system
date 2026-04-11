# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built using **Machine Learning + Streamlit**, which suggests similar movies based on user selection.

---

## 🚀 Live Demo  
🔗 [Add your deployed link here]  
(Example: https://movie-recommendation-system.streamlit.app)

---

## 📌 Project Overview  

This project recommends movies based on similarity scores calculated using **cosine similarity**.  

- Select a movie from the dropdown  
- Click on **Recommend**  
- Get 5 similar movie suggestions along with posters  

The system uses metadata like genres, keywords, cast, and crew to find similarities between movies.

---

## 🧠 How It Works  

- Data preprocessing and feature extraction  
- Text vectorization using **CountVectorizer**  
- Similarity calculation using **Cosine Similarity**  
- Recommendations based on highest similarity scores  

---

## 🛠️ Tech Stack  

- **Frontend/UI**: Streamlit  
- **Backend**: Python  
- **Libraries**: pandas, numpy, scikit-learn, requests  
- **Data Source**: TMDB (The Movie Database API)  
- **Model Storage**: Pickle (.pkl files)

---

## 📂 Project Structure
movie-recommendation-system/
│
├── app.py                  # Main Streamlit app
├── movie_dict.pkl          # Movie data
├── similarity.pkl          # Similarity matrix
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
└── .gitignore

---

## ⚙️ Installation & Setup  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/arpitagupta11/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2️⃣ Create virtual environment  
```bash
python -m venv venv
```

### 3️⃣ Activate environment  

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 4️⃣ Install dependencies  
```bash
pip install -r requirements.txt
```

### 5️⃣ Run the app  
```bash
streamlit run app.py
```

---

## 🖼️ Screenshots  

### 🔹 Home Page  
*(Add screenshot here)*

### 🔹 Recommendations Output  
*(Add screenshot here)*

---

## 🔐 API Configuration  

This project uses TMDB API to fetch movie posters.

Replace your API key in the code or use environment variables:
TMDB_API_KEY=your_api_key_here

---

## 📈 Future Improvements  

- Add user authentication  
- Improve UI (Netflix-style design)  
- Add filtering (genre, rating, year)  
- Deploy with scalable backend (FastAPI + React)  
- Use collaborative filtering for better recommendations  

---

## 🤝 Contributing  

Contributions are welcome! Feel free to fork this repo and submit a pull request.

---

## 👩‍💻 Author  

**Arpita Gupta**  
🔗 https://github.com/arpitagupta11  

---

## ⭐ If you like this project  

Give it a ⭐ on GitHub and share it!
