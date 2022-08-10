/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ["./src/**/*.{html,js}", "./views/**/*.{html,js}"],
	theme: {
		extend: {},
	},
	plugins: [require("flowbite/plugin")],
};
