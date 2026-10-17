# textbook_toc_cd_os.py
# In-depth Master Textbook Modules for Theory of Computation (TOC), Compiler Design (CD), and Operating Systems (OS)
# Follows the exact pedagogical and visual architecture of User Images 2 & 3.

CHAPTERS_TOC_CD_OS = {}

# =============================================================================
# THEORY OF COMPUTATION (TOC)
# =============================================================================

# TOC Chapter 0: Finite Automata & Regular Expressions
CHAPTERS_TOC_CD_OS[("TOC", 0)] = {
    "sub_id": "TOC",
    "chap_idx": 0,
    "title": "Finite Automata, Regular Expressions & Minimization",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The Vending Machine Snack Dispenser (DFA State Transitions)",
            "text": "A vending machine sells a soda for ₹20 and accepts ₹5 and ₹10 coins. The machine has no hard drive or infinite memory; it only has 4 internal electrical states: {State 0: ₹0 received, State 1: ₹5 received, State 2: ₹10 received, State 3: ₹15 received}. When it reaches State 4 (₹20), a mechanical solenoid drops the soda can (Accepting / Final State). Because the memory needed is strictly finite and bounded, this machine is the physical manifestation of a Deterministic Finite Automaton (DFA)."
        },
        {
            "title": "Real-Life Example 2: The Google Search Email Regex Validator (Regular Expressions)",
            "text": "When you sign up for a web service and type your email, the server runs a Regular Expression like `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}`. The browser compiles this regex into an NFA, converts it to an equivalent DFA, and feeds your keystrokes one by one. If your typing halts inside a final accepting state, the green checkmark lights up instantly in linear O(n) time."
        },
        {
            "title": "Real-Life Example 3: Merging Duplicate Room Keys (DFA State Minimization via Myhill-Nerode)",
            "text": "In a luxury hotel, Room 201 and Room 202 both offer identical king beds, identical Wi-Fi, and identical room service. For any guest request ('order dinner', 'request towels'), both rooms produce identical outcomes. Maintaining two separate hotel wings with identical functionality is wasteful. The Table-Filling (Myhill-Nerode) algorithm finds all pairs of equivalent states and merges them into a single super-state, creating the absolute smallest, canonical Minimal DFA."
        }
    ],
    "foundations": [
        {
            "number": "20.1",
            "title": "Deterministic (DFA) vs Non-Deterministic Finite Automata (NFA)",
            "content": (
                "A Finite Automaton is a 5-tuple M = (Q, Σ, δ, q0, F).<br/>"
                "• <b>DFA:</b> Transition function δ: Q × Σ → Q. For every state and every input symbol, exactly <b>ONE</b> deterministic transition exists.<br/>"
                "• <b>NFA:</b> Transition function δ: Q × (Σ ∪ {ε}) → 2^Q. Can branch into multiple states or consume null string ε.<br/>"
                "• <b>Equivalence Theorem (Subset Construction):</b> Every NFA can be converted to an equivalent DFA with at most <b>2^|Q| states</b>. DFA and NFA recognize the <b>EXACT SAME CLASS of languages (Regular Languages)</b>."
            ),
            "crucial_rule": "CRUCIAL RULE: While DFA and NFA have identical expressive power for finite strings, an NFA with n states converted to a minimal DFA can require up to 2^n states in the worst case (e.g., language 'n-th symbol from the end is 1')."
        },
        {
            "number": "20.2",
            "title": "Regular Expressions, Arden's Theorem & Identities",
            "content": (
                "• <b>Arden's Theorem:</b> If P and Q are regular expressions over Σ, and P does NOT contain ε, then the equation <b>R = Q + RP</b> has a UNIQUE solution: <b>R = Q P*</b>.<br/>"
                "• <b>Standard Regular Identities:</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• (a + b)* = (a* b*)* = (a* + b*)* = a*(b a*)*.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• (a*)* = a* | ε* = ε | ∅* = ε | a ∅ = ∅.<br/>"
                "• <b>Closure Properties of Regular Languages:</b> Closed under Union, Intersection, Complement, Concatenation, Kleene Star, Reversal, Homomorphism, and Inverse Homomorphism."
            ),
            "crucial_rule": "CRUCIAL RULE: Regular languages are closed under ALL standard Boolean operations! If L1 and L2 are regular, then L1 ∩ L2, ~L1, and L1 - L2 are GUARANTEED to be regular."
        },
        {
            "number": "20.3",
            "title": "Myhill-Nerode Theorem & DFA Minimization (Table-Filling Method)",
            "content": (
                "Two states p and q are distinguishable if there exists a string w ∈ Σ* such that δ(p, w) ∈ F and δ(q, w) ∉ F.<br/>"
                "• <b>Algorithm Steps:</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;1. Draw lower-triangular table for all state pairs (p, q).<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;2. Mark all pairs where one state is Final and the other is Non-Final (0-distinguishable).<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;3. For unmarked pairs (p, q), if for some symbol a ∈ Σ, (δ(p, a), δ(q, a)) is already marked, mark (p, q).<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;4. Repeat until no more marks are added. Unmarked pairs are equivalent and merged."
            ),
            "crucial_rule": "CRUCIAL RULE: The Minimal DFA for any regular language is UNIQUE up to state renaming (isomorphism). No two different minimal DFAs can exist for the same regular language!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: Minimum States for 'Divisible by 3 in Binary'",
            "problem": "Construct the minimal DFA that accepts all binary strings whose decimal value is divisible by 3. What is the minimum number of states required?",
            "steps": [
                "Step 1: Decimal value modulo 3 can only have 3 possible remainders: Remainder 0 (r0), Remainder 1 (r1), Remainder 2 (r2).",
                "Step 2: Transition logic: If current value is V, appending binary bit 'b' changes value to V' = 2V + b.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• New remainder = (2 × (V mod 3) + b) mod 3.",
                "Step 3: State transitions from r0 (V mod 3 = 0):<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• On input 0: (2×0 + 0) mod 3 = 0 ⇒ State r0.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• On input 1: (2×0 + 1) mod 3 = 1 ⇒ State r1.",
                "Step 4: From r1 (V mod 3 = 1):<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• On input 0: (2×1 + 0) mod 3 = 2 ⇒ State r2.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• On input 1: (2×1 + 1) mod 3 = 0 ⇒ State r0.",
                "Step 5: From r2 (V mod 3 = 2):<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• On input 0: (2×2 + 0) mod 3 = 1 ⇒ State r1.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• On input 1: (2×2 + 1) mod 3 = 2 ⇒ State r2.",
                "Step 6: Initial state = r0. Accepting state = r0 (remainder 0). None of the 3 states are equivalent."
            ],
            "answer": "Minimum number of states = 3."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: Dead State in Minimal DFA",
            "warning": "When counting states in a minimal DFA for GATE, DO NOT FORGET THE DEAD (TRAP) STATE! Example: strings ending with 'ab' requires 3 active states plus 1 trap state = 4 total states if transitions are fully specified."
        }
    ]
}

