from flask import Flask, render_template, jsonify, request
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/threats', methods=['GET'])
def get_threats():
    conn = get_db_connection()
    threats = conn.execute('SELECT * FROM threats').fetchall()
    conn.close()

    return jsonify([dict(row) for row in threats])


@app.route('/api/add-threat', methods=['POST'])
def add_threat():
    data = request.json

    title = data.get('title')
    level = data.get('level')
    status = data.get('status')

    conn = get_db_connection()
    conn.execute(
        'INSERT INTO threats (title, level, status) VALUES (?, ?, ?)',
        (title, level, status)
    )
    conn.commit()
    conn.close()

    return jsonify({'message': 'Threat added successfully'})


@app.route('/api/stats')
def stats():
    conn = get_db_connection()

    total = conn.execute('SELECT COUNT(*) FROM threats').fetchone()[0]
    high = conn.execute("SELECT COUNT(*) FROM threats WHERE level='High'").fetchone()[0]
    medium = conn.execute("SELECT COUNT(*) FROM threats WHERE level='Medium'").fetchone()[0]
    low = conn.execute("SELECT COUNT(*) FROM threats WHERE level='Low'").fetchone()[0]

    conn.close()

    return jsonify({
        'total': total,
        'high': high,
        'medium': medium,
        'low': low
    })


if __name__ == '__main__':
    app.run(debug=True)
