"""Day 2: print the agent's real ReAct trace."""

from agent import agent

QUESTION = (
    "Which is cheaper: CS101 and AI202 with a 10% scholarship, "
    "or all three courses with a 25% scholarship? By how much?"
)

print("QUESTION:", QUESTION)
print()
print("--- the agent's actions and observations ---")

answer = agent(QUESTION, max_steps=8)

print()
print("FINAL ANSWER:", answer)