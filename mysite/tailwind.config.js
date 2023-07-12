/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["myapp/templates/myapp/index.html"],
  safelist: [
    {
      pattern: /./, // the "." means "everything"
    },
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
