import sqlite3
from werkzeug.security import generate_password_hash

DATABASE = "expense_tracker.db"

def get_db():
    """
    Returns a SQLite connection with row_factory set to sqlite3.Row
    and foreign key constraints enabled.
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def init_db():
    """
    Creates the users and expenses tables.
    """
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                category TEXT CHECK(category IN ('Food', 'Transport', 'Bills', 'Health', 'Entertainment', 'Shopping', 'Other')),
                date TEXT NOT NULL,
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            );
        """)
        conn.commit()

def seed_db():
    """
    Populates the database with initial development data.
    """
    with get_db() as conn:
        # 1. Insert Demo User
        demo_email = "demo@spendly.com"
        demo_password = generate_password_hash("password123")

        conn.execute(
            "INSERT OR IGNORE INTO users (name, email, password_hash) VALUES (?, ?, ?)",
            ("Demo User", demo_email, demo_password)
        )
        conn.commit()

        # Get the demo user id
        user = conn.execute("SELECT id FROM users WHERE email = ?", (demo_email,)).fetchone()
        if not user:
            return
        user_id = user["id"]

        # 2. Insert Sample Expenses
        # Check if expenses already exist for this user to prevent duplicates
        existing_expenses = conn.execute(
            "SELECT id FROM expenses WHERE user_id = ?", (user_id,)
        ).fetchone()

        if existing_expenses:
            return

        sample_expenses = [
            (user_id, 12.50, 'Food', '2026-09-01', 'Lunch at Cafe'),
            (user_id, 5.00, 'Transport', '2026-09-02', 'Bus Fare'),
            (user_id, 60.00, 'Bills', '2026-09-03', 'Internet Bill'),
            (user_id, 25.00, 'Health', '2026-09-04', 'Pharmacy'),
            (user_id, 15.00, 'Entertainment', '2026-09-05', 'Movie Ticket'),
            (user_id, 40.00, 'Shopping', '2026-09-06', 'New T-shirt'),
            (user_id, 10.00, 'Other', '2026-09-07', 'Gift Wrap'),
            (user_id, 8.00, 'Food', '2026-09-08', 'Coffee'),
        ]

        conn.executemany(
            "INSERT INTO expenses (user_id, amount, category, date, description) VALUES (?, ?, ?, ?, ?)",
            sample_expenses
        )
        conn.commit()
