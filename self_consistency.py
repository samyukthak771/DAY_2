from config import client, MODEL, banner
from cot_compare import QUESTIONS

def solve(question):
    prompt = f"""
Solve this question carefully and give the final answer:

{question}
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
    )

    return response.choices[0].message.content.strip()


banner("SELF-CONSISTENCY")

for i, question in enumerate(QUESTIONS, 1):
    print(f"\nQUESTION {i}: {question}")

    answers = []

    for run in range(5):
        answer = solve(question)
        answers.append(answer)
        print(f"\nRun {run + 1}:")
        print(answer)

    print("\n--- 5 runs completed ---")