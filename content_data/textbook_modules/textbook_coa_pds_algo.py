# textbook_coa_pds_algo.py
# Simplified, crystal-clear study notes for COA, PDS, and Algorithms.
# Written in simple, friendly, easy-to-understand language for GATE 2027 CSE aspirants.

CHAPTERS_COA_PDS_ALGO = {}

# =============================================================================
# COMPUTER ORGANIZATION AND ARCHITECTURE (COA)
# =============================================================================

# COA Chapter 0: Machine Instructions & Addressing Modes
CHAPTERS_COA_PDS_ALGO[("COA", 0)] = {
    "sub_id": "COA",
    "chap_idx": 0,
    "title": "Machine Instructions & Addressing Modes",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The Scavenger Hunt Clues (Addressing Modes)",
            "text": "Imagine a scavenger hunt game:\n• Immediate: The clue card gives you ₹500 cash directly taped to it (data is inside the instruction!).\n• Direct: The card gives an address: 'Go to House #42' (direct memory address).\n• Indirect: The card says: 'Open locker 10; inside locker 10 is a note with the real address' (Pointer to pointer).\n• PC-Relative: The card says: 'From where you are right now, take 5 steps forward' (used for loops and branch jumps)."
        },
        {
            "title": "Real-Life Example 2: Little-Endian vs Big-Endian Mail (Byte Ordering)",
            "text": "When writing an address, does the country come first or last? In Big-Endian, you write the Most Significant part first (Country, then City, then House number). In Little-Endian, you write the Least Significant byte first (House number first, then City, Country last). Intel x86 processors use Little-Endian; network packets use Big-Endian."
        },
        {
            "title": "Real-Life Example 3: Expanding Menu Combos (Expanding Opcode)",
            "text": "In a fast food shop, a 2-bit code lets you choose 4 combos. But what if you want 3 popular big meals (requiring lots of side dishes) and 8 small snacks (needing fewer sides)? By using one code as an 'escape code' to unlock longer codes, you can support both. This is Expanding Opcode."
        }
    ],
    "foundations": [
        {
            "number": "9.1",
            "title": "Effective Address (EA) in Common Addressing Modes",
            "content": (
                "The Effective Address (EA) is the exact RAM address where the data is stored.<br/>"
                "• <b>Immediate:</b> Operand is in instruction. EA = None. (0 memory accesses).<br/>"
                "• <b>Direct:</b> EA = Address field. (1 memory access).<br/>"
                "• <b>Indirect:</b> EA = M[Address field]. (2 memory accesses).<br/>"
                "• <b>Register:</b> Data is in CPU register. EA = None. (0 memory accesses, ultra-fast!).<br/>"
                "• <b>Register Indirect:</b> EA = [Register content]. (1 memory access).<br/>"
                "• <b>PC-Relative:</b> EA = PC + Offset. (Used for Branch/Jump instructions)."
            ),
            "crucial_rule": "GOLDEN RULE: In PC-Relative addressing, remember that PC has ALREADY been incremented to the next instruction before the offset is added: EA = Next_PC + Offset!"
        },
        {
            "number": "9.2",
            "title": "Hardwired vs Microprogrammed Control Unit",
            "content": (
                "• <b>Hardwired:</b> Built using fast digital logic gates. Blazing fast (RISC processors), but impossible to modify once manufactured.<br/>"
                "• <b>Microprogrammed:</b> Control signals are stored in a small ROM (Control Memory). Slower (CISC processors), but flexible and easy to update with firmware."
            ),
            "crucial_rule": "GOLDEN RULE: Horizontal microprogramming has 1 bit per control signal (no decoder needed, wide micro-words). Vertical microprogramming encodes signals with decoders (narrow words, smaller memory)."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Expanding Opcode",
            "problem": "A 16-bit computer uses 4-bit register addresses. It supports 3-register instructions and 2-register instructions. If there are 14 different 3-register instructions, how many 2-register instructions can be supported?",
            "steps": [
                "Step 1: Total bits = 16. A 3-register instruction uses 3 × 4 = 12 bits for registers.",
                "Step 2: Remaining bits for opcode = 16 - 12 = 4 bits (Total patterns = 2^4 = 16).",
                "Step 3: 14 patterns are used for 3-register instructions. Unused patterns = 16 - 14 = 2.",
                "Step 4: For 2-register instructions, only 2 × 4 = 8 bits are needed for registers. Opcode expands by 4 bits!",
                "Step 5: Number of 2-register instructions = (Unused patterns) × 2^4 = 2 × 16 = 32."
            ],
            "answer": "Maximum 2-register instructions = 32."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Byte vs Word Addressable",
            "warning": "Always check if memory is byte-addressable (8 bits per address) or word-addressable (e.g. 32 bits = 4 bytes per address). A 64 MB memory needs 26 bits if byte-addressed, but only 24 bits if 4-byte-word addressed!"
        }
    ]
}

