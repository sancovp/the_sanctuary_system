To make a ZK Agent:

Requires:```[LLM Chat with tool that makes LLM call to observe context and extract meaning, LLM call to observe meaning and extract links, recursive calls to enter everything into neo4j (if we are using neo4j for node management)]```

To build those requires:```[LLM framework (done), prompt management (im a prompt engineer), neo4j (this is rather easy to set up if all we are doing is calling CREATE queries or serving specific nodes and their children)]```


Here's how ZK could work:

An LLM chat where when the main assistant uses the "observe and catalog" tool, it outputs an emoji

A regex function inside "observe and catalog" that lifts from the last <that emoji> in the chat to the first one, chunks it, and sends it to an LLM to break down:```[ This is the entire context Now catalog entities from this chunk Now this one... etc. ]```

Pipe to a python function that calls LLM to observe meaning and extract links Check links against known nodes Create any new nodes/Linked nodes & If no node for link, create node for link and link it

User has chat with agent1 Agent1 has tool (execute_chat_type_lattice with lace_config for observe and describe) to python function for Agent2 (regexing the main thread and sending it with the correct prompts) Agent2 has tool (execute_chat_type_lattice with lace config for observe and link) to python function for Agent3 (moving its output to agent3 and sending it with the correct prompts) and handling the Agent3 output to neo4j

Then we give agent1 a retrieve node list tool as well, so the user can have agent1 get context from the graph

Talk to the ZK agent (Agent1) about X ZK Agent creates entry to neo4j about X and its links OR Create Agent that ports from neo4j to Notion to create an auto-wiki pipeline? Goes like this:```[ Agent4 has list of pages on Notion Agent4 receives list of nodes from neo4j Agent4 chooses any node from neo4j that is not on Notion (this process has python based verification) Agent4 uses create notion page tool for chosen node Agent4 uses create notion link tool to create links for page of chosen node (this process has python based verification to prevent duplication) ]```
