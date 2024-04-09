let currentPlayer = "X";
let board = [["", "", ""], ["", "", ""], ["", "", ""]];
let gameActive = true;
let playerXScore = 0;
let playerOScore = 0;

function makeMove(cell) {
    if (gameActive && cell.innerText === "") {
        const row = Array.from(cell.parentNode.children).indexOf(cell);
        const col = Array.from(cell.parentNode.parentNode.children).indexOf(cell.parentNode);
        
        board[col][row] = currentPlayer;
        cell.innerText = currentPlayer;
        
        if (checkWinner(col, row)) {
            document.getElementById("result").innerText = `¡Jugador ${currentPlayer} gana!`;
            updateScore(currentPlayer);
            gameActive = false;
        } else if (checkDraw()) {
            document.getElementById("result").innerText = "¡Empate!";
            gameActive = false;
        } else {
            currentPlayer = (currentPlayer === "X") ? "O" : "X";
        }
    }
}

function updateScore(player) {
    if (player === "X") {
        playerXScore++;
        document.getElementById("playerXScore").innerText = playerXScore;
    } else if (player === "O") {
        playerOScore++;
        document.getElementById("playerOScore").innerText = playerOScore;
    }
}

function checkWinner(row, col) {
    const symbols = ["X", "O"];
    
    for (let symbol of symbols) {
        let won = true;
        
        // Check row
        for (let i = 0; i < 3; i++) {
            if (board[col][i] !== symbol) {
                won = false;
                break;
            }
        }
        if (won) return true;
        
        won = true;
        
        // Check column
        for (let i = 0; i < 3; i++) {
            if (board[i][row] !== symbol) {
                won = false;
                break;
            }
        }
        if (won) return true;
        
        won = true;
        
        // Check diagonals
        if (row === col) {
            for (let i = 0; i < 3; i++) {
                if (board[i][i] !== symbol) {
                    won = false;
                    break;
                }
            }
            if (won) return true;
        }
        
        won = true;
        
        if (row + col === 2) {
            for (let i = 0; i < 3; i++) {
                if (board[i][2 - i] !== symbol) {
                    won = false;
                    break;
                }
            }
            if (won) return true;
        }
    }
    
    return false;
}


function checkDraw() {
    return board.flat().every(cell => cell !== "");
}

function resetGame() {
    currentPlayer = "X";
    board = [["", "", ""], ["", "", ""], ["", "", ""]];
    gameActive = true;

    const cells = document.querySelectorAll('.cell');
    cells.forEach(cell => {
        cell.innerText = "";
    });

    document.getElementById("result").innerText = "";
}