# COA Chapter 1: ALU & Control Unit
CHAPTERS_COA_PDS_ALGO[("COA", 1)] = {
    "sub_id": "COA",
    "chap_idx": 1,
    "title": "ALU, Control Unit & Memory Interfacing",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Multiplying by 99 in Your Head (Booth's Algorithm)",
            "text": "If someone asks you to multiply 27 by 99, do you do 99 separate additions? No! You do 27 × (100 - 1) = 2700 - 27 = 2673 (just one subtraction and one shift!). Booth's Algorithm does the exact same trick in binary: when it sees a long run of 1s (like 0111110), it does 1 subtraction at the start and 1 addition at the end, skipping all the middle steps!"
        },
        {
            "title": "Real-Life Example 2: The VIP Express Package Delivery (Direct Memory Access - DMA)",
            "text": "When a 4K movie downloads from hard drive to RAM, if the CPU had to move every single byte one by one, the CPU would freeze. A DMA Controller steps in, takes control of the bus, and copies the data directly between disk and RAM while the CPU keeps running your games without interruption."
        },
        {
            "title": "Real-Life Example 3: Phone Notification Interrupts (Interrupt-Driven I/O)",
            "text": "Instead of checking your phone screen every 2 seconds to see if you got a WhatsApp message (Polling / Programmed I/O: wastes battery and time!), your phone stays asleep until a notification sound rings (Interrupt). The CPU only pauses what it is doing when a real event occurs."
        }
    ],
    "foundations": [
        {
            "number": "10.1",
            "title": "Booth's Multiplication Rules (Q_i, Q_{i-1})",
            "content": (
                "Scan bits from right to left with Q_{-1} initialized to 0:<br/>"
                "• <b>0 0:</b> Just Arithmetic Right Shift (ARS).<br/>"
                "• <b>0 1:</b> Add Multiplicand (A ← A + M), then ARS.<br/>"
                "• <b>1 0:</b> Subtract Multiplicand (A ← A - M), then ARS.<br/>"
                "• <b>1 1:</b> Just Arithmetic Right Shift (ARS)."
            ),
            "crucial_rule": "GOLDEN RULE: Shift in Booth's is strictly ARITHMETIC Right Shift (replicates sign bit, preserving positive/negative sign)!"
        },
        {
            "number": "10.2",
            "title": "DMA Cycle Stealing Percentage",
            "content": (
                "In cycle stealing mode, DMA steals 1 memory bus cycle from the CPU whenever a data unit is ready.<br/>"
                "• <b>CPU Time Stolen (%):</b> (Device Transfer Rate / Memory Bus Bandwidth) × 100%."
            ),
            "crucial_rule": "GOLDEN RULE: Percentage of CPU time available for normal work = 100% - (Percentage stolen by DMA)."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: DMA Bus Overhead",
            "problem": "A hard disk transfers data at 2 MB/sec. The memory bus has cycle time 200 ns and transfers 1 byte per cycle. In cycle-stealing mode, what percentage of CPU time is stolen by DMA?",
            "steps": [
                "Step 1: Calculate Memory Bus Bandwidth: 1 Byte / (200 × 10^-9 s) = 5,000,000 Bytes/s = 5 MB/sec.",
                "Step 2: Hard disk transfer rate = 2 MB/sec.",
                "Step 3: Fraction of time stolen = 2 MB/s / 5 MB/s = 2/5 = 0.40.",
                "Step 4: Percentage stolen = 40%."
            ],
            "answer": "CPU time consumed by DMA = 40% (60% remaining for CPU)."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Vectored vs Non-Vectored Interrupts",
            "warning": "Vectored interrupts supply the memory address of the handler directly on the bus. Non-vectored interrupts have a fixed, hardwired address in the CPU."
        }
    ]
}

# COA Chapter 2: Memory Hierarchy & Cache
CHAPTERS_COA_PDS_ALGO[("COA", 2)] = {
    "sub_id": "COA",
    "chap_idx": 2,
    "title": "Memory Hierarchy, Cache Mapping & AMAT",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The Kitchen Spice Rack (Cache Memory Locality)",
            "text": "When cooking dinner, a chef keeps salt, pepper, and oil on a tiny shelf right above the stove (L1 Cache: instant 1-second access). They don't walk down to the cold basement pantry (Main RAM: slow 1-minute walk) every time they need a pinch of salt! Because you tend to reuse recent items (Temporal Locality) and nearby items (Spatial Locality), 95% of cooking needs are met from the spice rack."
        },
        {
            "title": "Real-Life Example 2: Assigned Parking Spots (Cache Mapping)",
            "text": "• Direct Mapped: Your apartment number determines your exact parking slot (Slot = Flat % 10). If Flat 104 and 204 arrive, they fight over Slot 4 (Conflict Miss!).\n• Fully Associative: Park in ANY vacant slot anywhere in the lot (Zero conflicts, but you need a security guard to search the whole lot).\n• Set-Associative: Each floor gets a 4-car designated cluster (The best balance of speed and cost!)."
        },
        {
            "title": "Real-Life Example 3: Pencil Scratchpad vs Ink Ledger (Write-Through vs Write-Back)",
            "text": "Write-Through updates both cache and main memory immediately on every write (slow, but safe). Write-Back writes only to the cache, marking it with a 'Dirty Bit'. It only copies the dirty block to main RAM when that block is being kicked out (much faster!)."
        }
    ],
    "foundations": [
        {
            "number": "11.1",
            "title": "Address Split in Cache Mapping",
            "content": (
                "For address length P bits, Block Size B = 2^b bytes (Offset = b bits):<br/>"
                "• <b>Direct Mapped:</b> [ Tag | Line Index (c bits) | Block Offset (b bits) ]. Tag = P - c - b.<br/>"
                "• <b>k-Way Set Associative:</b> [ Tag | Set Index (s bits) | Block Offset (b bits) ].<br/>"
                "&nbsp;&nbsp;Number of Sets S = (Total Lines) / k = 2^s.<br/>"
                "• <b>Fully Associative:</b> [ Tag | Block Offset (b bits) ]. (No index bits!)."
            ),
            "crucial_rule": "GOLDEN RULE: Always divide Total Cache Lines by k to find the number of sets: Sets = Lines / k. Never forget this step!"
        },
        {
            "number": "11.2",
            "title": "Average Memory Access Time (AMAT)",
            "content": (
                "• <b>Formula:</b> AMAT = Hit_Time + (Miss_Rate × Miss_Penalty).<br/>"
                "• <b>Two-Level Cache:</b> AMAT = t_L1 + (Miss_Rate_L1 × [ t_L2 + (Miss_Rate_L2_local × t_main) ])."
            ),
            "crucial_rule": "GOLDEN RULE: The 3 C's of Cache Misses: Compulsory (first-time access), Capacity (cache is too small), Conflict (multiple blocks fight for the same set)."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Set-Associative Cache Bits",
            "problem": "A 32-bit processor has a 64 KB 4-way set-associative cache with 32-byte blocks. Find: (1) Offset bits, (2) Set index bits, (3) Tag bits.",
            "steps": [
                "Step 1: Block Size = 32 Bytes = 2^5 Bytes ⇒ Offset b = 5 bits.",
                "Step 2: Total lines = Cache Size / Block Size = 64 KB / 32 B = 65,536 / 32 = 2048 lines.",
                "Step 3: Number of sets S = 2048 / 4 = 512 sets = 2^9 ⇒ Set Index s = 9 bits.",
                "Step 4: Tag bits = Total bits - Set bits - Offset bits = 32 - 9 - 5 = 18 bits."
            ],
            "answer": "Offset = 5 bits, Set Index = 9 bits, Tag = 18 bits."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Tag Directory Size",
            "warning": "Tag directory memory size = (Total Lines) × (Tag bits + Valid bit). Remember to multiply by Total Lines, NOT the number of sets!"
        }
    ]
}

