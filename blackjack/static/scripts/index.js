// Import the Socket.IO client library
import "https://unpkg.com/socket.io-client@4.7.2/dist/socket.io.min.js";

/**
 * Function to initialize the login modal when the page loads.
 *
 * @param {HTMLDivElement} modal - The modal element to display on page load
 * @param {HTMLDivElement} game - The game background to make transparent
 * @param {Socket} socket - The web socket connection
 */
async function initLoginModal(modal, game, socket) {
  // Display the modal and adjust game opacity
  modal.style.display = "block";
  game.style.opacity = "0.2";

  // Make a REST API call to get active players
  const response = await fetch("/api/active-players");

  if (response.status >= 200 && response.status < 300) {
    // If API call is successful, seat other players
    const activePlayers = await response.json();
    seatOtherPlayers(activePlayers);
  }

  // Listen for the form submission event
  const submitPlayerForm = document.getElementById("userInfoForm");
  submitPlayerForm.addEventListener("submit", (event) => {
    event.preventDefault();
    submitForm(modal, game, socket);
  });
}

/**
 * Function to close the modal and make the main content visible
 *
 * @param {HTMLDivElement} modal - The modal element to close
 * @param {HTMLDivElement} game - The game background to make visible
 */
function closeModal(modal, game) {
  modal.style.display = "none";
  game.style.opacity = "1";
}

/**
 * Function to handle form submission
 *
 * @param {HTMLDivElement} modal - The modal element to close
 * @param {HTMLDivElement} game - The game background to make visible
 * @param {Socket} socket - The web socket connection
 */
async function submitForm(modal, game, socket) {
  // Get player name and balance from the form
  const playerNameInput = document.getElementById("playerName");
  const playerBalanceInput = document.getElementById("playerBalance");

  // Validate the inputs
  const playerName = playerNameInput.value.trim();
  const playerBalance = parseFloat(playerBalanceInput.value);
  if (playerName === "" || isNaN(playerBalance) || playerBalance <= 0) {
    // Display an error message for invalid inputs
    alert("Please enter valid information.");
    return;
  }

  // Make a REST API call to check active players
  const response = await fetch("/api/active-players");

  if (response.status >= 200 && response.status < 300) {
    const activePlayers = await response.json();

    if (
      activePlayers[playerName] !== undefined &&
      activePlayers[playerName] !== null
    ) {
      console.log("Player name is already in use");
    } else {
      // Close the modal if inputs are valid and initialize join buttons
      closeModal(modal, game);
      initJoinPlayerButtons(playerName, playerBalance);
    }
  } else {
    console.log(await response.text());
  }
}

/**
 * Function to display other players at their respective seats.
 *
 * @param {Object} activePlayers - Object containing information about active players
 */
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
    seat.classList = `player-info player-${player.seat}-info`;
  }
}

/**
 * Function to handle player joining and initialize join buttons.
 *
 * @param {string} playerName - The name of the player joining
 * @param {number} playerBalance - The balance of the player joining
 */
function initJoinPlayerButtons(playerName, playerBalance) {
  const joinButtons = document.getElementsByClassName("player-info");
  for (const button of joinButtons) {
    button.addEventListener("click", async () => {
      const seatNumber = button.id.substring(6, 7);
      if (button.classList.contains("player-info-empty")) {
        // Make a REST API call to handle player joining
        const response = await fetch("/api/player-join", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            playerName: playerName,
            playerBalance: playerBalance,
            playerSeat: seatNumber,
          }),
        });
        if (response.status >= 200 && response.status < 300) {
          // Update the button's HTML and class if the join is successful
          button.innerHTML = `
          <div class="player-info-row">
              <h2>${playerName}</h2>
              <h2>${playerBalance}</h2>
          </div>
          <div class="player-cards" id="player-${seatNumber}-cards">
          </div>
          `;
          button.classList = `player-info player-${seatNumber}-info`;
        }
      }
    });
  }
}

/**
 * Function to display a player card at a specific seat.
 *
 * @param {string} seatNumber - The seat number where the card is displayed
 * @param {string} cardValue - The value of the card
 * @param {string} cardSuit - The suit of the card
 */
function dealPlayerCard(seatNumber, cardValue, cardSuit) {
  const player = document.getElementsByClassName(`player-${seatNumber}-cards`);
  player.innerHTML = `<div class="card" data-value="${cardValue}" data-suit="${cardSuit}"></div>`;
}

// Event listener for when the DOM content is fully loaded
document.addEventListener("DOMContentLoaded", () => {
  // Initialize the Socket.IO connection
  const socket = io();

  // Listen for the 'display-other-players' event
  socket.on("display-other-players", (player) => {
    seatOtherPlayers(player);
  });

  // Get references to the modal and game container
  const modal = document.getElementById("modal");
  const game = document.getElementById("game");

  // Initialize the login modal
  initLoginModal(modal, game, socket);
});
