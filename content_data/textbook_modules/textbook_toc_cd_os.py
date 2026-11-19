# textbook_toc_cd_os.py
# Simplified, crystal-clear study notes for TOC, Compiler Design, and Operating Systems.
# Written in simple, friendly, easy-to-understand language for GATE 2027 CSE aspirants.

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
            "text": "A soda can costs ₹20. The machine accepts ₹5 and ₹10 coins. The machine has no infinite hard drive; it only remembers 4 states: {₹0, ₹5, ₹10, ₹15}. When you reach state ₹20, the can drops (Final / Accepting State!). Because the machine only needs a small, fixed number of states, it is a Deterministic Finite Automaton (DFA)."
        },
        {
            "title": "Real-Life Example 2: Email Format Checking on a Website (Regular Expressions)",
            "text": "When you type your email into a website, a Regular Expression checks whether it has letters, an '@' symbol, and a domain like '.com'. The browser converts the regex into a tiny DFA and tests your letters one by one in milliseconds. If it ends in an accepting state, a green checkmark appears."
        },
        {
            "title": "Real-Life Example 3: Merging Duplicate Rooms in a Hotel (DFA Minimization)",
            "text": "If Hotel Room 201 and Room 202 have identical beds, identical Wi-Fi, and identical room service for every guest request, keeping them separate wastes space. The Table-Filling method finds states that behave identically for all future inputs and merges them into a single state, creating the smallest Minimal DFA."
        }
    ],
    "foundations": [
        {
            "number": "20.1",
            "title": "DFA vs NFA Equivalences",
            "content": (
                "• <b>DFA:</b> Exactly ONE transition for every state and input symbol. Deterministic.<br/>"
                "• <b>NFA:</b> Can have 0, 1, or multiple transitions on the same symbol, or jump without input (ε-moves).<br/>"
                "• <b>Power:</b> <b>DFA and NFA have the EXACT SAME POWER</b>! Every NFA can be converted to an equivalent DFA with at most 2^n states."
            ),
            "crucial_rule": "GOLDEN RULE: While DFA and NFA recognize the same languages, an NFA with n states might need up to 2^n states when converted to a minimal DFA (e.g. 'n-th symbol from right is 1')."
        },
        {
            "number": "20.2",
            "title": "Regular Language Closure Properties",
            "content": (
                "Regular languages are closed under <b>ALMOST EVERYTHING</b>:<br/>"
                "• Union (L1 ∪ L2) ✔<br/>"
                "• Intersection (L1 ∩ L2) ✔<br/>"
                "• Complement (~L) ✔<br/>"
                "• Concatenation (L1 · L2) ✔<br/>"
                "• Kleene Star (L*) ✔<br/>"
                "• Reversal (L^R) ✔"
            ),
            "crucial_rule": "GOLDEN RULE: If L1 and L2 are regular, any combination using Union, Intersection, or Complement is GUARANTEED to be regular!"
        },
        {
            "number": "20.3",
            "title": "Arden's Theorem for Regular Expressions",
            "content": (
                "If P and Q are regular expressions, and P does not contain ε:<br/>"
                "• The equation <b>R = Q + R P</b> has the unique solution: <b>R = Q P*</b>."
            ),
            "crucial_rule": "GOLDEN RULE: In Arden's theorem, R = Q + R P becomes Q P*. (Notice P* comes on the RIGHT!)."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: States for 'Binary Number Divisible by 3'",
            "problem": "How many states are in the minimal DFA that accepts binary strings whose decimal value is divisible by 3?",
            "steps": [
                "Step 1: Any number divided by 3 can have only 3 remainders: 0, 1, or 2.",
                "Step 2: Each remainder corresponds to one state: State 0 (remainder 0), State 1 (remainder 1), State 2 (remainder 2).",
                "Step 3: State 0 is the start state AND the only accepting state (remainder 0).",
                "Step 4: None of these 3 remainder states behave identically, so no states can be merged."
            ],
            "answer": "Minimum states = 3."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Dead / Trap State in DFA",
            "warning": "In a DFA, every state MUST have an outgoing arrow for every alphabet symbol! If a string becomes permanently invalid (e.g. starts with '0'), it goes to a Dead/Trap state. Don't forget to count the Dead State!"
        }
    ]
}

