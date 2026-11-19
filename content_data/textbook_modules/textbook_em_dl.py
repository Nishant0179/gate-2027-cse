# Master Textbook Module: Engineering Mathematics & Digital Logic (8 Chapters)
# Auto-generated comprehensive ChatGPT-style point-form guide

CHAPTERS_EM_DL = { ('DL', 0): { 'chapter_number': 5,
               'exam_traps': [ { 'title': 'Denormalized Exponent Bias Trap',
                                 'warning': 'For denormalized numbers (E = 0), the exponent power is 2^(-126), NOT '
                                            '2^(-127)! The hidden bit is 0, not 1.'}],
               'foundations': [ { 'content': '• <b>The Three Signed Number Formats for n Bits:</b><br/>\n'
                                             "<div class='font-mono text-xs p-3 bg-slate-900 text-slate-100 rounded-xl "
                                             "my-2 leading-relaxed overflow-x-auto'>\n"
                                             'Representation    │ Range for n bits                    │ Zero '
                                             'Representation(s)\n'
                                             '────────────────────────────────────────────────────────────────────────────────\n'
                                             'Sign-Magnitude    │ -(2ⁿ⁻¹ - 1) to +(2ⁿ⁻¹ - 1)          │ Two zeros (+0 '
                                             'and -0)\n'
                                             "1's Complement    │ -(2ⁿ⁻¹ - 1) to +(2ⁿ⁻¹ - 1)          │ Two zeros (+0 "
                                             'and -0)\n'
                                             "2's Complement    │ -2ⁿ⁻¹ to +(2ⁿ⁻¹ - 1)               │ UNIQUE ZERO "
                                             '(00...0)\n'
                                             '</div>\n'
                                             '\n'
                                             "• <b>Why Modern Computers Use 2's Complement Exclusively:</b><br/>\n"
                                             '&nbsp;&nbsp;1. <b>Unique Zero:</b> Only one representation for zero (no '
                                             '+0 and -0 ambiguity).<br/>\n'
                                             '&nbsp;&nbsp;2. <b>One Extra Negative Number:</b> For 8 bits, range is '
                                             '-128 to +127 (128 cannot be represented in +ve!).<br/>\n'
                                             '&nbsp;&nbsp;3. <b>Simplified Hardware:</b> Subtraction <code>A - '
                                             "B</code> is performed using existing adder hardware as <code>A + (2's "
                                             'complement of B)</code>.<br/><br/>\n'
                                             '\n'
                                             "• <b>Shortcut for Finding 2's Complement in Binary:</b><br/>\n"
                                             '&nbsp;&nbsp;- Scan bits from Right to Left. Keep all bits identical up '
                                             "to and including the FIRST '1'. Invert all remaining bits to the left!",
                                  'crucial_rule': "🎯 GOLDEN RULE FOR GATE: Sign extension in 2's complement: To "
                                                  'convert an n-bit signed number to m-bit (m > n), replicate the MSB '
                                                  "(sign bit) to the left! E.g. 4-bit '1101' (-3) becomes 8-bit "
                                                  "'11111101' (-3).",
                                  'number': '5.1',
                                  'title': "Signed Number Systems & 2's Complement"},
                                { 'content': '• <b>What is Overflow?</b> When the result of adding two signed numbers '
                                             'exceeds the representable range of n bits.<br/><br/>\n'
                                             '\n'
                                             '• <b>The Fundamental Rule of Overflow:</b><br/>\n'
                                             '&nbsp;&nbsp;• Adding two POSITIVE numbers results in a NEGATIVE number ⇒ '
                                             '<b>OVERFLOW!</b><br/>\n'
                                             '&nbsp;&nbsp;• Adding two NEGATIVE numbers results in a POSITIVE number ⇒ '
                                             '<b>OVERFLOW!</b><br/>\n'
                                             '&nbsp;&nbsp;• Adding numbers of OPPOSITE signs CAN NEVER cause '
                                             'overflow!<br/><br/>\n'
                                             '\n'
                                             '• <b>Hardware Detection Condition:</b><br/>\n'
                                             '&nbsp;&nbsp;<code>V = Cᵢₙ ⊕ Cₒᵤₜ</code> of the Most Significant Bit '
                                             '(MSB).<br/>\n'
                                             '&nbsp;&nbsp;If Carry-into-MSB ≠ Carry-out-of-MSB, an overflow has '
                                             'occurred!',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: Carry flag (C) is used for unsigned '
                                                  "arithmetic. Overflow flag (V) is used for signed 2's complement "
                                                  'arithmetic! Never confuse the two.',
                                  'number': '5.2',
                                  'title': "Arithmetic Overflow in 2's Complement"},
                                { 'content': '• <b>Single Precision (32-Bit) Format Layout:</b><br/>\n'
                                             "<div class='font-mono text-xs p-3 bg-slate-900 text-emerald-400 "
                                             "rounded-xl my-2 leading-relaxed'>\n"
                                             '[ Sign: 1 bit ] [ Exponent (E): 8 bits ] [ Mantissa / Fraction (M): 23 '
                                             'bits ]\n'
                                             'Bit 31          Bits 30-23               Bits 22-0\n'
                                             '</div>\n'
                                             '\n'
                                             '• <b>Decoding Formula for Normalized Numbers (1 ≤ E ≤ 254):</b><br/>\n'
                                             '&nbsp;&nbsp;<code>Value = (-1)ˢ × (1.M)₂ × 2^(E - 127)</code><br/>\n'
                                             '&nbsp;&nbsp;• <b>Sign bit (S):</b> 0 = Positive, 1 = Negative.<br/>\n'
                                             '&nbsp;&nbsp;• <b>Bias = 127:</b> The stored exponent E is biased: '
                                             '<code>E = Actual Exponent + 127</code>.<br/>\n'
                                             "&nbsp;&nbsp;• <b>Hidden Bit:</b> The leading '1.' before the mantissa is "
                                             'NOT stored in memory to save 1 bit of precision!<br/><br/>\n'
                                             '\n'
                                             '• <b>Special IEEE 754 Representations:</b><br/>\n'
                                             '&nbsp;&nbsp;• <code>E = 0, M = 0</code>: Represents Zero (±0 depending '
                                             'on S).<br/>\n'
                                             '&nbsp;&nbsp;• <code>E = 255, M = 0</code>: Represents Infinity '
                                             '(±∞).<br/>\n'
                                             '&nbsp;&nbsp;• <code>E = 255, M ≠ 0</code>: Represents <b>NaN</b> (Not a '
                                             'Number, e.g. 0/0).<br/>\n'
                                             '&nbsp;&nbsp;• <code>E = 0, M ≠ 0</code>: Denormalized numbers: '
                                             '<code>(-1)ˢ × (0.M)₂ × 2^(-126)</code>.',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: Double Precision (64-bit): 1 sign bit, 11 '
                                                  'exponent bits (Bias = 1023), 52 mantissa bits. Smallest positive '
                                                  'normalized number in 32-bit is 1.0 × 2^(-126).',
                                  'number': '5.3',
                                  'title': 'IEEE 754 Floating-Point Standard (32-Bit Single Precision)'}],
               'real_life_examples': [ { 'text': 'IEEE 754 is just binary scientific notation: instead of writing 6.02 '
                                                 '× 10²³, the computer writes 1.011 × 2⁴. The sign, power, and digits '
                                                 'are packed into 32 bits.',
                                         'title': 'Real-Life Analogy: Scientific Notation on Pocket Calculators'}],
               'title': 'Number Representation & Floating Point (IEEE 754)',
               'worked_examples': [ { 'answer': 'Hexadecimal IEEE 754 representation is 0xC11C0000.',
                                      'problem': 'Convert the decimal number -9.75 into 32-bit IEEE 754 '
                                                 'single-precision hexadecimal representation.',
                                      'steps': [ 'Step 1: Sign bit S = 1 (since number is negative).',
                                                 'Step 2: Convert magnitude 9.75 to binary: 9 = 1001, 0.75 = 0.11. So '
                                                 '9.75 = 1001.11₂.',
                                                 'Step 3: Normalize to scientific binary: 1001.11₂ = 1.00111₂ × 2³.',
                                                 'Step 4: Actual exponent = 3. Biased exponent E = 3 + 127 = 130 = '
                                                 '10000010₂.',
                                                 'Step 5: Mantissa bits (drop hidden 1): 00111000000000000000000 (pad '
                                                 'with zeros to 23 bits).',
                                                 'Step 6: Combine: [1] [10000010] [00111000000000000000000] = 1100 '
                                                 '0001 0001 1100 0000 0000 0000 0000.',
                                                 'Step 7: Group into hex digits: C11C0000₁₆.'],
                                      'title': 'Worked Example: Converting Decimal to IEEE 754 Format'}]},
  ('DL', 1): { 'chapter_number': 6,
               'exam_traps': [ { 'title': 'The False Minimal Expression Trap',
                                 'warning': 'A function can have multiple distinct minimal SOP expressions with the '
                                            'same number of terms and literals. Do not assume there is only one valid '
                                            'answer.'}],
               'foundations': [ { 'content': '• <b>Universal Logic Gates (NAND and NOR):</b><br/>\n'
                                             '&nbsp;&nbsp;- Any Boolean function can be implemented using ONLY NAND or '
                                             'ONLY NOR gates without requiring any other gate!<br/>\n'
                                             "<div class='font-mono text-xs p-3 bg-slate-900 text-slate-100 rounded-xl "
                                             "my-2 leading-relaxed overflow-x-auto'>\n"
                                             'Function / Gate to Implement │ Minimum NAND Gates Needed │ Minimum NOR '
                                             'Gates Needed\n'
                                             '────────────────────────────────────────────────────────────────────────────────\n'
                                             'NOT (Inverter)               │ 1                         │ 1\n'
                                             'AND Gate                     │ 2                         │ 3\n'
                                             'OR Gate                      │ 3                         │ 2\n'
                                             'XOR Gate                     │ 4                         │ 5\n'
                                             'XNOR Gate                    │ 5                         │ 4\n'
                                             '</div>\n'
                                             '\n'
                                             '• <b>The Consensus Theorem (GATE High-Yield Simplification '
                                             'Shortcut):</b><br/>\n'
                                             "&nbsp;&nbsp;<code>AB + A'C + BC = AB + A'C</code> (The term BC is "
                                             'redundant consensus!).<br/>\n'
                                             '&nbsp;&nbsp;• <b>How to spot Consensus in 5 seconds:</b><br/>\n'
                                             '&nbsp;&nbsp;&nbsp;&nbsp;1. Three terms, each with 2 variables.<br/>\n'
                                             '&nbsp;&nbsp;&nbsp;&nbsp;2. One variable appears complemented (A and '
                                             "A').<br/>\n"
                                             '&nbsp;&nbsp;&nbsp;&nbsp;3. The term containing the remaining two '
                                             'variables (BC) is COMPLETELY REDUNDANT and can be deleted!',
                                  'crucial_rule': "🎯 GOLDEN RULE FOR GATE: Dual of Consensus Theorem: (A + B)(A' + "
                                                  "C)(B + C) = (A + B)(A' + C). Keep an eye out for both SOP and POS "
                                                  'forms in GATE questions.',
                                  'number': '6.1',
                                  'title': 'Universal Logic Gates & Consensus Theorem'},
                                { 'content': '• <b>Gray Code Ordering in K-Maps:</b><br/>\n'
                                             '&nbsp;&nbsp;- K-map row/column labels MUST use Gray code: <b>00, 01, 11, '
                                             '10</b> (only 1 bit changes between adjacent cells).<br/>\n'
                                             '&nbsp;&nbsp;- Because of wrap-around adjacency, corners and edges are '
                                             'adjacent to each other!<br/><br/>\n'
                                             '\n'
                                             '• <b>Implicant Terminology (Tested in every GATE paper):</b><br/>\n'
                                             '&nbsp;&nbsp;• <b>Implicant:</b> Any single 1 or group of 1s (of size 1, '
                                             '2, 4, 8, ...).<br/>\n'
                                             "&nbsp;&nbsp;• <b>Prime Implicant (PI):</b> A rectangle of 1s (and don't "
                                             'cares) that CANNOT be merged into a larger group.<br/>\n'
                                             '&nbsp;&nbsp;• <b>Essential Prime Implicant (EPI):</b> A Prime Implicant '
                                             "that contains <b>at least one '1' that is NOT covered by any other "
                                             'PI</b>!<br/>\n'
                                             '&nbsp;&nbsp;• <b>Minimal SOP:</b> MUST include ALL EPIs + the minimum '
                                             'number of remaining PIs to cover leftover 1s.',
                                  'crucial_rule': "🎯 GOLDEN RULE FOR GATE: Never group don't cares (X) with other "
                                                  "don't cares! Only include a don't care in a group if it helps "
                                                  'expand a group of 1s to make it larger (reducing literal count).',
                                  'number': '6.2',
                                  'title': 'Karnaugh Maps (K-Maps) & Implicants'}],
               'real_life_examples': [ { 'text': 'Every transistor on a microchip consumes silicon real estate and '
                                                 'power. K-map logic minimization literally reduces the physical size '
                                                 'and battery consumption of smartphone processors.',
                                         'title': 'Real-Life Analogy: Silicon Chip Area & Cost'}],
               'title': 'Boolean Algebra, K-Maps & Tabular Method (Quine-McCluskey)',
               'worked_examples': [ { 'answer': '3 Prime Implicants, and all 3 are Essential Prime Implicants (EPIs).',
                                      'problem': 'For the Boolean function f(A,B,C,D) = ∑m(0, 2, 5, 7, 8, 10, 14, 15), '
                                                 'find the number of Prime Implicants and Essential Prime Implicants.',
                                      'steps': [ 'Step 1: Draw 4-variable K-Map with Gray codes 00, 01, 11, 10 for AB '
                                                 'and CD.',
                                                 'Step 2: Place 1s at minterms 0, 2, 8, 10 (four corners), 5, 7 '
                                                 '(adjacent in row 01), and 14, 15 (adjacent in row 11).',
                                                 "Step 3: Group four corners (0, 2, 8, 10) ⇒ Term: B'D'.",
                                                 "Step 4: Group (5, 7) ⇒ Term: A'BD.",
                                                 'Step 5: Group (14, 15) ⇒ Term: ABC.',
                                                 "Step 6: Check EPI status: Minterm 0 is only in B'D' (so B'D' is "
                                                 "EPI). Minterm 5 is only in A'BD (so A'BD is EPI). Minterm 14 is only "
                                                 'in ABC (so ABC is EPI).'],
                                      'title': 'Worked Example: Finding Prime Implicants and Essential PIs'}]},
  ('DL', 2): { 'chapter_number': 7,
               'exam_traps': [ { 'title': 'Select Line Order Inversion Trap',
                                 'warning': 'If S₁ is connected to B and S₀ is connected to A instead of A to S₁ and B '
                                            'to S₀, the row indices flip completely. Always verify which variable is '
                                            'MSB in the select lines.'}],
               'foundations': [ { 'content': '• <b>What is a Multiplexer?</b> A data selector with 2ⁿ data inputs, n '
                                             'select lines, and 1 output.<br/><br/>\n'
                                             '\n'
                                             '• <b>Implementing n-Variable Functions using (2ⁿ⁻¹)-to-1 MUX:</b><br/>\n'
                                             '&nbsp;&nbsp;• Connect (n - 1) variables to the select lines.<br/>\n'
                                             '&nbsp;&nbsp;• Connect the remaining 1 variable (in forms: 0, 1, V, or '
                                             "V') to the data inputs.<br/>\n"
                                             '&nbsp;&nbsp;• <b>Example:</b> To implement a 3-variable function f(A, B, '
                                             'C) using a 4-to-1 MUX:<br/>\n'
                                             '&nbsp;&nbsp;&nbsp;&nbsp;- Connect A and B to select lines S₁ and '
                                             'S₀.<br/>\n'
                                             '&nbsp;&nbsp;&nbsp;&nbsp;- Compare outputs for each combination of AB: '
                                             "find whether input Iᵢ equals 0, 1, C, or C'.",
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: Any n-variable Boolean function can be '
                                                  'implemented using a 2ⁿ-to-1 MUX with NO external gates, or using a '
                                                  '2ⁿ⁻¹-to-1 MUX with at most NOT gates!',
                                  'number': '7.1',
                                  'title': 'Multiplexers (MUX) as Universal Function Generators'},
                                { 'content': '• <b>Decoders (n-to-2ⁿ):</b><br/>\n'
                                             '&nbsp;&nbsp;- Generates all 2ⁿ minterms of the n input variables.<br/>\n'
                                             '&nbsp;&nbsp;- Any function f can be implemented using a Decoder + OR '
                                             'gate (for active-high outputs) or Decoder + NAND gate (for active-low '
                                             'outputs).<br/><br/>\n'
                                             '\n'
                                             '• <b>Priority Encoders:</b><br/>\n'
                                             '&nbsp;&nbsp;- Resolves simultaneous requests: if multiple inputs are 1, '
                                             'only the highest-priority input is encoded.<br/>\n'
                                             '&nbsp;&nbsp;- Includes a Valid output bit (V = 1 if at least one input '
                                             'is active).',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: Number of smaller m-to-2ᵐ decoders needed '
                                                  'to build an n-to-2ⁿ decoder = 2ⁿ / 2ᵐ.',
                                  'number': '7.2',
                                  'title': 'Decoders, Encoders & Priority Logic'},
                                { 'content': '• <b>Full Adder Equations:</b><br/>\n'
                                             '&nbsp;&nbsp;<code>Sum = A ⊕ B ⊕ Cᵢₙ</code><br/>\n'
                                             '&nbsp;&nbsp;<code>Carry = AB + BCᵢₙ + ACᵢₙ</code> (Can be implemented '
                                             'with 2 Half Adders and 1 OR gate).<br/><br/>\n'
                                             '\n'
                                             '• <b>Carry Lookahead Adder (CLA):</b><br/>\n'
                                             '&nbsp;&nbsp;• Eliminates ripple carry propagation delay by computing '
                                             'carries in parallel!<br/>\n'
                                             '&nbsp;&nbsp;• <b>Generate bit:</b> <code>Gᵢ = Aᵢ · Bᵢ</code> (Carry '
                                             'generated internally).<br/>\n'
                                             '&nbsp;&nbsp;• <b>Propagate bit:</b> <code>Pᵢ = Aᵢ ⊕ Bᵢ</code> (Carry '
                                             'propagated from previous stage).<br/>\n'
                                             '&nbsp;&nbsp;• Carries: <code>C₁ = G₀ + P₀C₀</code>, <code>C₂ = G₁ + P₁G₀ '
                                             '+ P₁P₀C₀</code>.<br/>\n'
                                             '&nbsp;&nbsp;• Total delay of an n-bit CLA is constant O(1), independent '
                                             'of n!',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: Ripple Carry Adder delay grows linearly '
                                                  'O(n). Carry Lookahead Adder delay is independent of n, limited only '
                                                  'by gate fan-in constraints.',
                                  'number': '7.3',
                                  'title': 'Adders & Carry Lookahead Architecture'}],
               'real_life_examples': [ { 'text': 'A multiplexer is like a railway track junction where multiple '
                                                 'incoming train tracks merge into a single line. The select line '
                                                 'controls which train gets routed forward.',
                                         'title': 'Real-Life Analogy: Railway Track Switcher'}],
               'title': 'Combinational Circuits - MUX, Decoders & Arithmetic Circuits',
               'worked_examples': [ { 'answer': "MUX inputs: I₀ = C, I₁ = C, I₂ = C', I₃ = C'.",
                                      'problem': 'Implement f(A,B,C) = ∑m(1, 3, 4, 6) using a 4-to-1 MUX with A and B '
                                                 'connected to select lines S₁ and S₀ respectively.',
                                      'steps': [ 'Step 1: Set up truth table grouped by AB values (00, 01, 10, 11).',
                                                 'Step 2: For AB = 00 (minterms 0, 1): m0=0, m1=1 ⇒ When C=0, f=0; '
                                                 'when C=1, f=1. So I₀ = C.',
                                                 'Step 3: For AB = 01 (minterms 2, 3): m2=0, m3=1 ⇒ When C=0, f=0; '
                                                 'when C=1, f=1. So I₁ = C.',
                                                 'Step 4: For AB = 10 (minterms 4, 5): m4=1, m5=0 ⇒ When C=0, f=1; '
                                                 "when C=1, f=0. So I₂ = C'.",
                                                 'Step 5: For AB = 11 (minterms 6, 7): m6=1, m7=0 ⇒ When C=0, f=1; '
                                                 "when C=1, f=0. So I₃ = C'."],
                                      'title': 'Worked Example: Implementing Logic with 4-to-1 MUX'}]},
  ('DL', 3): { 'chapter_number': 8,
               'exam_traps': [ { 'title': 'Ring Counter vs Johnson Counter State Count Trap',
                                 'warning': 'For 4 flip-flops: Ring counter has ONLY 4 states, whereas Johnson counter '
                                            'has 2 × 4 = 8 states. A normal binary counter has 2⁴ = 16 states.'}],
               'foundations': [ { 'content': '• <b>Characteristic Equations (Next State Q⁺):</b><br/>\n'
                                             "<div class='font-mono text-xs p-3 bg-slate-900 text-slate-100 rounded-xl "
                                             "my-2 leading-relaxed overflow-x-auto'>\n"
                                             'Flip-Flop │ Characteristic Equation      │ Forbidden / Invalid State\n'
                                             '───────────────────────────────────────────────────────────────────────\n'
                                             "SR        │ Q⁺ = S + R'Q (with SR = 0)     │ S = 1, R = 1\n"
                                             "JK        │ Q⁺ = JQ' + K'Q                 │ None (Toggles when J=K=1)\n"
                                             'D         │ Q⁺ = D                         │ None (Transparent / Delay)\n'
                                             "T         │ Q⁺ = T ⊕ Q = TQ' + T'Q         │ None (Toggles when T=1)\n"
                                             '</div>\n'
                                             '\n'
                                             '• <b>Excitation Tables (Required inputs to transition from Q → '
                                             'Q⁺):</b><br/>\n'
                                             "<div class='font-mono text-xs p-3 bg-slate-900 text-emerald-400 "
                                             "rounded-xl my-2 leading-relaxed overflow-x-auto'>\n"
                                             'Q  Q⁺ │ S   R │ J   K │ D │ T\n'
                                             '──────────────────────────────\n'
                                             '0  0  │ 0   X │ 0   X │ 0 │ 0\n'
                                             '0  1  │ 1   0 │ 1   X │ 1 │ 1\n'
                                             '1  0  │ 0   1 │ X   1 │ 0 │ 1\n'
                                             '1  1  │ X   0 │ X   0 │ 1 │ 0\n'
                                             '</div>',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: To convert Flip-Flop A to Flip-Flop B: '
                                                  'Write characteristic equation of B, and match it with the '
                                                  'excitation table of A.',
                                  'number': '8.1',
                                  'title': 'Flip-Flop Characteristic & Excitation Equations'},
                                { 'content': '• <b>Setup Time (tₛᵤ) & Hold Time (tₕ):</b><br/>\n'
                                             '&nbsp;&nbsp;• <b>Setup Time:</b> The minimum time the input data MUST '
                                             'remain stable <b>BEFORE</b> the active clock edge.<br/>\n'
                                             '&nbsp;&nbsp;• <b>Hold Time:</b> The minimum time the input data MUST '
                                             'remain stable <b>AFTER</b> the active clock edge.<br/>\n'
                                             '&nbsp;&nbsp;• Violating setup or hold times causes <b>Metastability</b> '
                                             '(unpredictable oscillating output).<br/><br/>\n'
                                             '\n'
                                             '• <b>Maximum Clock Frequency Formula:</b><br/>\n'
                                             '&nbsp;&nbsp;<code>T_clock ≥ t_cq + t_comb + t_setup</code><br/>\n'
                                             '&nbsp;&nbsp;<code>f_max = 1 / T_clock_min = 1 / (t_cq + t_comb + '
                                             't_setup)</code><br/>\n'
                                             '&nbsp;&nbsp;(where t_cq = clock-to-Q propagation delay, t_comb = '
                                             'combinational logic delay).',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: Hold time DOES NOT affect maximum clock '
                                                  'frequency! Hold time condition is: t_cq + t_comb ≥ t_hold.',
                                  'number': '8.2',
                                  'title': 'Flip-Flop Timing Constraints & Max Frequency'},
                                { 'content': '• <b>Asynchronous (Ripple) vs Synchronous Counters:</b><br/>\n'
                                             '&nbsp;&nbsp;• <b>Ripple Counter:</b> Output of each flip-flop clocks the '
                                             'next. Simple hardware, but propagation delay accumulates: <code>T_delay '
                                             '= n × t_pd</code>. Max frequency decreases rapidly with n.<br/>\n'
                                             '&nbsp;&nbsp;• <b>Synchronous Counter:</b> All flip-flops share the same '
                                             'clock line. All change simultaneously: <code>T_delay = t_pd + '
                                             't_comb</code> (much faster!).<br/><br/>\n'
                                             '\n'
                                             '• <b>Special Shift Register Counters (n Flip-Flops):</b><br/>\n'
                                             '&nbsp;&nbsp;• <b>Ring Counter:</b> Feedback from Qₙ to D₀. Number of '
                                             'unique states = <b>n</b>. Unused states = 2ⁿ - n.<br/>\n'
                                             "&nbsp;&nbsp;• <b>Johnson (Twisted Ring) Counter:</b> Feedback from Q'ₙ "
                                             'to D₀. Number of unique states = <b>2n</b>. Unused states = 2ⁿ - 2n.',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: A Mod-N counter counts N states (from 0 to '
                                                  'N-1) and requires ⌈log₂ N⌉ flip-flops.',
                                  'number': '8.3',
                                  'title': 'Synchronous & Asynchronous Counters, Shift Registers'}],
               'real_life_examples': [ { 'text': 'In a Moore machine, a pedestrian walk sign depends only on the '
                                                 'current light cycle (e.g. Red). In a Mealy machine, pressing the '
                                                 'crosswalk button can instantly change the sign immediately.',
                                         'title': 'Real-Life Analogy: Traffic Light Controller (Mealy vs Moore)'}],
               'title': 'Sequential Circuits - Flip-Flops, Counters & State Machines',
               'worked_examples': [ { 'answer': 'Maximum clock frequency is 100 MHz.',
                                      'problem': 'A sequential circuit has flip-flops with clock-to-Q delay of 3 ns, '
                                                 'setup time of 2 ns, and hold time of 1 ns. The combinational logic '
                                                 'between flip-flops has a maximum delay of 5 ns. Find the maximum '
                                                 'clock frequency at which this circuit can operate safely.',
                                      'steps': [ 'Step 1: Calculate the minimum clock period T_min using: T_min ≥ t_cq '
                                                 '+ t_comb + t_setup.',
                                                 'Step 2: Substitute values: T_min = 3 ns + 5 ns + 2 ns = 10 ns.',
                                                 'Step 3: Calculate maximum frequency f_max = 1 / T_min = 1 / (10 × '
                                                 '10⁻⁹ s) = 100 MHz.'],
                                      'title': 'Worked Example: Maximum Operating Clock Frequency'}]},
  ('EM', 0): { 'chapter_number': 1,
               'exam_traps': [ { 'title': 'The Vacuous Truth Trap in First-Order Logic',
                                 'warning': 'When evaluating ∀x [P(x) → Q(x)] on an empty set or a domain where P(x) '
                                            'is False for all elements, the formula evaluates to TRUE! Many students '
                                            "select False thinking 'no elements satisfy the condition'."},
                               { 'title': 'Anti-Symmetric vs Asymmetric Confusion',
                                 'warning': 'Anti-symmetric allows diagonal elements (a, a) to exist. Asymmetric '
                                            'STRICTLY FORBIDS diagonal elements! Hence, every Asymmetric relation is '
                                            'Anti-symmetric, but not vice versa.'}],
               'foundations': [ { 'content': '• <b>What is a Proposition? (Basic Definition):</b><br/>\n'
                                             '&nbsp;&nbsp;- A proposition is a declarative sentence that is strictly '
                                             '<b>True (T)</b> or strictly <b>False (F)</b>, but never both '
                                             'simultaneously.<br/>\n'
                                             "&nbsp;&nbsp;- Examples of propositions: <i>'7 is a prime number'</i> "
                                             "(True), <i>'Paris is in Japan'</i> (False).<br/>\n"
                                             "&nbsp;&nbsp;- NOT propositions: Questions (<i>'What time is it?'</i>), "
                                             "Commands (<i>'Close the door'</i>), or Paradoxes (<i>'This statement is "
                                             "false'</i>).<br/><br/>\n"
                                             '\n'
                                             '• <b>Master Truth Table for the 5 Logical Connectives:</b><br/>\n'
                                             "<div class='font-mono text-xs p-3 bg-slate-900 text-slate-100 rounded-xl "
                                             "my-2 leading-relaxed overflow-x-auto'>\n"
                                             'P   Q │ ~P (NOT) │ P ∧ Q (AND) │ P ∨ Q (OR) │ P → Q (Implication) │ P ↔ '
                                             'Q (Biconditional)\n'
                                             '──────────────────────────────────────────────────────────────────────────────────────────\n'
                                             'T   T │    F     │      T      │     T      │          T          '
                                             '│          T\n'
                                             'T   F │    F     │      F      │     T      │          F          '
                                             '│          F\n'
                                             'F   T │    T     │      F      │     T      │          T          '
                                             '│          F\n'
                                             'F   F │    T     │      F      │     F      │          T          '
                                             '│          T\n'
                                             '</div>\n'
                                             '\n'
                                             '• <b>Why is (F → T) and (F → F) True? (Vacuous Truth '
                                             'Explained):</b><br/>\n'
                                             '&nbsp;&nbsp;- Think of an implication <code>P → Q</code> as a '
                                             "conditional contract: <i>'If you score Rank 1 in GATE (P), I will buy "
                                             "you a laptop (Q)'</i>.<br/>\n"
                                             '&nbsp;&nbsp;- If you do NOT score Rank 1 (<code>P = False</code>), '
                                             'whatever happens next does NOT break the contract! Whether I give you a '
                                             'laptop or not, the contract was never breached.<br/>\n'
                                             '&nbsp;&nbsp;- Therefore: <b>When P is False, the implication P → Q is '
                                             'ALWAYS True by default!</b><br/><br/>\n'
                                             '\n'
                                             '• <b>The Most Critical Logical Equivalence in GATE:</b><br/>\n'
                                             '&nbsp;&nbsp;- <code>(P → Q) ≡ (~P ∨ Q)</code><br/>\n'
                                             '&nbsp;&nbsp;- In 90% of GATE logic questions, you can solve the question '
                                             'in 20 seconds by replacing every <code>P → Q</code> with <code>(~P ∨ '
                                             'Q)</code>!',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: P → Q is FALSE only in one single scenario: '
                                                  'P is True and Q is False! In all other 3 scenarios, P → Q is '
                                                  'strictly TRUE.',
                                  'number': '1.1',
                                  'title': 'Propositions, Truth Values & The 5 Core Connectives'},
                                { 'content': "• <b>Definitions for any Conditional Statement 'If P, then Q' (P → "
                                             'Q):</b><br/>\n'
                                             "&nbsp;&nbsp;1. <b>Contrapositive:</b> <code>~Q → ~P</code> ('If NOT Q, "
                                             "then NOT P').<br/>\n"
                                             "&nbsp;&nbsp;2. <b>Converse:</b> <code>Q → P</code> ('If Q, then "
                                             "P').<br/>\n"
                                             "&nbsp;&nbsp;3. <b>Inverse:</b> <code>~P → ~Q</code> ('If NOT P, then NOT "
                                             "Q').<br/><br/>\n"
                                             '\n'
                                             '• <b>Equivalence Relationships (GATE Must-Know):</b><br/>\n'
                                             '&nbsp;&nbsp;• <b>The Golden Identity:</b> <code>(P → Q) ≡ (~Q → '
                                             '~P)</code>.<br/>\n'
                                             '&nbsp;&nbsp;&nbsp;&nbsp;- A statement and its Contrapositive ALWAYS have '
                                             'the exact same truth value under all conditions.<br/>\n'
                                             '&nbsp;&nbsp;&nbsp;&nbsp;- <i>GATE Application:</i> If a mathematical '
                                             'theorem is difficult to prove directly (P → Q), prove its contrapositive '
                                             '(~Q → ~P) instead!<br/>\n'
                                             '&nbsp;&nbsp;• <b>The Converse Trap:</b> <code>(P → Q) ≢ (Q → P)</code>. '
                                             'The Converse is NOT equivalent to the original statement!<br/>\n'
                                             '&nbsp;&nbsp;• <b>The Inverse Relationship:</b> The Inverse (<code>~P → '
                                             '~Q</code>) is logically equivalent to the Converse (<code>Q → P</code>), '
                                             'but NOT to the original statement.',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: Original Statement ≡ Contrapositive. '
                                                  'Converse ≡ Inverse. A statement is NEVER guaranteed to equal its '
                                                  'converse!',
                                  'number': '1.2',
                                  'title': 'Contrapositive, Converse, and Inverse'},
                                { 'content': '• <b>The Two Core Quantifiers:</b><br/>\n'
                                             "&nbsp;&nbsp;• <b>Universal Quantifier (∀):</b> 'For all', 'For every', "
                                             "'For each'.<br/>\n"
                                             '&nbsp;&nbsp;&nbsp;&nbsp;- <code>∀x P(x)</code> is True only if P(x) is '
                                             'True for <i>every single element</i> in the domain.<br/>\n'
                                             "&nbsp;&nbsp;• <b>Existential Quantifier (∃):</b> 'There exists', 'For at "
                                             "least one', 'Some'.<br/>\n"
                                             '&nbsp;&nbsp;&nbsp;&nbsp;- <code>∃x P(x)</code> is True if there is <i>at '
                                             'least one element</i> that makes P(x) True.<br/><br/>\n'
                                             '\n'
                                             "• <b>De Morgan's Laws for Quantifiers (Negation Rules):</b><br/>\n"
                                             '&nbsp;&nbsp;• <code>~[∀x P(x)] ≡ ∃x [~P(x)]</code><br/>\n'
                                             "&nbsp;&nbsp;&nbsp;&nbsp;<i>Intuition:</i> To disprove 'Every student is "
                                             "honest', you only need to find ONE dishonest student!<br/>\n"
                                             '&nbsp;&nbsp;• <code>~[∃x P(x)] ≡ ∀x [~P(x)]</code><br/>\n'
                                             "&nbsp;&nbsp;&nbsp;&nbsp;<i>Intuition:</i> To disprove 'There exists a "
                                             "flying pig', you must show that ALL pigs cannot fly.<br/><br/>\n"
                                             '\n'
                                             '• <b>Order of Quantifiers (Commutativity vs '
                                             'Non-Commutativity):</b><br/>\n'
                                             '&nbsp;&nbsp;• Same quantifiers commute: <code>∀x ∀y P(x,y) ≡ ∀y ∀x '
                                             'P(x,y)</code> and <code>∃x ∃y P(x,y) ≡ ∃y ∃x P(x,y)</code>.<br/>\n'
                                             '&nbsp;&nbsp;• <b>Mixed quantifiers DO NOT commute!</b><br/>\n'
                                             "&nbsp;&nbsp;&nbsp;&nbsp;- <code>∀x ∃y Loves(x, y)</code> means: 'Every "
                                             "person loves someone' (Everyone has someone they love).<br/>\n"
                                             "&nbsp;&nbsp;&nbsp;&nbsp;- <code>∃y ∀x Loves(x, y)</code> means: 'There "
                                             "is a single celebrity whom everybody loves'!<br/>\n"
                                             '&nbsp;&nbsp;&nbsp;&nbsp;- Note: <code>∃y ∀x P(x, y) ⇒ ∀x ∃y P(x, '
                                             'y)</code>, but the converse is FALSE!',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: When translating English to FOL: Universal '
                                                  'quantifier (∀) almost always pairs with Implication (→): ∀x '
                                                  '[Student(x) → Hardworking(x)]. Existential quantifier (∃) pairs '
                                                  'with Conjunction (∧): ∃x [Student(x) ∧ Hardworking(x)]. Using ∃ '
                                                  'with → is a notorious trap because of vacuous truth!',
                                  'number': '1.3',
                                  'title': 'First-Order Logic: Quantifiers (∀ vs ∃) & Translation'},
                                { 'content': '• <b>Power Set:</b> For a set A with n elements (|A| = n), the power set '
                                             'P(A) contains <b>2ⁿ</b> subsets.<br/><br/>\n'
                                             '\n'
                                             '• <b>Relations on a Set A (|A| = n):</b><br/>\n'
                                             '&nbsp;&nbsp;A binary relation R on A is a subset of A × A. Total '
                                             'possible relations = <b>2^(n²)</b>.<br/>\n'
                                             "<div class='font-mono text-xs p-3 bg-slate-900 text-slate-100 rounded-xl "
                                             "my-2 leading-relaxed overflow-x-auto'>\n"
                                             'Relation Type   │ Definition Condition                  │ Total Possible '
                                             'Count Formula\n'
                                             '────────────────────────────────────────────────────────────────────────────────────────\n'
                                             'Reflexive       │ ∀a ∈ A: (a, a) ∈ R                    │ 2^(n² - n)\n'
                                             'Irreflexive     │ ∀a ∈ A: (a, a) ∉ R                    │ 2^(n² - n)\n'
                                             'Symmetric       │ (a, b) ∈ R ⇒ (b, a) ∈ R              │ 2^[n(n + 1) / '
                                             '2]\n'
                                             'Anti-Symmetric  │ (a, b) ∈ R and (b, a) ∈ R ⇒ a = b     │ 2ⁿ × 3^[n(n - '
                                             '1) / 2]\n'
                                             'Asymmetric      │ (a, b) ∈ R ⇒ (b, a) ∉ R              │ 3^[n(n - 1) / '
                                             '2]\n'
                                             '</div>\n'
                                             '\n'
                                             '• <b>Equivalence Relations:</b><br/>\n'
                                             '&nbsp;&nbsp;- A relation is an Equivalence Relation if it is '
                                             '<b>Reflexive, Symmetric, and Transitive</b>.<br/>\n'
                                             '&nbsp;&nbsp;- Every equivalence relation partitions the set into '
                                             'disjoint <b>Equivalence Classes</b>.<br/>\n'
                                             '&nbsp;&nbsp;- Total number of equivalence relations on a set of size n '
                                             'equals the <b>Bell Number B(n)</b>: B(1)=1, B(2)=2, B(3)=5, B(4)=15, '
                                             'B(5)=52.<br/><br/>\n'
                                             '\n'
                                             '• <b>Function Classifications (Mapping f: A → B, |A| = m, |B| = '
                                             'n):</b><br/>\n'
                                             '&nbsp;&nbsp;• <b>Injective (One-to-One):</b> Distinct inputs map to '
                                             'distinct outputs. Possible only if m ≤ n. Count = <code>ⁿPₘ = n! / (n - '
                                             'm)!</code>.<br/>\n'
                                             '&nbsp;&nbsp;• <b>Surjective (Onto):</b> Every element in B is covered. '
                                             'Possible only if m ≥ n. Count = <code>∑ (-1)ᵏ ⁿCₖ (n - k)ᵐ</code>.<br/>\n'
                                             '&nbsp;&nbsp;• <b>Bijective (One-to-One & Onto):</b> Possible only if m = '
                                             'n. Count = <code>n!</code>.',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: A relation can be BOTH Symmetric and '
                                                  'Anti-symmetric (e.g. Identity relation R = {(1,1), (2,2)}). But a '
                                                  'relation CANNOT be both Reflexive and Irreflexive (except for empty '
                                                  'set).',
                                  'number': '1.4',
                                  'title': 'Set Theory, Relations & Function Properties'},
                                { 'content': '• <b>What is a POSET? (Partially Ordered Set):</b><br/>\n'
                                             '&nbsp;&nbsp;- A relation R on set A is a Partial Order if it is: '
                                             '<b>Reflexive, Anti-symmetric, and Transitive</b> (RAT).<br/>\n'
                                             '&nbsp;&nbsp;- Visualized using a <b>Hasse Diagram</b> (transitive and '
                                             'reflexive edges omitted, smaller elements drawn below larger '
                                             'ones).<br/><br/>\n'
                                             '\n'
                                             '• <b>Key Elements in a POSET:</b><br/>\n'
                                             '&nbsp;&nbsp;• <b>Maximal Element:</b> An element x such that no element '
                                             'y exists with x < y (top of branch). A POSET can have <i>multiple</i> '
                                             'maximal elements!<br/>\n'
                                             '&nbsp;&nbsp;• <b>Greatest Element (Maximum):</b> An element g such that '
                                             '∀x, x ≤ g. If it exists, it is <b>UNIQUE</b>!<br/>\n'
                                             '&nbsp;&nbsp;• <b>Minimal Element:</b> An element with no element below '
                                             'it. Can have multiple.<br/>\n'
                                             '&nbsp;&nbsp;• <b>Least Element (Minimum):</b> An element l such that ∀x, '
                                             'l ≤ x. If it exists, it is <b>UNIQUE</b>!<br/><br/>\n'
                                             '\n'
                                             '• <b>What is a Lattice?</b><br/>\n'
                                             '&nbsp;&nbsp;- A POSET (L, ≤) is called a <b>Lattice</b> if every pair of '
                                             'elements {a, b} has:<br/>\n'
                                             '&nbsp;&nbsp;&nbsp;&nbsp;1. A unique <b>Least Upper Bound (LUB / Join: a '
                                             '∨ b)</b>.<br/>\n'
                                             '&nbsp;&nbsp;&nbsp;&nbsp;2. A unique <b>Greatest Lower Bound (GLB / Meet: '
                                             'a ∧ b)</b>.<br/>\n'
                                             '&nbsp;&nbsp;- <b>Bounded Lattice:</b> Has a greatest element (1) and '
                                             'least element (0). Every finite lattice is bounded!<br/>\n'
                                             '&nbsp;&nbsp;- <b>Distributive Lattice:</b> Satisfies distributive laws: '
                                             '<code>a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c)</code>. A lattice is distributive '
                                             'iff it does NOT contain the pentagon (N₅) or diamond (M₃) sublattices!',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: In any finite lattice, the Greatest element '
                                                  'and Least element MUST exist and be unique! If two top elements '
                                                  'have no single common ceiling, it is NOT a lattice.',
                                  'number': '1.5',
                                  'title': 'Partial Orders (POSETs) and Lattices'}],
               'real_life_examples': [ { 'text': "An employment contract states: 'If you complete the milestone (P), "
                                                 "you get a bonus (Q)'. If you do not finish the milestone (P = "
                                                 'False), the company has not broken its promise regardless of whether '
                                                 'it gives a bonus or not.',
                                         'title': 'Real-Life Analogy: Employment Contract & Vacuous Truth'}],
               'title': 'Discrete Mathematics - Mathematical Logic & Set Theory',
               'worked_examples': [ { 'answer': 'The formula is a TAUTOLOGY (Valid statement).',
                                      'problem': 'Simplify the compound propositional formula: [ (P → Q) ∧ (Q → R) ] → '
                                                 '(P → R). Determine whether it is a Tautology, Contradiction, or '
                                                 'Contingency.',
                                      'steps': [ 'Step 1: Identify that this formula represents the classical '
                                                 'Hypothetical Syllogism rule of inference.',
                                                 'Step 2: Rewrite using the implication equivalence A → B ≡ ~A ∨ B. '
                                                 'Let antecedent be H = (P → Q) ∧ (Q → R). The statement becomes ~H ∨ '
                                                 '(P → R).',
                                                 'Step 3: Analyze truth values. Assume the entire formula is False. '
                                                 'For an implication A → B to be False, antecedent A must be True and '
                                                 'consequent B must be False.',
                                                 'Step 4: If consequent (P → R) is False, we must have P = True and R '
                                                 '= False.',
                                                 'Step 5: Substitute P = True and R = False into antecedent H: H = '
                                                 '(True → Q) ∧ (Q → False) = Q ∧ ~Q = False.',
                                                 'Step 6: But H was assumed to be True! We reached a contradiction '
                                                 '(False = True). Hence, it is impossible for the formula to ever be '
                                                 'False.'],
                                      'title': 'Worked Example: Logic Equivalence & Implication Simplification'},
                                    { 'answer': '11,664 Anti-symmetric relations.',
                                      'problem': 'Let set A = {1, 2, 3, 4}. How many total relations on A are '
                                                 'Anti-symmetric?',
                                      'steps': [ 'Step 1: The size of set A is n = 4. The Cartesian product A × A has '
                                                 'n² = 16 pairs.',
                                                 'Step 2: Partition the 16 pairs into two groups: (a) Diagonal pairs '
                                                 '(x, x) where there are n = 4 pairs, and (b) Off-diagonal symmetric '
                                                 'pairs {(x, y), (y, x)} where x ≠ y. Total off-diagonal pairs = n(n - '
                                                 '1) / 2 = 4(3) / 2 = 6 pairs.',
                                                 'Step 3: For each diagonal pair (x, x), an anti-symmetric relation '
                                                 'can either include it or exclude it. So there are 2 choices per '
                                                 'diagonal pair. For 4 pairs: 2⁴ = 16 choices.',
                                                 'Step 4: For each pair of off-diagonal elements {(x, y), (y, x)}, an '
                                                 'anti-symmetric relation can: (1) Include (x, y) only, (2) Include '
                                                 '(y, x) only, or (3) Include neither. It CANNOT include both! So '
                                                 'there are 3 choices per pair.',
                                                 'Step 5: For 6 off-diagonal pairs: 3⁶ = 729 choices.',
                                                 'Step 6: Total anti-symmetric relations = 2⁴ × 3⁶ = 16 × 729 = '
                                                 '11,664.'],
                                      'title': 'Worked Example: Counting Anti-Symmetric Relations'}]},
  ('EM', 1): { 'chapter_number': 2,
               'exam_traps': [ { 'title': 'Eulerian Circuit vs Eulerian Path',
                                 'warning': 'If a question asks for an Eulerian CIRCUIT, ALL vertices must have even '
                                            'degree! If exactly 2 vertices have odd degree, it has an Eulerian PATH, '
                                            'NOT a circuit.'}],
               'foundations': [ { 'content': '• <b>Core Counting Principles:</b><br/>\n'
                                             '&nbsp;&nbsp;• <b>Permutation (Order matters):</b> <code>ⁿPᵣ = n! / (n - '
                                             'r)!</code>.<br/>\n'
                                             '&nbsp;&nbsp;• <b>Combination (Order does not matter):</b> <code>ⁿCᵣ = n! '
                                             '/ [r! (n - r)!]</code>.<br/><br/>\n'
                                             '\n'
                                             '• <b>Stars and Bars Theorem (Distributing identical items into distinct '
                                             'bins):</b><br/>\n'
                                             '&nbsp;&nbsp;• <b>Case 1: Non-negative integer solutions:</b> <code>x₁ + '
                                             'x₂ + ... + xᵣ = n</code> where <code>xᵢ ≥ 0</code>.<br/>\n'
                                             '&nbsp;&nbsp;&nbsp;&nbsp;<b>Formula:</b> <code>ⁿ⁺ʳ⁻¹Cᵣ₋₁</code>.<br/>\n'
                                             '&nbsp;&nbsp;• <b>Case 2: Positive integer solutions:</b> <code>x₁ + x₂ + '
                                             '... + xᵣ = n</code> where <code>xᵢ ≥ 1</code>.<br/>\n'
                                             '&nbsp;&nbsp;&nbsp;&nbsp;<b>Formula:</b> <code>ⁿ⁻¹Cᵣ₋₁</code>.<br/><br/>\n'
                                             '\n'
                                             '• <b>Derangements (Permutations where NO element appears in its original '
                                             'spot):</b><br/>\n'
                                             '&nbsp;&nbsp;• Formula: <code>Dₙ = n! × [1 - 1/1! + 1/2! - 1/3! + ... + '
                                             '(-1)ⁿ/n!]</code>.<br/>\n'
                                             '&nbsp;&nbsp;• Useful standard values: D₁ = 0, D₂ = 1, D₃ = 2, D₄ = 9, D₅ '
                                             '= 44.',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: In Pigeonhole Principle (PHP), if n items '
                                                  'are put into k containers, at least one container must contain at '
                                                  'least ⌈n / k⌉ items!',
                                  'number': '2.1',
                                  'title': 'Permutations, Combinations & Stars-and-Bars'},
                                { 'content': '• <b>The Handshaking Lemma (Fundamental Theorem of Graph '
                                             'Theory):</b><br/>\n'
                                             '&nbsp;&nbsp;<code>∑ deg(v) = 2|E|</code> for all vertices v ∈ V.<br/>\n'
                                             '&nbsp;&nbsp;<i>Why?</i> Every edge has two endpoints. When you sum all '
                                             'vertex degrees, every edge is counted exactly twice!<br/><br/>\n'
                                             '\n'
                                             '• <b>Critical Inferences from Handshaking Lemma:</b><br/>\n'
                                             '&nbsp;&nbsp;• The sum of degrees in ANY graph is ALWAYS an <b>EVEN</b> '
                                             'integer.<br/>\n'
                                             '&nbsp;&nbsp;• <b>The Odd Degree Theorem:</b> In any undirected graph, '
                                             'the number of vertices with ODD degree is ALWAYS <b>EVEN</b>! You can '
                                             'never have 3 or 5 odd-degree vertices.<br/><br/>\n'
                                             '\n'
                                             '• <b>Havel-Hakimi Theorem (Testing if a degree sequence is '
                                             'graphic):</b><br/>\n'
                                             '&nbsp;&nbsp;1. Sort the sequence in descending order: d₁, d₂, ..., '
                                             'dₙ.<br/>\n'
                                             '&nbsp;&nbsp;2. Remove d₁, and subtract 1 from the next d₁ numbers.<br/>\n'
                                             '&nbsp;&nbsp;3. Repeat sorting and reduction. If you reach all zeros, the '
                                             'sequence is graphic! If negative numbers appear, it is NOT graphic.',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: In a k-regular graph with n vertices, total '
                                                  'edges |E| = (n × k) / 2.',
                                  'number': '2.2',
                                  'title': 'Handshaking Lemma & Degree Sequences'},
                                { 'content': '• <b>What is a Planar Graph?</b> A graph that can be drawn in a plane '
                                             'such that no two edges cross each other.<br/><br/>\n'
                                             '\n'
                                             "• <b>Euler's Formula for Connected Planar Graphs:</b><br/>\n"
                                             '&nbsp;&nbsp;<code>V - E + F = 2</code> (where V = vertices, E = edges, F '
                                             '= faces/regions including the unbounded outer face).<br/><br/>\n'
                                             '\n'
                                             '• <b>Planar Edge Bounds (Essential for GATE MCQs):</b><br/>\n'
                                             '&nbsp;&nbsp;• For any simple planar graph with V ≥ 3: <code>E ≤ 3V - '
                                             '6</code>.<br/>\n'
                                             '&nbsp;&nbsp;• For a simple planar graph with <b>NO triangles</b> (e.g. '
                                             'bipartite planar graphs): <code>E ≤ 2V - 4</code>.<br/><br/>\n'
                                             '\n'
                                             "• <b>Kuratowski's Theorem (Planarity Test):</b><br/>\n"
                                             '&nbsp;&nbsp;- A graph is planar if and only if it does NOT contain a '
                                             'subgraph that is homeomorphic to (or can be contracted from) <b>K₅</b> '
                                             '(complete graph on 5 vertices) or <b>K₃,₃</b> (complete bipartite '
                                             'utility graph).',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: K₅ has V=5, E=10. By 3V-6 = 9, E exceeds '
                                                  'bound, so K₅ is non-planar! K₃,₃ has V=6, E=9. By 2V-4 = 8, K₃,₃ is '
                                                  'non-planar!',
                                  'number': '2.3',
                                  'title': "Planar Graphs & Euler's Formula"},
                                { 'content': '• <b>Eulerian Graphs (Traverse every EDGE exactly once):</b><br/>\n'
                                             '&nbsp;&nbsp;• <b>Eulerian Circuit:</b> Connected graph where <b>EVERY '
                                             'vertex has an EVEN degree</b>.<br/>\n'
                                             '&nbsp;&nbsp;• <b>Eulerian Path:</b> Connected graph with <b>EXACTLY TWO '
                                             'vertices of odd degree</b> (path starts at one odd vertex and ends at '
                                             'the other).<br/><br/>\n'
                                             '\n'
                                             '• <b>Hamiltonian Graphs (Visit every VERTEX exactly once):</b><br/>\n'
                                             '&nbsp;&nbsp;• A Hamiltonian cycle visits every vertex and returns to the '
                                             'start.<br/>\n'
                                             "&nbsp;&nbsp;• <b>Dirac's Theorem (Sufficient condition):</b> If |V| ≥ 3 "
                                             'and for every vertex deg(v) ≥ |V| / 2, the graph is '
                                             'Hamiltonian.<br/><br/>\n'
                                             '\n'
                                             '• <b>Graph Coloring & Chromatic Number χ(G):</b><br/>\n'
                                             '&nbsp;&nbsp;• Chromatic number χ(G) is the minimum colors needed to '
                                             'color vertices so no adjacent vertices share a color.<br/>\n'
                                             '&nbsp;&nbsp;• <b>Bipartite Graph:</b> χ(G) = 2. A graph is 2-colorable '
                                             '(bipartite) iff it contains <b>NO ODD CYCLES</b>!<br/>\n'
                                             '&nbsp;&nbsp;• <b>Four Color Theorem:</b> Every planar graph can be '
                                             'colored with at most 4 colors: χ(G) ≤ 4.',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: Checking Eulerian graph takes O(V+E) time '
                                                  '(just check vertex degrees). Checking Hamiltonian cycle is '
                                                  'NP-Complete!',
                                  'number': '2.4',
                                  'title': 'Eulerian & Hamiltonian Graphs, Graph Coloring'}],
               'real_life_examples': [ { 'text': 'An Eulerian circuit is a street sweeper who must clean every single '
                                                 'street (edge) once. A Hamiltonian cycle is a delivery driver who '
                                                 'must visit every home (vertex) once.',
                                         'title': 'Real-Life Analogy: Street Sweeper vs Traveling Salesperson'}],
               'title': 'Discrete Mathematics - Graph Theory & Combinatorics',
               'worked_examples': [ { 'answer': 'Total faces F = 12 (11 bounded, 1 unbounded).',
                                      'problem': 'A connected planar simple graph has 20 vertices and each vertex has '
                                                 'degree 3. How many bounded and unbounded faces does the graph divide '
                                                 'the plane into?',
                                      'steps': [ 'Step 1: Use Handshaking Lemma to find edges E. Sum of degrees = 20 × '
                                                 '3 = 60. So 2E = 60 ⇒ E = 30 edges.',
                                                 "Step 2: Apply Euler's Formula: V - E + F = 2.",
                                                 'Step 3: Substitute V = 20 and E = 30: 20 - 30 + F = 2 ⇒ -10 + F = 2 '
                                                 '⇒ F = 12 total faces.',
                                                 'Step 4: Out of 12 total faces, exactly 1 face is the unbounded '
                                                 'external face. Therefore, there are 11 bounded faces and 1 unbounded '
                                                 'face.'],
                                      'title': 'Worked Example: Planar Graph Face Calculation'}]},
  ('EM', 2): { 'chapter_number': 3,
               'exam_traps': [ { 'title': 'Eigenvalues vs Eigenvectors Scaling Trap',
                                 'warning': 'Eigenvectors are never unique; any non-zero scalar multiple of an '
                                            'eigenvector is also an eigenvector for the same eigenvalue.'}],
               'foundations': [ { 'content': '• <b>What is Rank of a Matrix?</b><br/>\n'
                                             '&nbsp;&nbsp;- The maximum number of linearly independent rows (or '
                                             'columns) in the matrix.<br/>\n'
                                             '&nbsp;&nbsp;- For an m × n matrix A: <code>Rank(A) ≤ min(m, '
                                             'n)</code>.<br/><br/>\n'
                                             '\n'
                                             '• <b>Properties of Rank (Frequently Tested in GATE):</b><br/>\n'
                                             '&nbsp;&nbsp;• <code>Rank(A + B) ≤ Rank(A) + Rank(B)</code>.<br/>\n'
                                             '&nbsp;&nbsp;• <code>Rank(AB) ≤ min(Rank(A), Rank(B))</code>.<br/>\n'
                                             '&nbsp;&nbsp;• <code>Rank(Aᵀ) = Rank(A)</code> and <code>Rank(Aᵀ A) = '
                                             'Rank(A)</code>.<br/>\n'
                                             '&nbsp;&nbsp;• A square n × n matrix is <b>Invertible (Non-singular)</b> '
                                             'if and only if <code>Rank(A) = n</code> (Full Rank, det(A) ≠ 0).',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: To find the rank quickly in exam, perform '
                                                  'elementary row operations to reduce to Row Echelon Form. The number '
                                                  'of non-zero rows is the Rank!',
                                  'number': '3.1',
                                  'title': 'Rank of a Matrix and Echelon Forms'},
                                { 'content': '• <b>Matrix Representation:</b> <code>A X = B</code>, where A is m × n '
                                             'coefficient matrix, X is n × 1 unknown vector, and [A|B] is the '
                                             'augmented matrix.<br/><br/>\n'
                                             '\n'
                                             '• <b>Master Consistency Decision Matrix:</b><br/>\n'
                                             "<div class='font-mono text-xs p-3 bg-slate-900 text-slate-100 rounded-xl "
                                             "my-2 leading-relaxed overflow-x-auto'>\n"
                                             'Condition                                   │ System Nature │ Solutions\n'
                                             '──────────────────────────────────────────────────────────────────────────\n'
                                             'Rank(A) < Rank([A|B])                       │ Inconsistent  │ NO '
                                             'SOLUTION (0)\n'
                                             'Rank(A) = Rank([A|B]) = n (number of vars) │ Consistent    │ UNIQUE '
                                             'SOLUTION (1)\n'
                                             'Rank(A) = Rank([A|B]) = r < n               │ Consistent    │ INFINITELY '
                                             'MANY SOLUTIONS\n'
                                             '</div>\n'
                                             '\n'
                                             '• <b>Homogeneous Systems (AX = 0):</b><br/>\n'
                                             '&nbsp;&nbsp;- Always consistent because X = 0 (Trivial solution) is '
                                             'always a solution!<br/>\n'
                                             '&nbsp;&nbsp;- If <code>det(A) ≠ 0</code> (Rank = n): ONLY the trivial '
                                             'zero solution exists.<br/>\n'
                                             '&nbsp;&nbsp;- If <code>det(A) = 0</code> (Rank < n): Non-trivial '
                                             '(non-zero) infinite solutions exist!',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: For AX = 0 to have a NON-ZERO solution, '
                                                  'det(A) MUST equal 0. This is the single most tested condition in '
                                                  'GATE linear algebra!',
                                  'number': '3.2',
                                  'title': 'System of Linear Equations (AX = B)'},
                                { 'content': '• <b>Characteristic Equation:</b> <code>det(A - λI) = 0</code>. Roots of '
                                             'this polynomial are the eigenvalues λ.<br/><br/>\n'
                                             '\n'
                                             '• <b>5 Gold-Plated Eigenvalue Theorems:</b><br/>\n'
                                             '&nbsp;&nbsp;1. <b>Sum of Eigenvalues = Trace of A</b> (sum of main '
                                             'diagonal elements): <code>∑ λᵢ = Trace(A)</code>.<br/>\n'
                                             '&nbsp;&nbsp;2. <b>Product of Eigenvalues = Determinant of A</b>: <code>∏ '
                                             'λᵢ = det(A)</code>.<br/>\n'
                                             '&nbsp;&nbsp;3. If λ is an eigenvalue of A, then:<br/>\n'
                                             '&nbsp;&nbsp;&nbsp;&nbsp;- <code>kλ</code> is an eigenvalue of '
                                             '<code>kA</code>.<br/>\n'
                                             '&nbsp;&nbsp;&nbsp;&nbsp;- <code>λᵐ</code> is an eigenvalue of '
                                             '<code>Aᵐ</code>.<br/>\n'
                                             '&nbsp;&nbsp;&nbsp;&nbsp;- <code>1 / λ</code> is an eigenvalue of '
                                             '<code>A⁻¹</code> (if det(A) ≠ 0).<br/>\n'
                                             '&nbsp;&nbsp;4. Eigenvalues of a <b>Triangular</b> or <b>Diagonal</b> '
                                             'matrix are simply its main diagonal entries!<br/>\n'
                                             '&nbsp;&nbsp;5. <b>Special Matrices:</b><br/>\n'
                                             '&nbsp;&nbsp;&nbsp;&nbsp;- Real Symmetric Matrix: All eigenvalues are '
                                             'strictly <b>REAL</b>.<br/>\n'
                                             '&nbsp;&nbsp;&nbsp;&nbsp;- Skew-Symmetric Matrix: All eigenvalues are '
                                             'either <b>pure imaginary</b> or <b>zero</b>.<br/>\n'
                                             '&nbsp;&nbsp;&nbsp;&nbsp;- Orthogonal Matrix: Absolute value of each '
                                             'eigenvalue is <b>1</b> (|λ| = 1).<br/>\n'
                                             '&nbsp;&nbsp;&nbsp;&nbsp;- Idempotent Matrix (A² = A): Eigenvalues are '
                                             'only <b>0 or 1</b>.<br/>\n'
                                             '&nbsp;&nbsp;&nbsp;&nbsp;- Nilpotent Matrix (Aᵏ = 0): ALL eigenvalues are '
                                             'strictly <b>0</b>.',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: Before doing lengthy characteristic '
                                                  'equation algebra, ALWAYS check: (1) Does sum of options equal '
                                                  'Trace? (2) Does product of options equal Determinant? 80% of GATE '
                                                  'questions are solved in 10 seconds this way!',
                                  'number': '3.3',
                                  'title': 'Eigenvalues, Eigenvectors & Properties'},
                                { 'content': '• <b>Cayley-Hamilton Theorem:</b><br/>\n'
                                             "&nbsp;&nbsp;- <i>'Every square matrix satisfies its own characteristic "
                                             "equation.'</i><br/>\n"
                                             '&nbsp;&nbsp;- If characteristic equation is <code>λ² - 5λ + 6 = '
                                             '0</code>, then <code>A² - 5A + 6I = 0</code>.<br/>\n'
                                             '&nbsp;&nbsp;- Multiplying by A⁻¹ gives: <code>A - 5I + 6A⁻¹ = 0 ⇒ A⁻¹ = '
                                             '(5I - A) / 6</code>.<br/><br/>\n'
                                             '\n'
                                             '• <b>LU Decomposition (A = L · U):</b><br/>\n'
                                             '&nbsp;&nbsp;- Factors matrix A into a Lower triangular matrix L and an '
                                             'Upper triangular matrix U.<br/>\n'
                                             '&nbsp;&nbsp;- <b>Doolittle Algorithm:</b> Diagonal elements of L are all '
                                             '1s (Lᵢᵢ = 1).<br/>\n'
                                             '&nbsp;&nbsp;- <b>Determinant:</b> <code>det(A) = det(L) × det(U) = 1 × ∏ '
                                             'Uᵢᵢ</code> (product of diagonal elements of U).<br/>\n'
                                             '&nbsp;&nbsp;- Solving AX = B: First solve <code>L Y = B</code> (Forward '
                                             'substitution), then solve <code>U X = Y</code> (Back substitution). '
                                             'Takes O(n²) once factorized!',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: LU decomposition exists for matrix A '
                                                  'without row exchanges if and only if all leading principal '
                                                  'submatrices of A have non-zero determinants.',
                                  'number': '3.4',
                                  'title': 'Cayley-Hamilton Theorem & LU Decomposition'}],
               'real_life_examples': [ { 'text': "Google's original PageRank algorithm models the entire internet as a "
                                                 'giant transition matrix. The rank of every website on Earth is '
                                                 'literally the principal eigenvector of that matrix!',
                                         'title': 'Real-Life Analogy: Google PageRank & Eigenvectors'}],
               'title': 'Linear Algebra - Systems, Eigenvalues & LU Decomposition',
               'worked_examples': [ { 'answer': 'Eigenvalues are 1 and 6.',
                                      'problem': 'Find the eigenvalues of matrix A = [[2, -1], [-4, 5]].',
                                      'steps': [ 'Step 1: Calculate Trace(A) = sum of diagonal elements = 2 + 5 = 7.',
                                                 'Step 2: Calculate Determinant det(A) = (2)(5) - (-1)(-4) = 10 - 4 = '
                                                 '6.',
                                                 'Step 3: We need two eigenvalues λ₁, λ₂ such that λ₁ + λ₂ = 7 and λ₁ '
                                                 '· λ₂ = 6.',
                                                 'Step 4: Solve the quadratic equation λ² - (Trace)λ + det(A) = 0 ⇒ λ² '
                                                 '- 7λ + 6 = 0.',
                                                 'Step 5: Factorize: (λ - 1)(λ - 6) = 0 ⇒ λ₁ = 1, λ₂ = 6.'],
                                      'title': 'Worked Example: Finding Eigenvalues using Trace and Det'}]},
  ('EM', 3): { 'chapter_number': 4,
               'exam_traps': [ { 'title': 'Independent vs Mutually Exclusive Trap',
                                 'warning': 'Mutually exclusive means P(A ∩ B) = 0 (cannot happen together). '
                                            'Independent means P(A ∩ B) = P(A) · P(B). If P(A) > 0 and P(B) > 0, '
                                            'events CANNOT be both mutually exclusive and independent!'}],
               'foundations': [ { 'content': "• <b>L'Hôpital's Rule for Indeterminate Limits:</b><br/>\n"
                                             '&nbsp;&nbsp;- Applicable ONLY for forms <code>0 / 0</code> or <code>∞ / '
                                             '∞</code>.<br/>\n'
                                             "&nbsp;&nbsp;- <code>lim [f(x) / g(x)] = lim [f'(x) / g'(x)]</code> "
                                             '(Differentiate numerator and denominator separately until '
                                             'determinate).<br/><br/>\n'
                                             '\n'
                                             '• <b>Maxima and Minima Checklist:</b><br/>\n'
                                             '&nbsp;&nbsp;1. Find critical points by setting first derivative to zero: '
                                             "<code>f'(x) = 0</code>.<br/>\n"
                                             "&nbsp;&nbsp;2. Compute second derivative <code>f''(x)</code> at critical "
                                             'point c:<br/>\n'
                                             "&nbsp;&nbsp;&nbsp;&nbsp;- If <code>f''(c) < 0</code>: Local "
                                             '<b>MAXIMUM</b> at c.<br/>\n'
                                             "&nbsp;&nbsp;&nbsp;&nbsp;- If <code>f''(c) > 0</code>: Local "
                                             '<b>MINIMUM</b> at c.<br/>\n'
                                             "&nbsp;&nbsp;&nbsp;&nbsp;- If <code>f''(c) = 0</code>: Test fails (use "
                                             'higher derivatives or first derivative sign test).',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: Differentiability ALWAYS implies '
                                                  'Continuity. But Continuity DOES NOT imply Differentiability (e.g. '
                                                  'f(x) = |x| is continuous at 0 but not differentiable at 0).',
                                  'number': '4.1',
                                  'title': 'Calculus: Limits, Continuity & Maxima-Minima'},
                                { 'content': '• <b>Conditional Probability:</b><br/>\n'
                                             '&nbsp;&nbsp;<code>P(A | B) = P(A ∩ B) / P(B)</code> (where P(B) > '
                                             '0).<br/>\n'
                                             '&nbsp;&nbsp;• <b>Independent Events:</b> A and B are independent iff '
                                             '<code>P(A ∩ B) = P(A) · P(B)</code>. (Notice: Mutually exclusive events '
                                             'with non-zero probability can NEVER be independent!).<br/><br/>\n'
                                             '\n'
                                             "• <b>Bayes' Theorem Formula:</b><br/>\n"
                                             '&nbsp;&nbsp;<code>P(Bᵢ | A) = [P(A | Bᵢ) · P(Bᵢ)] / [∑ P(A | Bⱼ) · '
                                             'P(Bⱼ)]</code><br/>\n'
                                             '&nbsp;&nbsp;• <i>Intuition:</i> Updates the prior probability P(Bᵢ) '
                                             'after observing new evidence A to get the posterior probability P(Bᵢ | '
                                             'A).',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: In Bayes medical testing questions, even '
                                                  'with a 99% accurate test, if the disease is extremely rare (e.g. '
                                                  '0.1%), the probability of actually having the disease given a '
                                                  'positive test is surprisingly low due to false positives!',
                                  'number': '4.2',
                                  'title': "Probability Axioms & Bayes' Theorem"},
                                { 'content': '• <b>Discrete Distributions:</b><br/>\n'
                                             "<div class='font-mono text-xs p-3 bg-slate-900 text-slate-100 rounded-xl "
                                             "my-2 leading-relaxed overflow-x-auto'>\n"
                                             'Distribution │ PMF P(X = k)                  │ Mean E[X] │ Variance '
                                             'Var(X)\n'
                                             '─────────────────────────────────────────────────────────────────────────────\n'
                                             'Binomial     │ ⁿCₖ pᵏ (1-p)ⁿ⁻ᵏ               │ np        │ np(1 - p)\n'
                                             'Poisson      │ (e⁻ᵝ · λᵏ) / k!               │ λ         │ λ (Mean = '
                                             'Variance!)\n'
                                             'Geometric    │ (1-p)ᵏ⁻¹ · p                  │ 1 / p     │ (1 - p) / p²\n'
                                             '</div>\n'
                                             '\n'
                                             '• <b>Continuous Distributions:</b><br/>\n'
                                             '&nbsp;&nbsp;• <b>Uniform Distribution on [a, b]:</b> Mean = (a + b) / 2, '
                                             'Variance = (b - a)² / 12.<br/>\n'
                                             '&nbsp;&nbsp;• <b>Exponential Distribution (Parameter λ):</b><br/>\n'
                                             '&nbsp;&nbsp;&nbsp;&nbsp;- PDF: <code>f(x) = λ e⁻ᵝˣ</code> (for x ≥ 0). '
                                             'Mean = 1/λ, Variance = 1/λ².<br/>\n'
                                             '&nbsp;&nbsp;&nbsp;&nbsp;- <b>Memoryless Property:</b> <code>P(X > s + t '
                                             '| X > s) = P(X > t)</code>. The past waiting time gives zero information '
                                             'about future waiting time!<br/>\n'
                                             '&nbsp;&nbsp;• <b>Normal (Gaussian) Distribution:</b> Bell curve, '
                                             'Symmetric about mean μ. 68.2% data within μ ± σ, 95.4% within μ ± 2σ, '
                                             '99.7% within μ ± 3σ.',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: For Poisson distribution, Mean is ALWAYS '
                                                  'equal to Variance! If an exam question gives Mean = 4, Variance is '
                                                  'guaranteed to be 4.',
                                  'number': '4.3',
                                  'title': 'Discrete & Continuous Probability Distributions'}],
               'real_life_examples': [ { 'text': 'An exponential distribution represents electronic components. If a '
                                                 'lightbulb has survived 100 hours, the probability it lasts another '
                                                 '10 hours is identical to a brand new bulb lasting 10 hours.',
                                         'title': 'Real-Life Analogy: The Memoryless Lightbulb'}],
               'title': 'Calculus & Probability - Distributions and Bayes Theorem',
               'worked_examples': [ { 'answer': 'Probability is approximately 4.72%.',
                                      'problem': 'A rare disease affects 0.1% of a population. A diagnostic test is '
                                                 '99% accurate for sick people, but has a 2% false positive rate for '
                                                 'healthy people. If a randomly chosen person tests positive, what is '
                                                 'the probability they actually have the disease?',
                                      'steps': [ 'Step 1: Define events: D = Person has disease, T = Test is positive. '
                                                 'P(D) = 0.001, P(~D) = 0.999.',
                                                 'Step 2: Test sensitivities: P(T | D) = 0.99, P(T | ~D) = 0.02.',
                                                 'Step 3: Calculate Total Probability P(T) = P(T|D)P(D) + P(T|~D)P(~D) '
                                                 '= (0.99)(0.001) + (0.02)(0.999) = 0.00099 + 0.01998 = 0.02097.',
                                                 "Step 4: Apply Bayes' Rule: P(D | T) = P(T|D)P(D) / P(T) = 0.00099 / "
                                                 '0.02097 ≈ 0.0472 (4.72%).'],
                                      'title': "Worked Example: Bayes' Theorem Medical Diagnostic Test"}]}}