# TOC Chapter 1: Grammars, Pushdown Automata & Pumping Lemma
CHAPTERS_TOC_CD_OS[("TOC", 1)] = {
    "sub_id": "TOC",
    "chap_idx": 1,
    "title": "Grammars, Pushdown Automata & Pumping Lemma",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Parentheses Matching in a Code Editor (Pushdown Automaton)",
            "text": "When writing code like `if (((x + y) * (z - w)) > 0)`, the code editor highlights matching brackets. A Finite Automaton fails here because brackets can be nested 50 levels deep: you need infinite counter memory! A Pushdown Automaton (PDA) solves this using an internal Stack. Every time it sees an open '(', it pushes a token; every time it sees a closing ')', it pops a token. If the stack is empty at the end, parentheses match. This stack memory elevates the automaton to Context-Free Languages (CFL)."
        },
        {
            "title": "Real-Life Example 2: The Two-Balance Limit (Pumping Lemma for Regular vs CFL)",
            "text": "Imagine an old mechanical scale that can balance two pans (a^n b^n). A Pushdown Automaton can match 'a's and 'b's easily by pushing 'a' and popping for 'b'. But what if you ask it to match THREE things: a^n b^n c^n? The moment it pops all the 'a's to balance 'b's, its stack is empty: the memory is wiped out! It has no way to remember 'n' when counting 'c's. The Pumping Lemma proves mathematically that a^n b^n c^n is NOT context-free."
        },
        {
            "title": "Real-Life Example 3: The Ambiguous Legal Contract (Grammar Ambiguity)",
            "text": "Consider the sentence: 'I saw the man with a telescope'. Did I use a telescope to see the man, or did the man have a telescope in his hand? Two completely different parse trees exist for the exact same sentence. In programming languages, ambiguity like the 'Dangling Else' problem causes compiler nightmares. Grammars for programming languages must be strictly disambiguated."
        }
    ],
    "foundations": [
        {
            "number": "21.1",
            "title": "Chomsky Normal Form (CNF) & Derivation Steps",
            "content": (
                "A Context-Free Grammar is in CNF if all production rules are of the form:<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;<b>A → BC</b> (two non-terminals) or <b>A → a</b> (single terminal) [with S → ε allowed if S does not appear on RHS].<br/>"
                "• <b>Derivation Length Theorem:</b> To derive a string of length n (n ≥ 1) from a grammar in CNF, exactly <b>2n - 1 derivation steps</b> are required.<br/>"
                "• <b>Parse Tree Height:</b> A string of length n derived in CNF requires a parse tree with height at least <b>⌈log2(n)⌉ + 1</b>."
            ),
            "crucial_rule": "CRUCIAL RULE: In GATE, if a string w has length |w| = 10, deriving it from a CNF grammar ALWAYS requires exactly 2(10) - 1 = 19 production steps!"
        },
        {
            "number": "21.2",
            "title": "Deterministic PDA (DPDA) vs Non-Deterministic PDA (NPDA)",
            "content": (
                "• <b>DPDA:</b> At most one transition possible for any state, input, and stack top symbol.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Recognizes <b>Deterministic Context-Free Languages (DCFL)</b>. Strictly less powerful than NPDA!<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;DCFL is closed under <b>Complement</b>, but NOT closed under Union, Intersection, or Concatenation.<br/>"
                "• <b>NPDA:</b> Recognizes all <b>Context-Free Languages (CFL)</b>.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Example: Palindromes with center marker (w c w^R) is DCFL; even-length palindromes without marker (w w^R) requires guessing the midpoint, hence is <b>CFL but NOT DCFL</b>!"
            ),
            "crucial_rule": "CRUCIAL RULE: CFLs are NOT closed under Intersection or Complement! If L1 and L2 are CFL, L1 ∩ L2 might not be CFL (e.g. {a^n b^n c^m} ∩ {a^m b^n c^n} = {a^n b^n c^n})."
        },
        {
            "number": "21.3",
            "title": "Pumping Lemma for Regular Languages & CFLs",
            "content": (
                "• <b>Pumping Lemma for Regular Languages:</b> For any regular L, ∃ p such that any string w ∈ L with |w| ≥ p can be split into w = xyz such that:<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;1. |y| ≥ 1, 2. |xy| ≤ p, 3. xy^i z ∈ L for all i ≥ 0.<br/>"
                "• <b>Pumping Lemma for CFLs:</b> Any w ∈ L with |w| ≥ p can be split into w = uvxyz such that:<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;1. |vy| ≥ 1, 2. |vxy| ≤ p, 3. u v^i x y^i z ∈ L for all i ≥ 0.<br/>"
                "• Used strictly as an <b>adversarial game to prove a language is NOT regular or NOT context-free</b>."
            ),
            "crucial_rule": "CRUCIAL RULE: Pumping Lemma CANNOT be used to prove that a language IS regular! It is strictly a negative test (contrapositive proof tool)."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: Proving Non-Regularity via Pumping Lemma",
            "problem": "Use Pumping Lemma to prove that language L = { 0^n 1^n | n ≥ 0 } is not regular.",
            "steps": [
                "Step 1: Assume for contradiction that L is regular with pumping length p.",
                "Step 2: Choose string w = 0^p 1^p. Clearly w ∈ L and |w| = 2p ≥ p.",
                "Step 3: According to Pumping Lemma, w must decompose into w = xyz with |xy| ≤ p and |y| ≥ 1.",
                "Step 4: Since |xy| ≤ p, string y must consist entirely of 0s: y = 0^k where 1 ≤ k ≤ p.",
                "Step 5: Pump y with i = 2: w' = x y^2 z = 0^(p+k) 1^p.",
                "Step 6: In w', the number of 0s is p+k, while the number of 1s is p. Since k ≥ 1, p+k ≠ p, so w' ∉ L!",
                "Step 7: Contradiction reached. Therefore, L is NOT regular."
            ],
            "answer": "Proved: L = {0^n 1^n} is strictly Context-Free and Non-Regular."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: DCFL vs CFL Closure Misconceptions",
            "warning": "Remember: DCFL IS CLOSED under Complement, but CFL is NOT! GATE frequently tests: 'If L is CFL, is ~L guaranteed to be CFL?' The answer is NO."
        }
    ]
}

