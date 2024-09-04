/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./templates/**/*.html",
    "./static/src/**/*.js",
    "./node_modules/flowbite/**/*.js",
    "node_modules/preline/dist/*.js",
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require("flowbite/plugin"),
    require('preline/plugin'),
  ],
}

