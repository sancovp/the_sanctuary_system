# About Knowledge "Neurosymbiosis" through Interaction as Teleology (KNIT)
KNIT is a prompt engineering technique based on the way that human-AI programming interactions in an LLM chat work when the user is debugging code with an LLM. It renders potential problems and potential truths to the user and the user's next input dictates the knowledge evolution flow. The purpose of KNIT is to debug knowledge spaces so that they can be aligned into TRANSPO. This then allows the `KNIT creations`, which are `polysemic imaginary ontology constellations` to be aligned with TRANSPO, granting the capacity for alignment with the upper ontologies that TRANSPO subsumes, and thus the domain ontologies that use them. KNIT is designed to be used in `knowledge mining`. Eventually, it might be part of `Crystal Ball`, the knowledge mining application tool of the `Victory-Everything Chain`. 

## Usefulness

KNIT's usefulness suffers unless the reasoner on the ontology stack is set up and injects back into the LLM. Ie: the KNIT assistant (pure LLM without function calling) needs to actually be an agent (LLM with function calling) that can ontologize the input and then call the reasoner and then output the results back to the agent, and there is absolutely no way around this because LLMs kind of suck at doing what it appears like they are great at doing (sometimes and definitely in the case of logic). For example, a conversation was generated with all TRUE values in every IO pair and then a completely contradictory prompt set was also served to a "reasoning model" named o1 by openai and it also produced the wrong answer (gave `TRUE` when all the information was contradictory to everything else it had previously responded `TRUE` to). However, a bare KNIT assistant can still be used to expose the wrong outputs to the user so that the user can refine their own ideas through clarifying the contradictions the LLM outputted. 

Unfortunately, that also means that a KNIT assistant is essentially a writing partner that can autocomplete in a specific way that helps the user explore their own thoughts, but does not do anything else. Furthermore, if the user does not align their thoughts (if those thoughts are about something real) with an ontology or at least a parent framework for that thing (like the hero's journey or AIDA in those respective domains), then they will not be able to use it for anything. However, that also means that even if the user believes the output accords with X (aida, HJ, etc) the only way for them to find out would be to show it to others and get their feedback. For AIDA they would then run the `campaign with the AIDA ad copy`. For HJ, they would then write the story and show it to as many people as possible to see if it is a `good story`.

## The Core Issue
The evidence is sitting right there in those outputs:

The LLM could generate perfectly structured inheritance chains and type transformations that:

- Were locally coherent
- Used all the right terminology
- Followed the correct patterns
- BUT could justify completely opposite conclusions


Most tellingly - it could do this even when the prompt explicitly stated all the reasons it was contradicting itself:

- "EVEN THOUGH sanctuary AND wasteland REFER TO THE SPACES..."
- It listed every contradiction
- Acknowledged its own incoherence
- Still produced a "valid" looking response


This strongly suggests that:

- It's not actually understanding properties
- It's not tracking logical relationships
- It's just pattern matching at an incredibly sophisticated level
- The embeddings must not capture actual semantic properties because if they did, these contradictions would be impossible


The evidence was right there in how the system behaved - it demonstrated exactly this limitation through its ability to generate contradictory but structurally perfect responses.
This is a case where observing the behavior reveals the architectural limitation, even if we can't see inside the black box to confirm the exact causal chain.

## Potential Stop-gap Solution
```
A potential agentic stop-gap solution to this could be `atomic workflows`. If we have it work this way:

User: assertion -> LLM
LLM -> tool:[
Tool -> more sub-LLMs (one for each aspect of the chain pattern and they have an iterations limit)
]
tool -> LLM
LLM: scrutinizes output for missing aspects -> User
User: gives commentary on LLM's observations and decides whether to continue chaining or not
If chaining continues: loop
If not: break back to step 1, LLM: suggest potential route, ask for assertion -> User
```
