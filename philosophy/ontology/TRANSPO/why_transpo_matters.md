Let's say you try to represent a Cat and you start with something like this:

Cat has_FurType

###### Observation
But look, your instance of Cat has_FurType when actually we know a Cat cant have a general `FurType` but can only have a `CatFurType` since it is a Cat. 

###### Realization
When we fully expand *what ontology engineering is*, isn't it, itself, a meta-language that has templated patterns (ie criteria for applying relationships as edges between nodes) that are always the same and always indicate the same things and the differentiator between all the truth values is simply semantic as long as those patterns are satisfied? Otherwise, we have multiple layers of problems because we can say things that SOUND RIGHT but when expanded have ontological issues.


#### The Problem With Reasoners
Ontology Reasoners lack semantic recognition so they can only map between what they have. So they cant propose what template maps to which new labels because they cannot do any reasoning about the semantics... AND this cannot be easily solved with LLMs because LLMs skip layers of formal representation (they themselves need the templates to be applied to their outputs, and the reasoner cannot look at the semantics, so that means you need a huge nest of LLMs watching LLMs in order to get to the level of semantic mapping you need for the reasoner to work correctly in tandem with the LLM).

#### How TRANSPO Solves This Problem
TRANSPO is the ontology of pattern templates required for that nest of LLMs. It is an ontology that explains ontology engineering (ie, a meta-ontology).