# TOC Chapter 2: Turing Machines & Undecidability
CHAPTERS_TOC_CD_OS[("TOC", 2)] = {
    "sub_id": "TOC",
    "chap_idx": 2,
    "title": "Turing Machines, Chomsky Hierarchy & Undecidability",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The Modern Laptop as a Universal Turing Machine",
            "text": "Before 1936, a 'calculator' was a machine built to do just one specific thing: an adding machine only added. Alan Turing realized that you don't need a million different machines: you build ONE machine that reads a description of ANY program from an infinite tape and simulates it. Your modern laptop, smartphone, or cloud server is a Universal Turing Machine (UTM): it runs an infinite variety of programs (Photoshop, Minecraft, Compilers) simply by swapping software inputs."
        },
        {
            "title": "Real-Life Example 2: The Infinite Antivirus Scanning Loop (The Halting Problem)",
            "text": "Imagine an antivirus company claiming: 'Our AI tool analyzes any program and guarantees with 100% accuracy whether it will ever freeze in an infinite loop!' Can such an antivirus exist? Turing proved it is mathematically IMPOSSIBLE. If you feed the antivirus a malicious program designed to 'Halt if the antivirus says it loops, and Loop if the antivirus says it halts', the antivirus is trapped in an inescapable logical paradox. The Halting Problem is Undecidable."
        },
        {
            "title": "Real-Life Example 3: The Russian Matryoshka Complexity Boxes (Chomsky Hierarchy)",
            "text": "Languages fit inside each other like nested Russian dolls: Regular Languages (inside Finite Automata) ⊂ DCFL ⊂ CFL (inside Pushdown Automata) ⊂ Context-Sensitive (inside Linear Bounded Automata) ⊂ Recursive (Decidable, halts on all inputs) ⊂ Recursively Enumerable (Turing Recognizable, might loop forever on invalid inputs)."
        }
    ],
    "foundations": [
        {
            "number": "22.1",
            "title": "Recursive (REC) vs Recursively Enumerable (RE) Languages",
            "content": (
                "• <b>Recursive Language (REC / Decidable):</b> Recognized by a Turing Machine that <b>HALTS on all inputs</b> (always says YES or NO in finite time).<br/>"
                "• <b>Recursively Enumerable Language (RE / Semi-decidable):</b> Recognized by a Turing Machine that halts and accepts if w ∈ L, but may <b>LOOP FOREVER</b> if w ∉ L.<br/>"
                "• <b>Fundamental Complement Theorem:</b> Language L is Recursive (Decidable) IF AND ONLY IF <b>both L and its complement ~L are Recursively Enumerable (RE)</b>."
            ),
            "crucial_rule": "CRUCIAL RULE: If L is RE but NOT Recursive, then its complement ~L CANNOT be RE (it is strictly Non-RE)!"
        },
        {
            "number": "22.2",
            "title": "Rice's Theorem for Language Properties of Turing Machines",
            "content": (
                "• <b>Rice's Theorem (Part 1):</b> Any <b>non-trivial semantic property</b> of the language recognized by a Turing Machine is <b>UNDECIDABLE</b>.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• <b>Semantic Property:</b> A property about the LANGUAGE recognized by the TM (e.g. 'Is L(M) empty?', 'Is L(M) regular?', 'Does L(M) contain string 101?').<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• <b>Non-trivial:</b> True for at least one TM language, and False for at least one TM language.<br/>"
                "• <b>Syntactic Properties (Not Rice's):</b> Properties of the TM's physical code (e.g. 'Does TM have 5 states?', 'Does TM take 10 steps on input w?'). These are <b>DECIDABLE</b>."
            ),
            "crucial_rule": "CRUCIAL RULE: If a GATE question asks whether a property of L(M) is decidable: if it depends on the language recognized by the TM and is non-trivial, it is ALWAYS UNDECIDABLE by Rice's Theorem!"
        },
        {
            "number": "22.3",
            "title": "Decidability Summary Table across Language Classes",
            "content": (
                "• <b>Regular Languages:</b> Membership (D), Emptiness (D), Finiteness (D), Equivalence (D), Disjointness (D) -> <b>ALL DECIDABLE</b>.<br/>"
                "• <b>CFL:</b> Membership (D via CYK algorithm), Emptiness (D), Finiteness (D). But Equivalence (L1=L2?), Ambiguity, and Universality (L=Σ*?) are <b>UNDECIDABLE</b>.<br/>"
                "• <b>Turing Machines (RE):</b> Halting Problem, Emptiness, Equivalence, Regularity -> <b>ALL UNDECIDABLE</b>.<br/>"
                "• <b>Post Correspondence Problem (PCP):</b> Undecidable in general; Decidable for alphabet size 1 or domino count 1 or 2."
            ),
            "crucial_rule": "CRUCIAL RULE: Emptiness is DECIDABLE for Regular and Context-Free languages, but UNDECIDABLE for Context-Sensitive and Recursively Enumerable languages."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: Decidability Classification",
            "problem": "Classify the following problems as Decidable or Undecidable:\nP1: Given a CFG G and string w, does w ∈ L(G)?\nP2: Given a CFG G, is L(G) = Σ*?\nP3: Given a Turing Machine M, does M halt on empty tape ε?",
            "steps": [
                "Step 1: Analyze P1: CFG membership problem. Can be decided in O(n³) time using CYK algorithm. Result: DECIDABLE.",
                "Step 2: Analyze P2: CFG universality problem (L(G) = Σ*). CFLs are not closed under complement; testing if complement is empty reduces to Halting problem. Result: UNDECIDABLE.",
                "Step 3: Analyze P3: Halting problem on blank tape for TM. Reduces directly to the general Halting Problem. Result: UNDECIDABLE."
            ],
            "answer": "P1 is Decidable; P2 and P3 are Undecidable."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: Confusing Membership with Equivalence in CFLs",
            "warning": "In CFLs, Membership (w ∈ L) is Decidable. But Equivalence (L1 = L2) is strictly Undecidable! Never confuse testing a single string with testing equality of two entire grammars."
        }
    ]
}

# =============================================================================
# COMPILER DESIGN (CD)
# =============================================================================

