async function loadThreats() {
    const tableBody = document.getElementById('threatTableBody');
    tableBody.innerHTML = '';

    threats.forEach(threat => {
        const row = `
            <tr>
                <td>${threat.id}</td>
                <td>${threat.title}</td>
                <td>${threat.level}</td>
                <td>${threat.status}</td>
            </tr>
        `;

        tableBody.innerHTML += row;
    });
}


async function loadStats() {
    const response = await fetch('/api/stats');
    const stats = await response.json();

    document.getElementById('totalThreats').innerText = stats.total;
    document.getElementById('highThreats').innerText = stats.high;
    document.getElementById('mediumThreats').innerText = stats.medium;
    document.getElementById('lowThreats').innerText = stats.low;
}


document.getElementById('threatForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const title = document.getElementById('title').value;
    const level = document.getElementById('level').value;
    const status = document.getElementById('status').value;

    await fetch('/api/add-threat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            title,
            level,
            status
        })
    });

    loadThreats();
    loadStats();

    document.getElementById('threatForm').reset();
});


window.onload = () => {
    loadThreats();
    loadStats();
};
