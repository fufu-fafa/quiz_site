# Quiz Site

A simple, single-page quiz app. Load a quiz from a JSON file (upload it or paste it), answer the questions one at a time, and get a score with a full review at the end. No build step and no dependencies.

## Features

- Load a quiz by **uploading** a `.json` file (file picker or drag and drop) or by **pasting** the JSON text
- Questions and answer options are **shuffled** every time a quiz starts, including retakes
- Instant feedback after each answer, with an optional explanation
- Keyboard support: press `1`–`9` to pick an option
- Final score with a review of every question
- Clear error messages for invalid JSON or invalid quiz content
- Light and dark theme (follows your system setting)

## Getting started

Because the "Try the sample quiz" and "Download sample file" buttons load `sample-quiz.json` from the server, serve the folder over HTTP rather than opening `index.html` directly from disk:

```bash
python3 -m http.server 8000
```

Then open <http://localhost:8000/index.html>.

Uploading and pasting a quiz also work if you open `index.html` directly, but the sample buttons need a server because browsers block reading local files from a page opened from disk.

## Quiz file format

```json
{
  "title": "My Quiz",
  "description": "Optional intro text",
  "questions": [
    {
      "question": "What is 2 + 2?",
      "options": ["3", "4", "5"],
      "answer": 1,
      "explanation": "Optional, shown after answering"
    }
  ]
}
```

| Field | Required | Description |
| --- | --- | --- |
| `title` | No | Quiz title. Defaults to "Quiz". |
| `description` | No | Short intro text shown under the title. |
| `questions` | Yes | A non-empty array of question objects. |
| `questions[].question` | Yes | The question text. |
| `questions[].options` | Yes | At least 2 choices (text or numbers). |
| `questions[].answer` | Yes | The correct option, either as its position starting at `0`, or as the exact option text. |
| `questions[].explanation` | No | Shown after the question is answered. |

`answer` always refers to the option order as written in your file. The page shuffles the options when the quiz starts and keeps track of the correct one for you.

## Files

| File | Purpose |
| --- | --- |
| `index.html` | The whole app: markup, styles and script. |
| `sample-quiz.json` | Example quiz, loaded by the "Try the sample quiz" button. |