# CD Chapter 0: Lexical Analysis & Top-Down Parsing
CHAPTERS_TOC_CD_OS[("CD", 0)] = {
    "sub_id": "CD",
    "chap_idx": 0,
    "title": "Lexical Analysis & Top-Down Parsing (LL(1))",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The Fast-Reading English Proofreader (Lexical Analyzer Tokenizer)",
            "text": "When you read a book, your eyes don't process individual ink pixels or blank spaces one by one. Your brain chunks letters into recognized words: 'while' (Keyword), 'student_count' (Identifier), '<=' (Relational Operator), '50' (Number Literal). A Lexical Analyzer (Scanner) scans raw ASCII character streams using DFAs, tossing out useless whitespace and comments, and passing clean structured Tokens to the syntax parser."
        },
        {
            "title": "Real-Life Example 2: The 1-Lookahead Train Signal Switcher (LL(1) Parser)",
            "text": "An LL(1) parser is like a high-speed train engineer who approaches a track junction. They look at exactly ONE track signal ahead (1 token of lookahead). If the signal is green, they choose Track A; if amber, Track B. They never need to reverse the train (Zero Backtracking). But if two different tracks share the exact same starting signal (Non-deterministic Grammar), the train crashes. Left Factoring splits the shared track so 1 lookahead is always unambiguous."
        },
        {
            "title": "Real-Life Example 3: The Mirror Maze of Left Recursion",
            "text": "Imagine following a recipe rule: 'To bake a cake (A), first bake a cake (A), then add frosting (α)'. If you follow this top-down, you enter an infinite recursive loop without ever cracking an egg! This is Left Recursion (A → Aα). Top-down parsers get stuck in infinite recursion unless left recursion is eliminated into right recursion (A → βA', A' → αA' | ε)."
        }
    ],
    "foundations": [
        {
            "number": "23.1",
            "title": "Lexical Analysis: Token, Pattern, Lexeme & Lexical Errors",
            "content": (
                "• <b>Lexeme:</b> The actual concrete sequence of source code characters matching a pattern (e.g. `sum`, `3.1415`).<br/>"
                "• <b>Token:</b> Abstract category passed to parser: `<ID, pointer>`, `<NUM, 3.1415>`.<br/>"
                "• <b>Longest Match Rule (Maximal Munch):</b> Lexer always matches the longest possible valid prefix (e.g. `---` scanned as `--` followed by `-`).<br/>"
                "• <b>Keyword vs Identifier:</b> Keywords are entered into symbol table prior to scanning; reserved keywords cannot be used as variable identifiers."
            ),
            "crucial_rule": "CRUCIAL RULE: Lexical errors are detected ONLY when no regular expression pattern matches the remaining input (e.g. illegal character `@` in C). Transposed variable names or unmatched parentheses are NOT lexical errors!"
        },
        {
            "number": "23.2",
            "title": "FIRST and FOLLOW Sets Computation Rules",
            "content": (
                "• <b>FIRST(α):</b> The set of terminals that can appear as the first symbol of a string derived from α.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;1. If X is a terminal, FIRST(X) = {X}.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;2. If X → ε is a production, then ε ∈ FIRST(X).<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;3. If X → Y1 Y2 ... Yk, add FIRST(Y1) - {ε}. If Y1 can derive ε, add FIRST(Y2) - {ε}, etc.<br/>"
                "• <b>FOLLOW(A):</b> The set of terminals that can appear immediately to the right of non-terminal A in any sentential form.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;1. Add `$` (End-marker) to FOLLOW(S) where S is the start symbol.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;2. If production A → α B β exists, add (FIRST(β) - {ε}) to FOLLOW(B).<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;3. If production A → α B or A → α B β where ε ∈ FIRST(β), add ALL of FOLLOW(A) to FOLLOW(B)."
            ),
            "crucial_rule": "CRUCIAL RULE: FOLLOW sets NEVER CONTAIN ε! The empty string ε can be in FIRST sets, but it is strictly forbidden from FOLLOW sets."
        },
        {
            "number": "23.3",
            "title": "LL(1) Parsing Table Construction & Disambiguation",
            "content": (
                "An LL(1) table entry M[A, a] stores the production A → α if terminal a ∈ FIRST(α). If ε ∈ FIRST(α), store A → α for all b ∈ FOLLOW(A).<br/>"
                "• <b>LL(1) Condition:</b> A grammar is LL(1) iff for every production A → α | β:<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;1. FIRST(α) ∩ FIRST(β) = ∅.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;2. If ε ∈ FIRST(α), then FIRST(β) ∩ FOLLOW(A) = ∅.<br/>"
                "• <b>Disqualifiers for LL(1):</b> Ambiguous grammars, Left-recursive grammars, Non-left-factored grammars are <b>NEVER LL(1)</b>!"
            ),
            "crucial_rule": "CRUCIAL RULE: A grammar with multiple entries in ANY cell of its LL(1) parsing table is NOT LL(1). Multiple entries denote FIRST/FIRST or FIRST/FOLLOW conflicts."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: FIRST and FOLLOW Computation",
            "problem": "Given grammar: S → A B, A → a | ε, B → b | c. Compute FIRST and FOLLOW for all non-terminals.",
            "steps": [
                "Step 1: Compute FIRST(B): from B → b | c, FIRST(B) = {b, c}.",
                "Step 2: Compute FIRST(A): from A → a | ε, FIRST(A) = {a, ε}.",
                "Step 3: Compute FIRST(S): S → AB. FIRST(S) includes FIRST(A) - {ε} = {a}. Since ε ∈ FIRST(A), FIRST(S) also includes FIRST(B) = {b, c}. Thus FIRST(S) = {a, b, c}.",
                "Step 4: Compute FOLLOW(S): S is start symbol ⇒ FOLLOW(S) = {$}.",
                "Step 5: Compute FOLLOW(A): In S → AB, B follows A ⇒ FOLLOW(A) = FIRST(B) = {b, c}.",
                "Step 6: Compute FOLLOW(B): In S → AB, nothing follows B ⇒ FOLLOW(B) = FOLLOW(S) = {$}."
            ],
            "answer": "FIRST(S)={a,b,c}, FIRST(A)={a,ε}, FIRST(B)={b,c} | FOLLOW(S)={$}, FOLLOW(A)={b,c}, FOLLOW(B)={$}."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: Left Recursion Eliminator Order",
            "warning": "When eliminating left recursion from A → Aα | β, the result is A → βA', A' → αA' | ε. Notice that β must NOT begin with A. If β is absent, the language is empty!"
        }
    ]
}

# CD Chapter 1: Bottom-Up Parsing
CHAPTERS_TOC_CD_OS[("CD", 1)] = {
    "sub_id": "CD",
    "chap_idx": 1,
    "title": "Bottom-Up Parsing (LR Parsers) & Parser Comparisons",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Assembling a Lego Castle from the Ground Up (Shift-Reduce Parsing)",
            "text": "Top-down parsing tries to guess what the finished castle looks like from the roof down. Bottom-Up parsing starts with raw Lego bricks scattered on the carpet. You grab a brick from the box and place it on your work surface (Shift). When 4 red bricks form a stable square matching a blueprint sub-assembly, you snap them together into a 'Tower Base' (Reduce via grammar rule). You keep shifting and reducing until a single majestic completed Castle sits on the board (Accept)."
        },
        {
            "title": "Real-Life Example 2: The Two-Way Stare-Down at an Intersection (Shift-Reduce Conflict)",
            "text": "Imagine driving into an intersection where you don't know whether to drive forward across the street (Shift the next token) or brake and turn your wheel (Reduce the tokens you already passed). If the compiler's parsing table has BOTH actions in the same cell, the parser freezes in panic. The classic example is the 'Dangling Else': should an `else` attach to the inner `if` (Shift) or close the outer `if` (Reduce)?"
        },
        {
            "title": "Real-Life Example 3: The Four Generations of Night-Vision Goggles (LR Parser Hierarchy)",
            "text": "LR(0) is like parsing in pitch-black darkness: you reduce without looking at what's coming next. SLR(1) uses cheap flashlights: it only looks at the global FOLLOW set. LALR(1) uses smart infrared goggles: it tracks exact contextual lookaheads while cleverly merging identical core states, keeping memory tiny (Yacc and Bison use this). CLR(1) uses military-grade satellite radar: it never merges states, providing maximum parsing power at the cost of huge state tables."
        }
    ],
    "foundations": [
        {
            "number": "24.1",
            "title": "Shift-Reduce Conflicts, Reduce-Reduce Conflicts & Handles",
            "content": (
                "• <b>Handle:</b> A substring that matches the right-hand side of a production rule, and whose reduction represents one step in the reverse of a rightmost derivation.<br/>"
                "• <b>Shift-Reduce (S-R) Conflict:</b> Parser cannot decide whether to shift the next input symbol or reduce the current stack symbols.<br/>"
                "• <b>Reduce-Reduce (R-R) Conflict:</b> Parser has two different valid productions on top of stack and cannot decide which one to reduce.<br/>"
                "• <b>Handle Pruning:</b> Bottom-up parsing repeatedly locates the handle and reduces it until the start symbol is reached."
            ),
            "crucial_rule": "CRUCIAL RULE: Operator precedence and associativity declarations (e.g. `%left '+'`, `%left '*'`) resolve Shift-Reduce conflicts directly without rewriting ambiguous grammars!"
        },
        {
            "number": "24.2",
            "title": "LR Parser Family: LR(0), SLR(1), LALR(1), and CLR(1)",
            "content": (
                "• <b>LR(0):</b> Items have no lookahead: `A → α · β`. Reduces blindly on ALL input symbols in a state with complete item `A → α ·`.<br/>"
                "• <b>SLR(1):</b> Same states as LR(0). Reduces `A → α ·` ONLY for terminals in <b>FOLLOW(A)</b>.<br/>"
                "• <b>CLR(1) (Canonical LR):</b> Items include exact lookahead: `[A → α · β, a]`. Reduces ONLY on lookahead symbol `a`. Most powerful, but huge number of states.<br/>"
                "• <b>LALR(1):</b> Merges CLR(1) states that have <b>IDENTICAL LR(0) CORES</b> (differing only in lookaheads).<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;State count is <b>EXACTLY EQUAL to LR(0) state count</b>!"
            ),
            "crucial_rule": "CRUCIAL RULE: State Count Hierarchy: <b>State Count(LR(0)) = State Count(SLR(1)) = State Count(LALR(1)) < State Count(CLR(1))</b>."
        },
        {
            "number": "24.3",
            "title": "Conflict Creation During LALR(1) State Merging",
            "content": (
                "When merging CLR(1) states to form LALR(1):<br/>"
                "• <b>Shift-Reduce Conflicts:</b> CAN NEVER BE CREATED by merging! If the original CLR(1) grammar had no S-R conflicts, the merged LALR(1) will NEVER have an S-R conflict.<br/>"
                "• <b>Reduce-Reduce Conflicts:</b> <b>CAN BE CREATED</b> by merging states! Two different reductions with disjoint lookaheads in CLR(1) might collide in the merged state.<br/>"
                "• <b>Parsing Power Ordering:</b> <b>LL(1) < SLR(1) < LALR(1) < CLR(1)</b>."
            ),
            "crucial_rule": "CRUCIAL RULE: If a grammar is CLR(1), it is NOT necessarily LALR(1), because merging states with identical cores may introduce a Reduce-Reduce (R-R) conflict!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: LR(0) State Item Transitions",
            "problem": "Given augmented grammar: S' → S, S → C C, C → c C | d. Compute the items in initial state I0, and find transition on symbol 'c'.",
            "steps": [
                "Step 1: I0 starts with closure of [S' → · S].",
                "Step 2: Expand S: add [S → · C C].",
                "Step 3: Expand C: add [C → · c C] and [C → · d].",
                "Step 4: Initial state I0 contains: {[S' → · S], [S → · C C], [C → · c C], [C → · d]}.",
                "Step 5: Transition GOTO(I0, c): advance dot past 'c' in [C → · c C]:",
                "&nbsp;&nbsp;&nbsp;&nbsp;Kernel item = [C → c · C].",
                "&nbsp;&nbsp;&nbsp;&nbsp;Closure expands C: add [C → · c C] and [C → · d].",
                "&nbsp;&nbsp;&nbsp;&nbsp;Resulting state = {[C → c · C], [C → · c C], [C → · d]}."
            ],
            "answer": "GOTO(I0, c) produces the state {[C → c · C], [C → · c C], [C → · d]}."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: LALR vs SLR State Count",
            "warning": "Students often wrongly assume LALR has more states than SLR. In reality, LALR(1) and SLR(1) have the EXACT SAME NUMBER OF STATES, because LALR merges all states down to the LR(0) core!"
        }
    ]
}

