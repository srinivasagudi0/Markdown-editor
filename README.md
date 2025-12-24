# Markdown Editor

A simple interactive command-line Markdown editor written in Python.  
This tool allows users to generate Markdown content by choosing formatting options interactively and saves the result to a file.

---

## Features

- Plain text input
- **Bold** formatting
- *Italic* formatting
- Inline code formatting
- Headers (levels 1–6)
- Ordered lists
- Unordered lists
- Links
- Add new lines
- Export output to `output.md`

---

## How It Works

The program runs in a loop where the user selects a formatter.  
Based on the selection, the program asks for the required input and appends the formatted Markdown to the final output.

When the user enters `!done`, the Markdown content is saved to a file named `output.md`.

---

## Available Commands

### Formatters
- `plain`
- `bold`
- `italic`
- `inline-code`
- `header`
- `link`
- `ordered-list`
- `unordered-list`
- `new-line`

### Special Commands
- `!help` – Show available formatters
- `!done` – Save output and exit

---

## Usage

### Run the program
```bash
python main.py