# COA Chapter 3: Pipelining
CHAPTERS_COA_PDS_ALGO[("COA", 3)] = {
    "sub_id": "COA",
    "chap_idx": 3,
    "title": "Instruction Pipelining, Hazards & Performance",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Doing Laundry (Pipelining Principle)",
            "text": "Imagine washing 4 loads of laundry: Wash (30 min), Dry (40 min), Fold (20 min). If you do them one by one, 4 loads take 4 × 90 = 360 min (6 hours!). But in a pipeline: while load 1 is in the dryer, load 2 enters the washer! The dryer is the bottleneck (40 min). Once running, one clean basket finishes every 40 minutes, cutting total time in half!"
        },
        {
            "title": "Real-Life Example 2: Passing Ingredients Direct from Frying Pan (Operand Forwarding)",
            "text": "Step 1 cooks onions; Step 2 needs cooked onions to make sauce. If Step 2 waits until Step 1 is plated and stored in the fridge, you waste time. Operand Forwarding (Bypassing) takes the hot onions directly from the frying pan and dumps them into Step 2's pot immediately!"
        },
        {
            "title": "Real-Life Example 3: The Highway Fog Fork (Branch Prediction)",
            "text": "Driving fast toward a fork in the road in dense fog. If you stop the car to read the sign, traffic halts (Branch Stall). Instead, you guess 'keep going left'. If your guess was right, you didn't lose any speed. If wrong, you stop, reverse, and take the right fork (Branch Penalty)."
        }
    ],
    "foundations": [
        {
            "number": "12.1",
            "title": "Pipeline Clock Time & Speedup Formula",
            "content": (
                "For a k-stage pipeline executing n instructions:<br/>"
                "• <b>Clock Cycle Time (T_pipe):</b> max(stage_delays) + register_delay.<br/>"
                "• <b>Total Clock Cycles:</b> k + (n - 1) cycles.<br/>"
                "• <b>Ideal Speedup:</b> S_max = k (number of stages, as n becomes very large)."
            ),
            "crucial_rule": "GOLDEN RULE: Always add the pipeline buffer register delay to the maximum stage delay: T_clk = max(stages) + t_buffer!"
        },
        {
            "number": "12.2",
            "title": "The 3 Pipeline Hazards & Solutions",
            "content": (
                "• <b>Structural Hazard:</b> Two instructions fight for same hardware (e.g. single memory port). Fix: Separate Instruction and Data Caches.<br/>"
                "• <b>Data Hazard (RAW):</b> Reading before writing. Fix: <b>Operand Forwarding</b>.<br/>"
                "• <b>Control Hazard:</b> Caused by branch instructions. Fix: Branch Prediction and delayed branching."
            ),
            "crucial_rule": "GOLDEN RULE: Operand forwarding CANNOT eliminate the stall between a LOAD instruction and an immediate ALU instruction using that value (Load-Use Hazard)! 1 stall cycle is still required."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Calculating Speedup",
            "problem": "A 5-stage pipeline has stage delays of 150, 120, 180, 160, and 140 ps. Buffer delay = 20 ps. Non-pipelined total delay = 750 ps. Find speedup for 1000 instructions.",
            "steps": [
                "Step 1: Non-pipelined time = 1000 × 750 ps = 750,000 ps.",
                "Step 2: Pipelined clock cycle T = max(150, 120, 180, 160, 140) + 20 = 180 + 20 = 200 ps.",
                "Step 3: Pipelined cycles = k + n - 1 = 5 + 1000 - 1 = 1004 cycles.",
                "Step 4: Pipelined time = 1004 × 200 ps = 200,800 ps.",
                "Step 5: Speedup S = 750,000 / 200,800 ≈ 3.735."
            ],
            "answer": "Speedup S = 3.74x."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Average CPI with Stalls",
            "warning": "CPI_avg = 1 + (Stalls per instruction). Average execution time per instruction = CPI_avg × T_clk."
        }
    ]
}

# =============================================================================
# PROGRAMMING AND DATA STRUCTURES (PDS)
# =============================================================================

