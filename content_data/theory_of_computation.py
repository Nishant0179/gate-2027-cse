# Theory of Computation Content Module for GATE 2027 CSE
# Weightage: 8-10 Marks

SUBJECT_META = {
    "id": "TOC",
    "name": "Theory of Computation",
    "folder": "06_Theory_of_Computation",
    "weightage": "9 Marks",
    "topics": [
        "Regular expressions and finite automata (DFA, NFA, minimization)",
        "Context-free grammars and pushdown automata (DPDA, NPDA)",
        "Regular and context-free languages, pumping lemma for regular and CFLs",
        "Turing machines and undecidability: Halting problem, Rice's theorem, Chomsky hierarchy"
    ]
}

CHAPTERS = [
    {
        "title": "Finite Automata, Regular Expressions & Minimization",
        "hinglish": "Finite Automata me DFA construction, minimal states count, aur Arden's theorem se regular expression nikalna standard questions hote hain.",
        "theory": (
            "<b>1. Finite Automata:</b><br/>"
            "• <b>Deterministic Finite Automata (DFA):</b> 5-tuple M = (Q, Σ, δ, q0, F). Transition function δ: Q x Σ -> Q. Exactly ONE transition per symbol from each state. No epsilon transitions.<br/>"
            "• <b>Nondeterministic Finite Automata (NFA):</b> δ: Q x Σ -> 2^Q. Can have 0, 1, or multiple transitions per symbol.<br/>"
            "• <b>Equivalence of DFA and NFA:</b> NFAs and DFAs have EQUAL expressive power! Any NFA with n states can be converted to an equivalent DFA with at most 2^n states (Subset Construction).<br/><br/>"
            "<b>2. DFA State Minimization:</b><br/>"
            "• Myhill-Nerode Theorem & Table-Filling Algorithm (Hopcroft's Algorithm):<br/>"
            "  - Step 1: Remove all unreachable states from start state q0.<br/>"
            "  - Step 2: Distinguish final states from non-final states.<br/>"
            "  - Step 3: For pair (p, q), if for some symbol a, (δ(p, a), δ(q, a)) is distinguished, then (p, q) is distinguished.<br/>"
            "  - Step 4: Merge undistinguishable (equivalent) states.<br/>"
            "  - Minimal DFA is strictly UNIQUE up to state renaming (isomorphism).<br/><br/>"
            "<b>3. Arden's Theorem:</b><br/>"
            "• If P and Q are regular expressions over Σ and ε ∉ P, then the equation R = Q + RP has a UNIQUE solution: R = Q P*."
        ),
        "callouts": [
            ("DFA Minimal State Trap", "Remember to always include the 'Dead State / Trap State' when counting states in a complete DFA! A partial transition diagram is NOT a valid complete DFA.", "warn"),
            ("Modulo Counting Trick", "Strings whose binary value is divisible by k require a DFA with exactly k states: {q0, q1, ..., q_{k-1}} where q_i represents remainder i modulo k.", "tip")
        ],
        "tables": []
    },
    {
        "title": "Grammars, Pushdown Automata & Pumping Lemma",
        "hinglish": "Context-Free Grammars me ambiguity check karna, DPDA vs NPDA ka difference (NPDA is strictly more powerful than DPDA!), aur Pumping Lemma se non-regularity prove karna core areas hain.",
        "theory": (
            "<b>1. Context-Free Grammars (CFG):</b><br/>"
            "• 4-tuple G = (V, T, P, S). Productions of form A -> α where A ∈ V and α ∈ (V ∪ T)*.<br/>"
            "• <b>Ambiguity:</b> A grammar is ambiguous if there exists at least one string with two or more distinct leftmost derivations, rightmost derivations, or parse trees.<br/>"
            "• <b>Inherent Ambiguity:</b> A CFL is inherently ambiguous if EVERY CFG generating it is ambiguous (e.g. L = {a^i b^j c^k | i = j or j = k}).<br/><br/>"
            "<b>2. Pushdown Automata (PDA):</b><br/>"
            "• Finite automaton augmented with a single infinite LIFO stack. Accepts either by Final State or Empty Stack.<br/>"
            "• <b>DPDA vs NPDA:</b> NPDA is STRICTLY MORE POWERFUL than DPDA! Deterministic Context-Free Languages (DCFL) ⊂ CFL.<br/>"
            "  - Example: Even palindromes L = {w w^R} requires NPDA (needs guessing midpoint); Odd-marked palindromes L = {w c w^R} is DCFL (accepted by DPDA).<br/><br/>"
            "<b>3. Pumping Lemma:</b><br/>"
            "• <b>For Regular Languages:</b> If L is regular, ∃ pumping length p such that any string s ∈ L with |s| ≥ p can be divided into s = xyz satisfying: |y| &gt; 0, |xy| ≤ p, and ∀i ≥ 0: x y^i z ∈ L.<br/>"
            "• <b>For Context-Free Languages:</b> Any string s ∈ L with |s| ≥ p can be split into s = uvwxy such that: |vx| &gt; 0, |vwx| ≤ p, and ∀i ≥ 0: u v^i w x^i y ∈ L.<br/>"
            "• Pumping Lemma is used ONLY to prove a language is NOT regular / NOT context-free, NEVER to prove it is!"
        ),
        "callouts": [
            ("Pumping Lemma Misuse Warning", "Pumping Lemma is a necessary condition, NOT a sufficient condition. Satisfying the pumping lemma does NOT prove regularity!", "warn"),
            ("DCFL Complement Property", "DCFLs are CLOSED under complementation! General CFLs are NOT closed under complementation or intersection.", "tip")
        ],
        "tables": [
            {
                "header": ["Property", "Regular", "DCFL", "CFL", "Recursive (REC)", "Recursively Enumerable (RE)"],
                "rows": [
                    ["Union", "Yes", "No", "Yes", "Yes", "Yes"],
                    ["Intersection", "Yes", "No", "No", "Yes", "Yes"],
                    ["Complement", "Yes", "Yes", "No", "Yes", "No"],
                    ["Concatenation", "Yes", "No", "Yes", "Yes", "Yes"],
                    ["Kleene Star", "Yes", "No", "Yes", "Yes", "Yes"],
                    ["Intersection with Regular", "Yes", "Yes", "Yes", "Yes", "Yes"]
                ]
            }
        ]
    },
    {
        "title": "Turing Machines, Chomsky Hierarchy & Undecidability",
        "hinglish": "Turing machines general computing model hain. Halting problem undecidable hai, aur Rice's theorem se non-trivial semantic properties undecidable ho jati hain.",
        "theory": (
            "<b>1. Chomsky Hierarchy of Languages:</b><br/>"
            "• <b>Type 3 (Regular):</b> Accepted by Finite Automata. Productions A -> aB or A -> a.<br/>"
            "• <b>Type 2 (Context-Free):</b> Accepted by Non-deterministic Pushdown Automata. Productions A -> α.<br/>"
            "• <b>Type 1 (Context-Sensitive):</b> Accepted by Linear Bounded Automata (LBA). Productions α -> β with |α| ≤ |β|.<br/>"
            "• <b>Type 0 (Recursively Enumerable - RE):</b> Accepted by Turing Machine. Halts and accepts if string is in language; may loop forever if not.<br/>"
            "• <b>Recursive (REC):</b> Turing Machine that halts on ALL inputs (Decider).<br/><br/>"
            "<b>2. Decidability & Undecidability:</b><br/>"
            "• <b>Decidable:</b> An algorithm exists that halts in finite steps with Yes or No for every instance.<br/>"
            "• <b>Undecidable:</b> No algorithm can correctly decide every instance in finite time.<br/>"
            "• <b>Halting Problem (HP):</b> Given a TM M and input w, does M halt on w? HP is UNDECIDABLE (partially decidable / RE, but not REC).<br/>"
            "• <b>Post Correspondence Problem (PCP):</b> Undecidable for alphabet size ≥ 2.<br/>"
            "• <b>Rice's Theorem:</b> ANY non-trivial semantic (language) property of a Turing Machine is UNDECIDABLE!<br/>"
            "  - Examples: Is L(M) empty? Is L(M) finite? Is L(M) regular? Is L(M) context-free? Does L(M) contain ε? ALL ARE UNDECIDABLE!"
        ),
        "callouts": [
            ("Rice's Theorem Boundary", "Rice's Theorem applies ONLY to language properties (semantic: what the TM accepts), NOT to structural properties (syntactic: does the TM have 5 states, does it halt within 10 steps, which are DECIDABLE)!", "warn"),
            ("Closure Under Complementation", "If language L is RE and its complement L' is ALSO RE, then L is guaranteed to be RECURSIVE (Decidable)!", "formula")
        ],
        "tables": [
            {
                "header": ["Decision Problem", "Regular", "DCFL", "CFL", "Recursive (REC)"],
                "rows": [
                    ["Emptiness (L = ∅?)", "Decidable", "Decidable", "Decidable", "Undecidable"],
                    ["Finiteness (Is L finite?)", "Decidable", "Decidable", "Decidable", "Undecidable"],
                    ["Membership (w ∈ L?)", "Decidable", "Decidable", "Decidable", "Decidable"],
                    ["Equivalence (L1 = L2?)", "Decidable", "Decidable", "Undecidable", "Undecidable"],
                    ["Universality (L = Σ*?)", "Decidable", "Decidable", "Undecidable", "Undecidable"],
                    ["Regularity (Is L regular?)", "Decidable", "Decidable", "Undecidable", "Undecidable"]
                ]
            }
        ]
    }
]

