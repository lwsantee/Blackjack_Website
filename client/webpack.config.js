const path = require("path");

module.exports = {
  mode: "development",
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: "ts-loader",
        exclude: /node_modules/,
      },
    ],
  },
  resolve: {
    extensions: [".tsx", ".ts", ".js"],
  },
  entry: {},
  output: {
    filename: "[name].bundle.js",
    path: path.resolve(__dirname, "dist/scripts"),
  },
};