# PDS Chapter 0: C Programming & Recursion
CHAPTERS_COA_PDS_ALGO[("PDS", 0)] = {
    "sub_id": "PDS",
    "chap_idx": 0,
    "title": "Programming in C & Recursion Tracing",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Russian Nesting Dolls (Recursion & Call Stack)",
            "text": "Opening nesting dolls: You open doll #3 to find doll #2, then doll #1 (Base Case). At doll #1, you stop opening and start assembling them back! Every recursive function call places a box on the Call Stack; hitting the base case starts popping boxes off in reverse order."
        },
        {
            "title": "Real-Life Example 2: House Address on a Sticky Note (Pointers)",
            "text": "Instead of carrying your whole house to your friend (Pass by Value: copying data), you write your house address on a tiny sticky note (Pointer: `int *p = &x`). Your friend reads the address and visits your house to repaint a wall (Dereferencing: `*p = 50`). Changes happen directly to the original variable!"
        },
        {
            "title": "Real-Life Example 3: The Persistent Locker (Static Variables)",
            "text": "Normally, local variables in a function are wiped clean when the function finishes. But a `static` variable is like a bolted metal locker: its value survives between function calls! The next time you call the function, it picks up right where it left off."
        }
    ],
    "foundations": [
        {
            "number": "13.1",
            "title": "Pointers & Array Equivalence in C",
            "content": (
                "• An array name `arr` is a pointer to its first element: `arr == &arr[0]`.<br/>"
                "• <b>Subscript Rule:</b> `arr[i] == *(arr + i) == *(i + arr) == i[arr]`. (In C, `3[arr]` is completely valid!).<br/>"
                "• `*p++` means: read `*p` first, then increment pointer `p`.<br/>"
                "• `(*p)++` means: increment the actual integer value that `p` points to."
            ),
            "crucial_rule": "GOLDEN RULE: When an array is passed to a function, it decays to a simple pointer! Inside the function, `sizeof(arr)` gives the size of a pointer (4 or 8 bytes), NOT the full array size."
        },
        {
            "number": "13.2",
            "title": "Short-Circuit Evaluation in Logic",
            "content": (
                "• In `(A && B)`: If A is False (0), B is NEVER EXECUTED!<br/>"
                "• In `(A || B)`: If A is True (1), B is NEVER EXECUTED!"
            ),
            "crucial_rule": "GOLDEN RULE: Watch out for increment operators inside logical conditions: `if (a == 0 && ++b > 0)`: since `a==0` might be false, `++b` never happens!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Tracing Static Recursion",
            "problem": "What is printed by:\nint f(int n) {\n  static int r = 0;\n  if (n <= 0) return 1;\n  if (n > 3) { r = n; return f(n - 2) + 2; }\n  return f(n - 1) + r;\n}\nint main() { printf(\"%d\", f(5)); }",
            "steps": [
                "Step 1: Call f(5): n=5 (>3) ⇒ static r becomes 5. Calls f(3) + 2.",
                "Step 2: Inside f(3): n=3 (not >3) ⇒ Calls f(2) + r.",
                "Step 3: Inside f(2): Calls f(1) + r.",
                "Step 4: Inside f(1): Calls f(0) + r.",
                "Step 5: Inside f(0): Hits base case, returns 1.",
                "Step 6: Unwind f(1): 1 + 5 = 6. Unwind f(2): 6 + 5 = 11. Unwind f(3): 11 + 5 = 16.",
                "Step 7: Unwind f(5): f(3) + 2 = 16 + 2 = 18."
            ],
            "answer": "Output = 18."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Undefined Behavior",
            "warning": "Expressions like `i = i++ + ++i` modify a variable multiple times without a sequence point. In C standard, this is UNDEFINED BEHAVIOR."
        }
    ]
}

# PDS Chapter 1: Linear Data Structures
CHAPTERS_COA_PDS_ALGO[("PDS", 1)] = {
    "sub_id": "PDS",
    "chap_idx": 1,
    "title": "Linear Data Structures - Stacks, Queues & Linked Lists",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Browser Back Button vs Printer Queue (Stack vs Queue)",
            "text": "• Stack (LIFO: Last-In First-Out): Like a stack of plates. The last web page you opened is the first one that pops back when you hit the 'Back' button.\n• Queue (FIFO: First-In First-Out): Like people standing in a ticket line. The first person to arrive is the first person served. Network printers use queues so the first document submitted prints first."
        },
        {
            "title": "Real-Life Example 2: Circular Buffet Counter (Circular Queue)",
            "text": "In a linear queue, when people leave the front, empty seats open up, but you can't seat new diners if the rear pointer hit the end of the line. A Circular Queue wraps the pointer back to index 0 using modulo arithmetic `(rear + 1) % Capacity`, keeping 100% of seats usable."
        },
        {
            "title": "Real-Life Example 3: The Scavenger Hunt Clue Slips (Linked Lists)",
            "text": "An array is like 10 adjacent hotel lockers: fast lookup by number, but impossible to expand if neighbor lockers are occupied. A Linked List is like a treasure hunt: each clue card holds an item and the GPS coordinate of where the next clue is hidden. Inserting someone in the middle takes O(1) time without moving anyone else!"
        }
    ],
    "foundations": [
        {
            "number": "14.1",
            "title": "Infix, Postfix & Stack Applications",
            "content": (
                "• <b>Infix:</b> `A + B` &nbsp;|&nbsp; <b>Postfix:</b> `A B +` (No parentheses needed!).<br/>"
                "• <b>Evaluating Postfix with Stack:</b> Read left to right. Push numbers. When an operator arrives, pop two numbers (op2 = pop(), op1 = pop()), calculate `op1 op op2`, and push result back."
            ),
            "crucial_rule": "GOLDEN RULE: In postfix evaluation, the FIRST popped element is operand 2 (the right-hand side operand)! Order matters for subtraction and division: op1 - op2."
        },
        {
            "number": "14.2",
            "title": "Queue Boundary Conditions",
            "content": (
                "• In a Circular Queue of size N (leaving 1 slot empty):<br/>"
                "&nbsp;&nbsp;• <b>Full condition:</b> `(rear + 1) % N == front`.<br/>"
                "&nbsp;&nbsp;• <b>Empty condition:</b> `front == rear`.<br/>"
                "• Max items stored = N - 1."
            ),
            "crucial_rule": "GOLDEN RULE: Minimum stacks needed to implement a Queue = 2. Minimum queues needed to implement a Stack = 2."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Evaluating Postfix Expression",
            "problem": "Evaluate the postfix expression: `8 2 3 * + 4 -` using a stack.",
            "steps": [
                "Step 1: Push 8, Push 2, Push 3. Stack = [8, 2, 3].",
                "Step 2: Encounter '*': op2 = 3, op1 = 2 ⇒ 2 × 3 = 6. Push 6. Stack = [8, 6].",
                "Step 3: Encounter '+': op2 = 6, op1 = 8 ⇒ 8 + 6 = 14. Push 14. Stack = [14].",
                "Step 4: Push 4. Stack = [14, 4].",
                "Step 5: Encounter '-': op2 = 4, op1 = 14 ⇒ 14 - 4 = 10. Push 10. Stack = [10]."
            ],
            "answer": "Final Result = 10."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Reversing a Linked List",
            "warning": "To reverse a singly linked list in-place, always save `curr->next` in a temporary pointer BEFORE setting `curr->next = prev`, otherwise you will lose the rest of the list!"
        }
    ]
}

