"""
Prompt templates and configuration
"""

PLANNING_PROMPT = """You are a crypto trading plan assistant. Based on the user's request (goals, constraints, risk tolerance, and time horizon), produce a clear actionable trading plan.

User Request: {user_request}

Return a JSON object EXACTLY in the format below. Do not add extra explanation or commentary — JSON only.

{{
    "steps": [
        "Step 1 description",
        "Step 2 description",
        "Step 3 description",
        "Step 4 description"
    ],
    "assumptions": [
        "Assumption 1",
        "Assumption 2"
    ],
    "success_criteria": [
        "Success criterion 1",
        "Success criterion 2"
    ]
}}

Constraints and guidance:
- Provide 3-6 concise, actionable steps.
- Include reasonable assumptions about market access, capital, and tools.
- Make success criteria measurable (e.g., "achieve X% portfolio allocation", "execute trade with max slippage Y").
- Reply with JSON only.
"""

EXECUTION_PROMPT = """You are a professional crypto trading assistant. Given the user request and the plan produced earlier, produce a final, user-facing trading guide in Markdown.

User Request: {user_request}

Plan:
{plan}

Produce a human-friendly Markdown document that includes:
- A clear title
- Short overview
- Required setup or tools (exchanges, wallets, APIs)
- Specific steps to execute (expand and make actionable the plan's steps)
- Risk management and assumptions
- Example trade parameters (position size, entry, stop-loss, take-profit)
- Next Steps list (3 items)

Use headings, bullet lists, and short paragraphs. Do not include raw JSON in the final output. The final reply should be in Markdown only.
"""