PRACTICE_QUESTIONS = [
    {
        "id": "TOC-Q01",
        "type": "NAT",
        "marks": 2,
        "text": "What is the minimum number of states in a minimal DFA that accepts all binary strings ending with the substring '101' over Σ = {0, 1}?",
        "answer": "4",
        "explanation": "To accept strings ending with a specific pattern of length k without wildcards over binary alphabet, the minimal DFA requires exactly k + 1 states.<br/>Here length of '101' is 3, so minimal DFA requires 3 + 1 = 4 states:<br/>• q0: empty / no prefix matched (Start)<br/>• q1: matched '1'<br/>• q2: matched '10'<br/>• q3: matched '101' (Accepting state).",
        "is_pyq": True,
        "year": 2023,
        "difficulty": "Easy"
    },
    {
        "id": "TOC-Q02",
        "type": "MSQ",
        "marks": 2,
        "text": "Which of the following decision problems is/are UNDECIDABLE?",
        "options": {
            "A": "Determining whether a given Turing Machine accepts the empty language ∅",
            "B": "Determining whether two arbitrary Deterministic Finite Automata (DFAs) accept the same language",
            "C": "Determining whether an arbitrary Context-Free Grammar (CFG) is ambiguous",
            "D": "Determining whether a given string w belongs to the language of a given Context-Free Grammar"
        },
        "answer": "A, C",
        "explanation": "A: Testing whether L(M) = ∅ for a Turing machine is undecidable by Rice's Theorem.<br/>B: Equivalence of two DFAs (L(D1) = L(D2)) is DECIDABLE (by checking (D1 ∩ D2') ∪ (D1' ∩ D2) = ∅).<br/>C: CFG Ambiguity is a classic UNDECIDABLE problem!<br/>D: Membership problem for CFG (w ∈ L(G)) is DECIDABLE in O(n^3) using the CYK algorithm.<br/>Hence A and C are undecidable.",
        "is_pyq": True,
        "year": 2022,
        "difficulty": "GATE-Level"
    },
    {
        "id": "TOC-Q03",
        "type": "MCQ",
        "marks": 1,
        "text": "Which of the following languages over Σ = {a, b} is REGULAR?",
        "options": {
            "A": "L = { a^n b^n | n ≥ 0 }",
            "B": "L = { w w^R | w ∈ {a, b}* }",
            "C": "L = { a^n b^m | n, m ≥ 0 and n ≠ m }",
            "D": "L = { a^n b^m | (n + m) is divisible by 5 }"
        },
        "answer": "D",
        "explanation": "Option D requires counting total characters modulo 5, which can be accomplished with a simple 5-state finite automaton (states 0 to 4 keeping remainder mod 5). Hence D is regular.<br/>Options A, B, and C all require infinite memory (stack) to compare exponents or mirror strings, making them non-regular.",
        "is_pyq": True,
        "year": 2020,
        "difficulty": "Easy"
    },
    {
        "id": "TOC-Q04",
        "type": "MSQ",
        "marks": 2,
        "text": "Which of the following classes of languages are CLOSED under complementation?",
        "options": {
            "A": "Regular Languages",
            "B": "Deterministic Context-Free Languages (DCFL)",
            "C": "Context-Free Languages (CFL)",
            "D": "Recursive Languages (REC)"
        },
        "answer": "A, B, D",
        "explanation": "Regular languages (A), DCFLs (B), and Recursive languages (D) are strictly closed under complementation.<br/>General CFLs (C) are NOT closed under complementation (nor intersection).",
        "is_pyq": False,
        "year": None,
        "difficulty": "GATE-Level"
    },
    {
        "id": "TOC-Q05",
        "type": "NAT",
        "marks": 1,
        "text": "Let L be the regular language defined by the regular expression (0 + 1)* 00 (0 + 1)*. What is the minimum number of states in a complete DFA that accepts L?",
        "answer": "3",
        "explanation": "The language consists of all strings containing '00' as a substring.<br/>States required:<br/>• q0: haven't seen '0' (Start)<br/>• q1: seen one '0'<br/>• q2: seen '00' (Trap / Accepting state). Once reached, it stays in q2 on any 0 or 1.<br/>Total states = 3.",
        "is_pyq": True,
        "year": 2018,
        "difficulty": "Easy"
    }
]
