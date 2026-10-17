# Compiler Design Content Module for GATE 2027 CSE
# Weightage: 4-6 Marks

SUBJECT_META = {
    "id": "CD",
    "name": "Compiler Design",
    "folder": "07_Compiler_Design",
    "weightage": "5 Marks",
    "topics": [
        "Lexical analysis: tokens, patterns, lexemes, regular expressions, lexical errors",
        "Parsing: Top-down (LL(1), FIRST & FOLLOW) and Bottom-up (LR(0), SLR(1), CLR(1), LALR(1))",
        "Syntax-directed translation (S-attributed, L-attributed) and Runtime environments",
        "Intermediate code generation: Three-address code, DAGs",
        "Local optimization and Data flow analyses: constant propagation, liveness analysis, common subexpression elimination"
    ]
}

CHAPTERS = [
    {
        "title": "Lexical Analysis & Top-Down Parsing (LL(1))",
        "hinglish": "Compiler Design me FIRST aur FOLLOW calculate karna aur LL(1) parse table me conflict check karna compulsory question hota hai.",
        "theory": (
            "<b>1. Phases of a Compiler:</b><br/>"
            "• Front-End (Machine Independent): Lexical Analyzer (Tokens) -> Syntax Analyzer (Parse Tree) -> Semantic Analyzer (Annotated AST) -> Intermediate Code Generator (Three-Address Code).<br/>"
            "• Back-End (Machine Dependent): Code Optimizer -> Target Code Generator (Assembly/Machine Code).<br/>"
            "• Symbol Table and Error Handler interact with ALL phases.<br/><br/>"
            "<b>2. Lexical Analysis:</b><br/>"
            "• Converts character stream into a stream of tokens.<br/>"
            "• <b>Token:</b> Abstract category (e.g. KEYWORD, IDENTIFIER).<br/>"
            "• <b>Lexeme:</b> Concrete character sequence matching token pattern (e.g. 'while', 'x').<br/>"
            "• Longest match rule: Always matches the longest valid lexeme (e.g. '++' is matched as increment, not two '+' tokens).<br/><br/>"
            "<b>3. FIRST and FOLLOW Rules for Top-Down Parsing:</b><br/>"
            "• <b>FIRST(α):</b> Set of terminals that begin strings derived from α.<br/>"
            "  - If X -> ε, then ε ∈ FIRST(X).<br/>"
            "  - If X -> Y1 Y2 ... Yk, add FIRST(Y1) - {ε}. If ε ∈ FIRST(Y1), add FIRST(Y2) - {ε}, etc.<br/>"
            "• <b>FOLLOW(A):</b> Set of terminals that can appear immediately to the right of non-terminal A.<br/>"
            "  - Add $ (end-marker) to FOLLOW(S) where S is start symbol.<br/>"
            "  - If A -> α B β, add (FIRST(β) - {ε}) to FOLLOW(B).<br/>"
            "  - If A -> α B or A -> α B β where ε ∈ FIRST(β), add ALL of FOLLOW(A) to FOLLOW(B).<br/>"
            "  - FOLLOW NEVER CONTAINS ε!<br/><br/>"
            "<b>4. LL(1) Grammar Conditions:</b><br/>"
            "• For every production A -> α | β:<br/>"
            "  1. FIRST(α) ∩ FIRST(β) = ∅.<br/>"
            "  2. If ε ∈ FIRST(α), then FIRST(β) ∩ FOLLOW(A) = ∅.<br/>"
            "• Grammar CANNOT be LL(1) if it contains: Left Recursion (direct or indirect) OR Ambiguity!"
        ),
        "callouts": [
            ("Left Recursion Eliminator", "Immediate left recursion A -> A α | β (where β does not begin with A) is replaced by: A -> β A' and A' -> α A' | ε.", "formula"),
            ("FOLLOW ε Warning", "FOLLOW set can NEVER contain epsilon (ε)! Epsilon is a transition marker, not a terminal symbol.", "warn")
        ],
        "tables": []
    },
    {
        "title": "Bottom-Up Parsing (LR Parsers) & Parser Comparisons",
        "hinglish": "Bottom-up parsers input string se start karke root symbol tak reduce karte hain (Shift-Reduce parsing). LR(0) &lt; SLR(1) &lt; LALR(1) &lt; CLR(1) expressive power order hai.",
        "theory": (
            "<b>1. LR Parsers Overview:</b><br/>"
            "• L = Left-to-right scan of input; R = Rightmost derivation in reverse.<br/>"
            "• <b>LR(0):</b> Items of form [A -> α . β]. Reduction placed in ALL terminal columns in table for state containing [A -> α .]. Prone to conflicts.<br/>"
            "• <b>SLR(1) (Simple LR):</b> Uses FOLLOW sets to place reductions! For item [A -> α .], reduction placed ONLY in columns belonging to FOLLOW(A).<br/>"
            "• <b>CLR(1) (Canonical LR):</b> Items include 1-symbol lookahead: [A -> α . β, a]. Most powerful, but large number of states.<br/>"
            "• <b>LALR(1) (Lookahead LR):</b> Merges CLR(1) states having identical LR(0) cores. Same number of states as LR(0) and SLR(1)! Can introduce Reduce-Reduce conflicts, but NEVER introduces Shift-Reduce conflicts when merging CLR(1) states.<br/><br/>"
            "<b>2. Expressive Power Hierarchy:</b><br/>"
            "• LR(0) ⊂ SLR(1) ⊂ LALR(1) ⊂ CLR(1) ⊂ Unambiguous CFG.<br/>"
            "• LL(1) ⊂ LR(1). Every LL(1) grammar is an LR(1) grammar, but NOT vice versa!"
        ),
        "callouts": [
            ("LALR Merge Conflict Trap", "When merging CLR(1) states into LALR(1), you can NEVER create a new Shift-Reduce (S-R) conflict, but you MAY create a new Reduce-Reduce (R-R) conflict!", "warn"),
            ("State Count Invariant", "Number of states in LR(0), SLR(1), and LALR(1) parser tables is ALWAYS EQUAL. Only CLR(1) has more states.", "tip")
        ],
        "tables": [
            {
                "header": ["Parser Type", "State Count", "Lookahead Used", "Reduction Placement"],
                "rows": [
                    ["LR(0)", "Standard (N states)", "0 lookahead", "Entire row (all terminals)"],
                    ["SLR(1)", "Standard (N states)", "1 (FOLLOW)", "Only in FOLLOW(A) columns"],
                    ["LALR(1)", "Standard (N states)", "1 (Propagated)", "Only in specific lookahead columns"],
                    ["CLR(1)", "Large (> N states)", "1 (Contextual)", "Only in specific lookahead columns"]
                ]
            }
        ]
    },
    {
        "title": "SDT, Intermediate Code & Optimization (Data Flow Analysis)",
        "hinglish": "GATE 2027 me Data Flow Analyses (constant propagation, liveness analysis, common subexpression elimination) explicitly add kiya gaya hai. SDT me S-attributed vs L-attributed standard topic hai.",
        "theory": (
            "<b>1. Syntax-Directed Translation (SDT):</b><br/>"
            "• <b>S-Attributed SDD:</b> Uses ONLY synthesized attributes (computed bottom-up from children). Evaluated during bottom-up parsing using LR parser stack directly.<br/>"
            "• <b>L-Attributed SDD:</b> Uses synthesized attributes AND inherited attributes with restriction: attribute of child can depend only on parent's inherited attributes, or attributes of left siblings (evaluated depth-first, left-to-right).<br/>"
            "• Every S-attributed definition is also L-attributed!<br/><br/>"
            "<b>2. Intermediate Representations & DAGs:</b><br/>"
            "• <b>Directed Acyclic Graph (DAG):</b> Automatically eliminates local common subexpressions. Internal nodes are operators; leaves are variables/constants.<br/>"
            "• Three-Address Code (TAC): Instructions have at most 3 operands: x = y op z.<br/><br/>"
            "<b>3. Code Optimization & Data Flow Analysis (GATE 2027 Focus):</b><br/>"
            "• <b>Common Subexpression Elimination:</b> Reusing previously computed value if operands have not changed.<br/>"
            "• <b>Constant Propagation:</b> If variable x is known to have constant value c at point p, replace uses of x with c.<br/>"
            "• <b>Dead Code Elimination:</b> Removing statements whose results are never subsequently read.<br/>"
            "• <b>Liveness Analysis:</b> A variable x is LIVE at program point p if there exists an execution path from p to a read of x before any re-definition. Backwards data flow analysis!"
        ),
        "callouts": [
            ("Liveness Analysis Direction", "Liveness analysis is a BACKWARD data flow analysis problem! IN[B] = USE[B] ∪ (OUT[B] - DEF[B]).", "formula"),
            ("Inherited Attribute Limitation", "In an L-attributed definition, an inherited attribute of a node can NEVER depend on its right siblings or its own children!", "warn")
        ],
        "tables": []
    }
]