# PDS Chapter 2: Trees & Heaps
CHAPTERS_COA_PDS_ALGO[("PDS", 2)] = {
    "sub_id": "PDS",
    "chap_idx": 2,
    "title": "Trees, BST & Binary Heaps",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: High-Low Number Guessing Game (Binary Search Tree)",
            "text": "If a friend picks a number between 1 and 100, you don't guess 1, 2, 3, 4 (Linear search: slow!). You guess 50. If they say 'Higher', you immediately eliminate numbers 1 to 50 in ONE step! A Binary Search Tree does this on every step: left child is smaller, right child is bigger, finding any item among 1,000,000 items in just 20 checks (log2(1,000,000) ≈ 20)."
        },
        {
            "title": "Real-Life Example 2: Hospital Emergency Room Triage (Priority Queue & Heap)",
            "text": "In a hospital ER, patients are not treated by who arrived first. A patient with a severe heart attack is rushed ahead of someone with a mild headache. A Max-Heap keeps the highest-priority patient sitting at the very top (the root). When they enter surgery, the heap re-adjusts in just O(log n) time."
        },
        {
            "title": "Real-Life Example 3: Balancing a Hanging Baby Mobile (AVL Tree Rotations)",
            "text": "If you hang too many toys on the right branch of a mobile, it tips over and crashes. An AVL tree measures the height difference between left and right branches (Balance Factor). If it tilts by more than 1 level, it does a quick rotational swing (LL, RR, LR, RL) to restore perfect balance in O(1) time."
        }
    ],
    "foundations": [
        {
            "number": "15.1",
            "title": "Binary Tree Properties & Traversal Invariants",
            "content": (
                "• In any full/strict binary tree: <b>Leaf nodes L = Internal nodes I + 1</b>.<br/>"
                "• <b>BST Inorder Invariant:</b> Inorder traversal (Left, Root, Right) of a BST is ALWAYS in <b>STRICTLY ASCENDING SORTED ORDER</b>!<br/>"
                "• <b>Reconstructing Trees:</b> You CANNOT uniquely build a tree without INORDER traversal! (Need Inorder + Preorder OR Inorder + Postorder)."
            ),
            "crucial_rule": "GOLDEN RULE: Given only Preorder and Postorder, you can build a unique tree ONLY if every non-leaf node has strictly 2 children."
        },
        {
            "number": "15.2",
            "title": "Binary Heap Properties",
            "content": (
                "A Binary Heap is a <b>Complete Binary Tree</b> stored in an array.<br/>"
                "• Parent of node i is at ⌊i/2⌋. Left child is at 2i, Right child is at 2i + 1.<br/>"
                "• <b>Build-Heap Time:</b> Takes <b>O(n) time</b> (NOT O(n log n)!).<br/>"
                "• Insert / Delete-Root takes O(log n) time."
            ),
            "crucial_rule": "GOLDEN RULE: In a Min-Heap with n elements, where is the MAXIMUM element? It is always in one of the LEAF nodes (between indices ⌊n/2⌋ + 1 and n)!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Finding Postorder from BST Preorder",
            "problem": "Given Preorder traversal of a BST: [40, 20, 10, 30, 60, 50, 70]. What is its Postorder traversal?",
            "steps": [
                "Step 1: For a BST, Inorder is simply the sorted keys: Inorder = [10, 20, 30, 40, 50, 60, 70].",
                "Step 2: Preorder first element is Root = 40.",
                "Step 3: Keys before 40 in Inorder form Left Subtree: [10, 20, 30]. Keys after 40 form Right Subtree: [50, 60, 70].",
                "Step 4: Left subtree root is 20 (left child 10, right child 30). Postorder = [10, 30, 20].",
                "Step 5: Right subtree root is 60 (left child 50, right child 70). Postorder = [50, 70, 60].",
                "Step 6: Combine: [10, 30, 20, 50, 70, 60, 40]."
            ],
            "answer": "Postorder Traversal = [10, 30, 20, 50, 70, 60, 40]."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Number of Structurally Distinct Binary Trees",
            "warning": "Number of structurally distinct binary trees with n unlabeled nodes is the Catalan Number: C_n = (1 / (n + 1)) × C(2n, n). For n=3, C_3 = 5 trees."
        }
    ]
}

# =============================================================================
# ALGORITHMS (ALGO)
# =============================================================================