# CD Chapter 2: SDT & Code Optimization
CHAPTERS_TOC_CD_OS[("CD", 2)] = {
    "sub_id": "CD",
    "chap_idx": 2,
    "title": "SDT, Intermediate Code & Optimization (Data Flow Analysis)",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The Factory Invoice Calculator (Syntax-Directed Translation)",
            "text": "When parsing a receipt like `Total = (5 * 20) + (2 * 50)`, parsing the grammar only tells us the structure. Syntax-Directed Translation (SDT) attaches mathematical actions to the grammar rules: 'When reducing `Expr -> Term * Factor`, multiply their dollar values; when reducing to `Total`, print the grand sum'. Synthesized attributes bubble up like prices from line items to the invoice total."
        },
        {
            "title": "Real-Life Example 2: The Redundant Commute Shortcut (Common Subexpression & Loop Optimization)",
            "text": "Suppose every morning you drive to the corner store to buy milk, drive home, and then drive to the exact same store to buy bread. A smart person combines both into one trip: buy milk AND bread together (Common Subexpression Elimination). And if your daily workout says: 'Do 100 pushups, and during each pushup calculate the square root of 999999', Code Motion (Loop Invariant Code Motion) computes that constant once outside before you start dropping to the floor."
        },
        {
            "title": "Real-Life Example 3: The Ghost Town Bulldozer (Dead Code Elimination & Liveness)",
            "text": "If a construction company builds a high-tech bridge in the desert that connects an abandoned quarry to nowhere (a variable `x = a + b` whose value is never read again before program exit), the variable is 'Dead'. Compiler Liveness Analysis detects that no future instruction reads `x`, and immediately bulldozes the calculation out of the final assembly binary."
        }
    ],
    "foundations": [
        {
            "number": "25.1",
            "title": "Syntax-Directed Translation (SDT): Synthesized vs Inherited Attributes",
            "content": (
                "• <b>Synthesized Attribute:</b> Computed from the attribute values of the node's <b>CHILDREN</b>. Can be evaluated during bottom-up parsing.<br/>"
                "• <b>Inherited Attribute:</b> Computed from the attribute values of the node's <b>PARENT and/or SIBLINGS</b>.<br/>"
                "• <b>S-Attributed SDT:</b> Uses <b>ONLY synthesized attributes</b>. Can be evaluated naturally during bottom-up LR parsing on a shift-reduce stack.<br/>"
                "• <b>L-Attributed SDT:</b> Attributes can be synthesized or inherited, but inherited attributes can depend ONLY on <b>parents and LEFT siblings</b> (never right siblings!)."
            ),
            "crucial_rule": "CRUCIAL RULE: Every S-attributed definition is strictly an L-attributed definition! (S-Attributed ⊂ L-Attributed). L-attributed SDTs can be evaluated in a single depth-first, left-to-right parse tree traversal."
        },
        {
            "number": "25.2",
            "title": "Three-Address Code (TAC): Quadruples, Triples & Indirect Triples",
            "content": (
                "Three-Address Code instructions have at most one operator on RHS: `x = y op z`.<br/>"
                "• <b>Quadruples:</b> 4 fields: `[op, arg1, arg2, result]`. Explicit temporary names stored in result field.<br/>"
                "• <b>Triples:</b> 3 fields: `[op, arg1, arg2]`. Results referenced by table position `(i)`. Avoids temporary variable names.<br/>"
                "• <b>Indirect Triples:</b> Uses an array of pointers to Triples. Reordering code for optimization requires reordering only the pointer array without moving large triple structures."
            ),
            "crucial_rule": "CRUCIAL RULE: In Triples, moving code during optimization is difficult because statements reference explicit row indices. Indirect triples solve this cleanly."
        },
        {
            "number": "25.3",
            "title": "GATE 2027 Data Flow Analysis: Liveness Analysis & Constant Propagation",
            "content": (
                "• <b>Basic Block:</b> A sequence of consecutive instructions with single entry (first instruction) and single exit (last instruction).<br/>"
                "• <b>Liveness Analysis:</b> A variable `v` is LIVE at point `p` if there is a path from `p` to a use of `v` along which `v` is not redefined.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;<b>Backward Data Flow:</b> IN[B] = USE[B] ∪ (OUT[B] - DEF[B]).<br/>"
                "• <b>Constant Propagation:</b> If a variable is assigned a known compile-time constant (`x = 5`), replace subsequent uses of `x` with `5`.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;<b>Forward Data Flow:</b> OUT[B] = GEN[B] ∪ (IN[B] - KILL[B])."
            ),
            "crucial_rule": "CRUCIAL RULE: Liveness Analysis is a BACKWARD MUST/MAY data flow problem! You start from the program exit and propagate backwards toward the entry."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: Computing Live Variables at Basic Block Boundaries",
            "problem": "Given Basic Block B:\n1: a = b + c\n2: d = a - e\n3: b = d * 2\nIf OUT[B] = {b, e}, find IN[B].",
            "steps": [
                "Step 1: Identify USE and DEF sets for Block B from bottom to top.",
                "Step 2: Line 3 (b = d * 2): def={b}, uses={d}.",
                "Step 3: Line 2 (d = a - e): def={d}, uses={a, e}.",
                "Step 4: Line 1 (a = b + c): def={a}, uses={b, c}.",
                "Step 5: Aggregated DEF[B] = {a, d, b}. Variables defined before use: 'a', 'd', 'b'.",
                "Step 6: Aggregated USE[B] = {b, c, e}. Note that 'b' is used in line 1 before being redefined in line 3!",
                "Step 7: Apply Liveness equation: IN[B] = USE[B] ∪ (OUT[B] - DEF[B]):<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;OUT[B] - DEF[B] = {b, e} - {a, d, b} = {e}.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;IN[B] = {b, c, e} ∪ {e} = {b, c, e}."
            ],
            "answer": "IN[B] = {b, c, e}."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: L-Attributed Evaluation Order in Embedded Actions",
            "warning": "In an SDT, action position matters! An action in the middle of a rule `A → B {action} C` executes AFTER B is parsed, but BEFORE C is parsed. It cannot read attributes of C!"
        }
    ]
}

