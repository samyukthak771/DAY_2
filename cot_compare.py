from config import client, MODEL, banner

QUESTIONS = [
    "A course costs 15000. It is discounted by 15%. What is the final price?",
    "A student attends 3 classes each week for 10 weeks. How many classes do they attend?",
    "Ravi is taller than Arun. Arun is taller than Priya. Who is the tallest and who is the shortest?",
]

def ask(prompt):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )
    return response.choices[0].message.content

banner("DIRECT VS CHAIN-OF-THOUGHT COMPARISON")

for i, question in enumerate(QUESTIONS, 1):
    print(f"\nQUESTION {i}: {question}")

    direct_prompt = f"""
Answer this question directly and give only the final answer:

{question}
"""

    cot_prompt = f"""
Solve this question carefully.
Work through the reasoning step by step, then give the final answer:

{question}
"""

    print("\nDIRECT:")
    print(ask(direct_prompt))

    print("\nCHAIN-OF-THOUGHT:")
    print(ask(cot_prompt))