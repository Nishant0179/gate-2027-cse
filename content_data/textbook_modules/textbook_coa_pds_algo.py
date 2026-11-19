# textbook_coa_pds_algo.py
# Simple English, point-by-point study notes for COA, PDS, and Algorithms.
# Written in crystal-clear, student-friendly language for GATE 2027 CSE aspirants.

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
            "title": "Real-Life Example 1: The Scavenger Hunt Clues (Addressing Modes Made Simple)",
            "text": (
                "Imagine you are playing a scavenger hunt game to find cash prize money:\n"
                "• Immediate Mode: The clue paper has the cash ₹500 taped directly onto it! You get the money instantly without going anywhere.\n"
                "• Direct Mode: The paper gives you an address: 'Go to House #42'. You walk there and pick up the money from the house.\n"
                "• Indirect Mode: The paper says: 'Open locker 10; inside locker 10 is a key and another note with the final address'. You make two trips.\n"
                "• Register Mode: The money is already sitting inside your own pocket (CPU register). Zero walking required!\n"
                "• PC-Relative Mode: The paper says: 'From where you are standing right now, take 5 steps forward'. This is how loops and jumps work in software."
            )
        },
        {
            "title": "Real-Life Example 2: Little-Endian vs Big-Endian (How Bytes are Stored)",
            "text": (
                "When writing a mailing address, which order do you use?\n"
                "• Big-Endian: You write the biggest part first (Country, then State, then City, then House number). The Most Significant Byte (MSB) gets stored at the lowest memory address.\n"
                "• Little-Endian: You write the smallest part first (House number first, then City, State, and Country last). The Least Significant Byte (LSB) gets stored at the lowest memory address.\n"
                "• Everyday fact: Intel x86 processors use Little-Endian. Internet network packets use Big-Endian."
            )
        },
        {
            "title": "Real-Life Example 3: Expanding Menu Combos (Expanding Opcode Technique)",
            "text": (
                "In a burger shop, you have a 4-bit order slip that can represent 16 total combo meals. But what if you need some large meals (that take 3 extra side-dishes) and some small meals (that only need 2 side-dishes)?\n"
                "By keeping 14 codes for large meals and reserving the remaining 2 unused codes as 'escape signals', you can expand the order slip to unlock dozens of smaller meal options. This is called Expanding Opcode."
            )
        }
    ],
    "foundations": [
        {
            "number": "9.1",
            "title": "Effective Address (EA) in Common Addressing Modes",
            "content": (
                "<b>What is Effective Address (EA)?</b><br/>"
                "It is the exact physical RAM location where your data (operand) lives.<br/><br/>"
                "Here is how each addressing mode finds the data, explained point by point:<br/>"
                "• <b>Immediate Addressing:</b><br/>"
                "&nbsp;&nbsp;- The data is written directly inside the instruction itself (e.g. <code>ADD R1, #5</code>).<br/>"
                "&nbsp;&nbsp;- EA = None (No RAM lookup needed). Number of memory accesses to fetch data = 0.<br/>"
                "• <b>Direct Addressing:</b><br/>"
                "&nbsp;&nbsp;- The instruction directly gives the RAM address (e.g. <code>LOAD R1, [1000]</code>).<br/>"
                "&nbsp;&nbsp;- EA = Address field. Memory accesses = 1 (to read data from address 1000).<br/>"
                "• <b>Indirect Addressing:</b><br/>"
                "&nbsp;&nbsp;- The instruction points to an address, which holds ANOTHER address where data is stored.<br/>"
                "&nbsp;&nbsp;- EA = Content of Memory[Address]. Memory accesses = 2 (first to read the pointer, second to read the data).<br/>"
                "• <b>Register Addressing:</b><br/>"
                "&nbsp;&nbsp;- The data is stored inside a fast CPU register (e.g. <code>ADD R1, R2</code>).<br/>"
                "&nbsp;&nbsp;- EA = None. Memory accesses = 0 (blazing fast!).<br/>"
                "• <b>Register Indirect Addressing:</b><br/>"
                "&nbsp;&nbsp;- A register holds the RAM memory address of the data (like a C pointer).<br/>"
                "&nbsp;&nbsp;- EA = Content of Register. Memory accesses = 1.<br/>"
                "• <b>PC-Relative Addressing:</b><br/>"
                "&nbsp;&nbsp;- Used for jump and branch instructions (<code>if/else</code>, <code>loops</code>).<br/>"
                "&nbsp;&nbsp;- EA = Next Instruction PC + Offset."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: In PC-Relative mode, the Program Counter (PC) has ALREADY moved to the next instruction before the offset is added! Formula: Target Address = Next_PC + Offset."
        },
        {
            "number": "9.2",
            "title": "Hardwired vs Microprogrammed Control Unit",
            "content": (
                "<b>What does a Control Unit do?</b><br/>"
                "It acts like the conductor of an orchestra, generating electronic signals that tell the ALU, registers, and memory when to read, write, or calculate.<br/><br/>"
                "Two ways to build it:<br/>"
                "• <b>Hardwired Control Unit:</b><br/>"
                "&nbsp;&nbsp;- Built using physical logic gates (AND, OR, flip-flops).<br/>"
                "&nbsp;&nbsp;- Speed: Extremely fast (used in RISC processors).<br/>"
                "&nbsp;&nbsp;- Flexibility: Zero flexibility. If you find a bug, you cannot change the hardware after manufacturing.<br/>"
                "• <b>Microprogrammed Control Unit:</b><br/>"
                "&nbsp;&nbsp;- Control signals are written as tiny binary micro-instructions stored in a special ROM called Control Memory.<br/>"
                "&nbsp;&nbsp;- Speed: Slower (because it must fetch micro-instructions from ROM).<br/>"
                "&nbsp;&nbsp;- Flexibility: Very flexible and easy to update via firmware (used in CISC processors).<br/>"
                "• <b>Horizontal vs Vertical Microprogramming:</b><br/>"
                "&nbsp;&nbsp;- Horizontal: 1 bit per control signal. No decoder needed. Micro-instructions are very wide, but super fast.<br/>"
                "&nbsp;&nbsp;- Vertical: Signals are encoded in groups and decoded using decoders (e.g. 3 bits decoded to 8 signals). Words are narrower, saving memory."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: If a control unit has 32 independent control signals: Horizontal microprogramming needs 32 bits. Vertical microprogramming with 4 groups of 8 mutually exclusive signals needs only 4 × log2(8) = 12 bits!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Expanding Opcode",
            "problem": "A 16-bit computer uses 4-bit register addresses. It supports 3-register instructions and 2-register instructions. If there are 14 different 3-register instructions, how many 2-register instructions can be supported?",
            "steps": [
                "Step 1: Check total instruction length = 16 bits.",
                "Step 2: A 3-register instruction needs: Opcode + Reg1(4 bits) + Reg2(4 bits) + Reg3(4 bits) = Opcode + 12 bits.",
                "Step 3: Bits available for Opcode = 16 - 12 = 4 bits. Total possible opcode combinations = 2^4 = 16.",
                "Step 4: The system uses 14 combinations for 3-register instructions. Unused opcode patterns = 16 - 14 = 2 patterns.",
                "Step 5: For a 2-register instruction, only 2 × 4 = 8 bits are used for registers. The opcode can expand by 4 extra bits!",
                "Step 6: Total 2-register instructions possible = (Unused patterns) × 2^(extra bits) = 2 × 2^4 = 2 × 16 = 32."
            ],
            "answer": "Maximum 2-register instructions supported = 32."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Byte-Addressable vs Word-Addressable Memory",
            "warning": "Always read the question carefully: Is the memory Byte-addressable (1 byte per address) or Word-addressable (e.g. 4 bytes per address)? For a 64 MB memory: If byte-addressed, you need 26 bits (since 64 MB = 2^26 B). If 4-byte-word addressed, you need only 24 bits (since 64 MB / 4 B = 16 M words = 2^24 words)!"
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
            "text": (
                "If someone asks you to multiply 27 × 99, do you perform 99 separate additions? Of course not!\n"
                "You simply do 27 × (100 - 1) = 2700 - 27 = 2673. That took just one subtraction and one shift!\n"
                "Booth's Algorithm does the exact same trick in binary: when it sees a long string of 1s (like 0111110), it does 1 subtraction at the beginning and 1 addition at the end, skipping all the steps in between."
            )
        },
        {
            "title": "Real-Life Example 2: The VIP Express Highway (Direct Memory Access - DMA)",
            "text": (
                "Imagine downloading a 4K movie from your SSD into RAM. If the CPU had to move every single byte by hand, your entire computer would freeze.\n"
                "Instead, a DMA Controller acts like an express highway: it takes control of the memory bus and streams data straight into RAM while the CPU keeps running your games without waiting."
            )
        },
        {
            "title": "Real-Life Example 3: Phone Notification vs Continuous Screen Checking (Interrupts vs Polling)",
            "text": (
                "• Polling (Programmed I/O): Checking your phone screen every 5 seconds to see if a WhatsApp message arrived. Wastes huge battery and CPU time!\n"
                "• Interrupt-Driven I/O: You keep working on your laptop. When a message arrives, your phone chimes (sends an interrupt signal), you quickly read it, and return to work."
            )
        }
    ],
    "foundations": [
        {
            "number": "10.1",
            "title": "Booth's Multiplication Rules (Q_i, Q_{i-1})",
            "content": (
                "<b>How Booth's Algorithm works:</b><br/>"
                "• It multiplies signed numbers in 2's complement without extra sign conversion.<br/>"
                "• You scan multiplier bits from right to left, starting with an extra helper bit Q_{-1} = 0.<br/><br/>"
                "<b>The 4 Simple Action Rules:</b><br/>"
                "• <b>Case (0, 0):</b> String of zeros. Action: Only Arithmetic Right Shift (ARS).<br/>"
                "• <b>Case (0, 1):</b> End of a string of 1s. Action: Add Multiplicand (A = A + M), then ARS.<br/>"
                "• <b>Case (1, 0):</b> Beginning of a string of 1s. Action: Subtract Multiplicand (A = A - M), then ARS.<br/>"
                "• <b>Case (1, 1):</b> Inside a string of 1s. Action: Only Arithmetic Right Shift (ARS)."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: In Booth's algorithm, the shift is strictly an ARITHMETIC Right Shift (ARS). The sign bit (MSB) is copied into itself so the sign of positive and negative numbers is always preserved!"
        },
        {
            "number": "10.2",
            "title": "DMA Cycle Stealing Percentage",
            "content": (
                "<b>What is Cycle Stealing?</b><br/>"
                "The DMA controller transfers one data word, pauses, gives the bus back to the CPU, and repeats.<br/><br/>"
                "<b>Formulas to remember:</b><br/>"
                "• Time taken by DMA to transfer 1 word = (1 Word Size) / (Device Transfer Rate).<br/>"
                "• Fraction of CPU time stolen = (Time bus is busy with DMA) / (Total Time).<br/>"
                "• <b>Direct Shortcut:</b> CPU Time Stolen (%) = (Device Transfer Rate / Memory Bus Bandwidth) × 100%."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: Percentage of CPU time available for useful processing = 100% - (Percentage stolen by DMA)!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: DMA Bus Overhead",
            "problem": "A hard disk transfers data at 2 MB/sec. The memory bus has cycle time 200 ns and transfers 1 byte per cycle. In cycle-stealing mode, what percentage of CPU time is stolen by DMA?",
            "steps": [
                "Step 1: Find Memory Bus Bandwidth = 1 Byte / (200 × 10^-9 sec) = 5,000,000 Bytes/sec = 5 MB/sec.",
                "Step 2: Hard disk transfer rate = 2 MB/sec.",
                "Step 3: Calculate the ratio of bus usage = (Device Rate) / (Bus Bandwidth) = 2 MB/s / 5 MB/s = 0.40.",
                "Step 4: Multiply by 100% to find percentage = 40%."
            ],
            "answer": "CPU time consumed by DMA = 40% (CPU gets remaining 60% of time)."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Vectored vs Non-Vectored Interrupts",
            "warning": "Vectored interrupt: The interrupting device supplies the handler address directly on the data bus. Non-vectored interrupt: The CPU jumps to a fixed, hardwired memory address in the interrupt vector table."
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
            "title": "Real-Life Example 1: The Kitchen Spice Rack (Why Cache Works)",
            "text": (
                "When cooking, a chef keeps salt, pepper, and oil on a tiny shelf right above the stove (L1 Cache: 1-second access).\n"
                "They don't walk down to the basement grocery store (Main Memory: 2-minute walk) every time they need a pinch of salt!\n"
                "Because you reuse the same ingredients (Temporal Locality) and nearby ingredients (Spatial Locality), 95% of cooking needs are met straight from the spice shelf."
            )
        },
        {
            "title": "Real-Life Example 2: Assigned Parking Spots (Direct Mapped Cache)",
            "text": (
                "In an apartment parking lot, car owner #14 is strictly assigned to Spot #4 (14 mod 10 = 4).\n"
                "It is super fast to check if their car is home: you only check Spot #4! But if resident #24 arrives, they both fight for Spot #4 even if spots 5, 6, 7 are completely empty. This is Conflict Miss."
            )
        },
        {
            "title": "Real-Life Example 3: Free-For-All Parking (Fully Associative Cache)",
            "text": (
                "Any car can park in any empty spot. Zero conflict misses! But when you search for your car, you must scan all 100 spots at the exact same time using expensive comparator hardware."
            )
        }
    ],
    "foundations": [
        {
            "number": "11.1",
            "title": "Breaking Down a Memory Address in Cache Mapping",
            "content": (
                "Every memory address is split into 3 fields depending on cache mapping:<br/><br/>"
                "• <b>1. Direct Mapped Cache:</b><br/>"
                "&nbsp;&nbsp;- [ Tag Bits | Line/Block Bits | Word Offset Bits ]<br/>"
                "&nbsp;&nbsp;- Word Offset = log2(Block Size in bytes).<br/>"
                "&nbsp;&nbsp;- Line Bits = log2(Number of Cache Lines).<br/>"
                "&nbsp;&nbsp;- Tag Bits = Total Address Bits - (Line Bits + Word Offset).<br/><br/>"
                "• <b>2. k-Way Set Associative Cache:</b><br/>"
                "&nbsp;&nbsp;- [ Tag Bits | Set Bits | Word Offset Bits ]<br/>"
                "&nbsp;&nbsp;- Number of Sets = (Total Cache Lines) / k.<br/>"
                "&nbsp;&nbsp;- Set Bits = log2(Number of Sets).<br/>"
                "&nbsp;&nbsp;- Tag Bits = Total Address Bits - (Set Bits + Word Offset).<br/><br/>"
                "• <b>3. Fully Associative Cache:</b><br/>"
                "&nbsp;&nbsp;- [ Tag Bits | Word Offset Bits ]<br/>"
                "&nbsp;&nbsp;- There is no set or line index. Tag Bits = Total Address Bits - Word Offset."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: Total Cache Size = (Number of Lines) × (Block Size). Tag Directory Size = (Number of Lines) × (Tag Bits + Valid Bit + Dirty Bit)."
        },
        {
            "number": "11.2",
            "title": "Average Memory Access Time (AMAT)",
            "content": (
                "<b>Formula for AMAT:</b><br/>"
                "• <b>Hierarchical Cache (CPU checks L1 first; on miss, visits L2/Main Memory):</b><br/>"
                "&nbsp;&nbsp;AMAT = Hit_Time_L1 + (Miss_Rate_L1 × Miss_Penalty_L1).<br/><br/>"
                "• <b>Simultaneous Access (CPU searches L1 and Main Memory simultaneously):</b><br/>"
                "&nbsp;&nbsp;AMAT = (Hit_Rate × Hit_Time) + ((1 - Hit_Rate) × Main_Memory_Access_Time)."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: Unless the question explicitly specifies 'simultaneous access', ALWAYS use the Hierarchical formula where Miss Penalty includes the access to the next lower level!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Cache Tag Size Calculation",
            "problem": "A 32-bit byte-addressable system has a 64 KB 4-way set associative cache with 32-byte blocks. Find the number of Tag bits.",
            "steps": [
                "Step 1: Find Word Offset: Block size = 32 Bytes = 2^5 B ⇒ Offset = 5 bits.",
                "Step 2: Find Total Cache Lines: Total Cache Size / Block Size = 64 KB / 32 B = 65536 / 32 = 2048 lines.",
                "Step 3: Find Number of Sets: 2048 lines / 4 lines per set = 512 sets = 2^9 sets ⇒ Set bits = 9 bits.",
                "Step 4: Calculate Tag bits: Total Address (32 bits) - Set bits (9) - Offset bits (5) = 32 - 14 = 18 bits."
            ],
            "answer": "Tag field size = 18 bits."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Write-Through vs Write-Back Cache",
            "warning": "Write-Through updates both cache and RAM immediately (needs a Write Buffer). Write-Back updates only the cache block and sets a 'Dirty Bit'; RAM is updated only when that block is evicted!"
        }
    ]
}

# COA Chapter 3: Pipelining & Hazards
CHAPTERS_COA_PDS_ALGO[("COA", 3)] = {
    "sub_id": "COA",
    "chap_idx": 3,
    "title": "Pipeline Hazards, Speedup & Instruction Level Parallelism",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The Laundromat Pipeline (Instruction Pipelining)",
            "text": (
                "Doing 4 loads of laundry: Washer (30 mins), Dryer (40 mins), Folding (20 mins).\n"
                "• Non-pipelined: Wait until load 1 is completely washed, dried, and folded before starting load 2. Total time = 4 × 90 mins = 360 mins.\n"
                "• Pipelined: As soon as load 1 moves to the dryer, put load 2 into the washer! Each stage stays busy continuously. Total time shrinks dramatically to ~180 mins."
            )
        },
        {
            "title": "Real-Life Example 2: Waiting for the Oven (Data Hazard: RAW)",
            "text": (
                "You want to frost a cake (Instruction 2), but the cake is still baking in the oven (Instruction 1 hasn't written its result yet!).\n"
                "You must wait (stall / bubble) until the cake cools down before you can frost it. In CPU design, Operand Forwarding is like taking the warm cake directly from the oven shelf instead of waiting for it to be packaged."
            )
        }
    ],
    "foundations": [
        {
            "number": "12.1",
            "title": "The Three Classic Pipeline Hazards",
            "content": (
                "<b>1. Structural Hazard (Hardware Conflict):</b><br/>"
                "• Two instructions need the exact same physical resource at the same time (e.g. instruction fetch and data read both trying to access a single-port RAM).<br/>"
                "• Solution: Separate Instruction Cache and Data Cache (Harvard Architecture).<br/><br/>"
                "<b>2. Data Hazard (RAW, WAR, WAW):</b><br/>"
                "• <b>RAW (Read After Write - True Dependency):</b> Inst 2 wants to read R1 before Inst 1 finishes writing to R1. Solved by <b>Operand Forwarding</b> or inserting NOP stalls.<br/>"
                "• <b>WAR (Write After Read - Anti-dependency):</b> Inst 2 writes before Inst 1 reads.<br/>"
                "• <b>WAW (Write After Write - Output dependency):</b> Inst 2 writes before Inst 1 writes, leaving old data.<br/><br/>"
                "<b>3. Control Hazard (Branch Hazard):</b><br/>"
                "• Occurs on Conditional Jumps (<code>if/else</code>, <code>goto</code>) because the CPU doesn't know which path to fetch next.<br/>"
                "• Solution: Branch Prediction (Dynamic/Static) and Delayed Branching."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: In a standard 5-stage pipeline without operand forwarding, a RAW dependency between consecutive instructions causes 2 stall cycles. With operand forwarding, stalls reduce to 0 (or 1 stall if dependent on a LOAD instruction)!"
        },
        {
            "number": "12.2",
            "title": "Pipeline Clock Period, Speedup & CPI",
            "content": (
                "<b>Key Formulas to memorize:</b><br/>"
                "• <b>Clock Cycle Time (T_clk):</b> Max(Stage Delays) + Buffer Delay (Register Delay).<br/>"
                "• <b>Execution time for n instructions in k-stage pipeline:</b> Time = (k + n - 1) × T_clk.<br/>"
                "• <b>Ideal Speedup (when n is very large and no stalls):</b> Speedup = k (number of stages).<br/>"
                "• <b>Actual Speedup with stalls:</b> Speedup = (Non-pipelined time) / (Pipelined time) = (k × CPI_ideal) / (CPI_actual)."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: The slowest pipeline stage determines the clock frequency of the entire processor! Clock frequency = 1 / [Max(stage delay) + buffer delay]."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Calculating Pipeline Speedup",
            "problem": "A 5-stage pipeline has stage delays of 150 ps, 120 ps, 160 ps, 140 ps, and 110 ps. The pipeline register delay is 10 ps. What is the clock cycle time, and what is the speedup for 1000 instructions compared to non-pipelined execution?",
            "steps": [
                "Step 1: Find the bottleneck stage: Max(150, 120, 160, 140, 110) = 160 ps.",
                "Step 2: Add register delay: Clock Cycle (T_clk) = 160 ps + 10 ps = 170 ps.",
                "Step 3: Non-pipelined time per instruction = Sum of stage delays = 150 + 120 + 160 + 140 + 110 = 680 ps.",
                "Step 4: Non-pipelined total time for 1000 instructions = 1000 × 680 ps = 680,000 ps.",
                "Step 5: Pipelined time for 1000 instructions = (k + n - 1) × T_clk = (5 + 1000 - 1) × 170 ps = 1004 × 170 = 170,680 ps.",
                "Step 6: Speedup = 680,000 / 170,680 = 3.984 (close to theoretical 4x)."
            ],
            "answer": "Clock Cycle = 170 ps, Speedup = 3.98x."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Average CPI with Stalls",
            "warning": "Average CPI = 1 + (Stalls per instruction). If 20% of instructions are branch instructions and each causes 2 stalls, CPI = 1 + (0.20 × 2) = 1.4!"
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
            "text": (
                "Imagine opening Russian nesting dolls:\n"
                "You open Doll #3 to find Doll #2 inside. You open Doll #2 to find Doll #1. At Doll #1, there are no more dolls inside: this is the Base Case!\n"
                "You now stop opening and start assembling them back in reverse order. In computer memory, every recursive call pushes a frame onto the Call Stack. When the base case hits, frames pop off in Last-In First-Out (LIFO) order."
            )
        },
        {
            "title": "Real-Life Example 2: House Address on a Sticky Note (Pointers in C)",
            "text": (
                "• Pass by Value: You build an entire duplicate copy of your house and ship it to your friend. Wasteful and slow!\n"
                "• Pass by Reference (Pointers): You write your house address on a tiny sticky note (`int *p = &x`). Your friend reads the address, walks into your house, and paints the living room green (`*p = 50`). The original house is modified directly!"
            )
        },
        {
            "title": "Real-Life Example 3: The Bolted Metal Locker (Static Variables in C)",
            "text": (
                "Normally, when a function ends, all its local variables are erased from memory.\n"
                "A `static` variable is like a bolted metal locker: its value survives between function calls! The next time you call that function, it picks up with whatever number was left inside the locker."
            )
        }
    ],
    "foundations": [
        {
            "number": "13.1",
            "title": "Pointers & Array Equivalence in C (Explained Step by Step)",
            "content": (
                "In C language, pointers and arrays are closely connected. Here is how they work in simple point form:<br/><br/>"
                "• <b>1. What is an array name?</b><br/>"
                "&nbsp;&nbsp;- When you declare <code>int arr[5] = {10, 20, 30, 40, 50};</code>, the word <code>arr</code> is NOT the whole array.<br/>"
                "&nbsp;&nbsp;- It is simply a pointer to its first element: <code>arr == &arr[0]</code>.<br/><br/>"
                "• <b>2. How does index notation arr[i] actually work?</b><br/>"
                "&nbsp;&nbsp;- In C, there is no separate index operator! C secretly translates <code>arr[i]</code> into pointer arithmetic:<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;<code>arr[i]</code> &nbsp;≡&nbsp; <code>*(arr + i)</code><br/>"
                "&nbsp;&nbsp;- Since addition is commutative (<code>a + b == b + a</code>), <code>*(arr + i)</code> is identical to <code>*(i + arr)</code>.<br/>"
                "&nbsp;&nbsp;- <b>Surprising C Fact:</b> You can legally write <code>3[arr]</code> in C, and it gives the exact same value as <code>arr[3]</code>!<br/><br/>"
                "• <b>3. The Big Difference: *p++ vs (*p)++</b><br/>"
                "&nbsp;&nbsp;- <code>*p++</code>: Moves the pointer! The <code>++</code> is attached to <code>p</code>. It reads the current value, then advances pointer <code>p</code> to point to the next integer in memory.<br/>"
                "&nbsp;&nbsp;- <code>(*p)++</code>: Modifies the value! The parentheses protect <code>p</code>. The pointer stays at the same memory box, but increments the integer value inside that box by 1 (e.g. 10 becomes 11).<br/><br/>"
                "• <b>4. What is Array Decay?</b><br/>"
                "&nbsp;&nbsp;- When you pass an array into a function (like <code>solve(arr)</code>), C never copies the whole array.<br/>"
                "&nbsp;&nbsp;- The array 'decays' into a simple pointer to the first element."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: Because arrays decay to pointers inside functions, running sizeof(arr) inside a function returns the size of a pointer (4 bytes on 32-bit, 8 bytes on 64-bit), NOT the total bytes of the array! Always pass array length as a separate argument."
        },
        {
            "number": "13.2",
            "title": "Short-Circuit Evaluation in Logical Expressions",
            "content": (
                "C evaluates logical expressions from left to right and stops as soon as the outcome is certain:<br/><br/>"
                "• <b>In Logical AND (A && B):</b><br/>"
                "&nbsp;&nbsp;- If <code>A</code> evaluates to False (0), the entire condition is guaranteed to be False.<br/>"
                "&nbsp;&nbsp;- Therefore, <b>B is NEVER EXECUTED</b>!<br/><br/>"
                "• <b>In Logical OR (A || B):</b><br/>"
                "&nbsp;&nbsp;- If <code>A</code> evaluates to True (non-zero), the entire condition is guaranteed to be True.<br/>"
                "&nbsp;&nbsp;- Therefore, <b>B is NEVER EXECUTED</b>!"
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: Watch out for increment operators inside logical checks! Example: in if (a == 0 && ++b > 0), if a is 1 (False), the second expression ++b is skipped entirely, leaving b unchanged!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Tracing Static Recursion",
            "problem": "What is printed by this C program?\nint f(int n) {\n  static int r = 0;\n  if (n <= 0) return 1;\n  if (n > 3) { r = n; return f(n - 2) + 2; }\n  return f(n - 1) + r;\n}\nint main() { printf(\"%d\", f(5)); }",
            "steps": [
                "Step 1: Call f(5). Here n = 5 (> 3). Static r is updated to 5. It returns f(3) + 2.",
                "Step 2: Now call f(3). Here n = 3 (not > 3). It goes to line: return f(2) + r.",
                "Step 3: Call f(2). It returns f(1) + r.",
                "Step 4: Call f(1). It returns f(0) + r.",
                "Step 5: Call f(0). Here n <= 0, so it hits the base case and returns 1.",
                "Step 6: Now unwind the call stack (remember static r is STILL 5!):",
                "  - f(1) = f(0) + r = 1 + 5 = 6.",
                "  - f(2) = f(1) + r = 6 + 5 = 11.",
                "  - f(3) = f(2) + r = 11 + 5 = 16.",
                "Step 7: Finally compute original return: f(5) = f(3) + 2 = 16 + 2 = 18."
            ],
            "answer": "Final printed output = 18."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Multiple Modifications in One Expression",
            "warning": "Writing expressions like `i = i++ + ++i` modifies variable `i` multiple times between sequence points. According to the ISO C standard, this is UNDEFINED BEHAVIOR, and questions asking for a fixed output are technically invalid or ambiguous!"
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
            "title": "Real-Life Example 1: Browser Back Button vs Ticket Counter (Stack vs Queue)",
            "text": (
                "• Stack (LIFO: Last-In First-Out): Like a stack of dinner plates. The last plate placed on top is the first one picked up. The browser 'Back' button uses a stack to pop the most recent website you visited.\n"
                "• Queue (FIFO: First-In First-Out): Like a movie ticket counter. The first person in line gets tickets first. Printer queues work the same way so the first print job sent is printed first."
            )
        },
        {
            "title": "Real-Life Example 2: Circular Dining Table (Circular Queue)",
            "text": (
                "In a regular linear queue, when people leave from the front, empty seats open up, but you can't seat new people if the rear reached the end of the room.\n"
                "A Circular Queue connects the last seat back to the first seat using modulo arithmetic `(rear + 1) % Capacity`, ensuring every single empty seat can be reused."
            )
        },
        {
            "title": "Real-Life Example 3: Treasure Hunt Clue Slips (Linked Lists)",
            "text": (
                "An array is like 10 adjacent hotel lockers: super fast lookup by number, but impossible to expand if neighboring lockers are occupied.\n"
                "A Linked List is like a treasure hunt: each clue card holds an item and the GPS coordinate of the next clue. You can insert a new clue anywhere in O(1) time without moving other clues!"
            )
        }
    ],
    "foundations": [
        {
            "number": "14.1",
            "title": "Infix, Postfix & Stack Conversions",
            "content": (
                "<b>Why do computers prefer Postfix notation?</b><br/>"
                "• Human notation (Infix): <code>A + B * C</code> requires remembering operator precedence rules and parentheses.<br/>"
                "• Computer notation (Postfix / Reverse Polish): <code>A B C * +</code> requires zero parentheses and can be evaluated in a single pass using a stack!<br/><br/>"
                "<b>How to evaluate Postfix using a Stack:</b><br/>"
                "1. Scan symbols from left to right.<br/>"
                "2. If you see an operand (number), push it onto the stack.<br/>"
                "3. If you see an operator (+, -, *, /):<br/>"
                "&nbsp;&nbsp;- Pop the top element as <b>Operand 2</b>.<br/>"
                "&nbsp;&nbsp;- Pop the next element as <b>Operand 1</b>.<br/>"
                "&nbsp;&nbsp;- Calculate: <code>Result = Operand 1 (operator) Operand 2</code>.<br/>"
                "&nbsp;&nbsp;- Push the Result back onto the stack.<br/>"
                "4. When the expression ends, the stack top holds the final answer."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: When popping two operands for non-commutative operators like '-' and '/': The FIRST popped item is Operand 2, and the SECOND popped item is Operand 1! Result = Op1 / Op2 (NOT Op2 / Op1)."
        },
        {
            "number": "14.2",
            "title": "Circular Queue Full and Empty Conditions",
            "content": (
                "In an array of size N implementing a circular queue:<br/>"
                "• <b>Empty Condition:</b> <code>front == rear</code>.<br/>"
                "• <b>Full Condition (sacrificing 1 slot to distinguish from empty):</b><br/>"
                "&nbsp;&nbsp;<code>(rear + 1) % N == front</code>.<br/>"
                "• Maximum elements the queue can hold = <b>N - 1</b>."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: If an array has size N = 8, a circular queue can store at most 7 elements without confusing the Full condition with the Empty condition!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Evaluating Postfix Expression",
            "problem": "Evaluate the postfix expression: 6  2  3  +  *  10  -",
            "steps": [
                "Step 1: Read '6' (number) ⇒ Push to stack: [6].",
                "Step 2: Read '2' (number) ⇒ Push to stack: [6, 2].",
                "Step 3: Read '3' (number) ⇒ Push to stack: [6, 2, 3].",
                "Step 4: Read '+' (operator) ⇒ Pop 3 (Op2), Pop 2 (Op1). Calculate 2 + 3 = 5. Push 5: [6, 5].",
                "Step 5: Read '*' (operator) ⇒ Pop 5 (Op2), Pop 6 (Op1). Calculate 6 * 5 = 30. Push 30: [30].",
                "Step 6: Read '10' (number) ⇒ Push to stack: [30, 10].",
                "Step 7: Read '-' (operator) ⇒ Pop 10 (Op2), Pop 30 (Op1). Calculate 30 - 10 = 20. Push 20: [20]."
            ],
            "answer": "Final evaluated result = 20."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Reversing a Singly Linked List",
            "warning": "To reverse a singly linked list in-place in O(n) time and O(1) space, you need exactly 3 pointers: `prev = NULL`, `curr = head`, and `next = NULL`. Forgetting to save `curr->next` before redirecting the link breaks the list!"
        }
    ]
}

# PDS Chapter 2: Non-Linear Data Structures
CHAPTERS_COA_PDS_ALGO[("PDS", 2)] = {
    "sub_id": "PDS",
    "chap_idx": 2,
    "title": "Trees, Binary Search Trees & Binary Heaps",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The Hospital Emergency Triage (Priority Queue & Binary Heap)",
            "text": (
                "In a hospital emergency room, patients are not treated in first-come first-served order. A patient with a heart attack is treated immediately ahead of someone with a sprained ankle!\n"
                "A Binary Heap (Max-Heap) guarantees that the most critical element is always at the root (index 0), allowing the doctors to extract the highest priority patient in O(log n) time."
            )
        },
        {
            "title": "Real-Life Example 2: Searching a Dictionary (Binary Search Tree - BST)",
            "text": (
                "In a BST, every node follows one golden rule: All values in the left branch are smaller, and all values in the right branch are larger.\n"
                "To look up any word, you compare and throw away half of the tree at every step, just like opening a physical dictionary right in the middle."
            )
        }
    ],
    "foundations": [
        {
            "number": "15.1",
            "title": "Binary Tree Fundamental Properties",
            "content": (
                "Here are the core mathematical properties every GATE aspirant must know:<br/><br/>"
                "• <b>Handshaking Lemma for Trees:</b><br/>"
                "&nbsp;&nbsp;In any binary tree, the number of leaf nodes (L) is always 1 more than the number of nodes with two children (n2):<br/>"
                "&nbsp;&nbsp;<b>L = n2 + 1</b>.<br/><br/>"
                "• <b>Tree Traversals:</b><br/>"
                "&nbsp;&nbsp;- Pre-order: Root → Left → Right.<br/>"
                "&nbsp;&nbsp;- In-order: Left → Root → Right (<b>Always yields strictly sorted order in a BST!</b>).<br/>"
                "&nbsp;&nbsp;- Post-order: Left → Right → Root.<br/><br/>"
                "• <b>Reconstructing a Unique Tree:</b><br/>"
                "&nbsp;&nbsp;To reconstruct a unique binary tree, you MUST be given <b>In-order</b> along with either Pre-order or Post-order."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: In-order traversal of a Binary Search Tree (BST) is ALWAYS strictly sorted in ascending order! If an exam question gives only Pre-order traversal of a BST, you can find the In-order yourself simply by sorting the numbers!"
        },
        {
            "number": "15.2",
            "title": "Binary Heap Array Indexing & Build-Heap Complexity",
            "content": (
                "A binary heap is a Complete Binary Tree stored inside a simple array without pointers:<br/><br/>"
                "• For a node at index <code>i</code> (0-based indexing):<br/>"
                "&nbsp;&nbsp;- Left Child = <code>2i + 1</code>.<br/>"
                "&nbsp;&nbsp;- Right Child = <code>2i + 2</code>.<br/>"
                "&nbsp;&nbsp;- Parent = <code>floor((i - 1) / 2)</code>.<br/><br/>"
                "• <b>Build-Heap Algorithm Time Complexity:</b><br/>"
                "&nbsp;&nbsp;- Building a heap of size n from an unsorted array takes <b>O(n) time</b> (linear time), NOT O(n log n)!"
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: Inserting 1 element into a heap takes O(log n). But building a full heap of n elements from scratch takes O(n) using the bottom-up Build-Heap procedure!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Tree Reconstruction",
            "problem": "Given Preorder: [A, B, D, E, C, F] and Inorder: [D, B, E, A, F, C]. Find the Postorder traversal.",
            "steps": [
                "Step 1: First element of Preorder is root ⇒ Root = 'A'.",
                "Step 2: Find 'A' in Inorder: [D, B, E] are in Left subtree, [F, C] are in Right subtree.",
                "Step 3: In Left subtree [D, B, E], Preorder has 'B' first ⇒ Root of left subtree = 'B'. Inorder [D, B, E] means 'D' is left of B, 'E' is right of B.",
                "Step 4: In Right subtree [F, C], Preorder has 'C' first ⇒ Root of right subtree = 'C'. Inorder [F, C] means 'F' is left child of C.",
                "Step 5: Write Postorder (Left, Right, Root):",
                "  - Left branch of A: D, E, B.",
                "  - Right branch of A: F, C.",
                "  - Root: A."
            ],
            "answer": "Postorder = [D, E, B, F, C, A]."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Number of Unique BSTs with n keys",
            "warning": "The number of structurally unique Binary Search Trees that can be formed with n distinct keys is given by the n-th Catalan Number: C_n = (1 / (n + 1)) × C(2n, n). For n = 3: C_3 = 5. For n = 4: C_4 = 14."
        }
    ]
}

# =============================================================================
# ALGORITHMS (ALGO)
# =============================================================================

# ALGO Chapter 0: Asymptotic Analysis & Recurrences
CHAPTERS_COA_PDS_ALGO[("ALGO", 0)] = {
    "sub_id": "ALGO",
    "chap_idx": 0,
    "title": "Asymptotic Analysis, Master Theorem & Recurrences",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Carrier Pigeon vs Internet Bandwidth (Asymptotic Growth)",
            "text": (
                "If you send a 16 GB flash drive strapped to a carrier pigeon, the pigeon takes 1 hour to fly across the city regardless of whether the drive has 1 GB or 1000 GB (O(1) constant time!).\n"
                "If you send it over a 10 Mbps internet connection, time grows linearly with data size (O(n)). For small files, the internet wins. But as data grows to petabytes, the pigeon asymptotically beats the internet! Big-O measures this behavior as n grows towards infinity."
            )
        }
    ],
    "foundations": [
        {
            "number": "16.1",
            "title": "Big-O, Big-Omega & Big-Theta Explained",
            "content": (
                "Asymptotic notations describe how running time scales as input size n grows huge:<br/><br/>"
                "• <b>Big-O (O): Upper Bound (Worst-case ceiling)</b><br/>"
                "&nbsp;&nbsp;- <code>f(n) = O(g(n))</code> means f(n) will never grow faster than c × g(n).<br/>"
                "&nbsp;&nbsp;- Plain English: 'The algorithm will take at most this much time.'<br/><br/>"
                "• <b>Big-Omega (Ω): Lower Bound (Best-case floor)</b><br/>"
                "&nbsp;&nbsp;- <code>f(n) = Ω(g(n))</code> means f(n) will take at least c × g(n).<br/>"
                "&nbsp;&nbsp;- Plain English: 'The algorithm will take at least this much time.'<br/><br/>"
                "• <b>Big-Theta (Θ): Tight Bound (Exact growth rate)</b><br/>"
                "&nbsp;&nbsp;- <code>f(n) = Θ(g(n))</code> holds if and only if f(n) is BOTH O(g(n)) and Ω(g(n))."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: Common growth order from slowest to fastest: O(1) < O(log log n) < O(log n) < O(sqrt(n)) < O(n) < O(n log n) < O(n^2) < O(2^n) < O(n!). Remember that (log n)^1000 grows slower than n^0.001 as n reaches infinity!"
        },
        {
            "number": "16.2",
            "title": "Master Theorem for Divide and Conquer",
            "content": (
                "For recurrence relations of the form: <b>T(n) = a T(n/b) + Θ(n^k log^p n)</b>:<br/>"
                "Compare <code>a</code> with <code>b^k</code>:<br/><br/>"
                "• <b>Case 1: If a > b^k</b><br/>"
                "&nbsp;&nbsp;Roots dominate! T(n) = <b>Θ(n^(log_b a))</b>.<br/><br/>"
                "• <b>Case 2: If a == b^k</b><br/>"
                "&nbsp;&nbsp;T(n) = <b>Θ(n^k log^(p+1) n)</b>.<br/>"
                "&nbsp;&nbsp;(For standard mergesort where p = 0: T(n) = Θ(n log n)).<br/><br/>"
                "• <b>Case 3: If a < b^k</b><br/>"
                "&nbsp;&nbsp;Leaves dominate! T(n) = <b>Θ(n^k log^p n)</b>."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: Master theorem cannot be applied if: (1) 'a' is not a constant (e.g. T(n) = 2^n T(n/2)), (2) 'b' is a subtraction (e.g. T(n) = T(n-1) + 1), or (3) f(n) is not polynomial."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Solving Recurrence with Master Theorem",
            "problem": "Find the asymptotic time complexity of T(n) = 8 T(n/2) + n^2.",
            "steps": [
                "Step 1: Identify parameters: a = 8, b = 2, f(n) = n^2 (so k = 2, p = 0).",
                "Step 2: Calculate b^k = 2^2 = 4.",
                "Step 3: Compare 'a' and 'b^k': a = 8, b^k = 4. Since 8 > 4, Case 1 applies!",
                "Step 4: Compute log_b(a) = log_2(8) = 3.",
                "Step 5: Apply Case 1 formula: T(n) = Θ(n^(log_b a)) = Θ(n^3)."
            ],
            "answer": "Time Complexity = Θ(n^3)."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Decreasing Recurrence Relations",
            "warning": "For recurrences like T(n) = T(n-1) + n, do NOT use Master Theorem! Use iterative expansion: T(n) = n + (n-1) + (n-2) + ... + 1 = n(n+1)/2 = Θ(n^2)."
        }
    ]
}

# ALGO Chapter 1: Sorting, Searching & Hashing
CHAPTERS_COA_PDS_ALGO[("ALGO", 1)] = {
    "sub_id": "ALGO",
    "chap_idx": 1,
    "title": "Sorting Algorithms, Lower Bounds & Hash Tables",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Arranging Playing Cards (Insertion Sort vs Quick Sort)",
            "text": (
                "When you pick up playing cards one by one into your hand, you slide each new card into its sorted place among the cards you already hold: this is Insertion Sort (O(n) best-case for nearly sorted cards!).\n"
                "When sorting a huge pile of 10,000 exam sheets, you pick a pivot roll number (like 5000), split into piles < 5000 and > 5000, and repeat. This is Quick Sort."
            )
        }
    ],
    "foundations": [
        {
            "number": "17.1",
            "title": "Master Summary of Sorting Algorithms",
            "content": (
                "Here is the definitive comparison table tested in GATE:<br/><br/>"
                "• <b>Merge Sort:</b> Best: O(n log n) | Worst: O(n log n) | Space: O(n) | Stable: YES.<br/>"
                "• <b>Heap Sort:</b> Best: O(n log n) | Worst: O(n log n) | Space: O(1) in-place | Stable: NO.<br/>"
                "• <b>Quick Sort:</b> Best: O(n log n) | Worst: O(n^2) (sorted input) | Space: O(log n) | Stable: NO.<br/>"
                "• <b>Insertion Sort:</b> Best: O(n) (already sorted) | Worst: O(n^2) | Space: O(1) | Stable: YES.<br/>"
                "• <b>Counting Sort:</b> Time: O(n + k) | Space: O(n + k) | Non-comparison based | Stable: YES."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: Any comparison-based sorting algorithm requires at least Ω(n log n) comparisons in the worst case! To sort faster than O(n log n), you must use non-comparison algorithms like Counting Sort or Radix Sort."
        },
        {
            "number": "17.2",
            "title": "Hash Table Collisions: Chaining vs Open Addressing",
            "content": (
                "<b>What is a Collision?</b><br/>"
                "Two distinct keys produce the same hash slot: <code>h(k1) == h(k2)</code>.<br/><br/>"
                "<b>1. Separate Chaining:</b><br/>"
                "• Each slot points to a linked list. Can store infinite elements. Load factor α can exceed 1.<br/><br/>"
                "<b>2. Open Addressing (All keys stored inside the table itself; α <= 1):</b><br/>"
                "• Linear Probing: <code>h(k, i) = (h(k) + i) % m</code>. Problem: Primary Clustering (long continuous runs of occupied slots).<br/>"
                "• Quadratic Probing: <code>h(k, i) = (h(k) + c1*i + c2*i^2) % m</code>. Solves primary clustering; suffers from secondary clustering.<br/>"
                "• Double Hashing: <code>h(k, i) = (h1(k) + i * h2(k)) % m</code>. Best open addressing method; eliminates clustering."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: In Double Hashing, h2(k) must be relatively prime to the table size m (e.g. choose m as a prime number) so the probe sequence visits every single slot in the table!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Linear Probing Hash Table",
            "problem": "Insert keys [12, 22, 32, 42] into a hash table of size 10 using h(k) = k % 10 with Linear Probing. Find the slot where 42 is stored.",
            "steps": [
                "Step 1: Key 12: 12 % 10 = 2. Slot 2 is empty ⇒ Insert 12 at Slot 2.",
                "Step 2: Key 22: 22 % 10 = 2. Slot 2 is occupied! Probe (2 + 1) % 10 = 3. Slot 3 is empty ⇒ Insert 22 at Slot 3.",
                "Step 3: Key 32: 32 % 10 = 2. Slot 2 is occupied, Slot 3 is occupied! Probe (2 + 2) % 10 = 4. Slot 4 is empty ⇒ Insert 32 at Slot 4.",
                "Step 4: Key 42: 42 % 10 = 2. Slots 2, 3, 4 are occupied! Probe (2 + 3) % 10 = 5. Slot 5 is empty ⇒ Insert 42 at Slot 5."
            ],
            "answer": "Key 42 is stored at Slot index 5."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Deletion in Open Addressing",
            "warning": "In open addressing, you CANNOT simply erase an element and leave the slot empty! Leaving it empty will cause subsequent searches to terminate prematurely. You must mark deleted slots with a special 'DELETED' tombstone flag."
        }
    ]
}

# ALGO Chapter 2: Algorithm Design Paradigms
CHAPTERS_COA_PDS_ALGO[("ALGO", 2)] = {
    "sub_id": "ALGO",
    "chap_idx": 2,
    "title": "Greedy Algorithms, Dynamic Programming & Divide-and-Conquer",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Indian Rupee Coin Change (When Greedy Fails)",
            "text": (
                "With Indian currency denominations [₹1, ₹2, ₹5, ₹10], making change for ₹18 greedily (pick largest first: 10 + 5 + 2 + 1 = 4 coins) always gives the optimal answer.\n"
                "However, with custom coins like [₹1, ₹7, ₹10], to make ₹14:\n"
                "• Greedy picks: ₹10 + ₹1 + ₹1 + ₹1 + ₹1 = 5 coins.\n"
                "• Optimal Dynamic Programming picks: ₹7 + ₹7 = 2 coins!\n"
                "This proves Greedy choice fails unless the coin system has a specific mathematical property."
            )
        }
    ],
    "foundations": [
        {
            "number": "18.1",
            "title": "Greedy Method vs Dynamic Programming",
            "content": (
                "• <b>Greedy Method:</b><br/>"
                "&nbsp;&nbsp;- Makes the locally best choice at every step without ever backtracking.<br/>"
                "&nbsp;&nbsp;- Fast (typically O(n log n)), but only works if problem satisfies: (1) Greedy Choice Property, and (2) Optimal Substructure.<br/>"
                "&nbsp;&nbsp;- Examples: Fractional Knapsack, Kruskal MST, Prim MST, Dijkstra, Huffman Coding.<br/><br/>"
                "• <b>Dynamic Programming (DP):</b><br/>"
                "&nbsp;&nbsp;- Explores all subproblems but avoids redundant calculations by saving results in a table.<br/>"
                "&nbsp;&nbsp;- Required properties: (1) Optimal Substructure, and (2) <b>Overlapping Subproblems</b>.<br/>"
                "&nbsp;&nbsp;- Examples: 0/1 Knapsack, Longest Common Subsequence (LCS), Matrix Chain Multiplication, Floyd-Warshall."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: Fractional Knapsack is solved in O(n log n) by Greedy (sort by value/weight ratio). But 0/1 Knapsack CANNOT be solved greedily; it requires Dynamic Programming in O(n * W) pseudo-polynomial time!"
        },
        {
            "number": "18.2",
            "title": "Longest Common Subsequence (LCS) Recurrence",
            "content": (
                "Given two strings X of length m and Y of length n:<br/>"
                "• If last characters match (<code>X[m-1] == Y[n-1]</code>):<br/>"
                "&nbsp;&nbsp;<code>LCS(X, Y) = 1 + LCS(X[0..m-2], Y[0..n-2])</code>.<br/>"
                "• If characters do NOT match:<br/>"
                "&nbsp;&nbsp;<code>LCS(X, Y) = Max(LCS(X[0..m-2], Y), LCS(X, Y[0..n-2]))</code>.<br/>"
                "• Time Complexity: <b>O(m × n)</b> using a 2D table."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: Matrix Chain Multiplication: To multiply matrices A1(p0×p1), A2(p1×p2)... An(pn-1×pn), the minimum scalar multiplications can be found in O(n^3) time using dynamic programming."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Fractional Knapsack",
            "problem": "Knapsack capacity W = 50 kg. Items: A (v=60, w=10), B (v=100, w=20), C (v=120, w=30). Find maximum value.",
            "steps": [
                "Step 1: Compute value-to-weight ratio for each item:",
                "  - Item A: 60 / 10 = 6.0 per kg.",
                "  - Item B: 100 / 20 = 5.0 per kg.",
                "  - Item C: 120 / 30 = 4.0 per kg.",
                "Step 2: Pick highest ratio first (Item A): Take full 10 kg. Value = 60. Remaining capacity = 50 - 10 = 40 kg.",
                "Step 3: Next pick Item B: Take full 20 kg. Value = 60 + 100 = 160. Remaining capacity = 40 - 20 = 20 kg.",
                "Step 4: Next pick Item C: Only 20 kg capacity left! Take fraction (20 / 30) of Item C. Value = 160 + (2/3 × 120) = 160 + 80 = 240."
            ],
            "answer": "Maximum attainable value = 240."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Huffman Code Tree Uniqueness",
            "warning": "Huffman code lengths and total bits for the message are ALWAYS optimal and unique. However, the exact binary codes (0 vs 1 assignment to left/right branches) are NOT unique!"
        }
    ]
}

# ALGO Chapter 3: Graph Algorithms
CHAPTERS_COA_PDS_ALGO[("ALGO", 3)] = {
    "sub_id": "ALGO",
    "chap_idx": 3,
    "title": "Graph Traversals, MST & Shortest Paths",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Google Maps Navigation (Dijkstra's Algorithm)",
            "text": (
                "When Google Maps finds the fastest route from your home to college, cities and intersections are vertices, and roads with traffic delays are weighted edges.\n"
                "Dijkstra's algorithm expands outward like a ripple in a pond, always visiting the closest unvisited intersection first, finding the absolute shortest path in O((V + E) log V) time."
            )
        },
        {
            "title": "Real-Life Example 2: Connecting Cities with Electric Power Lines (Minimum Spanning Tree)",
            "text": (
                "A power company wants to electrify 10 cities with the minimum total kilometers of wire.\n"
                "You don't need a direct cable between every single city (no cycles needed!). You just need a Minimum Spanning Tree (MST): exactly V - 1 cables connecting all V cities at the lowest possible cost."
            )
        }
    ],
    "foundations": [
        {
            "number": "19.1",
            "title": "BFS vs DFS Comparison",
            "content": (
                "• <b>Breadth-First Search (BFS):</b><br/>"
                "&nbsp;&nbsp;- Data Structure: <b>Queue (FIFO)</b>.<br/>"
                "&nbsp;&nbsp;- Explores all immediate neighbors first, layer by layer.<br/>"
                "&nbsp;&nbsp;- Key Application: Finds the <b>shortest path in an unweighted graph</b>!<br/>"
                "&nbsp;&nbsp;- Time Complexity: <code>O(V + E)</code> using adjacency list.<br/><br/>"
                "• <b>Depth-First Search (DFS):</b><br/>"
                "&nbsp;&nbsp;- Data Structure: <b>Stack (LIFO / Recursion)</b>.<br/>"
                "&nbsp;&nbsp;- Explores deep down a branch until it hits a dead end, then backtracks.<br/>"
                "&nbsp;&nbsp;- Key Applications: Cycle detection, Topological Sorting, finding Strongly Connected Components (Tarjan/Kosaraju).<br/>"
                "&nbsp;&nbsp;- Time Complexity: <code>O(V + E)</code>."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: In DFS of an undirected graph, every edge is either a Tree Edge or a Back Edge (Cross edges NEVER exist in undirected DFS)! A Back Edge indicates the presence of a cycle."
        },
        {
            "number": "19.2",
            "title": "Dijkstra vs Bellman-Ford vs Floyd-Warshall",
            "content": (
                "• <b>Dijkstra's Algorithm (Single Source Shortest Path):</b><br/>"
                "&nbsp;&nbsp;- Condition: Edge weights must be <b>NON-NEGATIVE</b> (fails on negative weights!).<br/>"
                "&nbsp;&nbsp;- Time: <code>O((V + E) log V)</code> with Min-Heap.<br/><br/>"
                "• <b>Bellman-Ford Algorithm (Single Source Shortest Path):</b><br/>"
                "&nbsp;&nbsp;- Handles negative weights and detects negative weight cycles.<br/>"
                "&nbsp;&nbsp;- Time: <code>O(V × E)</code>.<br/><br/>"
                "• <b>Floyd-Warshall Algorithm (All-Pairs Shortest Path):</b><br/>"
                "&nbsp;&nbsp;- Dynamic programming approach computing shortest paths between all pairs of nodes.<br/>"
                "&nbsp;&nbsp;- Time: <code>O(V^3)</code>."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: Prim's algorithm and Dijkstra's algorithm look almost identical, but their relaxation step differs: Dijkstra updates d[v] = min(d[v], d[u] + weight(u,v)). Prim updates key[v] = min(key[v], weight(u,v))!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Kruskal's MST Algorithm",
            "problem": "A graph has vertices {A, B, C, D} and edges: (A-B: 1), (B-C: 2), (A-C: 3), (C-D: 4), (B-D: 5). Find the total weight of the MST.",
            "steps": [
                "Step 1: Sort all edges in non-decreasing order of weight:\n  (A-B: 1), (B-C: 2), (A-C: 3), (C-D: 4), (B-D: 5).",
                "Step 2: Pick smallest edge (A-B, wt 1). Add to MST. (Edges = 1).",
                "Step 3: Pick next edge (B-C, wt 2). Add to MST. (Edges = 2).",
                "Step 4: Pick next edge (A-C, wt 3). Both A and C are already in the same connected set! Adding A-C creates a cycle (A-B-C-A). Discard A-C!",
                "Step 5: Pick next edge (C-D, wt 4). D is not yet connected. Add to MST. (Edges = 3).",
                "Step 6: We have selected V - 1 = 4 - 1 = 3 edges. MST is complete!\n  Total MST weight = 1 + 2 + 4 = 7."
            ],
            "answer": "Minimum Spanning Tree Total Weight = 7."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Topological Sort",
            "warning": "Topological Sort is ONLY possible on a Directed Acyclic Graph (DAG). If a graph has even one directed cycle, a valid topological sort does NOT exist!"
        }
    ]
}
