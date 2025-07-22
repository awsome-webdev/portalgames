fetch('/games')
    .then(response => response.json())
    .then(data => {
        console.log(data)
        const gamesContainer = document.getElementById('games');
        gamesContainer.innerHTML = '';
        data.forEach(game => {
            const gameDiv = document.createElement('div');
            gameDiv.setAttribute('onclick', `opengame(this)`);
            gameDiv.className = 'game';
            gameDiv.innerHTML = `<h3 class="game-name">${game}</h3>`;
            gamesContainer.appendChild(gameDiv);
        });
    });
function opengame(gameDiv) {
    const gameName = gameDiv.querySelector('.game-name').textContent;
    const gameFrame = document.getElementById('game-frame');
    gameFrame.src = `/games/${gameName}`;
    gameFrame.style.display = 'block';
    document.getElementById('close-button').style.display = 'block';
    document.getElementById('games').style.display = 'none';
}
function closeGame() {
    const gameFrame = document.getElementById('game-frame');
    gameFrame.src = '';
    gameFrame.style.display = 'none';
    document.getElementById('close-button').style.display = 'none';
    document.getElementById('games').style.display = 'flex';
}