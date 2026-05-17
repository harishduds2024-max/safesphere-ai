import sqlite3

conn = sqlite3.connect('safesphere.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS threats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    level TEXT,
    status TEXT
)
''')

cursor.execute('''
INSERT INTO threats (title, level, status)
VALUES
('Phishing Attack', 'High', 'Detected')
''')

conn.commit()
conn.close()

print("Database Created Successfully")