# =============================================================================
# OPERATING SYSTEMS (OS)
# =============================================================================

# OS Chapter 0: Processes, Threads & Synchronization
CHAPTERS_TOC_CD_OS[("OS", 0)] = {
    "sub_id": "OS",
    "chap_idx": 0,
    "title": "Processes, Threads, Concurrency & Synchronization",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The Separate Bank Accounts vs Shared Kitchen (Process vs Thread)",
            "text": "Two independent bank customers have separate bank accounts, separate debit cards, and zero access to each other's funds. If one customer goes bankrupt, the other is completely unaffected (Processes: isolated Address Spaces, crash-proof, but sharing data requires formal wire transfers via IPC). Conversely, roommates in a shared apartment share the same refrigerator and kitchen counter (Threads: share code, data, open files). If roommate A puts milk in the fridge, B drinks it instantly (Fast shared memory), but if A burns down the kitchen, both die (Thread crash kills process)."
        },
        {
            "title": "Real-Life Example 2: The Single-Key Luxury Fitting Room (Binary Semaphore / Mutex)",
            "text": "At an upscale clothing boutique, there is one fitting room. A single physical brass key hangs by the door. Customer 1 takes the key and enters, locking the door (wait(S) / P(S): S decrements from 1 to 0). Customer 2 arrives, sees no key, and sits on the waiting bench (blocked). When Customer 1 leaves, they hang the key back (signal(S) / V(S): S increments to 1), waking Customer 2. Mutual Exclusion prevents two strangers from walking into the same room simultaneously."
        },
        {
            "title": "Real-Life Example 3: The Dining Philosophers Spaghetti Deadlock",
            "text": "Five philosophers sit around a round table with 5 bowls of spaghetti and 5 chopsticks (1 chopstick between each pair). To eat, a philosopher needs TWO chopsticks (left and right). If all 5 philosophers sit down at the exact same instant and simultaneously pick up their left chopstick with their left hand, every philosopher holds 1 chopstick and stares helplessly at their neighbor for the right chopstick. Nobody can eat, nobody drops their chopstick: Circular Wait freezes humanity forever (Deadlock)."
        }
    ],
    "foundations": [
        {
            "number": "26.1",
            "title": "Process States, PCB, Context Switching & Thread Models",
            "content": (
                "• <b>Process Control Block (PCB):</b> Contains PID, Program Counter, CPU registers, memory limits, list of open file descriptors.<br/>"
                "• <b>Process State Lifecycle:</b> New → Ready ↔ Running → Terminated (with Waiting/Blocked for I/O).<br/>"
                "• <b>Kernel-Level Threads (KLT) vs User-Level Threads (ULT):</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• ULT: Managed by user runtime library. Ultra-fast creation/switching (no kernel mode switch), but if one thread makes a blocking system call, the <b>ENTIRE PROCESS BLOCKS</b>.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• KLT: Managed directly by OS kernel. Multi-core parallelism supported; blocking thread does not freeze peers, but context switches incur kernel privilege mode overhead."
            ),
            "crucial_rule": "CRUCIAL RULE: Fork() in UNIX creates an exact clone child process. In parent, fork() returns child PID (> 0). In child, fork() returns 0. If fork fails, returns -1. Total processes created by n consecutive fork() calls = <b>2^n</b>."
        },
        {
            "number": "26.2",
            "title": "Critical Section Problem & The Three Mandatory Criteria",
            "content": (
                "To guarantee safe concurrent execution, any synchronization mechanism must satisfy:<br/>"
                "1. <b>Mutual Exclusion (Mandatory):</b> If process Pi is executing in its critical section, no other process can be executing in that critical section.<br/>"
                "2. <b>Progress (Mandatory):</b> Only processes that are NOT in their remainder section can participate in deciding who enters next, and this selection cannot be postponed indefinitely.<br/>"
                "3. <b>Bounded Waiting (Mandatory for Fairness):</b> There must be a bound on the number of times other processes are allowed to enter their critical sections after a process has requested entry (Prevents Starvation)."
            ),
            "crucial_rule": "CRUCIAL RULE: Strict Alternation (turn variable) satisfies Mutual Exclusion, but FAILS PROGRESS because if process P0 terminates or stays in remainder section, process P1 can NEVER enter its critical section again!"
        },
        {
            "number": "26.3",
            "title": "Counting Semaphores & Value Range Mechanics",
            "content": (
                "A Counting Semaphore S is an integer variable accessed via atomic operations:<br/>"
                "• `wait(S)` [or P(S)]: `S = S - 1; if (S < 0) block();`<br/>"
                "• `signal(S)` [or V(S)]: `S = S + 1; if (S <= 0) wakeup(process);`<br/>"
                "• <b>Physical Interpretation:</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;If S ≥ 0: S represents the number of <b>free available resources</b>.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;If S < 0: |S| represents the number of <b>processes currently waiting in the blocked queue</b>."
            ),
            "crucial_rule": "CRUCIAL RULE: If a semaphore is initialized to value 10, and then 12 wait() operations and 4 signal() operations are executed, current value = 10 - 12 + 4 = 2 (2 available resources, 0 processes waiting)."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: Tracing Counting Semaphore Operations",
            "problem": "A counting semaphore S is initialized to 7. A sequence of 20 P (wait) operations and 15 V (signal) operations are performed in arbitrary order. What is the final value of the semaphore, and how many processes are in the blocked queue?",
            "steps": [
                "Step 1: Net effect on semaphore variable S is: S_final = S_init - (Number of P operations) + (Number of V operations).",
                "Step 2: S_init = 7, P_ops = 20, V_ops = 15.",
                "Step 3: S_final = 7 - 20 + 15 = 7 - 5 = 2.",
                "Step 4: Analyze result: S_final = +2.",
                "Step 5: Since S_final ≥ 0, exactly 2 resources remain free, and NO processes are blocked."
            ],
            "answer": "Final semaphore value = 2; Number of blocked processes = 0."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: Counting Processes Created with fork() in Loops",
            "warning": "For `for(int i=0; i<3; i++) fork();`, total processes = 2^3 = 8 processes (1 original parent + 7 children). If asked 'How many CHILD processes are created?', the answer is 2^n - 1 = 7!"
        }
    ]
}