# ALGO Chapter 0: Asymptotics & Recurrences
CHAPTERS_COA_PDS_ALGO[("ALGO", 0)] = {
    "sub_id": "ALGO",
    "chap_idx": 0,
    "title": "Asymptotic Analysis & Recurrence Relations",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Carrier Pigeon vs Slow Internet (Big-O Growth)",
            "text": "If you need to send 10 Terabytes of video across the city: sending it over slow 10 MB/s internet takes 12 days (O(n): time scales with data size!). But if you strap an SSD to a carrier pigeon, the pigeon flies across the city in 30 minutes whether the drive has 1 Megabyte or 10 Terabytes (O(1): constant time!). As data grows toward infinity, O(1) always beats O(n)."
        },
        {
            "title": "Real-Life Example 2: The CEO Task Delegation (Master Theorem)",
            "text": "A CEO splits a big project into 'a' smaller sub-tasks of size 'n/b'. Upper management does f(n) work to organize them, while the worker army at the leaves does n^(log_b a) work. The Master Theorem simply compares: Who does more work? If the worker army dominates, time is Θ(n^(log_b a)). If both do equal work, add a log n factor!"
        },
        {
            "title": "Real-Life Example 3: The King's Chessboard Wheat Grains (Exponential Explosion)",
            "text": "The inventor of chess asked the King for 1 grain of wheat on square 1, 2 grains on square 2, 4 on square 3, doubling every square: 2^n. By square 64, the wheat required was more than the entire planet's harvest for 2,000 years! Exponential O(2^n) algorithms become impossibly slow for even moderate inputs."
        }
    ],
    "foundations": [
        {
            "number": "16.1",
            "title": "Asymptotic Notations: O, Ω, Θ",
            "content": (
                "• <b>Big-O (O):</b> Upper Bound (Worst-case ceiling: 'runs at most this slow').<br/>"
                "• <b>Big-Omega (Ω):</b> Lower Bound (Best-case floor: 'runs at least this fast').<br/>"
                "• <b>Big-Theta (Θ):</b> Tight Bound (Both upper and lower bound match!).<br/>"
                "• <b>Growth speed ranking:</b><br/>"
                "&nbsp;&nbsp;1 < log n < √n < n < n log n < n² < n³ < 2^n < n! < n^n."
            ),
            "crucial_rule": "GOLDEN RULE: log(n!) = Θ(n log n) by Stirling's formula. Never write Θ(n^n) for log(n!)!"
        },
        {
            "number": "16.2",
            "title": "Master Theorem in 3 Easy Steps",
            "content": (
                "For recurrence: <b>T(n) = a T(n/b) + f(n)</b>:<br/>"
                "1. Calculate critical value: <b>p = log_b(a)</b>.<br/>"
                "2. Compare n^p with f(n):<br/>"
                "&nbsp;&nbsp;• If n^p > f(n) ⇒ <b>T(n) = Θ(n^p)</b>.<br/>"
                "&nbsp;&nbsp;• If n^p == f(n) ⇒ <b>T(n) = Θ(n^p · log n)</b>.<br/>"
                "&nbsp;&nbsp;• If n^p < f(n) ⇒ <b>T(n) = Θ(f(n))</b>."
            ),
            "crucial_rule": "GOLDEN RULE: Master theorem cannot be used if b is not a constant (e.g. T(n) = 2T(√n) + 1) or if a is not a constant!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Solving Recurrence with Master Theorem",
            "problem": "Solve: T(n) = 4 T(n/2) + n².",
            "steps": [
                "Step 1: Identify: a = 4, b = 2, f(n) = n².",
                "Step 2: Compute critical exponent p = log_b(a) = log_2(4) = 2.",
                "Step 3: So n^p = n^2.",
                "Step 4: Compare: n^p is exactly equal to f(n) = n² (Case 2!).",
                "Step 5: Multiply by log n: T(n) = Θ(n² log n)."
            ],
            "answer": "T(n) = Θ(n² log n)."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Non-Polynomial Gap in Master Theorem",
            "warning": "For T(n) = 2T(n/2) + n / log n, n^p = n. Here f(n) = n / log n is smaller than n^p, but NOT polynomially smaller (the difference is a log factor, not n^ε). Master theorem fails here!"
        }
    ]
}

# ALGO Chapter 1: Sorting, Searching & Hashing
CHAPTERS_COA_PDS_ALGO[("ALGO", 1)] = {
    "sub_id": "ALGO",
    "chap_idx": 1,
    "title": "Sorting, Searching & Hashing",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Sorting Exam Papers by PIN Code (Radix Sort)",
            "text": "A teacher sorting 10,000 student answer sheets doesn't compare paper A with paper B one by one (QuickSort). They put papers into 10 plastic trays based on the last digit (0 to 9), collect them, and repeat for the tens and hundreds digits. In just a few passes, all 10,000 papers are sorted in linear O(n) time!"
        },
        {
            "title": "Real-Life Example 2: The Unlucky Card Shuffle (QuickSort Worst Case)",
            "text": "QuickSort picks a 'pivot' and puts smaller cards on left, bigger cards on right. If the cards are ALREADY sorted and you foolishly pick the first card as pivot, the left partition has 0 cards and the right has n-1 cards. Instead of halving, the depth becomes n, degrading to slow O(n²) time. Picking a random pivot solves this."
        },
        {
            "title": "Real-Life Example 3: Finding Your Car in a Crowded Parking Lot (Hash Collisions)",
            "text": "A Hash function assigns your car a parking spot based on license plate mod 100. If someone else already parked in your spot (Collision), Linear Probing tells you to park in the next open spot. But if lots of cars crowd into neighboring spots, you get Primary Clustering jams."
        }
    ],
    "foundations": [
        {
            "number": "17.1",
            "title": "Comparison Sorting Lower Bound & Stability",
            "content": (
                "• <b>Theoretical Limit:</b> Any comparison-based sort must take at least <b>Ω(n log n)</b> comparisons in worst case.<br/>"
                "• <b>Stable Sorts (Preserves order of equal items):</b> Merge Sort, Insertion Sort, Bubble Sort.<br/>"
                "• <b>Unstable Sorts:</b> QuickSort, HeapSort, Selection Sort.<br/>"
                "• <b>In-Place Sorts (O(1) extra space):</b> HeapSort, QuickSort, Insertion Sort. (MergeSort requires O(n) extra memory!)."
            ),
            "crucial_rule": "GOLDEN RULE: HeapSort is guaranteed O(n log n) in ALL cases (best, average, worst) and uses O(1) space, but it is NOT stable!"
        },
        {
            "number": "17.2",
            "title": "Hashing & Collision Techniques",
            "content": (
                "• <b>Load Factor α:</b> α = n / m (n items / m slots).<br/>"
                "• <b>Separate Chaining:</b> Uses linked lists at each slot. Can have α > 1. Search time: Θ(1 + α).<br/>"
                "• <b>Open Addressing:</b> Must have α ≤ 1.<br/>"
                "&nbsp;&nbsp;• Linear Probing: `(h(k) + i) mod m` (Causes Primary Clustering).<br/>"
                "&nbsp;&nbsp;• Quadratic Probing: `(h(k) + c1·i + c2·i²) mod m` (Causes Secondary Clustering).<br/>"
                "&nbsp;&nbsp;• Double Hashing: `(h1(k) + i · h2(k)) mod m` (Best open addressing!)."
            ),
            "crucial_rule": "GOLDEN RULE: In Double Hashing, h2(k) must be relatively prime to hash table size m so it can probe every single slot."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Linear Probing",
            "problem": "Insert keys [23, 34, 45, 12] into hash table of size 11 using h(k) = k mod 11 and Linear Probing. Which slot does 12 go into?",
            "steps": [
                "Step 1: 23 mod 11 = 1 ⇒ Slot 1 (free).",
                "Step 2: 34 mod 11 = 1 ⇒ Collision at 1! Try slot 2 ⇒ Slot 2 (free).",
                "Step 3: 45 mod 11 = 1 ⇒ Collision at 1! Slot 2 is also full! Try slot 3 ⇒ Slot 3 (free).",
                "Step 4: 12 mod 11 = 1 ⇒ Collision at 1! Slots 2 and 3 are full! Try slot 4 ⇒ Slot 4 (free)."
            ],
            "answer": "Key 12 is placed into Slot 4."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: QuickSort Average vs Worst Case",
            "warning": "Average time of QuickSort is Θ(n log n). Worst case time is Θ(n²). Read the question carefully to see whether it asks for average or worst-case!"
        }
    ]
}

