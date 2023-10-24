import { io } from "socket.io-client";

const socket = io();
socket.on("connect", () => {
  socket.emit("my event", { data: "Client connected!" });
  console.log("Connected!");
});