# TOC Chapter 1: Grammars & Pushdown Automata
CHAPTERS_TOC_CD_OS[("TOC", 1)] = {
    "sub_id": "TOC",
    "chap_idx": 1,
    "title": "Grammars, Pushdown Automata & Pumping Lemma",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Matching Parentheses in VS Code (Pushdown Automaton)",
            "text": "When you write code with nested brackets `((a + b) * (c - d))`, your editor highlights matching pairs. A simple Finite Automaton cannot do this because brackets can be nested 50 levels deep. A Pushdown Automaton (PDA) solves this using an internal Stack: push on '(', pop on ')'. If the stack is empty at the end, the code is balanced! Adding stack memory creates Context-Free Languages (CFL)."
        },
        {
            "title": "Real-Life Example 2: The Two-Hand Scale Limit (Why a^n b^n c^n is NOT Context-Free)",
            "text": "Imagine a physical balance scale with 2 pans. You can easily balance a^n against b^n by pushing 'a's and popping for 'b's. But what if you have THREE things: a^n b^n c^n? The moment you pop all the 'a's to match 'b's, your stack is completely empty: the memory is gone! You have no way to remember 'n' when counting 'c's. This is why a^n b^n c^n is NOT context-free."
        },
        {
            "title": "Real-Life Example 3: Ambiguous Newspaper Headlines (Grammar Ambiguity)",
            "text": "A headline reads: 'Enraged Cow Injures Farmer with Axe'. Did the cow hold an axe, or did the farmer hold an axe? Two completely different parse trees exist for the same sentence! In programming, an ambiguous grammar causes compiler bugs. Grammars must be designed to have only 1 unique parse tree for every valid statement."
        }
    ],
    "foundations": [
        {
            "number": "21.1",
            "title": "Chomsky Normal Form (CNF) Derivation Steps",
            "content": (
                "A grammar is in CNF if all rules look like <b>A → BC</b> or <b>A → a</b>.<br/>"
                "• <b>Derivation Steps:</b> To generate any string of length n (n ≥ 1) using a CNF grammar, it ALWAYS takes exactly <b>2n - 1 steps</b>!"
            ),
            "crucial_rule": "GOLDEN RULE: If a string has length 10, deriving it in CNF takes exactly 2(10) - 1 = 19 production steps. This is a direct 1-mark GATE question!"
        },
        {
            "number": "21.2",
            "title": "Deterministic PDA (DPDA) vs Non-Deterministic PDA (NPDA)",
            "content": (
                "• <b>DPDA (Deterministic CFL):</b> Recognizes languages like `w c w^R` (where 'c' marks the middle). Closed under <b>Complement</b>!<br/>"
                "• <b>NPDA (CFL):</b> Recognizes languages like `w w^R` (even-length palindrome without middle marker: needs guessing).<br/>"
                "• <b>Closure warning:</b> CFLs are <b>NOT closed under Intersection or Complement</b>!"
            ),
            "crucial_rule": "GOLDEN RULE: If L1 and L2 are Context-Free, L1 ∩ L2 might NOT be Context-Free!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Proving a Language is Not Regular",
            "problem": "Is L = { a^n b^n | n ≥ 0 } regular or context-free?",
            "steps": [
                "Step 1: Check memory needed: To ensure number of 'a's equals number of 'b's, the machine must count arbitrarily high.",
                "Step 2: A Finite Automaton has fixed finite states, so it cannot count arbitrary numbers. Hence, L is NOT regular.",
                "Step 3: A Pushdown Automaton can push 'a' onto a stack and pop for each 'b'. When input ends, if stack is empty, accept.",
                "Step 4: Since a PDA can accept it deterministically, L is a Deterministic Context-Free Language (DCFL)."
            ],
            "answer": "L is Non-Regular, but it is DCFL (Context-Free)."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: DCFL vs CFL Complement",
            "warning": "DCFL IS closed under complement. But general CFL is NOT closed under complement!"
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
            "title": "Real-Life Example 1: Your Laptop as a Universal Turing Machine",
            "text": "Before Alan Turing, a calculator was built to do only one thing (like an adding machine). Turing proved that you don't need a thousand different machines: you build ONE computer that reads a program and data from memory and executes it. Your laptop or phone is a Universal Turing Machine!"
        },
        {
            "title": "Real-Life Example 2: The Infinite Antivirus Loop (The Halting Problem)",
            "text": "Can someone write a perfect antivirus that inspects ANY program and guarantees whether it will ever freeze in an infinite loop? Turing proved this is mathematically IMPOSSIBLE. If you give that tool a program that says 'Halt if the tool says I loop, and Loop if the tool says I halt', the tool is trapped in a logical contradiction. The Halting Problem is Undecidable."
        },
        {
            "title": "Real-Life Example 3: Nested Russian Dolls (Chomsky Hierarchy)",
            "text": "Languages fit inside each other like Russian dolls:\nRegular ⊂ DCFL ⊂ CFL ⊂ Context-Sensitive ⊂ Recursive (Decidable) ⊂ Recursively Enumerable (Turing Recognizable)."
        }
    ],
    "foundations": [
        {
            "number": "22.1",
            "title": "Recursive (REC) vs Recursively Enumerable (RE)",
            "content": (
                "• <b>Recursive (REC / Decidable):</b> Turing machine ALWAYS halts and gives YES or NO in finite time (No infinite loops).<br/>"
                "• <b>Recursively Enumerable (RE / Semi-decidable):</b> Halts on YES, but might loop forever on NO.<br/>"
                "• <b>Complement Rule:</b> Language L is Decidable IF AND ONLY IF <b>both L and ~L are RE</b>."
            ),
            "crucial_rule": "GOLDEN RULE: If L is RE but not Recursive, then its complement ~L is strictly NOT RE!"
        },
        {
            "number": "22.2",
            "title": "Rice's Theorem in Plain Words",
            "content": (
                "Any question about the <b>LANGUAGE recognized by a Turing Machine</b> (like 'Is L(M) empty?', 'Is L(M) regular?', 'Does it accept string 01?') is <b>UNDECIDABLE</b>.<br/>"
                "• If it's a property about the code itself (e.g. 'Does TM have 5 states?'), it is DECIDABLE."
            ),
            "crucial_rule": "GOLDEN RULE: If a GATE question asks if a non-trivial property of the language of a Turing Machine is decidable, the answer is ALWAYS Undecidable by Rice's Theorem!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Decidability Checklist",
            "problem": "Is the Emptiness problem (Is L = ∅?) decidable for: (1) Regular languages, (2) Context-Free languages, (3) Turing Machines?",
            "steps": [
                "Step 1: For Regular languages: Check if there is a path from start state to any final state in the DFA. Easily solvable ⇒ DECIDABLE.",
                "Step 2: For Context-Free languages: Check if start symbol can derive any terminal string. Solvable in polynomial time ⇒ DECIDABLE.",
                "Step 3: For Turing Machines: Checking if a TM accepts nothing is equivalent to the Halting problem ⇒ UNDECIDABLE."
            ],
            "answer": "Regular: Decidable | CFL: Decidable | TM: Undecidable."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Equivalence of CFLs",
            "warning": "Testing if two Regular languages are equal (L1 == L2) is DECIDABLE. But testing if two Context-Free languages are equal is UNDECIDABLE!"
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
            "title": "Real-Life Example 1: Reading Words in a Book (Lexical Analyzer / Tokenizer)",
            "text": "When you read, you don't look at single ink dots or spaces. Your brain groups letters into words: 'int' (Keyword), 'score' (Variable Identifier), '=' (Assignment Operator), '100' (Number). The Lexical Analyzer does this: it strips out spaces and comments, and converts characters into clean Tokens for the parser."
        },
        {
            "title": "Real-Life Example 2: Train Track Signal (LL(1) 1-Token Lookahead)",
            "text": "An LL(1) parser is like a train driver who only looks at 1 signal light ahead. If green, go track A; if yellow, go track B. It never needs to put the train in reverse (Zero backtracking!). But if two different tracks share the same start signal, the train crashes. Left Factoring fixes this by splitting the shared track."
        },
        {
            "title": "Real-Life Example 3: The Mirror Loop of Left Recursion",
            "text": "If a recipe rule says: 'To bake a cake, first bake a cake, then add sugar' (A → Aα), you will be stuck in an infinite loop without ever cracking an egg! Top-down parsers get stuck in infinite loops when grammars have Left Recursion."
        }
    ],
    "foundations": [
        {
            "number": "23.1",
            "title": "Tokens, Patterns & Lexical Errors",
            "content": (
                "• <b>Lexeme:</b> The exact characters in code (e.g. `count`, `3.14`).<br/>"
                "• <b>Token:</b> The abstract category (e.g. `<ID>`, `<NUM>`).<br/>"
                "• <b>Longest Match (Maximal Munch):</b> Scans the longest valid token (e.g. `---` is scanned as `--` then `-`)."
            ),
            "crucial_rule": "GOLDEN RULE: Undeclared variables or missing semicolons are NOT lexical errors! They are Syntax or Semantic errors."
        },
        {
            "number": "23.2",
            "title": "FIRST and FOLLOW Rules",
            "content": (
                "• <b>FIRST(X):</b> All terminals that can appear as the first symbol of a string derived from X.<br/>"
                "• <b>FOLLOW(A):</b> All terminals that can appear immediately to the right of non-terminal A.<br/>"
                "&nbsp;&nbsp;1. Put `$` in FOLLOW(Start_Symbol).<br/>"
                "&nbsp;&nbsp;2. If rule is `A → α B β`, add (FIRST(β) - {ε}) to FOLLOW(B).<br/>"
                "&nbsp;&nbsp;3. If rule is `A → α B` or β derives ε, add all of FOLLOW(A) to FOLLOW(B)."
            ),
            "crucial_rule": "GOLDEN RULE: FOLLOW sets NEVER contain ε! The empty string ε can be in FIRST, but NEVER in FOLLOW."
        },
        {
            "number": "23.3",
            "title": "LL(1) Grammar Conditions",
            "content": (
                "A grammar is LL(1) if for every rule A → α | β:<br/>"
                "1. FIRST(α) and FIRST(β) do not share any common terminals.<br/>"
                "2. If α derives ε, then FIRST(β) and FOLLOW(A) do not share any common terminals.<br/>"
                "• <b>Never LL(1):</b> Ambiguous grammars, Left-Recursive grammars, and Non-Left-Factored grammars are NEVER LL(1)!"
            ),
            "crucial_rule": "GOLDEN RULE: If an LL(1) parsing table cell contains 2 productions, the grammar is NOT LL(1)!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Computing FIRST and FOLLOW",
            "problem": "Grammar: S → A B, A → a | ε, B → b. Find FIRST and FOLLOW for S, A, B.",
            "steps": [
                "Step 1: FIRST(B) = {b}.",
                "Step 2: FIRST(A) = {a, ε}.",
                "Step 3: FIRST(S): S → AB. Starts with A, so takes FIRST(A) - {ε} = {a}. Since A can be ε, it also takes FIRST(B) = {b}. Thus FIRST(S) = {a, b}.",
                "Step 4: FOLLOW(S) = {$} (since S is start symbol).",
                "Step 5: FOLLOW(A): In S → AB, B follows A ⇒ FOLLOW(A) = FIRST(B) = {b}.",
                "Step 6: FOLLOW(B): In S → AB, nothing follows B ⇒ FOLLOW(B) = FOLLOW(S) = {$}."
            ],
            "answer": "FIRST(S)={a,b}, FIRST(A)={a,ε}, FIRST(B)={b} | FOLLOW(S)={$}, FOLLOW(A)={b}, FOLLOW(B)={$}."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Eliminating Left Recursion",
            "warning": "For `A → Aα | β`, the non-recursive form is `A → βA'`, `A' → αA' | ε`. Remember: β comes first, NOT α!"
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
            "title": "Real-Life Example 1: Assembling Lego Bricks (Shift-Reduce Parsing)",
            "text": "Bottom-up parsing starts with scattered Lego pieces on the table. You pick up a piece from the input (Shift). When 4 pieces on your table form a completed sub-assembly matching a blueprint rule, you snap them together into a block (Reduce). You keep shifting and reducing until one complete Lego house is built (Accept!)."
        },
        {
            "title": "Real-Life Example 2: The Four Models of Night-Vision Goggles (LR Parsers)",
            "text": "• LR(0): Blind reduction without looking ahead.\n• SLR(1): Cheap flashlight: reduces only if lookahead is in FOLLOW set.\n• LALR(1): Smart infrared goggles: tracks lookahead while merging identical states to keep memory small (Used by Yacc and Bison!).\n• CLR(1): Full military satellite radar: most powerful, but huge table size."
        },
        {
            "title": "Real-Life Example 3: Dangling Else Dilemma (Shift-Reduce Conflict)",
            "text": "In `if (a) if (b) s1 else s2`: should `else` attach to the inner `if` (Shift) or close the outer `if` (Reduce)? Both choices are valid grammar moves! Most compilers choose Shift so `else` pairs with the closest preceding `if`."
        }
    ],
    "foundations": [
        {
            "number": "24.1",
            "title": "LR Parser Family Hierarchy",
            "content": (
                "• <b>Number of States:</b><br/>"
                "&nbsp;&nbsp;<b>State Count(LR(0)) == State Count(SLR(1)) == State Count(LALR(1)) < State Count(CLR(1))</b>.<br/>"
                "• <b>Parsing Power:</b><br/>"
                "&nbsp;&nbsp;<b>LL(1) < SLR(1) < LALR(1) < CLR(1)</b>."
            ),
            "crucial_rule": "GOLDEN RULE: LALR(1) and SLR(1) have the EXACT SAME number of states as LR(0) because LALR only merges states that share identical cores!"
        },
        {
            "number": "24.2",
            "title": "Conflicts When Merging States to LALR(1)",
            "content": (
                "When merging CLR(1) states to form LALR(1):<br/>"
                "• <b>Shift-Reduce Conflicts:</b> CAN NEVER BE CREATED by merging!<br/>"
                "• <b>Reduce-Reduce Conflicts:</b> <b>CAN BE CREATED</b> by merging!"
            ),
            "crucial_rule": "GOLDEN RULE: If a grammar is CLR(1), it might NOT be LALR(1) because state merging can create a Reduce-Reduce conflict."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Comparing Parser States",
            "problem": "A grammar has 10 states in LR(0). How many states will it have in SLR(1) and LALR(1)?",
            "steps": [
                "Step 1: SLR(1) uses the exact same states as LR(0), only adding FOLLOW checks to reduction cells.",
                "Step 2: LALR(1) merges CLR(1) states down to the exact LR(0) core.",
                "Step 3: Therefore, State Count is identical for all three: 10 states."
            ],
            "answer": "SLR(1) has 10 states, LALR(1) has 10 states."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Shift-Reduce Conflict Resolution",
            "warning": "Never declare a grammar ambiguous just because it has an S-R conflict. Declaring operator precedence and associativity easily resolves the conflict."
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
            "title": "Real-Life Example 1: Supermarket Billing Receipt (Synthesized Attributes)",
            "text": "When calculating a receipt: Item 1 is ₹20, Item 2 is ₹50. The total sum ₹70 is computed by adding the values of its children line items. An attribute calculated from child values is called a Synthesized Attribute (S-Attributed). It flows upward naturally during parsing."
        },
        {
            "title": "Real-Life Example 2: One Grocery Trip for Milk and Bread (Common Subexpression)",
            "text": "If your morning routine says: 'Drive to store and buy milk; then drive to store and buy bread', you do 2 trips. A smart person combines them into 1 trip: buy both together! Common Subexpression Elimination detects identical calculations (`a = b + c; d = b + c;`) and reuses the first answer."
        },
        {
            "title": "Real-Life Example 3: Moving Work Outside a Loop (Loop Invariant Code Motion)",
            "text": "If a workout routine says: 'Do 100 pushups, and during every single pushup calculate 1000 × 50', doing the math 100 times inside the loop is silly. Calculate 50,000 ONCE before you start, and just do the pushups!"
        }
    ],
    "foundations": [
        {
            "number": "25.1",
            "title": "S-Attributed vs L-Attributed Definitions",
            "content": (
                "• <b>S-Attributed:</b> Uses <b>ONLY synthesized attributes</b> (evaluated bottom-up on shift-reduce stack).<br/>"
                "• <b>L-Attributed:</b> Can use synthesized OR inherited attributes, but inherited attributes can depend ONLY on parents and <b>LEFT siblings</b> (never right siblings!).<br/>"
                "• Every S-attributed SDT is also L-attributed: <b>S-Attributed ⊂ L-Attributed</b>."
            ),
            "crucial_rule": "GOLDEN RULE: If an inherited attribute depends on a RIGHT sibling, it is NOT L-attributed!"
        },
        {
            "number": "25.2",
            "title": "Liveness Analysis (GATE 2027 Syllabus Focus)",
            "content": (
                "A variable is 'Live' at point p if its current value will be read by some future instruction.<br/>"
                "• <b>Equation:</b> IN[B] = USE[B] ∪ (OUT[B] - DEF[B]).<br/>"
                "• This is a <b>BACKWARD data flow problem</b> (computed from program end to start)."
            ),
            "crucial_rule": "GOLDEN RULE: If a variable is redefined in a block before being read, its old value is 'killed' and does NOT appear in USE[B]."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Basic Block Live Variables",
            "problem": "Block B has instructions: (1) a = b + c, (2) d = a - 5. If OUT[B] = {d}, find IN[B].",
            "steps": [
                "Step 1: Check uses and defs from bottom to top:",
                "&nbsp;&nbsp;Line 2 defines 'd', uses 'a'.",
                "&nbsp;&nbsp;Line 1 defines 'a', uses 'b' and 'c'.",
                "Step 2: Variables needed from outside: 'b' and 'c' are used before definition. 'a' is defined inside so it's not needed from outside.",
                "Step 3: IN[B] = {b, c}."
            ],
            "answer": "IN[B] = {b, c}."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Dead Code Elimination",
            "warning": "If a variable `x = y + z` is calculated, but `x` is never used anywhere in the rest of the program, `x` is Dead Code and can be removed completely."
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
            "title": "Real-Life Example 1: Separate Apartments vs Shared Kitchen (Process vs Thread)",
            "text": "• Processes: Like two neighboring families in separate locked apartments. Family A cannot touch Family B's fridge (isolated memory, safe from crashes, but sharing needs IPC).\n• Threads: Like roommates sharing the same kitchen and living room (shared memory, super fast communication, but if one roommate sets the stove on fire, everyone in the apartment goes down!)."
        },
        {
            "title": "Real-Life Example 2: Single Restroom Key (Mutex / Binary Semaphore)",
            "text": "A coffee shop has one restroom and one physical brass key hanging at the counter. Customer 1 takes the key and locks the door (wait: key count drops from 1 to 0). Customer 2 arrives, sees no key, and waits. When Customer 1 returns the key (signal: key count goes back to 1), Customer 2 enters. This guarantees Mutual Exclusion."
        },
        {
            "title": "Real-Life Example 3: The Fork() Family Tree",
            "text": "When a process calls `fork()`, it creates an exact identical twin clone of itself! In the parent process, fork() returns the baby's ID (> 0). Inside the new child process, fork() returns 0. If you call fork() 3 times in a row, you end up with 2^3 = 8 processes."
        }
    ],
    "foundations": [
        {
            "number": "26.1",
            "title": "Critical Section: The 3 Mandatory Requirements",
            "content": (
                "1. <b>Mutual Exclusion:</b> Only 1 process in critical section at a time.<br/>"
                "2. <b>Progress:</b> If critical section is free, only processes wanting to enter decide who goes next. No infinite waiting.<br/>"
                "3. <b>Bounded Waiting:</b> There is a limit on how many times others can enter before you get your turn (Prevents Starvation)."
            ),
            "crucial_rule": "GOLDEN RULE: Strict Alternation (using a turn variable) guarantees Mutual Exclusion, but FAILS PROGRESS because if process 0 stops, process 1 can never enter again!"
        },
        {
            "number": "26.2",
            "title": "Counting Semaphore Interpretation",
            "content": (
                "• <b>wait(S):</b> `S = S - 1; if (S < 0) block();`<br/>"
                "• <b>signal(S):</b> `S = S + 1; if (S <= 0) wakeup();`<br/>"
                "• <b>Meaning:</b><br/>"
                "&nbsp;&nbsp;• If S ≥ 0: S is the count of <b>free available resources</b>.<br/>"
                "&nbsp;&nbsp;• If S < 0: |S| is the count of <b>processes waiting in the blocked queue</b>."
            ),
            "crucial_rule": "GOLDEN RULE: Formula for final value: S_final = S_initial - (number of wait calls) + (number of signal calls)."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Counting Semaphore Value",
            "problem": "A semaphore is initialized to 8. A sequence of 15 wait() and 10 signal() operations occur. What is the final value of the semaphore, and how many processes are blocked?",
            "steps": [
                "Step 1: Write formula: S_final = S_init - wait_count + signal_count.",
                "Step 2: Plug in: S_final = 8 - 15 + 10 = 8 - 5 = 3.",
                "Step 3: Since S_final = +3 (positive), exactly 3 resources are free.",
                "Step 4: Blocked queue has 0 processes."
            ],
            "answer": "Final value = 3, Blocked processes = 0."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Counting Child Processes",
            "warning": "If a question asks: 'How many CHILD processes are created by n fork() calls?', the answer is 2^n - 1 (subtract 1 for the original parent!)."
        }
    ]
}