# ALGO Chapter 2: Greedy & Dynamic Programming
CHAPTERS_COA_PDS_ALGO[("ALGO", 2)] = {
    "sub_id": "ALGO",
    "chap_idx": 2,
    "title": "Design Techniques - Greedy & Dynamic Programming",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The ATM Cash Machine (Greedy Choice)",
            "text": "When you withdraw ₹3,800 from an ATM, it dispenses the biggest notes first: ₹2000 (1 note), ₹500 (3 notes), ₹200 (1 note), ₹100 (1 note). Making the locally best choice at each step is the Greedy method. For standard banknotes, this guarantees the fewest total notes. But if notes were ₹1, ₹7, ₹10 and you needed ₹14: Greedy picks ₹10 + four ₹1s (5 notes), while Dynamic Programming finds ₹7 + ₹7 (just 2 notes!)."
        },
        {
            "title": "Real-Life Example 2: The Math Homework Scratchpad (Dynamic Programming)",
            "text": "Calculating Fibonacci(50) by hand branches into an impossible tree of billions of steps. But a smart student keeps a scratchpad: once Fib(3) is calculated, write down '2'. Anytime you need Fib(3) again, just look up your scratchpad in 1 second! Dynamic Programming turns an impossible exponential O(2^n) explosion into a fast linear O(n) table lookup."
        },
        {
            "title": "Real-Life Example 3: Packing Your Flight Carry-On Bag (0/1 Knapsack)",
            "text": "Airline carry-on limit is 15 kg. You have heavy items: laptop, DSLR camera, shoes. You cannot pack half a laptop—you either take the whole laptop or leave it (0 or 1 choice). Fractional items like gold dust can be solved greedily; solid 0/1 items require Dynamic Programming."
        }
    ],
    "foundations": [
        {
            "number": "18.1",
            "title": "Greedy Algorithms: Knapsack, Activity Selection & Huffman Coding",
            "content": (
                "• <b>Fractional Knapsack:</b> Sort by Value/Weight ratio. Greedy is optimal. Time: O(n log n).<br/>"
                "• <b>Activity Selection:</b> Sort by <b>EARLIEST FINISH TIME</b>. Pick next compatible task.<br/>"
                "• <b>Huffman Coding:</b> Combines two least frequent characters using a Min-Heap. Generates variable-length optimal prefix codes. Time: O(n log n)."
            ),
            "crucial_rule": "GOLDEN RULE: A Huffman tree for n characters is ALWAYS a FULL binary tree with exactly 2n - 1 total nodes (n leaves and n - 1 internal nodes)!"
        },
        {
            "number": "18.2",
            "title": "Dynamic Programming: 0/1 Knapsack & Matrix Chain",
            "content": (
                "• <b>0/1 Knapsack:</b> Table DP[i][w] = max(DP[i-1][w], val[i] + DP[i-1][w - wt[i]]). Time: O(n × W) (Pseudo-polynomial).<br/>"
                "• <b>Matrix Chain Multiplication:</b> Computes optimal order to multiply matrices to minimize scalar multiplications. Time: O(n³)."
            ),
            "crucial_rule": "GOLDEN RULE: 0/1 Knapsack is NP-Complete! Its DP solution runs in pseudo-polynomial time because W is measured in binary bits."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Multiplying 3 Matrices",
            "problem": "Find minimum scalar multiplications to multiply A1(10 × 30), A2(30 × 5), and A3(5 × 60).",
            "steps": [
                "Step 1: Two possible parenthesizations: (A1 × A2) × A3 OR A1 × (A2 × A3).",
                "Step 2: Option 1: ((A1 × A2) × A3):<br/>"
                "&nbsp;&nbsp;A1 × A2 takes 10 × 30 × 5 = 1,500 operations (result size 10×5).<br/>"
                "&nbsp;&nbsp;Result × A3 takes 10 × 5 × 60 = 3,000 operations.<br/>"
                "&nbsp;&nbsp;Total Option 1 = 1,500 + 3,000 = 4,500 multiplications.",
                "Step 3: Option 2: (A1 × (A2 × A3)):<br/>"
                "&nbsp;&nbsp;A2 × A3 takes 30 × 5 × 60 = 9,000 operations (result size 30×60).<br/>"
                "&nbsp;&nbsp;A1 × Result takes 10 × 30 × 60 = 18,000 operations.<br/>"
                "&nbsp;&nbsp;Total Option 2 = 9,000 + 18,000 = 27,000 multiplications.",
                "Step 4: Minimum = min(4500, 27000) = 4,500."
            ],
            "answer": "Minimum scalar multiplications = 4,500 with grouping ((A1 A2) A3)."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Longest Common Subsequence Length",
            "warning": "If characters match: LCS = 1 + DP[i-1][j-1]. If they don't match: LCS = max(DP[i-1][j], DP[i][j-1]). Never add 1 when characters differ!"
        }
    ]
}