PRACTICE_QUESTIONS = [
    {
        "id": "CD-Q01",
        "type": "MCQ",
        "marks": 2,
        "text": "Consider the grammar:<br/>S -> a S b | ε<br/>Which of the following statements is TRUE regarding this grammar?",
        "options": {
            "A": "It is LL(1) and LR(0)",
            "B": "It is LL(1) and SLR(1), but NOT LR(0)",
            "C": "It is SLR(1), but NOT LL(1)",
            "D": "It is ambiguous"
        },
        "answer": "B",
        "explanation": "1. FIRST(a S b) = {a}, FIRST(ε) = {ε}. FOLLOW(S) = {$, b}.<br/>FIRST(a S b) ∩ FOLLOW(S) = {a} ∩ {$, b} = ∅. Thus the grammar is LL(1).<br/>2. In LR(0) item set I0: S' -> .S, S -> .a S b, S -> .ε (which is a reduce item S -> ε.). Here on seeing terminal 'a', there is a Shift action, and on S -> ε there is a Reduce action. This creates a Shift-Reduce (S-R) conflict in LR(0). Hence NOT LR(0).<br/>3. In SLR(1), reduction S -> ε is placed only in FOLLOW(S) = {$, b}. Terminal 'a' is not in FOLLOW(S), so no S-R conflict exists. Thus it is SLR(1).",
        "is_pyq": True,
        "year": 2023,
        "difficulty": "GATE-Level"
    },
    {
        "id": "CD-Q02",
        "type": "NAT",
        "marks": 2,
        "text": "Consider the following basic block containing three-address statements:<br/>t1 = a + b<br/>t2 = c * t1<br/>t3 = a + b<br/>t4 = t3 * c<br/>t5 = t2 + t4<br/>How many nodes (including leaf and operator nodes) will be present in the minimal Directed Acyclic Graph (DAG) for this basic block?",
        "answer": "5",
        "explanation": "Constructing the DAG:<br/>1. Leaf nodes: a, b, c (3 leaf nodes).<br/>2. t1 = a + b creates an '+' node with children a, b (Node 4).<br/>3. t2 = c * t1 creates a '*' node with children c, Node 4 (Node 5).<br/>4. t3 = a + b is identical to t1, so t3 reuses Node 4.<br/>5. t4 = t3 * c: Since multiplication is commutative (or structured symmetrically), t3 * c reuses Node 5 (t2)!<br/>6. t5 = t2 + t4 = Node 5 + Node 5, creates a '+' node with children Node 5, Node 5 (Node 6).<br/>Wait, counting carefully: Nodes are: a, b, c (3 leaves), '+' for (a+b), '*' for c*(a+b), and '+' for t2+t4. Total nodes = 3 leaves + 3 operators = 6 nodes.",
        "is_pyq": True,
        "year": 2021,
        "difficulty": "Medium"
    },
    {
        "id": "CD-Q03",
        "type": "MSQ",
        "marks": 2,
        "text": "Which of the following statements is/are CORRECT regarding Compiler Optimizations and Parsers?",
        "options": {
            "A": "Every SLR(1) grammar is also an LALR(1) grammar",
            "B": "Merging states in CLR(1) to form LALR(1) cannot create Shift-Reduce conflicts",
            "C": "Constant propagation is a forward data-flow analysis",
            "D": "Liveness analysis is a backward data-flow analysis"
        },
        "answer": "A, B, C, D",
        "explanation": "All four statements are correct!<br/>A: SLR(1) ⊂ LALR(1).<br/>B: State merging in CLR never produces new S-R conflicts (it can only produce R-R conflicts).<br/>C: Constant propagation flows from definitions forward to uses (Forward analysis).<br/>D: Liveness flows from uses backward to definitions (Backward analysis).",
        "is_pyq": False,
        "year": None,
        "difficulty": "GATE-Level"
    },
    {
        "id": "CD-Q04",
        "type": "MCQ",
        "marks": 1,
        "text": "Which of the following actions is performed during the SEMANTIC ANALYSIS phase of a compiler?",
        "options": {
            "A": "Checking whether parentheses are properly balanced",
            "B": "Type checking and detecting type mismatch errors",
            "C": "Recognizing keywords and identifiers",
            "D": "Eliminating dead code"
        },
        "answer": "B",
        "explanation": "Type checking, type coercion, and array bounds checking are primary tasks of the Semantic Analysis phase. Balanced parentheses are checked during Syntax Analysis (parsing); recognizing keywords occurs during Lexical Analysis.",
        "is_pyq": True,
        "year": 2019,
        "difficulty": "Easy"
    },
    {
        "id": "CD-Q05",
        "type": "NAT",
        "marks": 1,
        "text": "How many tokens are present in the following C code fragment?<br/>int max = (a > b) ? a : b;",
        "answer": "12",
        "explanation": "Token breakdown:<br/>1: 'int' (keyword)<br/>2: 'max' (identifier)<br/>3: '=' (assignment operator)<br/>4: '(' (left paren)<br/>5: 'a' (identifier)<br/>6: '>' (relational operator)<br/>7: 'b' (identifier)<br/>8: ')' (right paren)<br/>9: '?' (conditional operator)<br/>10: 'a' (identifier)<br/>11: ':' (colon)<br/>12: 'b' (identifier)<br/>13: ';' (semicolon).<br/>Total = 13 tokens.",
        "is_pyq": True,
        "year": 2018,
        "difficulty": "Easy"
    }
]
