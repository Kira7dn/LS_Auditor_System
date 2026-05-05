# Example: Complex Audit Process Flow

This diagram uses the professional styling defined in the Mermaid Expert skill to visualize a multi-departmental audit findings flow.

```mermaid
flowchart TD
    subgraph Discovery
        A[Raw Data] --> B{Data Quality?}
        B -- No --> C[Normalize Data]
        C --> B
    end

    subgraph Execution
        B -- Yes --> D[Variance Analysis]
        D --> E[Identify Exceptions]
        E --> F[Root Cause Synthesis]
    end

    subgraph Packaging
        F --> G[Evidence Dossier]
        G --> H[Solution Design]
    end

    %% Styles
    classDef highlight fill:#f96,stroke:#333,stroke-width:4px
    class D,F highlight
```

## Key Styling Features
- **Subgraphs**: Clear separation of audit phases.
- **Decision Nodes**: Explicit quality checks.
- **Highlights**: Important analysis nodes are colored for focus.