# OS Chapter 1: Scheduling & Deadlocks
CHAPTERS_TOC_CD_OS[("OS", 1)] = {
    "sub_id": "OS",
    "chap_idx": 1,
    "title": "CPU Scheduling, I/O Scheduling & Deadlocks",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Supermarket Express Checkout (SJF Scheduling)",
            "text": "Waiting in a grocery line behind someone with 3 overflowing carts takes 45 minutes (Convoy Effect in FCFS). You only want to buy 1 bottle of water (10 seconds!). Shortest Job First (SJF) lets the water bottle customer go first, drastically slashing average waiting time for everyone."
        },
        {
            "title": "Real-Life Example 2: The Bank Loan Safety Check (Banker's Algorithm)",
            "text": "A bank has ₹10,000 cash. Three customers have credit limits. Before handing out a ₹4,000 loan, the manager checks: 'If I give this cash, does there still exist at least one order where every customer can finish and return the money?' If yes, the state is SAFE. If not, the loan is paused to prevent Deadlock."
        },
        {
            "title": "Real-Life Example 3: Skyscraper Elevator (SCAN Disk Scheduling)",
            "text": "An elevator in a tall building doesn't jump randomly between floor 3, floor 80, and floor 5. It sweeps smoothly up to the top floor servicing every request along the way, then sweeps back down. SCAN (Elevator algorithm) prevents mechanical disk head thrashing."
        }
    ],
    "foundations": [
        {
            "number": "27.1",
            "title": "CPU Scheduling Formulas & SRTF",
            "content": (
                "• <b>Turnaround Time (TAT):</b> Completion Time - Arrival Time.<br/>"
                "• <b>Waiting Time (WT):</b> Turnaround Time - Burst Time.<br/>"
                "• <b>SRTF (Shortest Remaining Time First):</b> Preemptive SJF. <b>Provably gives minimum average waiting time</b> of all scheduling algorithms!"
            ),
            "crucial_rule": "GOLDEN RULE: In Round Robin scheduling, if a new process arrives at the exact same instant an old process finishes its time quantum, put the NEW process in the queue FIRST!"
        },
        {
            "number": "27.2",
            "title": "The 4 Coffman Deadlock Conditions",
            "content": (
                "Deadlock can occur only if ALL 4 conditions hold together:<br/>"
                "1. <b>Mutual Exclusion:</b> Resources cannot be shared.<br/>"
                "2. <b>Hold and Wait:</b> Holding resources while asking for more.<br/>"
                "3. <b>No Preemption:</b> Resources cannot be forcibly taken.<br/>"
                "4. <b>Circular Wait:</b> Circular chain of waiting processes."
            ),
            "crucial_rule": "GOLDEN RULE: Break even ONE of the 4 conditions, and Deadlock is 100% PREVENTED!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Banker's Algorithm Need Matrix",
            "problem": "Process P1 has Max Claim = (7, 5, 3) and Current Allocation = (2, 1, 1). What is its remaining Need?",
            "steps": [
                "Step 1: Need = Max - Allocation.",
                "Step 2: Resource A: 7 - 2 = 5.",
                "Step 3: Resource B: 5 - 1 = 4.",
                "Step 4: Resource C: 3 - 1 = 2."
            ],
            "answer": "Need(P1) = (5, 4, 2)."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Resource Graph Cycles",
            "warning": "A cycle in a Resource Allocation Graph guarantees deadlock ONLY IF every resource has strictly 1 single instance! If resources have multiple instances, a cycle might NOT cause deadlock."
        }
    ]
}

