
### Task Description
- Build a compiler for a simple programming language supporting various token types: identifiers, keywords, integers, floating-point numbers, and symbols.
- Implement tokenization using Finite State Automata (FSAs) for each token type.
- Prioritize token classification based on a hierarchy if there are matching patterns (keywords, identifiers, numbers).

### Specifications
#### Tokenization
- **Token Types:** identifiers, keywords, integers, floating-point numbers, symbols.
- **FSAs:** Implement FSAs for each token type to perform lexical analysis.

#### Token Hierarchy
- Prioritize token classification based on a hierarchy (keywords > identifiers > numbers).

#### Syntactic Analysis
- Follow the provided grammar rules for syntactic analysis.

#### Rules for Syntactic Analysis
1. **S → statement**
2. **statement → if (A) | (statement)(statement) | y**
3. **y ∈ statement alphabets [Σstatement]**
4. **A → (cond)(statement) | (cond)(statement)(else)(statement)**
5. **cond → (x)(op1)(x) | x**
6. **op1 → + | - | * | / | ˆ | < | > | =**
7. **x → R | cond | y**

#### Note
- **Σstatement = numbers ∪ keywords ∪ identifiers - ’if’ and ’else’. It does NOT include operations.**
- **Brackets in the grammar are for reference; implementation can be without brackets.**

### Instructions
1. **Input:** Source code in the supported programming language.
2. **Output:** Compiler performing tokenization, prioritizing token hierarchy, and syntactic analysis based on the provided grammar.
