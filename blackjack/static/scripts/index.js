import "https://unpkg.com/socket.io-client@4.7.2/dist/socket.io.min.js";

/**
 * When the page loads, display the modal and adjust game opacity
 *
 * @param {HTMLDivElement} modal The modal element to display on page load
 * @param {HTMLDivElement} game The game background to make transparent
 */
function initLoginModal(modal, game, socket) {
  modal.style.display = "block";
  game.style.opacity = "0.2";

  const submitPlayerForm = document.getElementById("userInfoForm");
  submitPlayerForm.addEventListener("submit", (event) => {
    event.preventDefault();
    submitForm(modal, game, socket);
  });
}

/**
 * Function to close the modal and make the main content visible
 *
 * @param {HTMLDivElement} modal The modal element to display on page load
 * @param {HTMLDivElement} game The game background to make transparent
 */
function closeModal(modal, game) {
  modal.style.display = "none";
  game.style.opacity = "1";
}

/**
 * Function to handle form submission
 *
 * @param {HTMLDivElement} modal The modal element to display on page load
 * @param {HTMLDivElement} game The game background to make transparent
 * @param {Socket} socket The web socket connection
 */
async function submitForm(modal, game, socket) {
  // Get player name and balance from the form
  const playerNameInput = document.getElementById("playerName");
  const playerBalanceInput = document.getElementById("playerBalance");

  // Validate the inputs
  const playerName = playerNameInput.value.trim();
  const playerBalance = parseFloat(playerBalanceInput.value);
  if (playerName === "" || isNaN(playerBalance) || playerBalance <= 0) {
    // Display an error message or take appropriate action for invalid inputs
    alert("Please enter valid information.");
    return;
  }

  const response = await fetch("/api/active-players");

  if (response.status >= 200 && response.status < 300) {
    const activePlayers = await response.json();

    if (
      activePlayers[playerName] !== undefined &&
      activePlayers[playerName] !== null
    ) {
      console.log("Player name is already in use");
    } else {
      // Close the modal if inputs are valid
      closeModal(modal, game);
      seatOtherPlayers(activePlayers);
      initJoinPlayerButtons(playerName, playerBalance);
    }
  } else {
    console.log(await response.text());
  }
}

function seatOtherPlayers(activePlayers) {
  for (const [name, player] of Object.entries(activePlayers)) {
    const seat = document.getElementById(`player${player.seat}Info`);
    seat.innerHTML = `
        <div class="player-info-row">
            <h2>${name}</h2>
            <h2>${player.balance}</h2>
        </div>
        <div class="player-cards">
        </div>
        `;
  }
}

// Function to handle player joining
function initJoinPlayerButtons(playerName, playerBalance) {
  const joinButtons = document.getElementsByClassName("player-info");
  for (const button of joinButtons) {
    button.addEventListener("click", async () => {
      const seatNumer = button.id.substring(6, 7);
      const response = await fetch("/api/player-join", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          playerName: playerName,
          playerBalance: playerBalance,
          playerSeat: seatNumer,
        }),
      });

      if (response.status >= 200 && response.status < 300) {
        button.innerHTML = `
        <div class="player-info-row">
            <h2>${playerName}</h2>
            <h2>${playerBalance}</h2>
        </div>
        <div class="player-cards">
        </div>
        `;
      }
    });
  }
}

document.addEventListener("DOMContentLoaded", () => {
  const socket = io({ autoConnect: false });

  // Get references to the modal and game container
  const modal = document.getElementById("modal");
  const game = document.getElementById("game");
  initLoginModal(modal, game, socket);
});