# OS Chapter 2: Memory & File Systems
CHAPTERS_TOC_CD_OS[("OS", 2)] = {
    "sub_id": "OS",
    "chap_idx": 2,
    "title": "Memory Management, Virtual Memory & File Systems",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Library Study Desk vs Dark Basement (Paging & Page Fault)",
            "text": "A college library has 100,000 books in the basement, but your study desk only fits 4 books (RAM Frames). If the chapter you need is on the desk -> Page Hit (1 second). If the book is down in the cold basement -> Page Fault: reading pauses, the librarian rides the slow elevator, retrieves the book, and puts it on your desk (takes 10 milliseconds = 10,000,000 nanoseconds!)."
        },
        {
            "title": "Real-Life Example 2: The Bigger Parking Lot Paradox (Belady's Anomaly)",
            "text": "Normally, adding more capacity helps. But under FIFO page replacement, giving a program 4 memory frames instead of 3 can actually CAUSE MORE PAGE FAULTS for certain page sequences! FIFO kicks out pages blindly without knowing if you will need them in the next second."
        },
        {
            "title": "Real-Life Example 3: The Tree of Disk Pointers (UNIX Inode)",
            "text": "A UNIX file has 12 direct pointers (pointing straight to data blocks for small files: instant access). For huge movies, it uses 1 Singly Indirect and 1 Doubly Indirect pointer (a table pointing to tables of blocks), scaling up to Gigabytes effortlessly."
        }
    ],
    "foundations": [
        {
            "number": "28.1",
            "title": "Paging & Effective Memory Access Time (EMAT)",
            "content": (
                "Virtual address is split into: [ Page Number (p) | Offset (d) ].<br/>"
                "• <b>With TLB:</b> EMAT = h × (t_tlb + t_mem) + (1 - h) × (t_tlb + 2 × t_mem).<br/>"
                "• <b>Page Table Size:</b> (Total Pages) × (Page Table Entry Size)."
            ),
            "crucial_rule": "GOLDEN RULE: Watch units in EMAT! Memory access is in nanoseconds (ns), but Page Fault penalty is in MILLISECONDS (ms = 10^6 ns). Convert to the same unit before calculating!"
        },
        {
            "number": "28.2",
            "title": "Page Replacement Algorithms",
            "content": (
                "• <b>FIFO:</b> Replaces oldest page. Suffers from Belady's anomaly.<br/>"
                "• <b>Optimal:</b> Replaces page not needed for longest time in FUTURE. Minimum page faults, but impossible in practice.<br/>"
                "• <b>LRU:</b> Replaces page not used for longest time in PAST. Stack algorithm: <b>IMMUNE to Belady's Anomaly</b>."
            ),
            "crucial_rule": "GOLDEN RULE: LRU and Optimal algorithms can NEVER suffer from Belady's Anomaly!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: EMAT Calculation",
            "problem": "TLB search time = 20 ns, Main memory access time = 100 ns. TLB hit ratio = 90%. What is the Effective Memory Access Time?",
            "steps": [
                "Step 1: On Hit (90%): TLB search + 1 memory access = 20 + 100 = 120 ns.",
                "Step 2: On Miss (10%): TLB search + Page Table memory access + Data memory access = 20 + 100 + 100 = 220 ns.",
                "Step 3: EMAT = (0.90 × 120 ns) + (0.10 × 220 ns) = 108 + 22 = 130 ns."
            ],
            "answer": "EMAT = 130 ns."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Internal vs External Fragmentation",
            "warning": "Paging eliminates External Fragmentation completely! But it can still suffer from Internal Fragmentation in the very last page of a process."
        }
    ]
}
