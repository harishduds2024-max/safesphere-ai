import sqlite3

conn = sqlite3.connect('database/safesphere.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS threats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    level TEXT NOT NULL,
    status TEXT NOT NULL
)
''')

sample_data = [
    ('Phishing Attack', 'High', 'Detected'),
    ('Malware Risk', 'Medium', 'Monitoring'),
    ('Suspicious Login', 'Low', 'Resolved')
]

cursor.executemany(
    'INSERT INTO threats (title, level, status) VALUES (?, ?, ?)',
    sample_data
)

conn.commit()
conn.close()

print('Database initialized successfully')
