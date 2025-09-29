# 🪙 Crypto Trading Assistant - Prompt Chaining

This project demonstrates a two-stage prompt chaining application for crypto trading guidance using the Gemini API.

## 🎯 Project Goal

Use Prompt Chaining to implement a two-stage assistant:

1. Chain 1 (Planning): Turn the user's trading request into a short JSON plan that breaks the task into 3–6 concise steps.
2. Chain 2 (Execution): Use the JSON plan and the original request to produce a final, user-friendly trading guide in Markdown.

## 📋 Features

- Two-stage prompt chaining (planning → execution)
- JSON output for the plan and Markdown for the final guide
- CLI parameters for temperature, top_p, and max_tokens
- Robust JSON repair heuristics for malformed model output
- Diagnostic saving of raw responses when repair fails

## 🚀 Installation

1. Install dependencies

   ```powershell
   pip install -r requirements.txt
   ```

## 🧪 Examples

See `examples/inputs.txt` for sample prompts to try with the CLI.

## Usage

Run from the project root:

```powershell
python app.py --prompt "I want a short-term momentum trade on BTC/USDT. Capital: $1000, max risk 2%" --temperature 0.7
```

## Notes

- Set your `GEMINI_API_KEY` in the environment or a `.env` file.
- This project focuses on instructional planning and is not investment advice.