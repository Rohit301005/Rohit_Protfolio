
# 🌐 Rohit Kumar Rawat — Developer Portfolio

Welcome to my personal developer portfolio! This website showcases my technical skills, projects, educational background, and journey as a Computer Science Engineering student interested in software development and AI.

## 🚀 Live Demo

🔗 **Portfolio Website:** https://rohit-protfolio.onrender.com/

## 👨‍💻 About Me

I am Rohit Kumar Rawat, a Computer Science Engineering student at IES University, Bhopal, passionate about Python development, Django backend engineering, problem-solving, and Artificial Intelligence.

I enjoy building practical applications, learning new technologies, and developing solutions that solve real-world problems.

## ✨ Features

- Responsive personal portfolio website
- About Me section
- Technical skills showcase
- Projects portfolio
- Educational background
- Resume section
- Contact form
- AI-powered chatbot
- Django-powered backend
- Admin dashboard for managing portfolio content
- Static file handling with WhiteNoise
- Production deployment on Render

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap

### Backend
- Python
- Django

### Database
- SQLite / PostgreSQL

### AI Integration
- Groq API
- Large Language Models (LLMs)

### Tools & Deployment
- Git
- GitHub
- WhiteNoise
- Render

## 📂 Project Structure

```text
Rohit_Portfolio/
│
├── core/
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   ├── templates/
│   │   └── core/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── build.sh
└── README.md
```

*Note: The structure above is representative. Adjust it to match your actual project folders.*

## ⚙️ Installation & Setup

Follow these steps to run the project locally.

### 1. Clone the repository

```bash
git clone https://github.com/Rohit301005/Rohit_Portfolio.git
```

### 2. Navigate to the project directory

```bash
cd Rohit_Portfolio
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows (CMD):**

```cmd
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure environment variables

Create a `.env` file in the project root and configure the required variables:

```env
SECRET_KEY=your_django_secret_key
DEBUG=True
GROQ_API_KEY=your_groq_api_key
```

Never upload your real `.env` file or API keys to GitHub.

### 7. Apply database migrations

```bash
python manage.py migrate
```

### 8. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 9. Collect static files

```bash
python manage.py collectstatic --noinput
```

### 10. Run the development server

```bash
python manage.py runserver
```

Open your browser:

http://127.0.0.1:8000/

## 🔐 Environment Variables

| Variable | Description |
|---|---|
| `SECRET_KEY` | Django secret key |
| `DEBUG` | Enables/disables debug mode |
| `GROQ_API_KEY` | API key for the AI chatbot |
| `DATABASE_URL` | Production database connection, if configured |

## 🤖 AI Chatbot

The portfolio includes an AI-powered chatbot integrated with the Groq API.

It is designed to answer questions about my:
- Technical skills
- Projects
- Educational background
- Development experience
- Career interests

The chatbot is intended to provide portfolio-related information and does not represent a general-purpose AI assistant.

## 🌍 Deployment

The website is deployed using **Render**.

Deployment includes:
- Production environment variables
- Django database migrations
- Static file collection
- WhiteNoise for static file serving
- Gunicorn as the WSGI application server

## 📌 Future Improvements

- Add more full-stack projects
- Improve chatbot functionality
- Enhance UI/UX and animations
- Add more AI/ML projects
- Improve testing and security
- Implement advanced analytics

## 📬 Contact

**Rohit Kumar Rawat**

- 📧 Email: [rohitkumarrrawat04@gmail.com](mailto:rohitkumarrrawat04@gmail.com)
- 🐙 GitHub: [Rohit301005](https://github.com/Rohit301005)
- 💼 LinkedIn: [Connect with me](https://www.linkedin.com/in/rohit-kumar-rawat-81bb35339/)
- 🌐 Portfolio: [Visit Website](https://rohit-protfolio.onrender.com/)

---

⭐ If you find my work interesting, feel free to explore my repositories and connect with me!
