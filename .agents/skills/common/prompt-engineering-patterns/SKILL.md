---
name: prompt-engineering-patterns
description: Master advanced prompt engineering techniques to maximize LLM performance, reliability, and controllability in production. Use when optimizing prompts, improving LLM outputs, or designing production prompt templates.
---

## 1. Core Patterns
- **Chain-of-Thought (CoT)**: Guide the model to think step-by-step.
- **Few-Shot Prompting**: Provide clear examples of input/output pairs.
- **Structured Output**: Enforce JSON, Markdown, or specific schema formats.
- **Role Prompting**: Define a clear persona (e.g., "Expert Auditor", "Senior Developer").

## 2. Advanced Techniques
- **Progressive Disclosure**: Only load necessary context.
- **Constraint Engineering**: Explicitly define what NOT to do.
- **Variable Injection**: Use placeholders like `{{variable_name}}` for dynamic content.

## 3. Best Practices
- Keep instructions imperative and direct.
- Use delimiters (e.g., `###`, `---`, `xml tags`) to separate sections.
- Verify success with automated checks or specific "Exit Criteria".

## 4. Pitfalls to Avoid
- Avoid "Negative Constraints" alone (prefer "Do X instead of Y").
- Avoid overly long system prompts that dilute focus.
- Avoid vague terms like "be creative" or "be helpful" without specific metrics.