# OS Chapter 1: CPU Scheduling, I/O Scheduling & Deadlocks
CHAPTERS_TOC_CD_OS[("OS", 1)] = {
    "sub_id": "OS",
    "chap_idx": 1,
    "title": "CPU Scheduling, I/O Scheduling & Deadlocks",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The Express Supermarket Checkout (SJF Scheduling & Convoy Effect)",
            "text": "Imagine waiting in a supermarket queue behind someone with 3 overflowing shopping carts filled with 500 items (CPU burst: 60 minutes). You only want to buy one pack of chewing gum (CPU burst: 10 seconds). In First-Come-First-Served (FCFS), you wait an hour for your 10-second purchase (The Convoy Effect: average wait time skyrockets). Shortest Job First (SJF) sends the gum buyer through first, mathematically minimizing average waiting time for all shoppers."
        },
        {
            "title": "Real-Life Example 2: The Bank Cash Reserve Safety Check (Banker's Algorithm)",
            "text": "A bank has ₹100,000 cash in vault. Client A has a credit limit of ₹60,000, Client B has ₹50,000, Client C has ₹40,000. If the bank recklessly loans out all ₹100,000 right now, a sudden credit limit pull will cause a liquidity freeze (Deadlock). The Banker's Algorithm tests every loan before handing over cash: 'If I grant this loan, does there still exist at least one order where every customer can finish and return their cash?' If not, the loan is refused."
        },
        {
            "title": "Real-Life Example 3: The Skyscraper Elevator Algorithm (SCAN / Elevator Disk Scheduling)",
            "text": "An elevator in an 80-story skyscraper does not jump randomly from floor 2 to floor 75 to floor 4 to floor 70 (FCFS disk head thrashing). The elevator sweeps upwards continuously from floor 1 to 80, servicing every passenger along its path (SCAN / LOOK), then reverses and sweeps downwards. This prevents wild mechanical swings and minimizes disk head wear."
        }
    ],
    "foundations": [
        {
            "number": "27.1",
            "title": "CPU Scheduling Algorithms: FCFS, SJF, SRTF, Round Robin & Priority",
            "content": (
                "• <b>Turnaround Time (TAT):</b> TAT = Completion Time (CT) - Arrival Time (AT).<br/>"
                "• <b>Waiting Time (WT):</b> WT = Turnaround Time (TAT) - Burst Time (BT).<br/>"
                "• <b>Shortest Remaining Time First (SRTF):</b> Preemptive SJF. <b>PROVABLY OPTIMAL</b> for minimizing average waiting time, but causes starvation of long jobs.<br/>"
                "• <b>Round Robin (RR):</b> Time quantum q. Fair, interactive. If q is very large, RR degenerates to FCFS; if q is infinitesimally small, RR behaves as Processor Sharing with massive context switch overhead.<br/>"
                "• <b>Priority Inversion:</b> Lower priority process holds a lock needed by high priority process; solved via <b>Priority Inheritance Protocol</b>."
            ),
            "crucial_rule": "CRUCIAL RULE: In Round Robin scheduling, if a newly arriving process arrives at the EXACT SAME TIME that an executing process's quantum expires, the newly arrived process is placed into the ready queue BEFORE the expired process!"
        },
        {
            "number": "27.2",
            "title": "Deadlock Characterization & The 4 Coffman Conditions",
            "content": (
                "Deadlock occurs if and only if all 4 conditions hold simultaneously:<br/>"
                "1. <b>Mutual Exclusion:</b> Resources cannot be shared.<br/>"
                "2. <b>Hold and Wait:</b> Process holds at least 1 resource while requesting others.<br/>"
                "3. <b>No Preemption:</b> Resources cannot be forcibly taken from a process.<br/>"
                "4. <b>Circular Wait:</b> Circular chain P0 → P1 → ... → Pn → P0 exists.<br/>"
                "• <b>Deadlock Prevention:</b> Invalidate at least one Coffman condition (e.g. impose strict global ordering on resource requests to prevent Circular Wait).<br/>"
                "• <b>Deadlock Avoidance:</b> Banker's Algorithm. Safe state ⊂ Deadlock-free state."
            ),
            "crucial_rule": "CRUCIAL RULE: A cycle in a Resource Allocation Graph (RAG) is a SUFFICIENT condition for deadlock ONLY IF each resource type has strictly 1 single instance! If resources have multiple instances, a cycle DOES NOT guarantee deadlock."
        },
        {
            "number": "27.3",
            "title": "GATE 2027 I/O and Disk Scheduling Algorithms",
            "content": (
                "• <b>FCFS:</b> Requests serviced in arrival order. Zero starvation, but high seek time.<br/>"
                "• <b>SSTF (Shortest Seek Time First):</b> Services closest cylinder next. May cause starvation of distant tracks.<br/>"
                "• <b>SCAN (Elevator):</b> Moves in one direction servicing requests until it hits the end cylinder, then reverses.<br/>"
                "• <b>C-SCAN (Circular SCAN):</b> Moves in one direction servicing requests to the end, then immediately returns to cylinder 0 WITHOUT servicing requests on return trip (Provides uniform wait time).<br/>"
                "• <b>LOOK / C-LOOK:</b> Like SCAN/C-SCAN, but only goes as far as the last actual request in that direction (does not travel to empty end cylinders)."
            ),
            "crucial_rule": "CRUCIAL RULE: In LOOK and C-LOOK, the head reverses at the LAST REQUEST, NOT at the physical boundary (track 0 or track 199)!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: Banker's Algorithm Safe Sequence Verification",
            "problem": "5 processes (P0-P4) and 3 resource types A, B, C with total instances (10, 5, 7). Current Allocations: P0(0,1,0), P1(2,0,0), P2(3,0,2), P3(2,1,1), P4(0,0,2). Max claims: P0(7,5,3), P1(3,2,2), P2(9,0,2), P3(2,2,2), P4(4,3,3). Is system in safe state? Find a safe sequence.",
            "steps": [
                "Step 1: Compute Total Allocated: A = 0+2+3+2+0 = 7; B = 1+0+0+1+0 = 2; C = 0+0+2+1+2 = 5.",
                "Step 2: Available = Total - Allocated = (10-7, 5-2, 7-5) = (3, 3, 2).",
                "Step 3: Compute Need Matrix (Max - Allocation):<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Need(P0) = (7, 4, 3) | Need(P1) = (1, 2, 2)<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Need(P2) = (6, 0, 0) | Need(P3) = (0, 1, 1)<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Need(P4) = (4, 3, 1).",
                "Step 4: Test Available (3, 3, 2):<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• P1 needs (1,2,2) ≤ (3,3,2) ✔ ⇒ P1 finishes. New Avail = (3,3,2) + (2,0,0) = (5, 3, 2).<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• P3 needs (0,1,1) ≤ (5,3,2) ✔ ⇒ P3 finishes. New Avail = (5,3,2) + (2,1,1) = (7, 4, 3).<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• P4 needs (4,3,1) ≤ (7,4,3) ✔ ⇒ P4 finishes. New Avail = (7,4,3) + (0,0,2) = (7, 4, 5).<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• P0 needs (7,4,3) ≤ (7,4,5) ✔ ⇒ P0 finishes. New Avail = (7,4,5) + (0,1,0) = (7, 5, 5).<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• P2 needs (6,0,0) ≤ (7,5,5) ✔ ⇒ P2 finishes. All finished!"
            ],
            "answer": "Safe Sequence exists: <P1, P3, P4, P0, P2>. System is in a SAFE STATE."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: Non-Preemptive SJF Arrival Tie",
            "warning": "In Non-Preemptive SJF, if a process starts executing, it CANNOT be interrupted even if a brand new process arrives with a tiny burst time of 1 unit! Only SRTF preempts."
        }
    ]
}

