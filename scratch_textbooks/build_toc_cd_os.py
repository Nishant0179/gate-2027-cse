# scratch_textbooks/build_toc_cd_os.py
# Generates comprehensive, ChatGPT-style, point-by-point tutorials for TOC, Compiler Design & OS (9 Chapters).

import os
import pprint

CHAPTERS_TOC_CD_OS = {
    ('TOC', 0): {
        "chapter_number": 20,
        "title": "Finite Automata, Regular Expressions & Minimization",
        "foundations": [
            {
                "number": "20.1",
                "title": "DFA vs NFA: Equivalences, Power & State Bounds",
                "content": """• <b>Formal Definitions of Finite Automata:</b><br/>
&nbsp;&nbsp;Both DFA and NFA are 5-tuples: <code>(Q, Σ, δ, q₀, F)</code>.<br/>
&nbsp;&nbsp;• <b>DFA Transition:</b> <code>δ: Q × Σ → Q</code> (Deterministic: exactly 1 transition for every state-input pair).<br/>
&nbsp;&nbsp;• <b>NFA Transition:</b> <code>δ: Q × (Σ ∪ {ε}) → 2^Q</code> (Can transition to zero, one, or multiple states, or via ε-moves).<br/><br/>

• <b>Equivalence & Power:</b><br/>
&nbsp;&nbsp;• <b>DFA and NFA have the EXACT SAME EXPRESSIVE POWER!</b> Both recognize exactly the class of <b>Regular Languages</b>.<br/>
&nbsp;&nbsp;• <b>Subset Construction (Power Set Construction):</b> Converts an n-state NFA into an equivalent DFA.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;- Maximum states in equivalent DFA = <b>2ⁿ</b>.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;- Minimum states in equivalent DFA = <b>1</b> (e.g., if language is Σ*).<br/><br/>

• <b>Standard NFA to DFA State Bounds Tested in GATE:</b><br/>
&nbsp;&nbsp;• Language of strings where the <b>n-th symbol from the end</b> is 'a':<br/>
&nbsp;&nbsp;&nbsp;&nbsp;- NFA requires: <code>n + 1</code> states.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;- Minimal DFA requires: strictly <b>2ⁿ states</b> (Exponential blowup!).<br/>
&nbsp;&nbsp;• Language of strings where the <b>n-th symbol from the beginning</b> is 'a':<br/>
&nbsp;&nbsp;&nbsp;&nbsp;- Both NFA and DFA require: <code>n + 2</code> states.""",
                "crucial_rule": "🎯 GOLDEN RULE FOR GATE: Minimal DFA for any regular language is 100% UNIQUE up to state renaming (isomorphism)! Minimal NFA is NOT necessarily unique."
            },
            {
                "number": "20.2",
                "title": "DFA Minimization: Myhill-Nerode & Table-Filling Method",
                "content": """• <b>Two States are Distinguishable:</b><br/>
&nbsp;&nbsp;Two states p and q are distinguishable if there exists some string w ∈ Σ* such that δ(p, w) ∈ F and δ(q, w) ∉ F (one state accepts, the other rejects).<br/><br/>

• <b>Table-Filling Algorithm (Myhill-Nerode Theorem):</b><br/>
&nbsp;&nbsp;1. Remove all <b>unreachable states</b> from the start state q₀ (Dead code elimination).<br/>
&nbsp;&nbsp;2. Set up a triangular grid for all pairs {p, q}.<br/>
&nbsp;&nbsp;3. <b>Base Step:</b> Mark {p, q} if one is accepting (F) and the other is non-accepting (Q \\ F).<br/>
&nbsp;&nbsp;4. <b>Inductive Step:</b> For unmarked {p, q}, if for any input symbol a ∈ Σ the pair {δ(p, a), δ(q, a)} is already marked, then mark {p, q}!<br/>
&nbsp;&nbsp;5. Repeat until no more marks are added. Unmarked pairs are <b>EQUIVALENT</b> and can be merged into a single state!""",
                "crucial_rule": "🎯 GOLDEN RULE FOR GATE: Myhill-Nerode Theorem states that a language L is regular if and only if the number of equivalence classes of its indistinguishability relation RL is FINITE. The number of equivalence classes equals the number of states in the minimal DFA!"
            },
            {
                "number": "20.3",
                "title": "Closure Properties & Decidability of Regular Languages",
                "content": """• <b>Closure Properties of Regular Languages:</b><br/>
&nbsp;&nbsp;Regular languages are <b>CLOSED UNDER ALL STANDARD OPERATIONS</b>:<br/>
&nbsp;&nbsp;• Union, Intersection, Complement, Difference, Concatenation, Kleene Star (*), Reversal, Homomorphism, Inverse Homomorphism.<br/><br/>

• <b>Decidability Matrix for Regular Languages:</b><br/>
&nbsp;&nbsp;<b>ALL questions are DECIDABLE for Regular Languages!</b><br/>
&nbsp;&nbsp;• <b>Emptiness (L = ∅?):</b> Decidable (check if any final state is reachable from q₀ via BFS/DFS).<br/>
&nbsp;&nbsp;• <b>Finiteness (Is L finite?):</b> Decidable (check for cycles in paths leading to an accepting state).<br/>
&nbsp;&nbsp;• <b>Equivalence (L₁ = L₂?):</b> Decidable (construct DFA for (L₁ ∩ L₂') ∪ (L₁' ∩ L₂) and test if empty).<br/>
&nbsp;&nbsp;• <b>Universality (L = Σ*?):</b> Decidable (minimize DFA and check if it has 1 accepting state with self-loops).""",
                "crucial_rule": "🎯 GOLDEN RULE FOR GATE: If L₁ is Regular and L₂ is NOT Regular: L₁ ∪ L₂ may or may not be regular (e.g. Σ* ∪ non-regular = Σ*, which is regular). But L₁ ∩ L₂ is bounded by the regular set."
            }
        ],
        "worked_examples": [
            {
                "title": "Worked Example: Minimal DFA States for Modulo Counting",
                "problem": "How many states are in the minimal DFA that accepts all binary strings whose decimal value is divisible by 5?",
                "steps": [
                    "Step 1: A binary number divisible by 5 has remainder r ∈ {0, 1, 2, 3, 4} when divided by 5.",
                    "Step 2: Each distinct remainder modulo 5 represents a unique equivalence class in Myhill-Nerode relation.",
                    "Step 3: Define transition: Reading bit b transforms value V to 2V + b. Hence next state is (2r + b) mod 5.",
                    "Step 4: All 5 states (remainders 0, 1, 2, 3, 4) are reachable and pairwise distinguishable.",
                    "Step 5: The accepting state is remainder 0. Total states = 5."
                ],
                "answer": "Exactly 5 states in the minimal DFA."
            }
        ],
        "exam_traps": [
            {
                "title": "Dead State Omission Trap in DFA Count",
                "warning": "In a DFA, EVERY state must have an outgoing transition for EVERY input symbol! Incomplete transitions must route to a Dead/Trap state. Do not forget to count the trap state in DFA state counts."
            }
        ],
        "real_life_examples": [
            {
                "title": "Real-Life Analogy: Vending Machine Controller",
                "text": "A vending machine is a finite automaton. Depositing coins transitions between states (10¢, 20¢, 50¢). Once the total reaches 50¢, the accepting state dispenses the beverage."
            }
        ]
    },

    ('TOC', 1): {
        "chapter_number": 21,
        "title": "Grammars, Pushdown Automata & Pumping Lemma",
        "foundations": [
            {
                "number": "21.1",
                "title": "Context-Free Grammars (CFG) & Ambiguity",
                "content": """• <b>Context-Free Grammar (CFG):</b> 4-tuple <code>(V, Σ, R, S)</code> where productions have single non-terminal on LHS: <code>A → α</code>.<br/><br/>

• <b>Ambiguity in Grammars:</b><br/>
&nbsp;&nbsp;• A grammar is <b>Ambiguous</b> if there exists at least one string w ∈ L(G) that has:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;1. More than one <b>Leftmost Derivation</b> (LMD), OR<br/>
&nbsp;&nbsp;&nbsp;&nbsp;2. More than one <b>Rightmost Derivation</b> (RMD), OR<br/>
&nbsp;&nbsp;&nbsp;&nbsp;3. More than one distinct <b>Parse Tree</b>.<br/>
&nbsp;&nbsp;• <b>Inherent Ambiguity:</b> A CFL is <i>Inherently Ambiguous</i> if EVERY grammar generating it is ambiguous (e.g. L = {aⁿ bⁿ cᵐ} ∪ {aⁿ bᵐ cᵐ}).<br/>
&nbsp;&nbsp;• <b>Decidability:</b> Checking whether an arbitrary CFG is ambiguous is <b>UNDECIDABLE</b>!""",
                "crucial_rule": "🎯 GOLDEN RULE FOR GATE: Classical ambiguous grammar: E → E + E | E * E | id. To remove ambiguity, introduce precedence levels (Terms for *, Factors for primary operands) and left-associativity."
            },
            {
                "number": "21.2",
                "title": "Pushdown Automata: DPDA vs NPDA",
                "content": """• <b>PDA Mechanics:</b> Finite Automaton + 1 infinite Stack (LIFO memory).<br/><br/>

• <b>DPDA vs NPDA (CRITICAL DIFFERENCE):</b><br/>
&nbsp;&nbsp;• <b>DPDA (Deterministic PDA):</b> At any state, for any input and stack top, at most ONE move is possible. Recognizes <b>Deterministic Context-Free Languages (DCFL)</b>.<br/>
&nbsp;&nbsp;• <b>NPDA (Non-Deterministic PDA):</b> Multiple transitions allowed. Recognizes ALL <b>Context-Free Languages (CFL)</b>.<br/>
&nbsp;&nbsp;• <b>Expressive Power:</b> <code>DCFL ⊂ CFL</code> (Strict subset! Unlike finite automata, NPDA is strictly MORE powerful than DPDA!).<br/>
&nbsp;&nbsp;• <i>Classic Example:</i><br/>
&nbsp;&nbsp;&nbsp;&nbsp;- Even palindrome with center marker <code>L = {w c wᴿ | w ∈ {a, b}*}</code> is in <b>DCFL</b> (DPDA knows when to reverse via 'c').<br/>
&nbsp;&nbsp;&nbsp;&nbsp;- Unmarked even palindrome <code>L = {w wᴿ | w ∈ {a, b}*}</code> is in <b>CFL but NOT DCFL</b> (requires non-deterministic guessing of midpoint!).""",
                "crucial_rule": "🎯 GOLDEN RULE FOR GATE: DCFL is CLOSED under Complement! CFL is NOT closed under Complement or Intersection."
            },
            {
                "number": "21.3",
                "title": "Pumping Lemma for CFLs & Non-CFL Proofs",
                "content": """• <b>Pumping Lemma Statement for CFL:</b><br/>
&nbsp;&nbsp;If L is a CFL, there exists a pumping length p such that any string s ∈ L with |s| ≥ p can be partitioned as <code>s = u v x y z</code> such that:<br/>
&nbsp;&nbsp;1. <code>|v y| ≥ 1</code> (At least one of v or y is non-empty).<br/>
&nbsp;&nbsp;2. <code>|v x y| ≤ p</code>.<br/>
&nbsp;&nbsp;3. For all i ≥ 0, <code>u vⁱ x yⁱ z ∈ L</code>.<br/><br/>

• <b>Classic Non-CFL Languages (Memorize for GATE):</b><br/>
&nbsp;&nbsp;• <code>L = {aⁿ bⁿ cⁿ | n ≥ 1}</code> (NOT a CFL - requires matching 3 counts simultaneously).<br/>
&nbsp;&nbsp;• <code>L = {aⁿ bᵐ cⁿ dᵐ}</code> (NOT a CFL - interleaved dependencies).<br/>
&nbsp;&nbsp;• <code>L = {w w | w ∈ {a, b}*}</code> (NOT a CFL - requires queue, not stack).<br/>
&nbsp;&nbsp;• <code>L = {a^(p) | p is a prime}</code> (NOT a CFL).""",
                "crucial_rule": "🎯 GOLDEN RULE FOR GATE: A stack can only compare TWO counts simultaneously (e.g. {aⁿ bⁿ}). To compare 3 counts ({aⁿ bⁿ cⁿ}), you need a Turing Machine!"
            }
        ],
        "worked_examples": [
            {
                "title": "Worked Example: Classifying Language L = {aⁿ bⁿ cᵐ dᵐ}",
                "problem": "Identify the type of language: L = {aⁿ bⁿ cᵐ dᵐ | n, m ≥ 1}. Is it Regular, DCFL, or non-CFL?",
                "steps": [
                    "Step 1: Notice the structure: a block of a's followed by b's (with equal counts n), then c's followed by d's (with equal counts m).",
                    "Step 2: A PDA can push a's on stack, pop a's against b's until stack is empty. Then push c's on stack, and pop c's against d's.",
                    "Step 3: Since there is no backtracking or guessing required, a single deterministic stack can recognize it.",
                    "Step 4: It cannot be regular because n and m are unbounded (requires counting).",
                    "Step 5: Therefore, L is a Deterministic Context-Free Language (DCFL)."
                ],
                "answer": "L is a DCFL (Deterministic Context-Free Language)."
            }
        ],
        "exam_traps": [
            {
                "title": "Intersection of Two CFLs Trap",
                "warning": "L₁ = {aⁿ bⁿ cᵐ} is CFL. L₂ = {aᵐ bⁿ cⁿ} is CFL. But their intersection L₁ ∩ L₂ = {aⁿ bⁿ cⁿ} is NOT a CFL! CFLs are not closed under intersection."
            }
        ],
        "real_life_examples": [
            {
                "title": "Real-Life Analogy: HTML Tag Matching",
                "text": "Validating balanced HTML tags (<div><p></p></div>) is a context-free grammar handled by a PDA stack. Every opening tag is pushed and matched by a closing tag."
            }
        ]
    },

    ('TOC', 2): {
        "chapter_number": 22,
        "title": "Turing Machines, Chomsky Hierarchy & Undecidability",
        "foundations": [
            {
                "number": "22.1",
                "title": "The Chomsky Hierarchy of Languages",
                "content": """• <b>Chomsky Hierarchy Master Classification:</b><br/>
<div class='font-mono text-xs p-3 bg-slate-900 text-slate-100 rounded-xl my-2 leading-relaxed overflow-x-auto'>
Type   │ Language Class                   │ Automaton Machine                 │ Production Grammar Rules
──────────────────────────────────────────────────────────────────────────────────────────────────────────
Type-3 │ Regular                          │ Deterministic Finite Automata (DFA)│ A → aB or A → a (Right linear)
Type-2 │ Context-Free (CFL)               │ Non-Deterministic Pushdown (NPDA) │ A → α (Single non-terminal LHS)
Type-1 │ Context-Sensitive (CSL)          │ Linear Bounded Automata (LBA)     │ α → β with |α| ≤ |β| (Non-contracting)
Type-0 │ Recursively Enumerable (RE)      │ Turing Machine (TM)               │ α → β (No restrictions)
</div>

• <b>Subsets Inclusion:</b><br/>
&nbsp;&nbsp;<code>Regular ⊂ DCFL ⊂ CFL ⊂ CSL ⊂ Recursive (REC) ⊂ Recursively Enumerable (RE)</code>.""",
                "crucial_rule": "🎯 GOLDEN RULE FOR GATE: Recursive (REC / Turing Decidable) languages are HALTING Turing Machines (always halts with Yes or No). Recursively Enumerable (RE / Turing Recognizable) may loop infinitely on negative inputs!"
            },
            {
                "number": "22.2",
                "title": "Turing Halting Problem & Undecidability",
                "content": """• <b>What is a Decidable Problem?</b> A problem is decidable if there exists an algorithm (Turing machine that halts on ALL inputs) that answers Yes or No correctly.<br/><br/>

• <b>Turing Halting Problem (HP):</b><br/>
&nbsp;&nbsp;<i>'Given an arbitrary program M and input w, does M halt on w?'</i><br/>
&nbsp;&nbsp;• Proven <b>UNDECIDABLE</b> by Alan Turing using Cantor's Diagonalization Argument!<br/>
&nbsp;&nbsp;• It is <b>Semi-Decidable (RE)</b>, but NOT Decidable.<br/><br/>

• <b>Rice's Theorem (GATE Holy Grail for Undecidability):</b><br/>
&nbsp;&nbsp;<i>'Any non-trivial semantic property of the language recognized by a Turing Machine is UNDECIDABLE!'</i><br/>
&nbsp;&nbsp;• <b>Semantic Property:</b> A property of the LANGUAGE L(M) recognized (e.g., Is L(M) empty? Is L(M) finite? Is L(M) regular?).<br/>
&nbsp;&nbsp;• <b>Non-trivial:</b> Holds for some TMs and does not hold for others.<br/>
&nbsp;&nbsp;• <b>Rice's Theorem Verdict:</b> ALL such questions: 'Is L(M) empty?', 'Is L(M) = Σ*?', 'Is L(M) regular?' are strictly <b>UNDECIDABLE</b>!""",
                "crucial_rule": "🎯 GOLDEN RULE FOR GATE: Rice's Theorem applies ONLY to semantic properties of the language L(M)! Syntactic properties of the machine itself (e.g. 'Does TM M have 5 states?', 'Does M take >10 steps on input w?') are DECIDABLE."
            }
        ],
        "worked_examples": [
            {
                "title": "Worked Example: Applying Rice's Theorem",
                "problem": "Determine whether the following problem is Decidable: Given a Turing Machine M, is the language accepted by M, L(M), a regular language?",
                "steps": [
                    "Step 1: Check if this is a property of the language L(M). Yes, 'is L(M) regular' depends on the language accepted, not the machine description.",
                    "Step 2: Check if the property is non-trivial: (a) There exist TMs whose language is regular (e.g., L(M) = {a}*). (b) There exist TMs whose language is not regular (e.g., L(M) = {aⁿ bⁿ}).",
                    "Step 3: Since it is a non-trivial semantic property of the language of a TM, apply Rice's Theorem directly.",
                    "Step 4: By Rice's Theorem, the problem is UNDECIDABLE."
                ],
                "answer": "The problem is UNDECIDABLE."
            }
        ],
        "exam_traps": [
            {
                "title": "Complement of RE Languages Trap",
                "warning": "If language L is RE and its complement ~L is ALSO RE, then L is guaranteed to be RECURSIVE (Decidable)! If L is RE but undecidable (like Halting Problem), its complement ~L is strictly NOT RE."
            }
        ],
        "real_life_examples": [
            {
                "title": "Real-Life Analogy: The Antivirus Infinite Loop Checker",
                "text": "Writing an antivirus software that can guarantee whether ANY arbitrary computer program will ever freeze or terminate is mathematically impossible due to the Turing Halting Problem."
            }
        ]
    },

    ('CD', 0): {
        "chapter_number": 23,
        "title": "Lexical Analysis & Top-Down Parsing (LL(1))",
        "foundations": [
            {
                "number": "23.1",
                "title": "Lexical Tokens & Calculating FIRST and FOLLOW Sets",
                "content": """• <b>Lexical Analysis (Scanner):</b> Reads stream of characters and groups them into <b>Tokens</b> using Regular Expressions and DFA. Strips comments and whitespace.<br/><br/>

• <b>Rules for Calculating FIRST(X):</b><br/>
&nbsp;&nbsp;1. If X is a terminal: <code>FIRST(X) = {X}</code>.<br/>
&nbsp;&nbsp;2. If X → ε is a production: add ε to FIRST(X).<br/>
&nbsp;&nbsp;3. If X → Y₁ Y₂ ... Yₖ: add FIRST(Y₁) \\ {ε} to FIRST(X). If Y₁ derives ε, add FIRST(Y₂) \\ {ε}, and so forth until some Yᵢ does not derive ε. If all derive ε, add ε.<br/><br/>

• <b>Rules for Calculating FOLLOW(A) (Applies ONLY to Non-Terminals!):</b><br/>
&nbsp;&nbsp;1. Add <code>$</code> (end of input marker) to <code>FOLLOW(S)</code> (Start Symbol).<br/>
&nbsp;&nbsp;2. If production <code>A → α B β</code>: everything in <code>FIRST(β) \\ {ε}</code> is in <code>FOLLOW(B)</code>.<br/>
&nbsp;&nbsp;3. If production <code>A → α B</code> OR <code>A → α B β</code> where <code>β ⇒* ε</code>: everything in <code>FOLLOW(A)</code> is in <code>FOLLOW(B)</code>!""",
                "crucial_rule": "🎯 GOLDEN RULE FOR GATE: FOLLOW set can NEVER contain the empty string ε! If ε appears in your FOLLOW set calculation, you made an error."
            },
            {
                "number": "23.2",
                "title": "LL(1) Parser Conditions & Grammatical Disqualifiers",
                "content": """• <b>What is LL(1)?</b> Left-to-right scan, Leftmost derivation, 1 lookahead token.<br/><br/>

• <b>Conditions for a Grammar to be LL(1):</b><br/>
&nbsp;&nbsp;For every production with multiple choices <code>A → α | β</code>:<br/>
&nbsp;&nbsp;1. <code>FIRST(α) ∩ FIRST(β) = ∅</code> (No common prefix).<br/>
&nbsp;&nbsp;2. At most one of α or β can derive ε.<br/>
&nbsp;&nbsp;3. If <code>β ⇒* ε</code>, then <code>FIRST(α) ∩ FOLLOW(A) = ∅</code>.<br/><br/>

• <b>Instant LL(1) Disqualifiers (Must-Know for GATE):</b><br/>
&nbsp;&nbsp;• <b>Left Recursive Grammar:</b> <code>A → Aα</code> can NEVER be LL(1)! Must eliminate left recursion first.<br/>
&nbsp;&nbsp;• <b>Ambiguous Grammar:</b> Can NEVER be LL(1)!<br/>
&nbsp;&nbsp;• <b>Non-Deterministic (Common Prefix):</b> <code>A → aB | aC</code> can NEVER be LL(1)! Must left-factor first.""",
                "crucial_rule": "🎯 GOLDEN RULE FOR GATE: In the LL(1) parse table, if any cell [A, a] contains MULTIPLE production entries, the grammar is NOT LL(1)!"
            }
        ],
        "worked_examples": [
            {
                "title": "Worked Example: Computing FIRST and FOLLOW Sets",
                "problem": "Given grammar: S → ABc, A → a | ε, B → b | ε. Compute FIRST(S) and FOLLOW(A).",
                "steps": [
                    "Step 1: Calculate FIRST(A) = {a, ε}. Calculate FIRST(B) = {b, ε}.",
                    "Step 2: For S → ABc: FIRST(S) includes FIRST(A)\\{ε} = {a}. Since A can be ε, include FIRST(B)\\{ε} = {b}. Since B can also be ε, include terminal 'c'. So FIRST(S) = {a, b, c}.",
                    "Step 3: For FOLLOW(A): Look where A appears on RHS: S → ABc. Here A is followed by Bc. So FOLLOW(A) includes FIRST(Bc)\\{ε} = FIRST(B)\\{ε} ∪ {c} = {b, c}.",
                    "Step 4: Check if Bc can derive ε: Bc has terminal 'c', so it cannot derive ε. Hence FOLLOW(S) is not added."
                ],
                "answer": "FIRST(S) = {a, b, c}, FOLLOW(A) = {b, c}."
            }
        ],
        "exam_traps": [
            {
                "title": "Left Recursion Elimination Formula Trap",
                "warning": "To eliminate A → Aα | β: rewrite as A → β A' and A' → α A' | ε. Notice β comes FIRST! If you write A → α A', the language is ruined."
            }
        ],
        "real_life_examples": [
            {
                "title": "Real-Life Analogy: JSON Parser Lookahead",
                "text": "An LL(1) parser is like reading JSON: looking at the single next character ('{' or '[') immediately tells the parser whether to parse an Object or an Array."
            }
        ]
    },

    ('CD', 1): {
        "chapter_number": 24,
        "title": "Bottom-Up Parsing (LR Parsers) & Parser Comparisons",
        "foundations": [
            {
                "number": "24.1",
                "title": "Shift-Reduce Parsing & The 4 LR Parsers",
                "content": """• <b>Bottom-Up Parsing Mechanics:</b><br/>
&nbsp;&nbsp;- Constructs parse tree from the leaves (tokens) up to the root (Start symbol).<br/>
&nbsp;&nbsp;- Traces a <b>Rightmost Derivation in REVERSE</b>!<br/>
&nbsp;&nbsp;- Actions: <b>Shift</b> (push token to stack), <b>Reduce</b> (replace handle with LHS non-terminal), <b>Accept</b>, <b>Error</b>.<br/><br/>

• <b>The 4 LR Parsers Compared:</b><br/>
<div class='font-mono text-xs p-3 bg-slate-900 text-slate-100 rounded-xl my-2 leading-relaxed overflow-x-auto'>
Parser   │ Item Type Used │ Reduce Action Placed In                  │ States Count Comparison
─────────────────────────────────────────────────────────────────────────────────────────────
LR(0)    │ [A → α · β]    │ In ALL input cells of that state row     │ Smallest (Base DFA)
SLR(1)   │ [A → α · β]    │ ONLY in FOLLOW(A) cells of that row      │ Identical to LR(0) states!
LALR(1)  │ [A → α · β, a] │ ONLY in lookahead 'a' cells              │ Identical to LR(0) states! (Merged)
CLR(1)   │ [A → α · β, a] │ ONLY in lookahead 'a' cells              │ Largest number of states!
</div>

• <b>Parser Power Hierarchy (Strict Inclusions):</b><br/>
&nbsp;&nbsp;<code>LR(0) ⊂ SLR(1) ⊂ LALR(1) ⊂ CLR(1)</code> and <code>LL(1) ⊂ LALR(1) ⊂ CLR(1)</code>.<br/>
&nbsp;&nbsp;• CLR(1) is the most powerful deterministic parser, but requires massive state tables.<br/>
&nbsp;&nbsp;• LALR(1) merges states of CLR(1) that have identical LR(0) cores, preserving table size while keeping high parsing power!""",
                "crucial_rule": "🎯 GOLDEN RULE FOR GATE: Merging CLR(1) states to form LALR(1) can NEVER create a Shift-Reduce (S-R) conflict! However, it CAN potentially introduce Reduce-Reduce (R-R) conflicts."
            },
            {
                "number": "24.2",
                "title": "Shift-Reduce and Reduce-Reduce Conflicts",
                "content": """• <b>Shift-Reduce (S-R) Conflict:</b> Occurs when the parser cannot decide whether to shift the next input symbol or reduce the current handle: state has both <code>[A → α · a β]</code> and <code>[B → γ ·]</code>.<br/><br/>

• <b>Reduce-Reduce (R-R) Conflict:</b> Occurs when two distinct productions are ready to be reduced simultaneously in the same state: state has both <code>[A → α ·]</code> and <code>[B → β ·]</code>.""",
                "crucial_rule": "🎯 GOLDEN RULE FOR GATE: An ambiguous grammar can NEVER be parsed by ANY LR parser (LR(0), SLR(1), LALR(1), CLR(1)) because ambiguity inherently creates unresolvable conflicts!"
            }
        ],
        "worked_examples": [
            {
                "title": "Worked Example: State Count in SLR(1) vs LALR(1) vs CLR(1)",
                "problem": "If the canonical collection of LR(0) items for a grammar has 15 states, what is the number of states in the SLR(1) parsing table?",
                "steps": [
                    "Step 1: Recall the state count definition for SLR(1).",
                    "Step 2: SLR(1) uses the EXACT same canonical collection of LR(0) items as LR(0). It only changes where reduction actions are placed in the table (placing them in FOLLOW(A) instead of all columns).",
                    "Step 3: Therefore, the number of states in SLR(1) is ALWAYS exactly equal to the number of states in LR(0).",
                    "Step 4: States in SLR(1) = 15."
                ],
                "answer": "Exactly 15 states."
            }
        ],
        "exam_traps": [
            {
                "title": "LALR State Count Assumption Trap",
                "warning": "LALR(1) table size is ALWAYS identical to LR(0) and SLR(1) tables! It never has the larger state count of CLR(1)."
            }
        ],
        "real_life_examples": [
            {
                "title": "Real-Life Analogy: Yacc and Bison Tooling",
                "text": "Unix tools like Yacc and GNU Bison are LALR(1) parser generators because LALR(1) gives the maximum grammar coverage with the minimum table memory."
            }
        ]
    },

    ('CD', 2): {
        "chapter_number": 25,
        "title": "SDT, Intermediate Code & Optimization (Data Flow Analysis)",
        "foundations": [
            {
                "number": "25.1",
                "title": "S-Attributed vs L-Attributed Syntax-Directed Translations",
                "content": """• <b>Synthesized vs Inherited Attributes:</b><br/>
&nbsp;&nbsp;• <b>Synthesized Attribute:</b> Computed from children nodes in parse tree (Bottom-up flow).<br/>
&nbsp;&nbsp;• <b>Inherited Attribute:</b> Computed from parent or sibling nodes (Top-down / Left-to-Right flow).<br/><br/>

• <b>S-Attributed Definition:</b><br/>
&nbsp;&nbsp;- Uses <b>ONLY Synthesized Attributes</b>.<br/>
&nbsp;&nbsp;- Can be naturally evaluated during bottom-up parsing (LR parsers) using stack values!<br/><br/>

• <b>L-Attributed Definition:</b><br/>
&nbsp;&nbsp;- Uses Synthesized attributes AND restricted Inherited attributes.<br/>
&nbsp;&nbsp;- <b>The L-Restriction Rule:</b> In production <code>A → X₁ X₂ ... Xₙ</code>, an inherited attribute of Xᵢ can depend ONLY on:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;1. Attributes of symbols to its <b>LEFT</b> (X₁, X₂, ..., Xᵢ₋₁).<br/>
&nbsp;&nbsp;&nbsp;&nbsp;2. <b>Inherited</b> attributes of parent A.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;- It can NEVER depend on symbols to its right or synthesized attributes of parent A!""",
                "crucial_rule": "🎯 GOLDEN RULE FOR GATE: Every S-Attributed SDD is an L-Attributed SDD (S-Attributed ⊂ L-Attributed). S-attributed SDDs are evaluated during bottom-up LR parsing; L-attributed SDDs are evaluated during depth-first left-to-right traversals."
            },
            {
                "number": "25.2",
                "title": "Code Optimization & Data Flow Analysis",
                "content": """• <b>Machine-Independent Optimizations:</b><br/>
&nbsp;&nbsp;• <b>Constant Folding:</b> Compute compile-time constants: <code>x = 3 + 4</code> becomes <code>x = 7</code>.<br/>
&nbsp;&nbsp;• <b>Constant Propagation:</b> If <code>x = 7</code>, replace subsequent <code>y = x * 2</code> with <code>y = 14</code>.<br/>
&nbsp;&nbsp;• <b>Common Subexpression Elimination:</b> Avoid recomputing identical expressions.<br/>
&nbsp;&nbsp;• <b>Dead Code Elimination:</b> Remove instructions whose results are never read.<br/>
&nbsp;&nbsp;• <b>Loop Invariant Code Motion (Hoisting):</b> Move computations that don't change inside the loop outside before the loop begins.<br/>
&nbsp;&nbsp;• <b>Strength Reduction:</b> Replace expensive operations with cheaper ones (e.g. replace <code>x * 2</code> with <code>x + x</code> or <code>x << 1</code>).<br/><br/>

• <b>Data Flow Analysis Framework:</b><br/>
&nbsp;&nbsp;• <b>Liveness Analysis:</b> A variable is <i>live</i> at point p if its current value may be used along some path starting from p. Computed <b>Backwards</b>.<br/>
&nbsp;&nbsp;• <b>Reaching Definitions:</b> Which definitions d may reach point p. Computed <b>Forwards</b>.""",
                "crucial_rule": "🎯 GOLDEN RULE FOR GATE: Loop Invariant code motion and strength reduction yield the largest asymptotic runtime speedups in compiled binary loops."
            }
        ],
        "worked_examples": [
            {
                "title": "Worked Example: Identifying L-Attributed SDD Violations",
                "problem": "Consider production A → B C with semantic rule: B.in = C.syn + 2. Is this SDD L-Attributed?",
                "steps": [
                    "Step 1: Check attribute types: B.in is an inherited attribute of non-terminal B.",
                    "Step 2: Check dependency: B.in depends on C.syn.",
                    "Step 3: Inspect position in production: Symbol C is to the RIGHT of B in production A → B C.",
                    "Step 4: Recall the L-Attributed definition: An inherited attribute of a symbol can depend ONLY on symbols to its LEFT or inherited attributes of parent.",
                    "Step 5: Since B depends on an attribute to its right (C), it violates the L-attributed condition!"
                ],
                "answer": "NOT L-Attributed (depends on attribute to the right)."
            }
        ],
        "exam_traps": [
            {
                "title": "Three-Address Code Temporary Variable Minimization Trap",
                "warning": "When asked for the MINIMUM number of temporary variables to represent an expression in 3-address code, reuse temporary variables whose values are no longer live!"
            }
        ],
        "real_life_examples": [
            {
                "title": "Real-Life Analogy: GCC -O3 Optimization Flag",
                "text": "The gcc compiler flag -O3 runs all loop optimizations, constant propagation, and dead code elimination to produce blazing fast machine code without altering program behavior."
            }
        ]
    },

    ('OS', 0): {
        "chapter_number": 26,
        "title": "Processes, Threads, Concurrency & Synchronization",
        "foundations": [
            {
                "number": "26.1",
                "title": "The fork() System Call & Process Trees",
                "content": """• <b>How fork() Works:</b><br/>
&nbsp;&nbsp;- Creates a brand new child process that is an EXACT replica of the parent process (copies memory address space, registers, file descriptors).<br/>
&nbsp;&nbsp;- <b>Return Value of fork():</b><br/>
&nbsp;&nbsp;&nbsp;&nbsp;• Returns <b>0</b> to the CHILD process.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;• Returns <b>Child's PID (> 0)</b> to the PARENT process.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;• Returns <b>-1</b> on failure.<br/><br/>

• <b>Number of Processes Created by n Consecutive fork() Calls:</b><br/>
&nbsp;&nbsp;• Total processes = <b>2ⁿ</b>.<br/>
&nbsp;&nbsp;• Number of newly created child processes = <b>2ⁿ - 1</b>.<br/><br/>

• <b>Process Tree Execution Trace with Loops:</b><br/>
&nbsp;&nbsp;In <code>for(int i=0; i<3; i++) fork();</code>:<br/>
&nbsp;&nbsp;- i=0: 1 process becomes 2.<br/>
&nbsp;&nbsp;- i=1: 2 processes become 4.<br/>
&nbsp;&nbsp;- i=2: 4 processes become 8. Total = 2³ = 8 processes!""",
                "crucial_rule": "🎯 GOLDEN RULE FOR GATE: In fork() code with print statements: Unbuffered printf (printf('X\\n')) flushes immediately. Buffered printf without newline (printf('X')) copies the buffered character into the child, causing doubled prints!"
            },
            {
                "number": "26.2",
                "title": "Critical Section Criteria & Peterson's Solution",
                "content": """• <b>The Critical Section Problem:</b> Ensuring multiple concurrent processes access shared resources without race conditions.<br/><br/>

• <b>The 3 Mandatory Criteria for Critical Section:</b><br/>
&nbsp;&nbsp;1. <b>Mutual Exclusion (Mandatory):</b> If process Pi is executing in its critical section, no other process can enter.<br/>
&nbsp;&nbsp;2. <b>Progress (Mandatory):</b> If no process is in critical section, only processes wishing to enter can compete, and decision cannot be postponed indefinitely (NO deadlock!).<br/>
&nbsp;&nbsp;3. <b>Bounded Waiting (Optional for basic correctness, mandatory for fairness):</b> There must be a bound on the number of times other processes can enter before a requesting process is granted entry (NO starvation!).<br/><br/>

• <b>Peterson's Algorithm for 2 Processes:</b><br/>
&nbsp;&nbsp;Uses shared <code>flag[2]</code> (interest) and <code>turn</code> (polite tie-breaker):<br/>
&nbsp;&nbsp;<code>flag[i] = true; turn = j; while (flag[j] && turn == j); // Critical Section flag[i] = false;</code><br/>
&nbsp;&nbsp;Satisfies Mutual Exclusion, Progress, and Bounded Waiting!""",
                "crucial_rule": "🎯 GOLDEN RULE FOR GATE: Strict alternation (using only 'turn' variable) satisfies Mutual Exclusion, but FAILS Progress because a process cannot re-enter if the other process is not interested!"
            },
            {
                "number": "26.3",
                "title": "Counting & Binary Semaphores",
                "content": """• <b>Semaphore Definition:</b> An integer synchronization variable accessed ONLY via two atomic operations:<br/>
&nbsp;&nbsp;• <b>Wait(S) / P(S):</b> <code>S--; if (S < 0) block();</code><br/>
&nbsp;&nbsp;• <b>Signal(S) / V(S):</b> <code>S++; if (S <= 0) wakeup();</code><br/><br/>

• <b>Counting Semaphore Value Interpretation:</b><br/>
&nbsp;&nbsp;• If <code>S > 0</code>: Value represents the number of available resources.<br/>
&nbsp;&nbsp;• If <code>S = 0</code>: All resources in use, no processes waiting.<br/>
&nbsp;&nbsp;• If <code>S < 0</code>: Magnitude <code>|S|</code> represents the <b>exact number of processes currently blocked in the waiting queue</b>!""",
                "crucial_rule": "🎯 GOLDEN RULE FOR GATE: If a counting semaphore is initialized to 10, and 6 Wait operations and 2 Signal operations are performed: Current value = 10 - 6 + 2 = 6."
            }
        ],
        "worked_examples": [
            {
                "title": "Worked Example: Counting fork() Child Processes",
                "problem": "How many total processes are created by the following C code?\\n\\nint main() {\\n    fork();\\n    if (fork() == 0) {\\n        fork();\\n    }\\n    return 0;\\n}",
                "steps": [
                    "Step 1: Start with 1 original parent process P₀.",
                    "Step 2: First fork(): P₀ creates child C₁. Now 2 processes exist: {P₀, C₁}.",
                    "Step 3: Second fork() called by both P₀ and C₁: P₀ creates C₂, and C₁ creates C₃. Now 4 processes exist: {P₀, C₁, C₂, C₃}.",
                    "Step 4: Check if condition (fork() == 0): This evaluates to True ONLY in the newly created child processes (C₂ and C₃).",
                    "Step 5: Third fork() is executed ONLY by C₂ and C₃: C₂ creates child C₄, and C₃ creates child C₅.",
                    "Step 6: Total processes = 4 + 2 = 6 processes."
                ],
                "answer": "Total 6 processes created."
            }
        ],
        "exam_traps": [
            {
                "title": "Counting Semaphore Sign Value Trap",
                "warning": "When S is negative (e.g. S = -4), there are 4 processes in the blocked queue! Do not confuse negative semaphore values with errors."
            }
        ],
        "real_life_examples": [
            {
                "title": "Real-Life Analogy: The Restaurant Restroom Key",
                "text": "A binary semaphore is a single restroom key hanging on the restaurant wall. If the hook is empty, you must wait until the occupant returns the key."
            }
        ]
    },

    ('OS', 1): {
        "chapter_number": 27,
        "title": "CPU Scheduling, I/O Scheduling & Deadlocks",
        "foundations": [
            {
                "number": "27.1",
                "title": "CPU Scheduling Algorithms & Gantt Chart Tracing",
                "content": """• <b>Scheduling Metrics:</b><br/>
&nbsp;&nbsp;• <b>Turnaround Time (TAT):</b> <code>Completion Time - Arrival Time</code>.<br/>
&nbsp;&nbsp;• <b>Waiting Time (WT):</b> <code>Turnaround Time - Burst Time</code>.<br/>
&nbsp;&nbsp;• <b>Response Time (RT):</b> Time from arrival to first execution on CPU.<br/><br/>

• <b>Master Comparison of Scheduling Algorithms:</b><br/>
<div class='font-mono text-xs p-3 bg-slate-900 text-slate-100 rounded-xl my-2 leading-relaxed overflow-x-auto'>
Algorithm                      │ Preemptive? │ Optimal For                  │ Major Weakness / Pitfall
───────────────────────────────────────────────────────────────────────────────────────────────────────
FCFS (First-Come, First-Served)│ NO          │ Simple batch systems         │ Convoy Effect (Long process blocks short)
SJF (Shortest Job First)       │ NO          │ Minimizing Average WT!       │ Starvation of long burst jobs
SRTF (Shortest Remaining Time) │ YES         │ Minimizing Average WT!       │ Starvation & high context switch overhead
Round Robin (RR)               │ YES         │ Time-sharing / Response Time │ High context switches if quantum too small
Priority Scheduling            │ Either      │ Mission-critical tasks       │ Starvation (Solved via Aging)
</div>""",
                "crucial_rule": "🎯 GOLDEN RULE FOR GATE: SJF / SRTF gives the absolute theoretical MINIMUM average waiting time among all scheduling algorithms! In Round Robin, if Time Quantum q ≥ max(Burst Times), RR degenerates into FCFS."
            },
            {
                "number": "27.2",
                "title": "Deadlock Characterization & Banker's Algorithm",
                "content": """• <b>The 4 Coffman Conditions (Must ALL hold simultaneously for Deadlock):</b><br/>
&nbsp;&nbsp;1. <b>Mutual Exclusion:</b> Non-shareable resource mode.<br/>
&nbsp;&nbsp;2. <b>Hold and Wait:</b> Process holds resources while requesting additional ones.<br/>
&nbsp;&nbsp;3. <b>No Preemption:</b> Resources cannot be forcibly seized.<br/>
&nbsp;&nbsp;4. <b>Circular Wait:</b> Circular chain of processes where each holds a resource requested by next.<br/><br/>

• <b>Banker's Algorithm (Deadlock Avoidance):</b><br/>
&nbsp;&nbsp;• <b>Need Matrix Formula:</b> <code>Need[i, j] = Max[i, j] - Allocation[i, j]</code>.<br/>
&nbsp;&nbsp;• <b>Safety Check:</b> Find a process whose <code>Need ≤ Available</code>. Assume it finishes, release its allocated resources back to <code>Available = Available + Allocation</code>, and repeat.<br/>
&nbsp;&nbsp;• If all processes finish: State is <b>SAFE</b>! If not: State is <b>UNSAFE</b> (may lead to deadlock).""",
                "crucial_rule": "🎯 GOLDEN RULE FOR GATE: An UNSAFE state is NOT necessarily a Deadlock! Safe state guarantees NO deadlock. Unsafe state means deadlock is possible if worst-case requests occur."
            }
        ],
        "worked_examples": [
            {
                "title": "Worked Example: Round Robin Waiting Time Calculation",
                "problem": "Processes P1, P2, P3 arrive at time 0 with burst times 10, 4, 2 ms. The Round Robin time quantum is 2 ms. Find the average waiting time.",
                "steps": [
                    "Step 1: Trace Gantt chart with time quantum = 2 ms:",
                    "  [0-2: P1] (rem 8), [2-4: P2] (rem 2), [4-6: P3] (finishes at 6!),",
                    "  [6-8: P1] (rem 6), [8-10: P2] (finishes at 10!),",
                    "  [10-12: P1] (rem 4), [12-14: P1] (rem 2), [14-16: P1] (finishes at 16!).",
                    "Step 2: Completion Times: P3 = 6 ms, P2 = 10 ms, P1 = 16 ms.",
                    "Step 3: Turnaround Times (CT - AT): P1 = 16 - 0 = 16, P2 = 10 - 0 = 10, P3 = 6 - 0 = 6.",
                    "Step 4: Waiting Times (TAT - BT): P1 = 16 - 10 = 6, P2 = 10 - 4 = 6, P3 = 6 - 2 = 4.",
                    "Step 5: Average Waiting Time = (6 + 6 + 4) / 3 = 16 / 3 = 5.33 ms."
                ],
                "answer": "Average Waiting Time = 5.33 ms."
            }
        ],
        "exam_traps": [
            {
                "title": "Banker's Algorithm Resource Request Check Trap",
                "warning": "When evaluating a Resource Request, you MUST check BOTH: (1) Request ≤ Need, AND (2) Request ≤ Available! If either fails, the process must wait immediately."
            }
        ],
        "real_life_examples": [
            {
                "title": "Real-Life Analogy: The Four-Way Traffic Gridlock",
                "text": "Deadlock circular wait is a 4-way intersection where 4 cars turn right simultaneously: each car occupies one lane and waits for the next car to move, freezing traffic forever."
            }
        ]
    },

    ('OS', 2): {
        "chapter_number": 28,
        "title": "Memory Management, Virtual Memory & File Systems",
        "foundations": [
            {
                "number": "28.1",
                "title": "Paging & Effective Memory Access Time (EMAT) with TLB",
                "content": """• <b>Paging Architecture:</b><br/>
&nbsp;&nbsp;• Logical Address broken into: <code>[ Page Number (p) | Page Offset (d) ]</code>.<br/>
&nbsp;&nbsp;• Page Size = Frame Size = <code>2ᵈ bytes</code>.<br/>
&nbsp;&nbsp;• Number of Pages = <code>Logical Address Space / Page Size</code>.<br/>
&nbsp;&nbsp;• <b>Page Table Size:</b> <code>(Number of Pages) × (Page Table Entry Size)</code>.<br/><br/>

• <b>Effective Memory Access Time (EMAT) with TLB:</b><br/>
&nbsp;&nbsp;Let c = TLB lookup time, m = Main Memory access time, h = TLB hit ratio.<br/>
&nbsp;&nbsp;• <b>Formula:</b> <code>EMAT = h × (c + m) + (1 - h) × (c + 2m)</code><br/>
&nbsp;&nbsp;&nbsp;&nbsp;- On TLB Hit: 1 TLB lookup + 1 memory access to fetch data.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;- On TLB Miss: 1 TLB lookup + 1 memory access to read Page Table + 1 memory access to fetch data.<br/><br/>

• <b>Two-Level Paging EMAT Formula:</b><br/>
&nbsp;&nbsp;<code>EMAT = h × (c + m) + (1 - h) × (c + 3m)</code> (3 memory reads: Outer Page Table, Inner Page Table, Actual Data).""",
                "crucial_rule": "🎯 GOLDEN RULE FOR GATE: In n-level paging, a TLB miss requires (n + 1) memory accesses! On a 4-level paging system (like x86-64), a TLB miss requires 5 memory accesses."
            },
            {
                "number": "28.2",
                "title": "Page Replacement Algorithms & Belady's Anomaly",
                "content": """• <b>Algorithms Compared:</b><br/>
&nbsp;&nbsp;• <b>FIFO (First-In, First-Out):</b> Replaces oldest page loaded into memory.<br/>
&nbsp;&nbsp;• <b>Optimal (OPT / MIN):</b> Replaces page that will not be used for the longest period in the future (Theoretical benchmark; cannot be implemented in real OS).<br/>
&nbsp;&nbsp;• <b>LRU (Least Recently Used):</b> Replaces page not used for the longest time in the past.<br/><br/>

• <b>Belady's Anomaly:</b><br/>
&nbsp;&nbsp;- The bizarre phenomenon where <b>allocating MORE page frames causes MORE page faults</b>!<br/>
&nbsp;&nbsp;- <b>Occurs in:</b> FIFO page replacement.<br/>
&nbsp;&nbsp;- <b>CANNOT occur in:</b> Stack algorithms (like LRU and Optimal) because the set of pages in k frames is always a subset of pages in k+1 frames!""",
                "crucial_rule": "🎯 GOLDEN RULE FOR GATE: LRU and Optimal algorithms NEVER suffer from Belady's Anomaly. FIFO can suffer from Belady's Anomaly on reference strings like: 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5."
            }
        ],
        "worked_examples": [
            {
                "title": "Worked Example: EMAT Calculation with Multi-Level Paging",
                "problem": "A system has a TLB hit ratio of 90%. TLB access time is 10 ns, and main memory access time is 100 ns. The system uses 2-level paging. Calculate the Effective Memory Access Time (EMAT).",
                "steps": [
                    "Step 1: Identify parameters: h = 0.90, c = 10 ns, m = 100 ns, levels n = 2.",
                    "Step 2: On TLB Hit: Time = c + m = 10 + 100 = 110 ns.",
                    "Step 3: On TLB Miss: Time = c + (n + 1)m = 10 + 3(100) = 310 ns.",
                    "Step 4: Compute EMAT = h × (Hit Time) + (1 - h) × (Miss Time):",
                    "  EMAT = 0.90 × 110 + 0.10 × 310 = 99 + 31 = 130 ns."
                ],
                "answer": "EMAT = 130 ns."
            }
        ],
        "exam_traps": [
            {
                "title": "Page Table Size in Bytes vs Entries Trap",
                "warning": "Number of entries is 2^p. But Page Table SIZE in memory is 2^p × (PTE bytes)! For a 32-bit address space with 4 KB pages and 4-byte entries: Table size is 2²⁰ × 4 B = 4 MB."
            }
        ],
        "real_life_examples": [
            {
                "title": "Real-Life Analogy: The Book Index & Virtual Memory",
                "text": "Paging is like reading an encyclopedia: you don't load all 30 volumes onto your lap. You keep the 2 pages you are reading open on your desk and fetch new pages as needed."
            }
        ]
    }
}

if __name__ == "__main__":
    out_path = os.path.join("content_data", "textbook_modules", "textbook_toc_cd_os.py")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("# Master Textbook Module: TOC, Compiler Design & OS (9 Chapters)\n")
        f.write("# Auto-generated comprehensive ChatGPT-style point-form guide\n\n")
        f.write("CHAPTERS_TOC_CD_OS = " + pprint.pformat(CHAPTERS_TOC_CD_OS, indent=2, width=120) + "\n")
    print(f"Successfully generated {out_path} ({os.path.getsize(out_path)} bytes)!")
