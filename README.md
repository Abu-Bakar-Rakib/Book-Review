# 📚 Book Review Platform

A modern, full-featured web application for book enthusiasts to discover, review, and discuss literature. Built with Flask, this platform enables users to create accounts, browse curated collections, submit reviews with star ratings, and engage with a vibrant community of readers.

---

## ✨ Key Features

- **User Authentication** – Secure account registration and login with password hashing
- **Book Catalog** – Browse 12+ pre-loaded books with advanced search, filtering, and sorting
- **Review System** – Submit detailed reviews with 1–5 star ratings and edit or delete anytime
- **Rating Analytics** – Visual breakdown of review distributions per book
- **Helpful Votes** – Mark reviews as helpful to highlight quality contributions
- **Add Books** – Community members can expand the catalog with new titles
- **User Profiles** – View reviewer activity and contribution history
- **Responsive Design** – Mobile-friendly interface powered by modern HTML/CSS

<img width="1321" height="577" alt="image" src="https://github.com/user-attachments/assets/24214a0b-ee75-4d8d-b484-98f39737239c" />

---

## 🛠️ Tech Stack

- **Backend:** Flask 3.0.0, Flask-SQLAlchemy 3.1.1
- **Authentication:** Flask-Login 0.6.3
- **Forms & Validation:** Flask-WTF 1.2.1, WTForms
- **Database:** SQLite with SQLAlchemy ORM
- **Frontend:** HTML5, CSS (74.8% of codebase)
- **Security:** Werkzeug 3.0.1 for password hashing and CSRF protection

---

## 📁 Project Structure

```
Book-Review/
├── app.py                 Core Flask application, routes, and seed data
├── models.py              Database models (User, Book, Review, ReviewHelpful)
├── forms.py               WTForms validation schemas
├── config.py              Configuration management
├── run.py                 Application entry point
├── requirements.txt       Python dependencies
├── database.db            SQLite database
├── templates/             HTML templates for all pages
└── .secret_key            Flask secret key (git-ignored)
```

### How It Works

The application follows a classic MVC pattern. `app.py` manages HTTP routes and request handling, `models.py` defines the database schema (users, books, reviews with a many-to-many helpful votes relationship), and `forms.py` provides server-side validation for user inputs. The seed database initializes 12 classic and contemporary titles with pre-populated reviews on first run.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip package manager

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Abu-Bakar-Rakib/Book-Review.git
   cd Book-Review
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python run.py
   ```
   
   Or alternatively:
   ```bash
   python app.py
   ```

4. **Access the app**
   Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

### Demo Credentials

The database seeds automatically on first run with demo users:

| Username  | Email                  | Password     |
|-----------|------------------------|--------------|
| rahim     | rahim@example.com      | password123  |
| karim     | karim@example.com      | password123  |
| sumaiya   | sumaiya@example.com    | password123  |

---

## 📖 Usage Guide

### Browsing Books

- Visit the **Books** page to explore the full catalog
- Use filters by genre, search by title or author, and sort by rating or name

### Submitting a Review

1. Navigate to a book's detail page
2. Log in (or create an account if needed)
3. Fill out the review form with your rating and comments
4. Submit – your review appears immediately

### Managing Reviews

- **Edit:** Click the edit button on your review to update content or rating
- **Delete:** Remove reviews permanently with the delete button
- **Mark Helpful:** Click the helpful button on others' reviews to show appreciation

### Adding Books

- Click **Add Book** to contribute new titles to the catalog
- Provide title, author, genre, and description; cover image is optional

### View Profiles

- Click any reviewer's name to see their profile and review history

---

## 🔐 Security Features

- **Password Hashing:** Werkzeug secures all passwords
- **CSRF Protection:** Flask-WTF guards all forms against cross-site attacks
- **Session Management:** Secure login/logout with Flask-Login
- **SQL Injection Prevention:** SQLAlchemy parameterized queries
- **Input Validation:** Server-side validation on all user inputs

---

## 📊 Database Schema

### User
- Stores username, email, hashed password, and join date
- One-to-many relationship with Review

### Book
- Contains title, author, genre, description, and cover image URL
- Includes computed `average_rating()` method

### Review
- Captures user rating (1–5), review text, and timestamp
- Linked to User and Book; cascade delete ReviewHelpful entries

### ReviewHelpful
- Tracks which users marked which reviews as helpful
- Unique constraint prevents duplicate votes

---

## 🎨 Frontend

HTML templates are located in the `templates/` directory and include:
- **home.html** – Landing page with featured books and recent reviews
- **books.html** – Browsable catalog with search and filters
- **book_detail.html** – Individual book page with reviews and rating breakdown
- **add_book.html** – Form to contribute new books
- **profile.html** – User review history and stats
- **register.html / login.html** – Authentication pages
- **404.html / 500.html** – Error pages

---

## 🤝 Contributing

We welcome contributions! To improve the platform:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

---

## 📝 License

This project is open source and available under the MIT License.

---

## 👤 Author

**Abu-Bakar-Rakib**

- GitHub: [@Abu-Bakar-Rakib](https://github.com/Abu-Bakar-Rakib)
- Repository: [Book-Review](https://github.com/Abu-Bakar-Rakib/Book-Review)

---

## 💡 Future Enhancements

- [ ] User ratings and reviewer rankings
- [ ] Advanced recommendation engine based on reading history
- [ ] Email notifications for new reviews
- [ ] Social features: follow users, create reading lists
- [ ] Integration with Goodreads API for metadata enrichment
- [ ] Admin dashboard for moderation
- [ ] Rate limiting and spam prevention
- [ ] Dark mode UI toggle

---

## 📞 Support & Feedback

Found a bug? Have an idea? Please open an [issue](https://github.com/Abu-Bakar-Rakib/Book-Review/issues) on GitHub.

---

**Happy reading! 📖✨**
