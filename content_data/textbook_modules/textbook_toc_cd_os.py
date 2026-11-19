# textbook_toc_cd_os.py
# Simple English, point-by-point study notes for TOC, Compiler Design, and Operating Systems.
# Written in crystal-clear, student-friendly language for GATE 2027 CSE aspirants.

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
            "title": "Real-Life Example 1: The Soda Vending Machine (Finite Automaton)",
            "text": (
                "A can of soda costs ₹20. The machine accepts ₹5 and ₹10 coins.\n"
                "The machine does not have an infinite hard drive. It only needs to remember 4 simple states: {₹0, ₹5, ₹10, ₹15}.\n"
                "When you insert coins and reach state ₹20, the can drops (Final / Accepting State!).\n"
                "Because the machine needs only a small, fixed number of states, it is a Deterministic Finite Automaton (DFA)."
            )
        },
        {
            "title": "Real-Life Example 2: Email Format Validator (Regular Expressions)",
            "text": (
                "When you register on an app, a Regular Expression checks whether your text has letters, an '@' symbol, and a domain like '.com'.\n"
                "Your web browser compiles that regex into a tiny DFA and tests each character in microseconds. If it ends in an accepting state, a green checkmark appears."
            )
        }
    ],
    "foundations": [
        {
            "number": "20.1",
            "title": "DFA vs NFA Equivalences",
            "content": (
                "• <b>DFA (Deterministic Finite Automaton):</b><br/>"
                "&nbsp;&nbsp;- For every state and input symbol, there is <b>EXACTLY ONE</b> next state.<br/>"
                "&nbsp;&nbsp;- No ε-moves (cannot change state without reading input).<br/><br/>"
                "• <b>NFA (Non-Deterministic Finite Automaton):</b><br/>"
                "&nbsp;&nbsp;- Can have 0, 1, or multiple transitions on the same input symbol, plus optional ε-transitions.<br/><br/>"
                "• <b>Equivalent Power:</b><br/>"
                "&nbsp;&nbsp;- <b>DFA and NFA have the EXACT SAME expressive power!</b> Both recognize the exact set of Regular Languages.<br/>"
                "&nbsp;&nbsp;- Any NFA with n states can be converted into an equivalent DFA with at most <b>2^n states</b>."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: For the language 'all binary strings where the n-th symbol from the right is 1': The NFA needs only (n + 1) states, but the minimal DFA strictly requires 2^n states!"
        },
        {
            "number": "20.2",
            "title": "Regular Language Closure Properties",
            "content": (
                "Regular languages are closed under <b>ALMOST EVERY standard operation</b>:<br/><br/>"
                "• Union (L1 ∪ L2): <b>Closed ✔</b><br/>"
                "• Intersection (L1 ∩ L2): <b>Closed ✔</b><br/>"
                "• Complement (~L): <b>Closed ✔</b><br/>"
                "• Concatenation (L1 · L2): <b>Closed ✔</b><br/>"
                "• Kleene Star (L*): <b>Closed ✔</b><br/>"
                "• Reversal (L^R): <b>Closed ✔</b><br/>"
                "• Homomorphism & Substitution: <b>Closed ✔</b>"
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: To find the complement of a DFA: (1) Make sure the DFA is complete with all dead/trap states included, then (2) Swap Final states and Non-final states!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Arden's Theorem",
            "problem": "Solve the regular expression equation: R = b + R a.",
            "steps": [
                "Step 1: State Arden's Theorem: If P and Q are regular expressions, and P does not contain ε, then the equation R = Q + R P has a UNIQUE solution: R = Q P*.",
                "Step 2: Compare R = b + R a with R = Q + R P.",
                "Step 3: Identify terms: Q = b, and P = a (since P = a does not contain ε, Arden's rule applies).",
                "Step 4: Write unique solution: R = Q P* = b a*."
            ],
            "answer": "Solution: R = b a*."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Pumping Lemma",
            "warning": "Pumping Lemma is used ONLY to prove a language is NOT regular. You can NEVER use Pumping Lemma to prove a language IS regular!"
        }
    ]
}

# TOC Chapter 1: CFG, PDA & CFLs
CHAPTERS_TOC_CD_OS[("TOC", 1)] = {
    "sub_id": "TOC",
    "chap_idx": 1,
    "title": "Context-Free Grammars, Pushdown Automata & Chomsky Hierarchy",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Matching Parentheses in VS Code (Pushdown Automaton)",
            "text": (
                "When you write code with nested brackets `(( { [ ] } ))`, how does your code editor know that every opening bracket has a matching closing bracket?\n"
                "A finite automaton cannot do this because it cannot count to infinity! It needs an auxiliary Stack memory.\n"
                "Push each opening bracket onto the stack; when a closing bracket arrives, pop and verify. This is a Pushdown Automaton (PDA)."
            )
        }
    ],
    "foundations": [
        {
            "number": "21.1",
            "title": "Deterministic PDA vs Non-Deterministic PDA",
            "content": (
                "• <b>DPDA (Deterministic Pushdown Automata):</b><br/>"
                "&nbsp;&nbsp;- Recognizes <b>Deterministic Context-Free Languages (DCFL)</b>.<br/>"
                "&nbsp;&nbsp;- DCFLs are unambiguous and parsed efficiently in linear time by compilers.<br/>"
                "&nbsp;&nbsp;- Example: <code>{ a^n b^n | n >= 1 }</code>, balanced parentheses, programming languages.<br/><br/>"
                "• <b>NPDA (Non-Deterministic Pushdown Automata):</b><br/>"
                "&nbsp;&nbsp;- Recognizes <b>ALL Context-Free Languages (CFL)</b>.<br/>"
                "&nbsp;&nbsp;- <b>NPDA is strictly more powerful than DPDA!</b> (Unlike finite automata where NFA == DFA).<br/>"
                "&nbsp;&nbsp;- Example of CFL that is NOT DCFL: Even palindromes <code>{ w w^R }</code> (because you don't know where the middle is without guessing!)."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: DPDA is NOT equivalent to NPDA! DCFL is a strict proper subset of CFL: Regular ⊂ DCFL ⊂ CFL ⊂ CSL ⊂ Recursive ⊂ RE."
        },
        {
            "number": "21.2",
            "title": "CFL Closure Properties (The Famous Exceptions!)",
            "content": (
                "Context-Free Languages are closed under Union, Concatenation, and Kleene Star.<br/><br/>"
                "<b>The Two Famous Non-Closure Exceptions:</b><br/>"
                "• <b>Intersection: NOT CLOSED ✘</b> (The intersection of two CFLs is not necessarily context-free!).<br/>"
                "&nbsp;&nbsp;- Example: L1 = { a^n b^n c^m } (CFL) ∩ L2 = { a^m b^n c^n } (CFL) = { a^n b^n c^n } (CSL, NOT CFL!).<br/><br/>"
                "• <b>Complement: NOT CLOSED ✘</b> (If CFL were closed under complement, by De Morgan's laws it would be closed under intersection)."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: While CFL is not closed under intersection with another CFL, the intersection of a CFL with a REGULAR language is ALWAYS a CFL!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Language Classification",
            "problem": "Classify the language L = { a^n b^m c^k | n = m or m = k }.",
            "steps": [
                "Step 1: Notice the condition: n = m OR m = k.",
                "Step 2: L can be split into L1 ∪ L2, where L1 = { a^n b^n c^k } (CFL) and L2 = { a^n b^m c^m } (CFL).",
                "Step 3: Because CFLs are closed under Union, L = L1 ∪ L2 is guaranteed to be a Context-Free Language (CFL).",
                "Step 4: However, because it is an inherently ambiguous union, it cannot be recognized deterministically without guessing whether to match a's with b's or b's with c's."
            ],
            "answer": "L is a Context-Free Language (CFL), but NOT a Deterministic CFL (DCFL)."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: DCFL Complement",
            "warning": "While general CFLs are NOT closed under complement, Deterministic CFLs (DCFL) ARE closed under complement!"
        }
    ]
}

# TOC Chapter 2: Turing Machines & Decidability
CHAPTERS_TOC_CD_OS[("TOC", 2)] = {
    "sub_id": "TOC",
    "chap_idx": 2,
    "title": "Turing Machines, Decidability & Rice's Theorem",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The Infinite Loop Detector (The Halting Problem)",
            "text": (
                "Can you write a master antivirus or debugging tool that takes any C program as input and tells you with 100% certainty: 'Will this program ever finish, or will it loop forever?'\n"
                "Alan Turing proved that such a program is mathematically impossible! If it existed, you could feed it a paradoxical program that halts if and only if the checker says it loops, creating an unresolvable contradiction."
            )
        }
    ],
    "foundations": [
        {
            "number": "22.1",
            "title": "Recursive vs Recursively Enumerable Languages",
            "content": (
                "• <b>Recursive Language (Decidable):</b><br/>"
                "&nbsp;&nbsp;- A Turing Machine exists that halts on ALL inputs (halts and says YES if string is in language; halts and says NO if string is not).<br/>"
                "&nbsp;&nbsp;- <b>Closed under complement</b>: If L is Recursive, ~L is also Recursive.<br/><br/>"
                "• <b>Recursively Enumerable Language - RE (Semi-Decidable):</b><br/>"
                "&nbsp;&nbsp;- If string is in L, Turing Machine halts and says YES.<br/>"
                "&nbsp;&nbsp;- If string is NOT in L, Turing Machine may say NO, or <b>loop forever</b>!<br/>"
                "&nbsp;&nbsp;- If both L and ~L are RE, then L is strictly <b>Recursive</b>!"
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: Halting Problem of Turing Machine (HP) is Recursively Enumerable (RE) but UNDECIDABLE. The complement of the Halting Problem is NOT even Recursively Enumerable!"
        },
        {
            "number": "22.2",
            "title": "Rice's Theorem for Turing Machines",
            "content": (
                "<b>Rice's Theorem states:</b><br/>"
                "Any non-trivial semantic property of the language recognized by a Turing Machine is <b>UNDECIDABLE</b>.<br/><br/>"
                "• <b>What is a Semantic Property?</b><br/>"
                "&nbsp;&nbsp;A property about the language L(M) that the machine recognizes (e.g. 'Is L(M) empty?', 'Is L(M) regular?', 'Does L(M) contain palindrome?').<br/><br/>"
                "• <b>What does Non-trivial mean?</b><br/>"
                "&nbsp;&nbsp;Some Turing machines have this property, and some do not."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: If a question asks 'Is the language of Turing Machine M regular/finite/empty/CFL?', the answer is instantly UNDECIDABLE by Rice's Theorem!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Decidability Verification",
            "problem": "Which of the following is decidable? (A) Emptiness of DFA, (B) Emptiness of TM, (C) Equivalence of CFG, (D) Ambiguity of CFG.",
            "steps": [
                "Step 1: Check (A) Emptiness of DFA: Solved by checking graph reachability from start state to any final state using BFS in O(V + E) time ⇒ DECIDABLE!",
                "Step 2: Check (B) Emptiness of TM: Undecidable by Rice's Theorem.",
                "Step 3: Check (C) Equivalence of CFG: Undecidable (cannot check if L(G1) == L(G2)).",
                "Step 4: Check (D) Ambiguity of CFG: Undecidable by reduction from PCP."
            ],
            "answer": "Only (A) Emptiness of DFA is Decidable."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Membership in CFG",
            "warning": "Membership in CFG ('Does string w belong to CFG G?') IS DECIDABLE! It can be verified in O(n^3) time using the CYK algorithm."
        }
    ]
}

# =============================================================================
# COMPILER DESIGN (CD)
# =============================================================================

# CD Chapter 0: Lexical Analysis & First/Follow
CHAPTERS_TOC_CD_OS[("CD", 0)] = {
    "sub_id": "CD",
    "chap_idx": 0,
    "title": "Lexical Analysis, FIRST & FOLLOW Sets",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Reading Sentences vs Grammar Checking (Lexer vs Parser)",
            "text": (
                "When reading an English sentence:\n"
                "• Lexical Analyzer (Scanner): Groups individual letters into words (Tokens): [Noun, Verb, Adjective]. Whitespaces are discarded.\n"
                "• Syntax Analyzer (Parser): Checks whether the sequence of words follows grammatical rules (Sentence = Subject + Verb + Object)."
            )
        }
    ],
    "foundations": [
        {
            "number": "23.1",
            "title": "Rules for Calculating FIRST Sets",
            "content": (
                "For any grammar symbol X:<br/>"
                "• 1. If X is a terminal, <code>FIRST(X) = { X }</code>.<br/>"
                "• 2. If X → ε is a production, add <code>ε</code> to <code>FIRST(X)</code>.<br/>"
                "• 3. If X is non-terminal and X → Y1 Y2 Y3...:<br/>"
                "&nbsp;&nbsp;- Add all terminals from <code>FIRST(Y1)</code> (except ε) to <code>FIRST(X)</code>.<br/>"
                "&nbsp;&nbsp;- If Y1 can produce ε, add <code>FIRST(Y2)</code> as well, continuing until a symbol does NOT produce ε.<br/>"
                "&nbsp;&nbsp;- If all Y1, Y2... produce ε, add <code>ε</code> to <code>FIRST(X)</code>."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: ε can appear in a FIRST set, but ε NEVER appears in a FOLLOW set!"
        },
        {
            "number": "23.2",
            "title": "Rules for Calculating FOLLOW Sets",
            "content": (
                "For non-terminal A:<br/>"
                "• 1. If A is the Start Symbol, add <b>$ (end-marker)</b> to <code>FOLLOW(A)</code>.<br/>"
                "• 2. If there is a production <code>B → α A β</code>:<br/>"
                "&nbsp;&nbsp;- Everything in <code>FIRST(β)</code> (except ε) goes into <code>FOLLOW(A)</code>.<br/>"
                "• 3. If there is a production <code>B → α A</code>, or <code>B → α A β</code> where <code>FIRST(β)</code> contains ε:<br/>"
                "&nbsp;&nbsp;- Everything in <code>FOLLOW(B)</code> goes into <code>FOLLOW(A)</code>."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: In FOLLOW set calculations, look strictly at the RIGHT-HAND SIDE of productions to see what symbols immediately follow non-terminal A!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Computing FIRST and FOLLOW",
            "problem": "Given grammar: S → A a, A → b | ε. Compute FIRST(S) and FOLLOW(A).",
            "steps": [
                "Step 1: FIRST(A) = { b, ε }.",
                "Step 2: FIRST(S): S → A a. FIRST(A) has 'b', and because A produces ε, 'a' follows ⇒ FIRST(S) = { b, a }.",
                "Step 3: FOLLOW(A): Look where A appears on RHS: S → A a. What follows A? Terminal 'a'.",
                "Step 4: Therefore, FOLLOW(A) = { a }."
            ],
            "answer": "FIRST(S) = { a, b }, FOLLOW(A) = { a }."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Longest Prefix Match (Maximal Munch)",
            "warning": "If the input code is 'int_var', the lexer does NOT match 'int' as a keyword and '_var' as identifier! It reads the longest valid token: 'int_var' as a single identifier."
        }
    ]
}

# CD Chapter 1: Parsing
CHAPTERS_TOC_CD_OS[("CD", 1)] = {
    "sub_id": "CD",
    "chap_idx": 1,
    "title": "Top-Down (LL(1)) & Bottom-Up (LR) Parsing",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Lookahead at an Intersection (LL(1) Parser)",
            "text": (
                "When driving toward a fork in the road, an LL(1) parser looks exactly 1 token ahead into the future to decide which branch of grammar to take.\n"
                "If two different grammar rules start with the same token, the parser crashes with a conflict! That's why LL(1) grammars must be left-factored and cannot contain left recursion."
            )
        }
    ],
    "foundations": [
        {
            "number": "24.1",
            "title": "LL(1) Grammar Conditions",
            "content": (
                "A grammar G is LL(1) if and only if for every production <code>A → α | β</code>:<br/>"
                "• 1. <code>FIRST(α) ∩ FIRST(β) = ∅</code> (No common starting terminal).<br/>"
                "• 2. At most one of α, β can produce ε.<br/>"
                "• 3. If β produces ε, then <code>FIRST(α) ∩ FOLLOW(A) = ∅</code>.<br/><br/>"
                "• <b>Grammars that are NEVER LL(1):</b><br/>"
                "&nbsp;&nbsp;- Left-recursive grammars (<code>A → A α</code>).<br/>"
                "&nbsp;&nbsp;- Ambiguous grammars."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: Any grammar with Left Recursion is 100% GUARANTEED NOT to be LL(1)! Always eliminate left recursion before testing LL(1)."
        },
        {
            "number": "24.2",
            "title": "Hierarchy and Power of LR Parsers",
            "content": (
                "From least powerful to most powerful bottom-up parser:<br/><br/>"
                "<b>LR(0) ⊂ SLR(1) ⊂ LALR(1) ⊂ CLR(1)</b><br/><br/>"
                "• <b>LR(0):</b> Places reduce actions across the entire row without looking ahead.<br/>"
                "• <b>SLR(1):</b> Places reduce actions ONLY in the columns of <code>FOLLOW(A)</code>.<br/>"
                "• <b>LALR(1):</b> Merges CLR(1) states that have identical LR(0) cores.<br/>"
                "&nbsp;&nbsp;- <b>Number of states in LALR(1) == Number of states in LR(0) / SLR(1)</b>!<br/>"
                "&nbsp;&nbsp;- Merging states in LALR(1) can introduce <b>Reduce/Reduce conflicts</b>, but <b>NEVER Shift/Reduce conflicts</b>.<br/>"
                "• <b>CLR(1):</b> Most powerful deterministic parser; has the most states."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: If a grammar is SLR(1), it is GUARANTEED to be LALR(1) and CLR(1)! If a grammar has a Shift-Reduce conflict in LALR(1), that same conflict was ALREADY present in CLR(1)."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Eliminating Left Recursion",
            "problem": "Eliminate immediate left recursion from: E → E + T | T.",
            "steps": [
                "Step 1: Identify pattern: A → A α | β, where A = E, α = '+ T', β = 'T'.",
                "Step 2: Rule: Replace with A → β A' and A' → α A' | ε.",
                "Step 3: Write new productions: E → T E' and E' → + T E' | ε."
            ],
            "answer": "E → T E', E' → + T E' | ε."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Operator Precedence Grammar",
            "warning": "An Operator Grammar can NEVER contain ε-productions, and can NEVER have two non-terminals adjacent to each other on the right-hand side (e.g. A → B C is forbidden)!"
        }
    ]
}

# CD Chapter 2: SDT & Code Optimization
CHAPTERS_TOC_CD_OS[("CD", 2)] = {
    "sub_id": "CD",
    "chap_idx": 2,
    "title": "SDT, Intermediate Code & Optimization",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Constant Folding at Compile Time",
            "text": (
                "If your code writes: `int seconds = 60 * 60 * 24;`\n"
                "Does your CPU calculate that multiplication every time your app runs? No! The compiler evaluates 60 × 60 × 24 = 86400 right during compilation and simply replaces the code with `int seconds = 86400;`. This is Constant Folding."
            )
        }
    ],
    "foundations": [
        {
            "number": "25.1",
            "title": "S-Attributed vs L-Attributed SDT",
            "content": (
                "• <b>Synthesized Attribute:</b> Computed from the attribute values of children nodes (Bottom-up flow).<br/>"
                "• <b>Inherited Attribute:</b> Computed from parents or left siblings (Top-down / Left-to-right flow).<br/><br/>"
                "• <b>S-Attributed SDT:</b><br/>"
                "&nbsp;&nbsp;- Uses ONLY Synthesized attributes.<br/>"
                "&nbsp;&nbsp;- Evaluated during bottom-up LR parsing.<br/><br/>"
                "• <b>L-Attributed SDT:</b><br/>"
                "&nbsp;&nbsp;- Can use Synthesized attributes AND Inherited attributes that depend only on parents and <b>LEFT SIBLINGS</b>.<br/>"
                "&nbsp;&nbsp;- <b>Every S-Attributed SDT is automatically L-Attributed</b> (S ⊂ L)!"
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: In an L-attributed SDT, an inherited attribute of a node can depend on its left siblings, but NEVER its right siblings!"
        },
        {
            "number": "25.2",
            "title": "Common Code Optimizations",
            "content": (
                "• <b>Constant Folding:</b> Pre-calculates constant operations at compile time (e.g. <code>2 + 3 → 5</code>).<br/>"
                "• <b>Constant Propagation:</b> Replaces variables holding known constants with their values.<br/>"
                "• <b>Common Subexpression Elimination:</b> Re-uses already computed expressions.<br/>"
                "• <b>Dead Code Elimination:</b> Removes unreachable code or variables whose values are never used.<br/>"
                "• <b>Loop Invariant Code Motion:</b> Moves statements that don't change inside a loop to OUTSIDE the loop."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: In a Directed Acyclic Graph (DAG) for Basic Blocks: Leaf nodes represent initial values/identifiers. Interior nodes represent operators. A node with multiple parents represents a shared Common Subexpression!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Basic Block Identification",
            "problem": "How many basic blocks are in a program with: 1. i=1, 2. if i>10 goto 6, 3. x=x+i, 4. i=i+1, 5. goto 2, 6. print x?",
            "steps": [
                "Step 1: Leaders are: (1) First instruction, (2) Target of any jump/branch, (3) Instruction immediately following a jump/branch.",
                "Step 2: Line 1 is a leader (first statement).",
                "Step 3: Line 2 is a leader (target of goto in line 5).",
                "Step 4: Line 3 is a leader (immediately follows conditional branch at line 2).",
                "Step 5: Line 6 is a leader (target of jump at line 2).",
                "Step 6: Leaders are lines: 1, 2, 3, 6 ⇒ Total 4 Basic Blocks."
            ],
            "answer": "Total Basic Blocks = 4."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Static Single Assignment (SSA)",
            "warning": "In SSA form, every variable is assigned EXACTLY ONCE. Merging variables from different branches requires Φ (phi) functions."
        }
    ]
}

# =============================================================================
# OPERATING SYSTEMS (OS)
# =============================================================================

# OS Chapter 0: Processes, Threads & CPU Scheduling
CHAPTERS_TOC_CD_OS[("OS", 0)] = {
    "sub_id": "OS",
    "chap_idx": 0,
    "title": "Process Management, CPU Scheduling & Threads",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Grocery Store Checkout (CPU Scheduling Algorithms)",
            "text": (
                "• FCFS (First-Come First-Served): You wait behind someone with 3 overflowing carts (Convoy Effect: average wait time explodes!).\n"
                "• SJF (Shortest Job First): The customer with just 1 packet of gum checks out first (Provably gives the lowest average waiting time!).\n"
                "• Round Robin: Each customer gets 30 seconds of cashier scanning before rotating to the next person (Fair, highly responsive, zero starvation)."
            )
        }
    ],
    "foundations": [
        {
            "number": "26.1",
            "title": "The fork() System Call & Process Tree",
            "content": (
                "• <code>fork()</code> duplicates the calling process to create a child process.<br/>"
                "• Return value of <code>fork()</code>:<br/>"
                "&nbsp;&nbsp;- Returns <b>0</b> to the Child process.<br/>"
                "&nbsp;&nbsp;- Returns <b>Child PID (> 0)</b> to the Parent process.<br/>"
                "&nbsp;&nbsp;- Returns <b>negative</b> on failure.<br/><br/>"
                "• <b>Number of processes created:</b><br/>"
                "&nbsp;&nbsp;If <code>fork()</code> is called n times consecutively:<br/>"
                "&nbsp;&nbsp;Total processes created = <b>2^n</b>.<br/>"
                "&nbsp;&nbsp;Total child processes created = <b>2^n - 1</b>."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: When fork() is called inside loops or logical checks like fork() && fork(), trace child and parent branches independently: in (fork() && fork()), the second fork() executes ONLY in the parent process because fork() returns 0 (False) to the child!"
        },
        {
            "number": "26.2",
            "title": "CPU Scheduling Metrics & Formulas",
            "content": (
                "• <b>Turnaround Time (TAT):</b> Completion Time - Arrival Time.<br/>"
                "• <b>Waiting Time (WT):</b> Turnaround Time - Burst Time.<br/>"
                "• <b>Response Time:</b> First Time CPU is Allocated - Arrival Time.<br/><br/>"
                "• <b>SJF / SRTF:</b> Provably optimal for minimizing Average Waiting Time.<br/>"
                "• <b>Round Robin:</b> Performance depends heavily on Time Quantum (q):<br/>"
                "&nbsp;&nbsp;- If q is extremely large: Degenerates into FCFS.<br/>"
                "&nbsp;&nbsp;- If q is extremely small: High context switch overhead kills CPU efficiency."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: Non-preemptive scheduling algorithms (FCFS, Non-preemptive SJF, Priority) NEVER interrupt a running process until it either completes or yields CPU for I/O!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Calculating Average Waiting Time",
            "problem": "Processes P1, P2, P3 arrive at time 0 with burst times 24, 3, 3 ms under FCFS. Find Average Waiting Time.",
            "steps": [
                "Step 1: Draw Gantt Chart: [ P1: 0 to 24 ] -> [ P2: 24 to 27 ] -> [ P3: 27 to 30 ].",
                "Step 2: Waiting Time for P1 = 0 ms.",
                "Step 3: Waiting Time for P2 = 24 ms.",
                "Step 4: Waiting Time for P3 = 27 ms.",
                "Step 5: Average Waiting Time = (0 + 24 + 27) / 3 = 51 / 3 = 17 ms."
            ],
            "answer": "Average Waiting Time = 17 ms."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: User-Level vs Kernel-Level Threads",
            "warning": "If one User-Level Thread (ULT) makes a blocking system call, the ENTIRE PROCESS blocks! Kernel-Level Threads (KLT) allow other threads in the same process to keep running."
        }
    ]
}

# OS Chapter 1: Synchronization & Deadlocks
CHAPTERS_TOC_CD_OS[("OS", 1)] = {
    "sub_id": "OS",
    "chap_idx": 1,
    "title": "Process Synchronization, Semaphores & Deadlock Prevention",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Coffee Shop Single Restroom Key (Mutual Exclusion)",
            "text": (
                "A coffee shop has 1 restroom and 1 key hanging on the wall (Binary Semaphore = 1).\n"
                "When someone takes the key (wait / P operation), the key is gone (Semaphore = 0). Anyone else who arrives must wait outside.\n"
                "When the person returns the key (signal / V operation), the next waiting customer enters. This guarantees Mutual Exclusion."
            )
        },
        {
            "title": "Real-Life Example 2: The Gridlock Traffic Intersection (Deadlock)",
            "text": (
                "Four cars enter a 4-way intersection simultaneously, each blocking the road behind them while waiting for the car ahead to move.\n"
                "Nobody can move, and nobody will back up. All 4 conditions for Deadlock are present: Mutual Exclusion, Hold & Wait, No Preemption, and Circular Wait."
            )
        }
    ],
    "foundations": [
        {
            "number": "27.1",
            "title": "Critical Section Requirements & Semaphores",
            "content": (
                "Any valid solution to the Critical Section problem MUST satisfy:<br/>"
                "• <b>1. Mutual Exclusion (Mandatory):</b> Only 1 process in critical section at a time.<br/>"
                "• <b>2. Progress (Mandatory):</b> If no process is in critical section, only processes wanting to enter can participate in the decision.<br/>"
                "• <b>3. Bounded Waiting (Mandatory):</b> A limit must exist on the number of times other processes can enter before a request is granted.<br/><br/>"
                "• <b>Counting Semaphore:</b><br/>"
                "&nbsp;&nbsp;- <code>wait(S)</code> (or P): <code>S = S - 1</code>. If <code>S < 0</code>, process blocks.<br/>"
                "&nbsp;&nbsp;- <code>signal(S)</code> (or V): <code>S = S + 1</code>. If <code>S <= 0</code>, wakes up a blocked process.<br/>"
                "&nbsp;&nbsp;- Magnitude <code>|S|</code> when S < 0 gives the exact number of blocked processes waiting in the queue!"
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: If a counting semaphore is initialized to 10, and 6 wait() and 4 signal() operations are executed: Final S = 10 - 6 + 4 = 8."
        },
        {
            "number": "27.2",
            "title": "Deadlock: 4 Conditions & Banker's Algorithm",
            "content": (
                "Deadlock occurs if and only if ALL FOUR conditions hold simultaneously:<br/>"
                "1. Mutual Exclusion, 2. Hold and Wait, 3. No Preemption, 4. <b>Circular Wait</b>.<br/><br/>"
                "• <b>Deadlock Prevention:</b> Invalidate at least one of the 4 conditions (e.g. impose total ordering on resources to eliminate Circular Wait).<br/><br/>"
                "• <b>Banker's Algorithm (Deadlock Avoidance):</b><br/>"
                "&nbsp;&nbsp;- <code>Need Matrix = Max Demand - Currently Allocated</code>.<br/>"
                "&nbsp;&nbsp;- A state is SAFE if there exists at least one sequence of processes that can finish without causing deadlock."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: For m instances of a single resource shared by n processes, where each process requires at most k instances: The system is GUARANTEED to be deadlock-free if: Total Resources m ≥ n × (k - 1) + 1!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Minimum Resources to Prevent Deadlock",
            "problem": "A system has 4 processes, each needing a maximum of 3 tape drives. What is the minimum number of tape drives required to guarantee that deadlock will never occur?",
            "steps": [
                "Step 1: Formula for deadlock-free condition: R ≥ Σ(Max_i - 1) + 1.",
                "Step 2: Here n = 4 processes, each needing k = 3 units.",
                "Step 3: In the worst-case deadlock scenario, each process holds (k - 1) = (3 - 1) = 2 units.",
                "Step 4: Total held in worst case = 4 × 2 = 8 tape drives.",
                "Step 5: Adding just 1 more unit allows at least one process to finish, release its resources, and free the system.",
                "Step 6: Minimum tape drives R = 8 + 1 = 9."
            ],
            "answer": "Minimum tape drives needed = 9."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Safe State vs Deadlock",
            "warning": "A Safe state is NEVER deadlocked. An Unsafe state is NOT necessarily deadlocked; an unsafe state merely holds the potential to lead into a deadlock if worst-case requests occur!"
        }
    ]
}

# OS Chapter 2: Memory Management & Virtual Memory
CHAPTERS_TOC_CD_OS[("OS", 2)] = {
    "sub_id": "OS",
    "chap_idx": 2,
    "title": "Paging, Virtual Memory, TLB & Inodes",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The College Library Desk (Virtual Memory & Paging)",
            "text": (
                "A student desk (Physical RAM) has room for only 3 open books (Page Frames).\n"
                "Your research paper requires 100 books (Virtual Memory: 4 GB program on a 512 MB laptop!).\n"
                "When you need chapter 5, you walk to the library shelf (Hard Disk), place it on the desk, and swap out the book you haven't touched for the longest time (LRU Page Replacement)."
            )
        }
    ],
    "foundations": [
        {
            "number": "28.1",
            "title": "Paging & Effective Memory Access Time (EMAT) with TLB",
            "content": (
                "• <b>Paging Address Structure:</b><br/>"
                "&nbsp;&nbsp;Logical Address = [ Page Number (p) | Page Offset (d) ].<br/>"
                "&nbsp;&nbsp;Page Offset bits = log2(Page Size in bytes).<br/><br/>"
                "• <b>Translation Lookaside Buffer (TLB):</b><br/>"
                "&nbsp;&nbsp;High-speed cache that stores recent Page-to-Frame mappings.<br/><br/>"
                "• <b>EMAT Formula with TLB:</b><br/>"
                "&nbsp;&nbsp;<code>EMAT = Hit_Ratio × (TLB_time + RAM_time) + (1 - Hit_Ratio) × (TLB_time + 2 × RAM_time)</code>.<br/>"
                "&nbsp;&nbsp;(On a TLB miss, we must access RAM twice: first to read the page table, second to read actual data)."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: For a multi-level page table with k levels, a TLB miss requires (k + 1) memory accesses: k accesses to traverse the page table tree, plus 1 access to read data!"
        },
        {
            "number": "28.2",
            "title": "Page Replacement Algorithms",
            "content": (
                "• <b>FIFO (First-In First-Out):</b> Suffers from <b>Belady's Anomaly</b> (allocating MORE page frames can sometimes cause MORE page faults!).<br/>"
                "• <b>Optimal Page Replacement (OPT):</b> Replaces page that will not be used for longest time in the future. Provably minimum page faults (used as benchmark).<br/>"
                "• <b>LRU (Least Recently Used):</b> Replaces page that hasn't been accessed for longest time in the past. Free from Belady's anomaly (Stack algorithm)."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: Stack algorithms (like LRU and Optimal) NEVER suffer from Belady's Anomaly because the set of pages in an n-frame memory is always a subset of pages in an (n+1)-frame memory!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Calculating EMAT with TLB",
            "problem": "TLB search time = 20 ns, Main Memory access time = 100 ns. TLB hit ratio = 90%. Single-level paging. Find EMAT.",
            "steps": [
                "Step 1: Case 1 (TLB Hit): Access TLB (20 ns) + Access RAM for data (100 ns) = 120 ns. Occurs 90% of the time.",
                "Step 2: Case 2 (TLB Miss): Access TLB (20 ns) + Access RAM for Page Table (100 ns) + Access RAM for data (100 ns) = 220 ns. Occurs 10% of the time.",
                "Step 3: EMAT = (0.90 × 120 ns) + (0.10 × 220 ns) = 108 ns + 22 ns = 130 ns."
            ],
            "answer": "Effective Memory Access Time = 130 ns."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Thrashing in Virtual Memory",
            "warning": "Thrashing occurs when total memory demand of active processes exceeds available physical frames. The CPU spends almost 100% of its time swapping pages in/out rather than executing instructions!"
        }
    ]
}