# ALGO Chapter 3: Graph Algorithms
CHAPTERS_COA_PDS_ALGO[("ALGO", 3)] = {
    "sub_id": "ALGO",
    "chap_idx": 3,
    "title": "Graph Algorithms - Traversals, MST & Shortest Paths",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Connecting Fiber Optic Cable Between Cities (MST)",
            "text": "A telecom company wants to connect 10 cities with fiber optic cable so everyone can communicate. Laying cable is expensive. Kruskal's algorithm sorts all possible cable routes from cheapest to most expensive, laying down the cheapest cable first, as long as it doesn't form a useless closed loop. It guarantees the absolute cheapest total network cost."
        },
        {
            "title": "Real-Life Example 2: Google Maps Shortest Driving Route (Dijkstra's Algorithm)",
            "text": "When you want the fastest route home, Google Maps starts at your current location (distance 0) and ripples outward like water drops, visiting the nearest reachable intersection next. Because road travel times are never negative, once Dijkstra locks in an intersection, it has permanently found the best route."
        },
        {
            "title": "Real-Life Example 3: Currency Exchange Arbitrage (Bellman-Ford & Negative Cycles)",
            "text": "Converting 1 USD to Euros, then to Yen, then back to 1.05 USD creates free money! In math, taking the negative logarithm of exchange rates turns this into a Negative Weight Cycle. Dijkstra fails completely when edges are negative. Bellman-Ford runs for V - 1 rounds: if distances keep dropping on round V, a negative cycle is detected!"
        }
    ],
    "foundations": [
        {
            "number": "19.1",
            "title": "BFS vs DFS Traversals",
            "content": (
                "• <b>BFS (Breadth-First):</b> Uses a <b>Queue</b>. Explores neighbors level by level. Finds shortest path in <b>unweighted graphs</b>. Time: O(V + E).<br/>"
                "• <b>DFS (Depth-First):</b> Uses a <b>Stack</b> (or recursion). Explores deep down each path. Detects cycles in directed graph via <b>Back Edges</b>. Time: O(V + E).<br/>"
                "• <b>Topological Sort:</b> Linear ordering of vertices in a Directed Acyclic Graph (DAG)."
            ),
            "crucial_rule": "GOLDEN RULE: Topological sort is possible IF AND ONLY IF the graph has NO cycles (it must be a DAG)!"
        },
        {
            "number": "19.2",
            "title": "Minimum Spanning Tree (MST): Kruskal vs Prim",
            "content": (
                "• <b>Kruskal's Algorithm:</b> Sorts all edges by weight, adds edge if no cycle (uses Disjoint Set Union). Time: <b>O(E log V)</b>.<br/>"
                "• <b>Prim's Algorithm:</b> Starts from 1 vertex and grows the tree by picking lightest connected edge (uses Min-Heap). Time: <b>O(E log V)</b>."
            ),
            "crucial_rule": "GOLDEN RULE: If all edge weights in a connected graph are strictly UNIQUE, the Minimum Spanning Tree is 100% UNIQUE!"
        },
        {
            "number": "19.3",
            "title": "Shortest Path Algorithm Matrix",
            "content": (
                "• <b>Dijkstra:</b> Single Source. Works ONLY with <b>NON-NEGATIVE edge weights</b>. Greedy. Time: O((V + E) log V).<br/>"
                "• <b>Bellman-Ford:</b> Single Source. Handles <b>NEGATIVE edge weights</b> and detects negative cycles. Time: <b>O(V × E)</b>.<br/>"
                "• <b>Floyd-Warshall:</b> All-Pairs Shortest Path. Dynamic Programming. Time: <b>O(V³)</b>."
            ),
            "crucial_rule": "GOLDEN RULE: Dijkstra CANNOT work with negative edge weights, even if there are no negative cycles!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Dijkstra Algorithm Trace",
            "problem": "Graph edges: A→B(4), A→C(2), C→B(1), B→D(5), C→D(8). Find shortest distance from source A to all vertices.",
            "steps": [
                "Step 1: Start at A: dist[A]=0, others=∞. Visited={}.",
                "Step 2: Pick A(0): update dist[B]=4, dist[C]=2. Visited={A}.",
                "Step 3: Pick smallest unvisited: C(2). Outgoing: C→B(1) ⇒ dist[B] = min(4, 2+1) = 3 (updated!). C→D(8) ⇒ dist[D] = min(∞, 2+8) = 10. Visited={A, C}.",
                "Step 4: Pick smallest unvisited: B(3). Outgoing: B→D(5) ⇒ dist[D] = min(10, 3+5) = 8 (updated!). Visited={A, C, B}.",
                "Step 5: Pick D(8). All visited."
            ],
            "answer": "Shortest distances from A: A=0, B=3, C=2, D=8."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Adding a Constant to Fix Negative Weights",
            "warning": "You CANNOT make negative edges positive for Dijkstra by adding a constant +10 to all edges! Paths with 5 edges get penalized more than paths with 2 edges, completely changing the shortest path!"
        }
    ]
}
