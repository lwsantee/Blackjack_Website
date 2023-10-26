import "https://unpkg.com/socket.io-client@4.7.2/dist/socket.io.min.js";

const socket = io();
socket.on("connect", () => {
  socket.emit("my event", { data: "Client connected!" });
  console.log("Client connected");
});