# OS Chapter 2: Memory Management & Virtual Memory
CHAPTERS_TOC_CD_OS[("OS", 2)] = {
    "sub_id": "OS",
    "chap_idx": 2,
    "title": "Memory Management, Virtual Memory & File Systems",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The Library Card Catalog vs Missing Book Desk (Paging & Page Fault)",
            "text": "A university library has 1,000,000 books, but reading desks can only fit 10 books at a time. The Card Catalog tells you exactly which desk holds which chapter (Page Table). If you need Chapter 4 and it is already on Desk 3, you read it in 1 second (Page Hit). But if Chapter 4 is locked in the dark basement archive, you trigger an alarm: reading stops, a librarian rides the slow elevator to the basement, retrieves the book, and puts it on a desk (Page Fault: takes 10 milliseconds = 10,000,000 nanoseconds!)."
        },
        {
            "title": "Real-Life Example 2: The Belady's Anomaly Parking Garage Paradox",
            "text": "Normally, adding more capacity makes systems faster: building a bigger parking garage should reduce parking hassles. But in 1969, Laszlo Belady discovered that under FIFO page replacement, increasing physical memory frames from 3 frames to 4 frames actually CAUSED MORE PAGE FAULTS for certain reference strings! FIFO kicks out old pages blindly without caring if they will be needed immediately in the next microsecond."
        },
        {
            "title": "Real-Life Example 3: The Highway Pothole Patching (Internal vs External Fragmentation)",
            "text": "In Fixed Partitioning, a car gets an entire 40-foot semi-truck bay: the leftover 25 feet inside the bay is completely wasted and cannot be used by anyone else (Internal Fragmentation). In Dynamic Partitioning, bays shrink to car size, but as cars come and go, tiny 3-foot gaps open up between parked cars: total free space might be 60 feet, but no single gap fits a new car (External Fragmentation: solved by Paging)."
        }
    ],
    "foundations": [
        {
            "number": "28.1",
            "title": "Paging, Address Translation & TLB Hit Rate",
            "content": (
                "• <b>Virtual Address Split:</b> `[ Page Number (p) | Page Offset (d) ]`. Page size = 2^d bytes.<br/>"
                "• <b>Physical Address Split:</b> `[ Frame Number (f) | Frame Offset (d) ]`. Frame size = Page size.<br/>"
                "• <b>Page Table Size:</b> `(Number of Pages) × (Page Table Entry Size)` = `(2^p) × e` bytes.<br/>"
                "• <b>Effective Memory Access Time (EMAT) with TLB:</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;<b>EMAT = h × (t_tlb + t_m) + (1 - h) × (t_tlb + 2 × t_m)</b> (for single-level paging).<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;If multi-level paging with k levels: Miss penalty accesses memory k times: `t_tlb + (k + 1) × t_m`."
            ),
            "crucial_rule": "CRUCIAL RULE: In EMAT calculations, ALWAYS check whether TLB search and main memory access happen in PARALLEL or SEQUENTIALLY. If sequential: TLB miss takes t_tlb + 2·t_m; if parallel: (1-h)·(2·t_m)."
        },
        {
            "number": "28.2",
            "title": "Page Replacement Algorithms: FIFO, Optimal & LRU",
            "content": (
                "• <b>FIFO (First-In First-Out):</b> Replaces oldest page. Suffers from <b>Belady's Anomaly</b>.<br/>"
                "• <b>Optimal (Bélády's MIN):</b> Replaces page that will NOT be used for the longest period of time in future. Provably minimum page faults, but impossible to implement in practice.<br/>"
                "• <b>LRU (Least Recently Used):</b> Replaces page that has not been used for longest period in PAST. Approximation of Optimal. Stack algorithm: <b>IMMUNE TO BELADY'S ANOMALY</b>.<br/>"
                "• <b>Second-Chance (Clock) Algorithm:</b> Uses reference bit (0 or 1) to approximate LRU with FIFO overhead."
            ),
            "crucial_rule": "CRUCIAL RULE: Stack Algorithms (such as LRU and Optimal) can NEVER exhibit Belady's Anomaly because the set of pages in memory for n frames is always a strict subset of the pages for n+1 frames."
        },
        {
            "number": "28.3",
            "title": "UNIX Inode File System Architecture",
            "content": (
                "A standard UNIX Inode has 15 pointer blocks:<br/>"
                "• 12 Direct block pointers (point directly to data disk blocks).<br/>"
                "• 1 Singly Indirect pointer (points to block of disk addresses).<br/>"
                "• 1 Doubly Indirect pointer (points to block of singly indirect blocks).<br/>"
                "• 1 Triply Indirect pointer.<br/>"
                "• Maximum file size = `[ 12 + (B/D) + (B/D)² + (B/D)³ ] × BlockSize` (where B = Block Size, D = Disk Address Size)."
            ),
            "crucial_rule": "CRUCIAL RULE: Direct pointers provide O(1) access time for small files. Large files dynamically scale without file fragmentation using indirect pointers."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: Inode Maximum File Size Calculation",
            "problem": "An Inode-based file system has 1 KB block size and 4-byte disk addresses. The Inode has 8 direct pointers, 1 singly indirect, and 1 doubly indirect pointer. Calculate the maximum file size supported.",
            "steps": [
                "Step 1: Pointers per block = Block Size / Disk Address Size = 1 KB / 4 B = 1024 / 4 = 256 pointers.",
                "Step 2: Capacity from 8 Direct pointers = 8 × 1 KB = 8 KB.",
                "Step 3: Capacity from 1 Singly Indirect pointer = 256 × 1 KB = 256 KB.",
                "Step 4: Capacity from 1 Doubly Indirect pointer = 256 × 256 × 1 KB = 65,536 KB = 64 MB.",
                "Step 5: Total Maximum File Size = 8 KB + 256 KB + 65,536 KB = 65,800 KB ≈ 64.26 MB."
            ],
            "answer": "Maximum File Size = 65,800 KB (64.26 MB)."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: Forgetting Page Fault Service Time Unit Conversion",
            "warning": "Memory access time is in nanoseconds (e.g. 100 ns), but Page Fault Service Time is in MILLISECONDS (e.g. 8 ms = 8,000,000 ns!). Forgetting to convert units destroys EMAT calculation completely."
        }
    ]
}
