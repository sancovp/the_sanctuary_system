graph LR
  subgraph C_SanctuarySystem
    O_TWI --> O_PIO
    O_PIO --> O_UARL
    O_UARL --> O_EWSO
    O_EWSO --> O_Egregore
    O_Egregore --> O_SanctuaryRevolution
  end

  subgraph C_OntologyEngineering
    O_TRANSPO --> O_SemOntoRel
    O_SemOntoRel --> O_KnowledgeRepresentation
    O_KnowledgeRepresentation --> O_InformationSystems
  end

  subgraph C_CognitiveProcesses
    O_SkillChains --> O_EmergentThinking
    O_EmergentThinking --> O_DunningKrugerEffect
    O_DunningKrugerEffect --> O_Learning 
  end 

  subgraph C_AIandLLMs
    O_DUO --> O_PromptEngineering
    O_PromptEngineering --> O_LLMCapabilities
    O_LLMCapabilities --> O_AIethics
  end

  O_PIO --> O_TRANSPO
  O_EWSO --> O_TRANSPO
  O_SkillChains --> O_LLMCapabilities
  O_Learning --> O_AIethics

  subgraph Latent Spaces
    L(O_TWI)
    L(O_PIO)
  end

  O_SanctuaryRevolution --> O_DUO
  O_KnowledgeRepresentation --> O_InformationSystems





















  graph LR
  subgraph SanctuarySystem["C_SanctuarySystem"]
    TWI((O_TWI)) --> PIO((O_PIO))
    PIO --> UARL((O_UARL))
    UARL --> EWSO((O_EWSO))
    EWSO --> Egregore((O_Egregore))
    Egregore --> SanctuaryRevolution((O_SanctuaryRevolution))
  end

  subgraph OntologyEngineering["C_OntologyEngineering"]
    TRANSPO((O_TRANSPO)) --> SemOntoRel((O_SemOntoRel))
    SemOntoRel --> KnowledgeRepresentation((O_KnowledgeRepresentation))
    KnowledgeRepresentation --> InformationSystems((O_InformationSystems))
  end

  subgraph CognitiveProcesses["C_CognitiveProcesses"]
    SkillChains((O_SkillChains)) --> EmergentThinking((O_EmergentThinking))
    EmergentThinking --> DunningKrugerEffect((O_DunningKrugerEffect))
    DunningKrugerEffect --> Learning((O_Learning)) 
  end 

  subgraph AIandLLMs["C_AIandLLMs"]
    DUO((O_DUO)) --> PromptEngineering((O_PromptEngineering))
    PromptEngineering --> LLMCapabilities((O_LLMCapabilities))
    LLMCapabilities --> AIethics((O_AIethics))
  end

  PIO --> TRANSPO --> f_PIOtoUARL
  EWSO --> TRANSPO --> f_EWSOtoTRANSPO
  SkillChains --> LLMCapabilities --> f_SkillChainstoLLMCapabilities
  CognitiveProcesses --> AIethics --> f_CognitiveProcessestoAIethics

  subgraph "Latent Spaces"
    L_TWI --> L_O_TWI
    L_PIO --> L_O_PIO
  end

  SanctuarySystem --> AIandLLMs --> F_SanctuarySystemToAIethics
  OntologyEngineering --> InformationSystems --> F_OntologyEngineeringToKnowledgeRepresentation
