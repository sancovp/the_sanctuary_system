## Help with OWL

When building an ontology in OWL, if there is anything that cant be represented by OWL:

- Requires a new class to be made in that ontology that describes the thing missing in OWL
- Then anything requiring that should refer to the entity in the ontology, which is made with OWL base terms.

Basically, we use OWL but we create wrappers of OWL aspects when we have to inside of the ontology itself instead of inside of OWL or the program for ontology engineering.

For example:

`OWL can represent the ontology of a procedure but cannot perform it. When defining a procedure, simply define it as a Procedure subclass (is_a Procedure).`
