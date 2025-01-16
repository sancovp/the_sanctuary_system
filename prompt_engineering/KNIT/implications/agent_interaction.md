The formalization of PIO and LLMs being PIO types explains how this style of prompting and interaction can be more productive for the user, even if it cant necessarily be more productive for the LLM or an agent. But when we understand that, we can then create a nested system. We know we need a user callback at every step, but we can have depth of thought through subagents the agent calls to break down what it is thinking and generate a better or more complete output.

Fundamentally, this changes the agentic paradigm to this:
```
User -> Agent
Agent -> Subagent stack
Subagent stack -creates-> better output
Better output -injected_to-> Agent reflection
Agent reflection response -injected_to-> User thread
```
So the top level Agent simply calls a function and then looks at its own reflection's response to it
