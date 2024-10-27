/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}", // Add this to scan your React files
  ],
  theme: {
    extend: {
      fontFamily: {
        playwrite: ['"Playwrite BE VLG"', 'serif'],
        matemasie: ["Matemasie", "sans-serif"],
        suse: ["Suse", "sans-serif"],
      },
      colors: {
        primary: '#F8E16C', // Yellow color for primary
        secondary: '#ffffff', // White color for secondary
        border: '#e5e7eb', // Light gray for borders (matches Tailwind's gray-300)
        input: '#e5e7eb',
        ring: '#fbbf24', // Yellow color for focus ring (matches Tailwind's yellow-400)
        background: '#fef3c7', // Light yellow background color for overall feel
        foreground: '#1f2937', // Dark gray for foreground text (matches Tailwind's gray-800)
        destructive: {
          DEFAULT: '#ef4444', // Red for destructive actions
          foreground: '#ffffff',
        },
        muted: {
          DEFAULT: '#f3f4f6', // Light muted background
          foreground: '#6b7280', // Muted gray text (matches Tailwind's gray-500)
        },
        accent: {
          DEFAULT: '#d97706', // Deeper yellow-orange for accents
          foreground: '#ffffff',
        },
        popover: {
          DEFAULT: '#ffffff',
          foreground: '#374151', // Gray for popover text (matches Tailwind's gray-700)
        },
        card: {
          DEFAULT: '#ffffff',
          foreground: '#1f2937',
        },
      },
    },
  },
  plugins: [],
};
