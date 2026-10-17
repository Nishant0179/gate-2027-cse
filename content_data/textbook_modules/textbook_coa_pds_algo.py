# textbook_coa_pds_algo.py
# In-depth Master Textbook Modules for Computer Organization (COA), Programming & Data Structures (PDS), and Algorithms (ALGO)
# Follows the exact pedagogical and visual architecture of User Images 2 & 3.

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
            "title": "Real-Life Example 1: The Scavenger Hunt Clue Cards (Addressing Modes)",
            "text": "Imagine a scavenger hunt. An 'Immediate' clue card directly gives you ₹500 cash taped to the paper (Operand is inside the instruction). A 'Direct' clue card gives an exact street address: 'Go to House #42 on Baker Street' (Memory Address). An 'Indirect' clue card tells you: 'Go to Locker 10; inside Locker 10 is a slip of paper telling you which bank vault contains the treasure' (Pointer dereferencing). A 'Relative' clue card says: 'From where you are standing right now, walk 15 steps forward' (Program Counter relative offset for loops and jumps)."
        },
        {
            "title": "Real-Life Example 2: The Fast Food Combo Coupon vs Custom Meal (Instruction Formats & Opcode Expansion)",
            "text": "In a fast food restaurant, a 2-bit coupon can choose between 4 fixed combos (fixed-length opcode). But what if the manager wants 3 ultra-popular meals with 2 sides, plus 12 niche snacks with only 1 side? By reserving one combo code as an 'escape hatch' to unlock a longer code, the menu expands dynamically. This is Expanding Opcode: short opcodes for 3-register instructions, expanding to longer opcodes when fewer register fields are needed."
        },
        {
            "title": "Real-Life Example 3: Big-Endian vs Little-Endian Mail Addressing",
            "text": "In Japan or Germany, an address starts with the Country, then State, then City, down to the House Number (Most Significant part first: Big-Endian). In traditional British mail, you write the House Number first, then Street, City, and Country last (Least Significant byte first: Little-Endian). When storing 0x12345678 in memory at address 1000: Big-Endian puts 0x12 at 1000; Little-Endian puts 0x78 at 1000."
        }
    ],
    "foundations": [
        {
            "number": "9.1",
            "title": "Addressing Modes & Effective Address (EA) Calculations",
            "content": (
                "The Effective Address (EA) is the actual physical RAM address of the operand.<br/>"
                "• <b>Immediate Mode:</b> Operand is part of instruction. EA = None. No memory reference.<br/>"
                "• <b>Direct (Absolute) Mode:</b> EA = Address field (A). 1 memory reference.<br/>"
                "• <b>Indirect Mode:</b> EA = M[A]. Pointer to pointer. 2 memory references.<br/>"
                "• <b>Register Direct:</b> Operand in register R. 0 memory references.<br/>"
                "• <b>Register Indirect:</b> EA = [R]. Pointer stored in register. 1 memory reference.<br/>"
                "• <b>PC-Relative Mode:</b> EA = PC + Offset. Crucial for position-independent code (branch/jump).<br/>"
                "• <b>Base-Register Mode:</b> EA = Base Reg + Displacement. Crucial for relocating programs.<br/>"
                "• <b>Indexed Mode:</b> EA = Index Reg + Address field. Crucial for linear array traversals (A[i]).<br/>"
                "• <b>Auto-increment / Auto-decrement:</b> EA = [R], then R is incremented/decremented by step size. Implements stacks and queues efficiently."
            ),
            "crucial_rule": "CRUCIAL RULE: In PC-Relative addressing, remember that by the time the branch instruction executes, the Program Counter (PC) has ALREADY been incremented to point to the NEXT sequential instruction! Effective Address = (PC + instruction_length) + offset."
        },
        {
            "number": "9.2",
            "title": "Instruction Cycle, Register Transfers & Control Sequences",
            "content": (
                "Every instruction follows Fetch -> Decode -> Operand Fetch -> Execute -> Store.<br/>"
                "• <b>Fetch Phase Micro-operations:</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;T0: MAR ← PC<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;T1: MBR ← M[MAR], PC ← PC + I (word length)<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;T2: IR ← MBR<br/>"
                "• <b>Hardwired Control:</b> Combinational logic circuit using decoders and state flip-flops. Ultra-fast, RISC-oriented, but rigid and impossible to modify post-silicon.<br/>"
                "• <b>Microprogrammed Control:</b> Control signals stored in Control ROM (CROM). Slower, CISC-oriented, flexible, easily updated via microcode patches."
            ),
            "crucial_rule": "CRUCIAL RULE: Horizontal Microprogramming generates 1 control bit per control signal (no decoder needed, wide micro-words, maximum parallelism). Vertical Microprogramming groups mutually exclusive signals through decoders (narrow words, slower due to decoding delay)."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: Expanding Opcode Capacity",
            "problem": "A computer system uses 16-bit instructions with 6-bit register addresses. It supports two formats: (a) 3-register instructions, and (b) 2-register instructions. If there are 14 distinct 3-register instructions, what is the maximum number of 2-register instructions that can be supported?",
            "steps": [
                "Step 1: Total instruction length = 16 bits. Register field size = 6 bits.",
                "Step 2: For 3-register instructions: 3 × 6 = 18 bits, which exceeds 16 bits! Let us take register size = 4 bits (so 16 - 3×4 = 4 bits opcode).",
                "Step 3: Opcode field for 3-register = 16 - (3 × 4) = 4 bits ⇒ 2^4 = 16 total patterns.",
                "Step 4: Since 14 patterns are consumed by 3-register instructions, free patterns remaining = 16 - 14 = 2 patterns.",
                "Step 5: For 2-register instructions, the third register field (4 bits) is reclaimed by the opcode! New available opcode space = 2 × 2^4 = 2 × 16 = 32 distinct instructions."
            ],
            "answer": "Maximum 2-register instructions = 32."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: Word-Addressable vs Byte-Addressable Memory",
            "warning": "When calculating the number of bits required for memory addressing, ALWAYS check if memory is byte-addressable (cells of 8 bits) or word-addressable (e.g. cells of 32 bits). A 64 MB memory requires 26 bits if byte-addressable, but only 24 bits if 4-byte-word addressable!"
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
            "title": "Real-Life Example 1: The Orchestra Conductor vs Sheet Music (Control Unit)",
            "text": "An ALU is full of brilliant musicians (adders, shifters, logic gates), but they produce sheer noise if left alone. The Control Unit is the orchestra conductor. In a Hardwired system, the conductor reacts with lightning-fast muscular reflexes to every visual cue. In a Microprogrammed system, the conductor strictly turns the pages of a meticulously written musical score (Control Memory), reading micro-instructions one tick at a time."
        },
        {
            "title": "Real-Life Example 2: The Fast-Forward Shifter (Booth's Multiplication Algorithm)",
            "text": "If you multiply 15 by 31 (binary 011111), standard pencil-and-paper multiplication requires 5 separate additions of partial products. Booth's algorithm notices that 31 is just (32 - 1) = (2^5 - 2^0). Instead of 5 additions, Booth performs just ONE subtraction at the start of the block of 1s (transition 10) and ONE addition at the end (transition 01), skipping all intermediate 1s via lightning shifts!"
        },
        {
            "title": "Real-Life Example 3: The Toll Booth Express Lane (Direct Memory Access - DMA)",
            "text": "When a 4K movie file streams from a hard drive into RAM, if the CPU had to read each 4-byte word into an accumulator register and then write it to RAM, the CPU would be 100% frozen just playing the role of a dumb delivery boy (Programmed I/O). A DMA Controller takes over the system bus, streaming gigabytes directly from disk to RAM while the CPU continues running user applications completely uninterrupted."
        }
    ],
    "foundations": [
        {
            "number": "10.1",
            "title": "Booth's Multiplication Algorithm & Recoding Rules",
            "content": (
                "Booth's algorithm multiplies signed 2's complement integers by scanning pairs of bits (Q_i, Q_{i-1}) with Q_{-1} initialized to 0.<br/>"
                "• <b>Recoding Rules:</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• <b>0 0:</b> No operation (Shift only).<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• <b>0 1:</b> Add Multiplicand (End of block of 1s) -> A ← A + M, then Arithmetic Right Shift (ARS).<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• <b>1 0:</b> Subtract Multiplicand (Beginning of block of 1s) -> A ← A - M, then ARS.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• <b>1 1:</b> No operation (Middle of block of 1s, Shift only).<br/>"
                "• <b>Worst Case:</b> Alternating 01010101 requires n additions/subtractions.<br/>"
                "• <b>Best Case:</b> Consecutive blocks of 1s (e.g. 00011110) minimizes arithmetic operations."
            ),
            "crucial_rule": "CRUCIAL RULE: In Booth's algorithm, the shift operation is strictly ARITHMETIC RIGHT SHIFT (ARS), which replicates the sign bit (MSB), preserving the correct negative sign in 2's complement."
        },
        {
            "number": "10.2",
            "title": "I/O Organization: Programmed I/O, Interrupt-Driven & DMA Cycle Stealing",
            "content": (
                "• <b>Programmed I/O:</b> CPU continuously polls status flags (Busy Waiting). Extremely wasteful of CPU cycles.<br/>"
                "• <b>Interrupt-Driven I/O:</b> Device notifies CPU via hardware interrupt line when ready. CPU suspends current task, saves context, executes Interrupt Service Routine (ISR), and resumes.<br/>"
                "• <b>Direct Memory Access (DMA):</b> DMA controller transfers blocks of data between device and RAM without CPU intervention.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• <b>Burst Transfer Mode:</b> DMA holds the bus continuously until the entire data block is transferred.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• <b>Cycle Stealing Mode:</b> DMA steals 1 bus cycle from the CPU during the instruction execution phase (when CPU is not accessing memory)."
            ),
            "crucial_rule": "CRUCIAL RULE: Percentage of CPU time consumed by DMA in cycle-stealing mode = [Data Transfer Rate / Memory Bus Bandwidth] × 100%."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: DMA Cycle Stealing Bus Overhead",
            "problem": "A hard disk device transfers data at a rate of 2 MB/sec. The system memory bus has a clock cycle of 200 ns and transfers 1 byte per cycle. In cycle-stealing DMA mode, what percentage of CPU processing time is stolen by the DMA controller?",
            "steps": [
                "Step 1: Compute Memory Bus Bandwidth: Bus cycle = 200 ns = 200 × 10^-9 s. Bus transfers 1 byte per 200 ns.",
                "Step 2: Bus Bandwidth = 1 Byte / (200 × 10^-9 s) = 5 × 10^6 Bytes/sec = 5 MB/sec.",
                "Step 3: Device Transfer Rate = 2 MB/sec.",
                "Step 4: Fraction of time stolen = Device Rate / Bus Bandwidth = (2 MB/s) / (5 MB/s) = 2/5 = 0.40.",
                "Step 5: Percentage of CPU time consumed = 0.40 × 100% = 40%."
            ],
            "answer": "CPU time stolen by DMA = 40% (remaining 60% available for user computation)."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: Interrupt Vector Address Resolution",
            "warning": "Vectored interrupts supply the ISR memory address directly from the I/O device on the data bus. Non-vectored interrupts have a fixed, hardwired ISR address in CPU architecture. Do not confuse the two!"
        }
    ]
}

# COA Chapter 2: Memory Hierarchy, Cache Mapping & AMAT
CHAPTERS_COA_PDS_ALGO[("COA", 2)] = {
    "sub_id": "COA",
    "chap_idx": 2,
    "title": "Memory Hierarchy, Cache Mapping & AMAT",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The Kitchen Spice Rack vs The Basement Grocery Cellar (Cache Locality)",
            "text": "When cooking biryani, a master chef keeps salt, turmeric, and chili powder in a tiny spice rack right next to the stove (L1 Cache: ultra-fast, 1-second access). They do not run down two flights of stairs to the dark basement storage cellar (Main RAM: slow, 100-second access) for every pinch of salt! Because recipes reuse the same spices repeatedly (Temporal Locality) and nearby ingredients are used together (Spatial Locality), 95% of cooking needs are satisfied directly from the spice rack."
        },
        {
            "title": "Real-Life Example 2: The College Hostel Assigned Parking Slots (Cache Mapping Techniques)",
            "text": "In Direct Mapped parking, your room number modulo 10 determines your exact parking slot: Room 104 and Room 204 fight over Slot 4 (Conflict Miss!). If both students arrive, they constantly kick each other out. In Fully Associative parking, any car can park in any vacant spot in the entire lot (Zero conflicts, but you need 50 security guards with cameras to search everywhere: expensive associative comparator hardware). Set-Associative parking compromises: each floor gets a designated 4-car cluster."
        },
        {
            "title": "Real-Life Example 3: The Scribbled Notepad vs Formal Carbon Copy (Write-Through vs Write-Back)",
            "text": "When taking phone orders, Write-Through writes the order immediately to your scratch notepad AND runs across the office to write it into the permanent master ledger (safe, but slows down every call to ledger speed). Write-Back writes only to the scratch notepad, marking it with a red 'Dirty Bit'. You only update the permanent ledger when the notepad page fills up and is discarded, boosting speed tenfold."
        }
    ],
    "foundations": [
        {
            "number": "11.1",
            "title": "Cache Memory Mapping Architectures: Direct, Associative & Set-Associative",
            "content": (
                "Given Physical Address Size = P bits, Main Memory Size = 2^P bytes, Cache Size = C bytes, Block Size (Line Size) = B = 2^b bytes (Offset = b bits).<br/>"
                "• <b>Direct Mapped Cache:</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Number of cache lines N = C / B = 2^c lines.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Physical Address = <b>[ Tag | Line Index (c bits) | Block Offset (b bits) ]</b>.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Tag bits = P - c - b.<br/>"
                "• <b>Fully Associative Cache:</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;No line index field! Physical Address = <b>[ Tag (P - b bits) | Block Offset (b bits) ]</b>.<br/>"
                "• <b>k-Way Set-Associative Cache:</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Number of sets S = (C / B) / k = 2^s sets.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Physical Address = <b>[ Tag (P - s - b bits) | Set Index (s bits) | Block Offset (b bits) ]</b>.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Hardware Comparators needed = k (each comparing tag bits in parallel)."
            ),
            "crucial_rule": "CRUCIAL RULE: Cache tag directory size = (Number of Lines) × [Tag bits + Valid bit + Dirty bit (if write-back)]. In GATE, remember to multiply by the total number of lines, NOT the number of sets!"
        },
        {
            "number": "11.2",
            "title": "Average Memory Access Time (AMAT) & Multi-Level Hierarchies",
            "content": (
                "• <b>Single-Level Cache AMAT:</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;<b>AMAT = H × t_c + (1 - H) × t_m</b> (Parallel search) or <b>AMAT = t_c + (1 - H) × t_miss_penalty</b> (Hierarchical search).<br/>"
                "• <b>Two-Level Cache Hierarchy (L1 and L2):</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;<b>AMAT = t_L1 + (1 - H1) × [ t_L2 + (1 - H2_local) × t_main_mem ]</b>.<br/>"
                "• <b>Local vs Global Miss Rate:</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Local Miss Rate L2 = (Misses in L2) / (Accesses to L2).<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Global Miss Rate L2 = (Misses in L2) / (Total CPU Accesses) = (1 - H1) × (1 - H2_local)."
            ),
            "crucial_rule": "CRUCIAL RULE: The 3 C's of Cache Misses:<br/>1. <b>Compulsory (Cold) Miss:</b> First-time access to a block. Cannot be avoided by larger cache.<br/>2. <b>Capacity Miss:</b> Cache is full. Solved by increasing total cache size.<br/>3. <b>Conflict (Collision) Miss:</b> Multiple memory blocks map to the same set. Solved by increasing associativity (k)."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: Set-Associative Tag and Index Calculation",
            "problem": "A 32-bit byte-addressable processor has a 64 KB 4-way set-associative cache with 32-byte block size. Find: (1) Block offset bits, (2) Set index bits, and (3) Tag bits.",
            "steps": [
                "Step 1: Block size B = 32 Bytes = 2^5 Bytes ⇒ Block Offset b = 5 bits.",
                "Step 2: Total number of cache lines = Cache Size / Block Size = 64 KB / 32 B = (64 × 1024) / 32 = 2048 lines.",
                "Step 3: Number of sets S = Total Lines / k = 2048 / 4 = 512 sets = 2^9 sets ⇒ Set Index s = 9 bits.",
                "Step 4: Tag bits = Total Address bits - Set bits - Offset bits = 32 - 9 - 5 = 18 bits.",
                "Step 5: Address split is [Tag: 18 bits | Set Index: 9 bits | Block Offset: 5 bits]."
            ],
            "answer": "Offset = 5 bits, Set Index = 9 bits, Tag = 18 bits."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: Confusing Set Index Bits with Total Line Bits",
            "warning": "In k-way set associative caches, always divide total lines by k before taking log2! Taking log2 of total lines gives direct-mapped index bits, which destroys the tag calculation."
        }
    ]
}

# COA Chapter 3: Instruction Pipelining
CHAPTERS_COA_PDS_ALGO[("COA", 3)] = {
    "sub_id": "COA",
    "chap_idx": 3,
    "title": "Instruction Pipelining, Hazards & Performance",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The Commercial Laundromat Assembly Line (Pipelining Principle)",
            "text": "Imagine doing 4 loads of laundry. Each load requires: Washer (30 min), Dryer (40 min), Folding (20 min). If you do laundry sequentially, load 1 takes 90 min, load 2 takes 90 min... 4 loads take 360 min (6 hours!). But in a Pipelined laundromat: once load 1 enters the dryer, you immediately toss load 2 into the washer! The dryer is the bottleneck stage (40 min). After the initial filling phase, one fresh, clean, folded basket pops out every 40 minutes, boosting throughput by nearly 400%."
        },
        {
            "title": "Real-Life Example 2: The Chef Waiting for Chopped Garlic (RAW Data Hazard)",
            "text": "In a busy restaurant, Recipe 1 says: 'Mince garlic and saute in oil (produces browned garlic)'. Recipe 2 says: 'Mix browned garlic into the sauce'. If the junior chef starts Recipe 2 before Recipe 1 finishes browning the garlic, they dump raw garlic into the soup, ruining the dish! This is a Read-After-Write (RAW) data hazard. Operand Forwarding is the senior chef handing the sauteed garlic straight from their frying pan directly into Recipe 2's pot before it is even plated in the fridge."
        },
        {
            "title": "Real-Life Example 3: The Highway Fork in the Fog (Control Hazard & Branch Prediction)",
            "text": "You are driving at 120 km/h toward a highway fork hidden in dense fog. The GPS won't calculate whether to turn Left or Right until you are 50 meters away (Branch condition evaluation). If you come to a complete dead halt to wait for the GPS, you cause massive traffic stalls (Pipeline Stalls). Instead, you predict 'Keep going straight'. If correct, you maintain full speed. If wrong, you slam the brakes, reverse, and take the correct ramp (Pipeline Flush penalty)."
        }
    ],
    "foundations": [
        {
            "number": "12.1",
            "title": "Pipelining Metrics: Clock Cycle, Speedup, Throughput & Efficiency",
            "content": (
                "For a k-stage pipeline executing n instructions:<br/>"
                "• <b>Clock Cycle Time (T_pipe):</b> <b>T_pipe = max(t_i) + t_buffer_register</b> (governed by slowest stage).<br/>"
                "• <b>Non-pipelined execution time:</b> T_nonpipe = n × (∑ t_i).<br/>"
                "• <b>Pipelined execution time (Ideal, no stalls):</b> <b>T_pipe_total = (k + n - 1) × T_pipe</b>.<br/>"
                "• <b>Speedup (S):</b> S = T_nonpipe / T_pipe_total. As n → ∞, <b>Ideal Speedup S_max = k</b> (number of stages).<br/>"
                "• <b>Efficiency (η):</b> η = Speedup / k = n / (k + n - 1)."
            ),
            "crucial_rule": "CRUCIAL RULE: In real pipelines with clock buffer/register overhead, the pipeline cycle time MUST include the buffer delay: T_clk = max(stage_delays) + t_reg. Never forget the buffer register delay in numericals!"
        },
        {
            "number": "12.2",
            "title": "Pipeline Hazards: Structural, Data & Control",
            "content": (
                "• <b>Structural Hazard (Resource Conflict):</b> Multiple stages compete for the same physical hardware (e.g., single memory port for both instruction fetch and data operand load). Solved by separate Harvard L1 I-Cache and D-Cache.<br/>"
                "• <b>Data Hazards:</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;1. <b>RAW (Read After Write - True Dependency):</b> Instr J tries to read register before Instr I writes it. Solved by <b>Operand Forwarding (Bypassing)</b> or stalling.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;2. <b>WAR (Write After Read - Anti-dependency):</b> Cannot occur in standard in-order pipelines.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;3. <b>WAW (Write After Write - Output dependency):</b> Occurs in out-of-order execution.<br/>"
                "• <b>Control Hazard (Branch Hazard):</b> Branch outcome is evaluated in later stage (Decode or Execute). Stalls = Branch Penalty."
            ),
            "crucial_rule": "CRUCIAL RULE: CPI with stalls: <b>CPI_avg = 1 + (Stalls per instruction)</b>. Speedup with stalls: S = k / (1 + Stalls_avg)."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: Pipelined Speedup Calculation",
            "problem": "A 5-stage pipeline has stage delays of 150 ps, 120 ps, 180 ps, 160 ps, and 140 ps. Pipeline register delay is 20 ps. In a non-pipelined processor, total delay is the sum of stage delays with no register overhead. Find the speedup for executing 1000 independent instructions.",
            "steps": [
                "Step 1: Non-pipelined time per instruction: T_non = 150 + 120 + 180 + 160 + 140 = 750 ps.",
                "Step 2: Total time non-pipelined = 1000 × 750 ps = 750,000 ps.",
                "Step 3: Pipelined clock cycle T_clk = max(150, 120, 180, 160, 140) + 20 ps = 180 + 20 = 200 ps.",
                "Step 4: Clock cycles for 1000 instructions in 5-stage pipeline: Cycles = k + n - 1 = 5 + 1000 - 1 = 1004 cycles.",
                "Step 5: Total time pipelined = 1004 × 200 ps = 200,800 ps.",
                "Step 6: Speedup S = 750,000 ps / 200,800 ps ≈ 3.735."
            ],
            "answer": "Speedup = 3.74x."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: Forgetting RAW Hazard Even With Forwarding",
            "warning": "Operand forwarding DOES NOT eliminate stalls for a Load followed immediately by an ALU instruction (Load-Use Hazard)! Because data arrives from memory only at the end of the Memory (MEM) stage, a 1-cycle stall is STILL mandatory."
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
            "title": "Real-Life Example 1: Russian Matryoshka Nesting Dolls (Recursion & Call Stack)",
            "text": "Opening a nested Russian wooden doll is the physical embodiment of recursion. You open doll #4, which reveals doll #3, which reveals doll #2, down to the tiny solid doll #1 (Base Case). At doll #1, you stop opening and begin packing them back in reverse order: snap #1 into #2, #2 into #3, and #3 into #4. In a C program, every recursive function call pushes a stack frame onto the Call Stack; hitting the base case begins the unwind phase, returning values back up the stack."
        },
        {
            "title": "Real-Life Example 2: The GPS Coordinate Sticky Note (Pointers & Dereferencing)",
            "text": "Imagine your friend wants to borrow your laptop. Instead of hauling a heavy backpack to their house (Pass by Value: copying bytes), you hand them a tiny sticky note with your room address written on it (Pointer: `int *ptr = &laptop`). Your friend walks to that address and edits files directly on your screen (Dereferencing: `*ptr = 100`). Pass-by-reference is instantaneous and affects the master original variable."
        },
        {
            "title": "Real-Life Example 3: The Secret Vault Inside a Shared Hotel Room (Static Variables)",
            "text": "Normally, when a hotel guest checks out, housekeeping throws away all left-behind newspapers and resets the room (Automatic/Local variables destroyed upon function exit). But a `static` variable is like a heavy bolted floor safe: when the function exits, the safe remains completely untouched with its stored values intact. The next time the function is called, it reopens that same safe without re-initializing it."
        }
    ],
    "foundations": [
        {
            "number": "13.1",
            "title": "Pointers, Pointer Arithmetic & Array Equivalence",
            "content": (
                "• An array name `arr` decays to a constant pointer to its first element: `arr ≡ &arr[0]`.<br/>"
                "• <b>Pointer Arithmetic:</b> `ptr + i` adds `i × sizeof(*ptr)` bytes to the memory address.<br/>"
                "• <b>Subscript Rule:</b> `arr[i] ≡ *(arr + i) ≡ *(i + arr) ≡ i[arr]` (All mathematically identical in C!).<br/>"
                "• <b>2D Array Address Calculation (Row-Major):</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;For `arr[M][N]`, address of `arr[i][j]` = `Base + (i × N + j) × sizeof(element)`.<br/>"
                "• <b>Array of Pointers vs Pointer to Array:</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;`int *p[10];` -> Array of 10 integer pointers.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;`int (*p)[10];` -> Pointer to an array of 10 integers."
            ),
            "crucial_rule": "CRUCIAL RULE: `sizeof(arr)` gives the total byte size of the entire array, but when passed into a function as a parameter, `arr` decays to a pointer, so `sizeof(arr)` inside the function returns the pointer size (4 or 8 bytes)!"
        },
        {
            "number": "13.2",
            "title": "C Operator Precedence, Associativity & Evaluation Traps",
            "content": (
                "• <b>Highest Precedence:</b> Postfix `()` `[]` `->` `.` `++` `--` (Left to Right).<br/>"
                "• <b>Unary Operators:</b> Prefix `++` `--` `*` (deref) `&` `!` `~` `sizeof` (Right to Left associative!).<br/>"
                "• <b>Arithmetic:</b> `*` `/` `%` over `+` `-`.<br/>"
                "• <b>Relational & Equality:</b> `<` `<=` `>` `>=` over `==` `!=`.<br/>"
                "• <b>Bitwise:</b> `&` over `^` over `|`.<br/>"
                "• <b>Logical:</b> `&&` over `||` (Both use <b>Short-Circuit Evaluation</b>: if LHS determines outcome, RHS is NEVER executed!)."
            ),
            "crucial_rule": "CRUCIAL RULE: `*p++` evaluates as `*(p++)`: it dereferences pointer `p`, and increments the pointer address `p`. In contrast, `(*p)++` increments the VALUE pointed to by `p`!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: Tracing Static Recursion in C",
            "problem": "Determine the output of the following C code:\nint f(int n) {\n  static int r = 0;\n  if (n <= 0) return 1;\n  if (n > 3) {\n    r = n;\n    return f(n - 2) + 2;\n  }\n  return f(n - 1) + r;\n}\nint main() { printf(\"%d\", f(5)); return 0; }",
            "steps": [
                "Step 1: Call f(5): n=5 (>3) ⇒ static r = 5. Calls f(3) + 2.",
                "Step 2: Inside f(3): n=3 (not >3) ⇒ Calls f(2) + r.",
                "Step 3: Inside f(2): n=2 (not >3) ⇒ Calls f(1) + r.",
                "Step 4: Inside f(1): n=1 (not >3) ⇒ Calls f(0) + r.",
                "Step 5: Inside f(0): n=0 (<=0) ⇒ Hits base case, returns 1.",
                "Step 6: Unwind f(1): returns f(0) + r = 1 + 5 = 6.",
                "Step 7: Unwind f(2): returns f(1) + r = 6 + 5 = 11.",
                "Step 8: Unwind f(3): returns f(2) + r = 11 + 5 = 16.",
                "Step 9: Unwind f(5): returns f(3) + 2 = 16 + 2 = 18."
            ],
            "answer": "Console Output = 18."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: Modifying Variables Multiple Times Between Sequence Points",
            "warning": "Code like `printf(\"%d %d\", i++, ++i);` or `a[i] = i++;` causes Undefined Behavior in C! GATE often includes these in options as 'Undefined / Compiler Dependent'."
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
            "title": "Real-Life Example 1: The Browser 'Back' Button vs Printer Job Queue",
            "text": "When you browse the web, every page you visit is pushed onto a Stack (LIFO: Last-In, First-Out). Hitting 'Back' pops the most recent page immediately. Conversely, when 10 office workers send documents to a shared network printer, documents print in the exact arrival order from a Queue (FIFO: First-In, First-Out). You would be furious if a printer acted like a stack, printing the newest document first and ignoring your 20-page report sent an hour ago!"
        },
        {
            "title": "Real-Life Example 2: The Scavenger Hunt Train Cars (Linked List vs Array)",
            "text": "An Array is like a row of 10 adjacent hotel lockers: instant access by locker index O(1), but impossible to expand if the locker next door is occupied by someone else. A Linked List is like a treasure hunt where each participant holds a piece of paper pointing to the GPS coordinate of the next friend. Inserting a new friend into the middle requires zero shifting of other people: simply update two coordinate slips in O(1) time."
        },
        {
            "title": "Real-Life Example 3: The Circular Sushi Conveyor Belt (Circular Queue)",
            "text": "In a linear queue, when customers leave the front, empty seats open up, but you can't seat new diners if the rear pointer hit the end of the counter. A Circular Queue wraps the rear pointer back to seat #0 using modulo arithmetic `(rear + 1) % Capacity`. The sushi conveyor belt loops endlessly, achieving 100% capacity utilization."
        }
    ],
    "foundations": [
        {
            "number": "14.1",
            "title": "Stack Applications: Infix to Postfix & Evaluation Mechanics",
            "content": (
                "• <b>Infix to Postfix Conversion Rules:</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;1. Operands are output immediately.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;2. '(' has highest incoming precedence, lowest in-stack precedence.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;3. Pop operators from stack to output while in-stack operator precedence ≥ incoming operator precedence.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;4. ')' pops everything until '(' is discarded.<br/>"
                "• <b>Postfix Evaluation:</b> Scan left-to-right. Push operands onto stack. On operator, pop two operands (op2 = pop(), op1 = pop()), evaluate `op1 op op2`, and push result back."
            ),
            "crucial_rule": "CRUCIAL RULE: In postfix evaluation, the first popped element is operand 2 (the right-hand side operand)! For non-commutative operations like subtraction or division: result = op1 - op2 (or op1 / op2)."
        },
        {
            "number": "14.2",
            "title": "Queue Implementations & Circular Queue Boundary Conditions",
            "content": (
                "• <b>Circular Queue using Array of size N:</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Enqueue: `rear = (rear + 1) % N; queue[rear] = item;`<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Dequeue: `front = (front + 1) % N; item = queue[front];`<br/>"
                "• <b>Full Condition (sacrificing 1 slot):</b> `(rear + 1) % N == front`.<br/>"
                "• <b>Empty Condition:</b> `front == rear`.<br/>"
                "• Maximum elements stored = <b>N - 1</b> (one slot kept empty to distinguish full from empty)."
            ),
            "crucial_rule": "CRUCIAL RULE: Minimum number of Stacks needed to implement a Queue is <b>2</b>. Minimum Queues needed to implement a Stack is also <b>2</b>."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: Evaluating Postfix Expression",
            "problem": "Evaluate the postfix expression: `10 5 + 60 6 / * 8 -` using a stack.",
            "steps": [
                "Step 1: Push 10, Push 5. Stack = [10, 5].",
                "Step 2: Encounter '+': op2 = 5, op1 = 10 ⇒ 10 + 5 = 15. Push 15. Stack = [15].",
                "Step 3: Push 60, Push 6. Stack = [15, 60, 6].",
                "Step 4: Encounter '/': op2 = 6, op1 = 60 ⇒ 60 / 6 = 10. Push 10. Stack = [15, 10].",
                "Step 5: Encounter '*': op2 = 10, op1 = 15 ⇒ 15 * 10 = 150. Push 150. Stack = [150].",
                "Step 6: Push 8. Stack = [150, 8].",
                "Step 7: Encounter '-': op2 = 8, op1 = 150 ⇒ 150 - 8 = 142. Push 142. Stack = [142]."
            ],
            "answer": "Final Result = 142."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: Reversing Linked List Pointers",
            "warning": "When reversing a singly linked list in-place, you need THREE pointers: `prev`, `curr`, `next`. Forgetting to save `curr->next` before reassigning `curr->next = prev` permanently severs and loses the rest of the list!"
        }
    ]
}

# PDS Chapter 2: Trees, BST & Heaps
CHAPTERS_COA_PDS_ALGO[("PDS", 2)] = {
    "sub_id": "PDS",
    "chap_idx": 2,
    "title": "Trees, BST & Binary Heaps",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The Corporate CEO Hierarchy & Dictionary Search (BST)",
            "text": "In a well-organized company directory, names are sorted. Looking up an employee doesn't require checking 1,000 cubicles one by one. You walk to the middle manager: if the employee's name comes earlier alphabetically, you go left; if later, you go right. In a Binary Search Tree (BST), this eliminates half the remaining candidates with every step, locating any person among 1,000,000 employees in just 20 comparisons (log2(1,000,000) ≈ 20)."
        },
        {
            "title": "Real-Life Example 2: The Hospital Emergency Triage (Priority Queue & Binary Heap)",
            "text": "In a hospital emergency room, patients don't get treated by arrival order (FIFO Queue). A patient with a paper cut who arrived at 8:00 AM waits, while a gunshot victim who arrives at 8:30 AM is rushed to surgery immediately. A Max-Heap acts as an automated triage: the highest priority patient is ALWAYS sitting at the root (index 0). Popping the top patient and re-adjusting the pyramid takes O(log n) time."
        },
        {
            "title": "Real-Life Example 3: The Perfectly Balanced Mobile Hanging Mobile (AVL Tree)",
            "text": "Imagine hanging a decorative baby mobile from the ceiling. If you hang 5 heavy toys on the right branch and none on the left, the mobile tips over and crashes (Skewed BST: O(n) search time). An AVL Tree measures the balance factor (Height_left - Height_right) after every insertion. If the balance factor deviates beyond {-1, 0, +1}, it performs a smooth rotation (LL, RR, LR, RL) to restore perfect balance in O(1) time."
        }
    ],
    "foundations": [
        {
            "number": "15.1",
            "title": "Binary Tree Properties, Traversal Invariants & Reconstruction",
            "content": (
                "• <b>Number of Leaf Nodes:</b> In any binary tree where every node has 0 or 2 children (Strict Binary Tree): <b>L = I + 1</b> (Leaf nodes = Internal nodes + 1).<br/>"
                "• <b>Max Nodes in Binary Tree of height h (root at h=0):</b> 2^(h+1) - 1.<br/>"
                "• <b>In-order Traversal Invariant:</b> In a Binary Search Tree (BST), In-order traversal (Left, Root, Right) ALWAYS yields keys in <b>STRICTLY ASCENDING SORTED ORDER</b>.<br/>"
                "• <b>Tree Reconstruction:</b> A unique binary tree can be constructed if and only if <b>IN-ORDER traversal is provided along with either PRE-ORDER or POST-ORDER</b>."
            ),
            "crucial_rule": "CRUCIAL RULE: Given only Pre-order and Post-order traversals, a unique binary tree CANNOT be determined unless the tree is strictly Full (every node has either 0 or 2 children)."
        },
        {
            "number": "15.2",
            "title": "Binary Heaps & Priority Queues",
            "content": (
                "A Binary Heap is a <b>Complete Binary Tree</b> stored as a flat array where for index i (1-based):<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Parent = ⌊i/2⌋, Left Child = 2i, Right Child = 2i + 1.<br/>"
                "• <b>Max-Heap Property:</b> Key(parent) ≥ Key(children). Root holds maximum key.<br/>"
                "• <b>Min-Heap Property:</b> Key(parent) ≤ Key(children). Root holds minimum key.<br/>"
                "• <b>Building a Heap (Build-Heap):</b> Takes <b>O(n) time</b> (NOT O(n log n)!) using bottom-up sift-down.<br/>"
                "• Insert key: O(log n) | Extract Min/Max: O(log n) | Peek: O(1)."
            ),
            "crucial_rule": "CRUCIAL RULE: In a Min-Heap with n elements, where is the MAXIMUM element located? It MUST be in one of the LEAF nodes! Leaf nodes occupy indices ⌊n/2⌋ + 1 to n (taking O(n) time to find)."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: BST Reconstruction from Pre-order",
            "problem": "Given Pre-order traversal of a BST: [40, 20, 10, 30, 60, 50, 70]. What is its Post-order traversal?",
            "steps": [
                "Step 1: For a BST, In-order traversal is simply the keys sorted in ascending order: In-order = [10, 20, 30, 40, 50, 60, 70].",
                "Step 2: Pre-order first element is root: Root = 40.",
                "Step 3: In In-order, elements before 40 are Left Subtree: [10, 20, 30]. Elements after 40 are Right Subtree: [50, 60, 70].",
                "Step 4: Left Subtree root = 20 (from pre-order). Its left child = 10, right child = 30.",
                "Step 5: Right Subtree root = 60. Its left child = 50, right child = 70.",
                "Step 6: Post-order traversal (Left, Right, Root):",
                "&nbsp;&nbsp;&nbsp;&nbsp;Left subtree post-order: 10, 30, 20.",
                "&nbsp;&nbsp;&nbsp;&nbsp;Right subtree post-order: 50, 70, 60.",
                "&nbsp;&nbsp;&nbsp;&nbsp;Append Root: 10, 30, 20, 50, 70, 60, 40."
            ],
            "answer": "Post-order Traversal: [10, 30, 20, 50, 70, 60, 40]."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: Counting Structural Binary Trees",
            "warning": "Number of structurally distinct binary trees with n unlabeled nodes is given by the Catalan Number: C_n = (1 / (n + 1)) × C(2n, n). For n=3, C_3 = 5 trees. If keys are labeled, total distinct BSTs = C_n × n!."
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
    "title": "Asymptotic Analysis & Recurrence Relations",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The Flash Drive vs Carrier Pigeon (Big-O Scaling)",
            "text": "Suppose you need to send 10 Terabytes of video footage across the city. Over an internet cable with bandwidth 10 MB/s, transfer time scales linearly with data size: O(n) takes 12 days! But if you strap a 10 TB SSD to a homing pigeon and let it fly, flight time is strictly constant: O(1) takes 45 minutes regardless of whether the SSD holds 1 Megabyte or 50 Terabytes. As n grows toward infinity, the O(1) pigeon utterly annihilates the O(n) broadband."
        },
        {
            "title": "Real-Life Example 2: The Corporate Task Delegation Hierarchy (Master Theorem)",
            "text": "A CEO gets a massive project. In each phase, the CEO splits the work into 'a' sub-problems, each of size (n/b). The middle managers delegate further down the corporate pyramid until low-level interns finish base tasks. The Master Theorem compares the total work done at the leaf-level intern army (n^(log_b a)) versus the administrative overhead work done by upper management (f(n)). Whichever level dominates dictates the running time of the entire company."
        },
        {
            "title": "Real-Life Example 3: The Tower of Hanoi Legend (Exponential Complexity)",
            "text": "Ancient monks in a temple were tasked with moving 64 golden disks between three pegs without ever placing a larger disk on a smaller one. The recurrence relation is T(n) = 2T(n-1) + 1 = 2^n - 1 moves. For 64 disks, 2^64 - 1 moves at 1 move per second takes 584 BILLION years (longer than the age of the universe!). Exponential time O(2^n) algorithms are completely intractable for real computation."
        }
    ],
    "foundations": [
        {
            "number": "16.1",
            "title": "Asymptotic Notations: Big-O, Big-Omega, Big-Theta, Little-o, Little-omega",
            "content": (
                "• <b>Big-O (O):</b> Asymptotic Upper Bound. f(n) = O(g(n)) iff ∃ c > 0, n0 > 0 such that 0 ≤ f(n) ≤ c · g(n) for all n ≥ n0.<br/>"
                "• <b>Big-Omega (Ω):</b> Asymptotic Lower Bound. f(n) = Ω(g(n)) iff ∃ c > 0, n0 > 0 such that 0 ≤ c · g(n) ≤ f(n) for all n ≥ n0.<br/>"
                "• <b>Big-Theta (Θ):</b> Asymptotically Tight Bound. f(n) = Θ(g(n)) iff f(n) = O(g(n)) AND f(n) = Ω(g(n)).<br/>"
                "• <b>Standard Growth Ordering:</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;1 < log(log n) < log n < (log n)^k < √n < n < n log n < n^2 < n^3 < 2^n < 3^n < n! < n^n."
            ),
            "crucial_rule": "CRUCIAL RULE: 2^(2^n) grows faster than (2^n)!. And (log n)! grows asymptotically as n^(log log n), which is super-polynomial but sub-exponential."
        },
        {
            "number": "16.2",
            "title": "Master Theorem for Divide-and-Conquer Recurrences",
            "content": (
                "For recurrence: <b>T(n) = a T(n/b) + f(n)</b> where a ≥ 1, b > 1:<br/>"
                "Compute critical exponent <b>p = log_b(a)</b>:<br/>"
                "• <b>Case 1:</b> If f(n) = O(n^(p - ε)) for ε > 0 ⇒ <b>T(n) = Θ(n^p)</b> (Leaf-heavy).<br/>"
                "• <b>Case 2:</b> If f(n) = Θ(n^p · log^k(n)) for k ≥ 0 ⇒ <b>T(n) = Θ(n^p · log^(k+1)(n))</b> (Balanced).<br/>"
                "• <b>Case 3:</b> If f(n) = Ω(n^(p + ε)) for ε > 0 AND regularity condition a·f(n/b) ≤ c·f(n) holds ⇒ <b>T(n) = Θ(f(n))</b> (Root-heavy)."
            ),
            "crucial_rule": "CRUCIAL RULE: Master theorem FAILS when b is not constant (e.g. T(n) = 2T(√n) + log n), when a is not constant, or when f(n) falls into non-polynomial gaps like f(n) = n^p / log n."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: Solving Non-Standard Recurrence via Substitution",
            "problem": "Solve recurrence: T(n) = 2 T(√n) + log2(n), with base case T(2) = 1.",
            "steps": [
                "Step 1: Set n = 2^m ⇒ m = log2(n). Then √n = 2^(m/2).",
                "Step 2: Rewrite recurrence in terms of m: T(2^m) = 2 T(2^(m/2)) + m.",
                "Step 3: Define S(m) = T(2^m). Then S(m) = 2 S(m/2) + m.",
                "Step 4: Now S(m) is in standard Master Theorem form: a = 2, b = 2, f(m) = m.",
                "Step 5: Critical exponent p = log_2(2) = 1. Since f(m) = Θ(m^1), this is Case 2 (k=0).",
                "Step 6: S(m) = Θ(m · log2(m)).",
                "Step 7: Substitute back m = log2(n): T(n) = Θ(log2(n) · log2(log2(n)))."
            ],
            "answer": "T(n) = Θ(log n · log log n)."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: Mistaking log(n!) for O(n^n)",
            "warning": "By Stirling's approximation, log(n!) = Θ(n log n), NOT Θ(n^2) or Θ(2^n)! This appears almost every alternate year in GATE asymptotic ordering questions."
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
            "title": "Real-Life Example 1: The Postal Mail Sorting Cubbyholes (Bucket / Radix Sort)",
            "text": "A postal worker sorting 1,000,000 letters with 6-digit PIN codes doesn't compare letters against each other using QuickSort (which takes 20 million comparisons!). Instead, they toss letters into 10 physical bins based on the last digit (0 to 9), collect them, and repeat for the 10s digit, up to the 100,000s digit. In just 6 passes over the letters, all 1,000,000 letters are perfectly sorted in linear O(n) time."
        },
        {
            "title": "Real-Life Example 2: The Card Player's Worst Nightmare (QuickSort Worst Case)",
            "text": "When playing cards, QuickSort picks a 'pivot' and partitions cards smaller to the left and larger to the right. If the deck is ALREADY sorted and the algorithm foolishly picks the first card as pivot, the left partition is empty (0 cards) and the right partition has n-1 cards. Instead of splitting in half, the tree becomes a single stick of depth n, degenerating to disastrous O(n²) time. Picking a randomized or median-of-three pivot prevents this trap."
        },
        {
            "title": "Real-Life Example 3: The Highway Exit Ramp Collision (Hash Collisions & Clustering)",
            "text": "A hash table is like assigning parking spaces based on license plate numbers modulo 100. If two cars get assigned Spot 24, Linear Probing parks the second car in Spot 25. If Spot 25 is occupied, it checks 26, then 27. This creates massive traffic jams where occupied spots clump together (Primary Clustering), making search times degrade. Separate Chaining parks collisions in an elevator stack at Spot 24, avoiding adjacent clutter."
        }
    ],
    "foundations": [
        {
            "number": "17.1",
            "title": "Comparison-Based Sorting Lower Bound & Stability",
            "content": (
                "• <b>Theoretical Lower Bound:</b> Any comparison-based sorting algorithm requires at least <b>Ω(n log n)</b> comparisons in the worst case (proven by decision tree height: h ≥ ⌈log2(n!)⌉ ≈ n log2(n) - 1.44n).<br/>"
                "• <b>Stable Sorting Algorithms:</b> Preserves the relative order of records with equal keys. Examples: <b>Merge Sort, Insertion Sort, Bubble Sort, Radix Sort</b>.<br/>"
                "• <b>Unstable Sorting Algorithms:</b> <b>QuickSort, HeapSort, Selection Sort</b>.<br/>"
                "• <b>In-Place Sorting:</b> Requires O(1) auxiliary memory. Examples: HeapSort, Insertion Sort, Selection Sort. (MergeSort requires O(n) extra space!)."
            ),
            "crucial_rule": "CRUCIAL RULE: HeapSort is guaranteed O(n log n) in best, average, and worst cases, and is In-Place O(1) space, but it is UNSTABLE and suffers from poor cache locality compared to QuickSort."
        },
        {
            "number": "17.2",
            "title": "Hashing, Collision Resolution & Probing Formulas",
            "content": (
                "• <b>Load Factor (α):</b> α = n / m (n elements, m slots).<br/>"
                "• <b>Separate Chaining:</b> Average search time = Θ(1 + α).<br/>"
                "• <b>Open Addressing:</b> Requires α ≤ 1. No pointers stored.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;1. <b>Linear Probing:</b> h(k, i) = (h'(k) + i) mod m. Suffers from <b>Primary Clustering</b>.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;2. <b>Quadratic Probing:</b> h(k, i) = (h'(k) + c1·i + c2·i²) mod m. Eliminates primary clustering, but suffers from <b>Secondary Clustering</b>.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;3. <b>Double Hashing:</b> h(k, i) = (h1(k) + i · h2(k)) mod m. Eliminates both primary and secondary clustering."
            ),
            "crucial_rule": "CRUCIAL RULE: In Double Hashing, h2(k) MUST be relatively prime to hash table size m (e.g. m is prime and h2(k) < m) so that every slot in the table can be probed without infinite cycling."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: Linear Probing Sequence",
            "problem": "Insert keys [25, 42, 96, 101, 102, 162] into a hash table of size m = 11 using hash function h(k) = k mod 11 and Linear Probing. Find the slot where key 162 is stored.",
            "steps": [
                "Step 1: Table has slots 0 to 10 (all empty).",
                "Step 2: 25 mod 11 = 3 ⇒ Slot 3. (Slots occupied: {3: 25})",
                "Step 3: 42 mod 11 = 9 ⇒ Slot 9. (Occupied: {3: 25, 9: 42})",
                "Step 4: 96 mod 11 = 8 ⇒ Slot 8. (Occupied: {3: 25, 8: 96, 9: 42})",
                "Step 5: 101 mod 11 = 2 ⇒ Slot 2. (Occupied: {2: 101, 3: 25, 8: 96, 9: 42})",
                "Step 6: 102 mod 11 = 3 (Collision at 3). Probing: slot 4 is free ⇒ Slot 4. (Occupied: {2: 101, 3: 25, 4: 102, 8: 96, 9: 42})",
                "Step 7: 162 mod 11 = 8 (Collision at 8). Probes: Slot 8 (occupied), Slot 9 (occupied), Slot 10 (free!) ⇒ Slot 10."
            ],
            "answer": "Key 162 is stored in Slot 10."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: QuickSort Average vs Worst Case",
            "warning": "The worst case of QuickSort is O(n²) when the array is already sorted and pivot is extreme. But its AVERAGE case is strictly O(n log n). If an exam question asks 'Worst case running time of QuickSort', the answer is strictly Θ(n²)."
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
            "title": "Real-Life Example 1: The ATM Cash Dispenser (Greedy Choice Property)",
            "text": "When you withdraw ₹3,800 from an Indian ATM, the machine dispenses: ₹2000 (1 note), ₹500 (3 notes), ₹200 (1 note), ₹100 (1 note). It greedily grabs the largest banknote possible at each step. In standard currency denominations, this Greedy approach guarantees the absolute minimum number of notes. However, if currency denominations were {₹1, ₹7, ₹10} and you wanted ₹14, Greedy picks ₹10 + ₹1 + ₹1 + ₹1 + ₹1 (5 notes), whereas Dynamic Programming picks ₹7 + ₹7 (just 2 notes!)."
        },
        {
            "title": "Real-Life Example 2: The Fibonacci Scratchpad (Dynamic Programming Memoization)",
            "text": "Computing Fibonacci(50) naively branches into two sub-calls: Fib(49) and Fib(48). Those branch into four, then eight... computing 2^50 operations (thousands of years). But a smart student keeps a small scratchpad on their desk. When Fib(3) is calculated once, they write down '2'. Any future call asking for Fib(3) instantly looks up the scratchpad in O(1) time. Dynamic Programming turns an impossible exponential O(2^n) explosion into a 50-step linear O(n) breeze."
        },
        {
            "title": "Real-Life Example 3: The Aircraft Luggage Weight Allowance (0/1 vs Fractional Knapsack)",
            "text": "An airline allows a 20 kg carry-on bag. A thief in a gold vault has solid gold bars and liquid gold dust. For liquid gold dust, they can scoop fractions (Fractional Knapsack: solved greedily by sorting value/weight ratio in O(n log n)). For solid indivisible diamond statues, they cannot chop a statue in half (0/1 Knapsack: Greedy FAILS, requires Dynamic Programming in O(n·W) pseudo-polynomial time)."
        }
    ],
    "foundations": [
        {
            "number": "18.1",
            "title": "Greedy Strategy: Optimal Substructure & Greedy Choice Property",
            "content": (
                "A problem exhibits Greedy Choice if a locally optimal choice leads to a globally optimal solution.<br/>"
                "• <b>Fractional Knapsack:</b> Greedy on Value/Weight ratio is optimal. Time: O(n log n).<br/>"
                "• <b>Activity Selection / Interval Scheduling:</b> Sort activities by <b>EARLIEST FINISH TIME</b>. Always pick the next compatible activity with minimum finish time. Time: O(n log n).<br/>"
                "• <b>Huffman Coding:</b> Greedy prefix code tree using Min-Heap. Always merges the two lowest-frequency trees. Time: O(n log n).<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Prefix Property: No character code is a prefix of any other code, ensuring unambiguous decoding."
            ),
            "crucial_rule": "CRUCIAL RULE: In Huffman coding with n distinct characters, the generated Huffman tree is ALWAYS a STRICT (FULL) BINARY TREE containing exactly <b>2n - 1 total nodes</b> (n leaf nodes and n - 1 internal nodes)."
        },
        {
            "number": "18.2",
            "title": "Dynamic Programming: Overlapping Subproblems & Matrix Chain Multiplication",
            "content": (
                "• <b>0/1 Knapsack Recurrence:</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;DP[i][w] = DP[i-1][w] (if wt[i] > w)<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;DP[i][w] = max(DP[i-1][w], val[i] + DP[i-1][w - wt[i]]) (otherwise).<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Time Complexity: O(n × W) (Pseudo-polynomial).<br/>"
                "• <b>Matrix Chain Multiplication (MCM):</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;To multiply chain of matrices A1 × A2 × ... × An with dimensions d0 × d1 × ... × dn.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;M[i, j] = min_{i ≤ k < j} { M[i, k] + M[k+1, j] + di-1 · dk · dj }.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Time Complexity: O(n³) | Space: O(n²)."
            ),
            "crucial_rule": "CRUCIAL RULE: Longest Common Subsequence (LCS) of strings X[1..m] and Y[1..n]: If X[i] == Y[j], LCS = 1 + DP[i-1][j-1]. If X[i] != Y[j], LCS = max(DP[i-1][j], DP[i][j-1]). Time: O(m × n)."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: Matrix Chain Multiplication Operations",
            "problem": "Find the minimum number of scalar multiplications required to multiply three matrices A1(10 × 30), A2(30 × 5), and A3(5 × 60).",
            "steps": [
                "Step 1: Dimensions: d0 = 10, d1 = 30, d2 = 5, d3 = 60.",
                "Step 2: There are only two possible parenthesizations: (A1 × A2) × A3 OR A1 × (A2 × A3).",
                "Step 3: Option 1: ((A1 × A2) × A3):",
                "&nbsp;&nbsp;&nbsp;&nbsp;Multiplying A1(10×30) and A2(30×5) takes 10 × 30 × 5 = 1,500 multiplications, resulting in matrix of size (10×5).",
                "&nbsp;&nbsp;&nbsp;&nbsp;Multiplying (A1A2)(10×5) with A3(5×60) takes 10 × 5 × 60 = 3,000 multiplications.",
                "&nbsp;&nbsp;&nbsp;&nbsp;Total Option 1 = 1,500 + 3,000 = 4,500 multiplications.",
                "Step 4: Option 2: (A1 × (A2 × A3)):",
                "&nbsp;&nbsp;&nbsp;&nbsp;Multiplying A2(30×5) and A3(5×60) takes 30 × 5 × 60 = 9,000 multiplications, resulting in (30×60).",
                "&nbsp;&nbsp;&nbsp;&nbsp;Multiplying A1(10×30) with (A2A3)(30×60) takes 10 × 30 × 60 = 18,000 multiplications.",
                "&nbsp;&nbsp;&nbsp;&nbsp;Total Option 2 = 9,000 + 18,000 = 27,000 multiplications.",
                "Step 5: Minimum = min(4500, 27000) = 4,500."
            ],
            "answer": "Minimum scalar multiplications = 4,500 with parenthesization ((A1 A2) A3)."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: 0/1 Knapsack is NP-Complete",
            "warning": "The O(n·W) DP solution for 0/1 Knapsack is PSEUDO-POLYNOMIAL because W is represented in log2(W) bits. As W grows exponentially with input size, the algorithm is not polynomial. 0/1 Knapsack is strictly NP-Complete!"
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
            "title": "Real-Life Example 1: The Fiber-Optic Broadband Grid (Minimum Spanning Tree)",
            "text": "A telecom giant wants to connect 100 cities with high-speed fiber-optic cables so every city can communicate with any other city. Laying cables across mountains and rivers costs millions per kilometer. Kruskal's algorithm behaves like an ultra-frugal accountant: it sorts all proposed cable segments by cost, laying down the cheapest cable anywhere in the country first, as long as it doesn't create a useless redundant loop (cycle checked via Disjoint Set Union). It guarantees the cheapest possible total network cost."
        },
        {
            "title": "Real-Life Example 2: Google Maps Turn-by-Turn GPS Navigation (Dijkstra's Algorithm)",
            "text": "When driving home during rush hour, Google Maps uses Dijkstra's algorithm. It sets your current location as distance 0 and all other intersections as infinity. It explores outward like an expanding water ripple, visiting the nearest reachable intersection next. Because road travel times are strictly positive, the moment Dijkstra locks in an intersection, it has permanently found the guaranteed shortest travel time to that corner."
        },
        {
            "title": "Real-Life Example 3: The Currency Arbitrage Loophole (Bellman-Ford & Negative Cycles)",
            "text": "In currency trading, converting 1 USD -> 0.90 EUR -> 140 JPY -> 1.02 USD creates free money (Arbitrage). Taking the negative logarithm of exchange rates turns multiplication into addition of edge weights: an arbitrage opportunity becomes a Negative Weight Cycle! Dijkstra's algorithm breaks down completely with negative weights. Bellman-Ford runs for V - 1 relaxing passes: if edge distances can STILL decrease on pass V, an infinite money-printing negative cycle is detected."
        }
    ],
    "foundations": [
        {
            "number": "19.1",
            "title": "Graph Traversals: BFS, DFS & Applications",
            "content": (
                "• <b>Breadth-First Search (BFS):</b> Uses a <b>Queue</b> (FIFO). Explores nodes level by level.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Finds shortest path in <b>unweighted graphs</b>. Detects bipartite graphs. Time: O(V + E).<br/>"
                "• <b>Depth-First Search (DFS):</b> Uses a <b>Stack</b> (or recursion). Explores down each branch fully.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;<b>Edge Classification:</b> Tree edges, Back edges, Forward edges, Cross edges.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• A directed graph has a cycle iff DFS detects at least one <b>BACK EDGE</b>.<br/>"
                "• <b>Topological Sorting:</b> Linear ordering of vertices in Directed Acyclic Graphs (DAG) such that for every directed edge u → v, u comes before v. Time: O(V + E)."
            ),
            "crucial_rule": "CRUCIAL RULE: Topological sorting is possible IF AND ONLY IF the graph is a Directed Acyclic Graph (DAG). If a graph has even one cycle, topological sorting is IMPOSSIBLE!"
        },
        {
            "number": "19.2",
            "title": "Minimum Spanning Tree (MST): Kruskal's vs Prim's",
            "content": (
                "An MST connects all V vertices with V - 1 edges while minimizing total weight.<br/>"
                "• <b>Kruskal's Algorithm:</b> Edge-based greedy. Sorts all edges by weight, adds edge if it does not form a cycle (using Disjoint Set Union with path compression). Time: <b>O(E log E) = O(E log V)</b>.<br/>"
                "• <b>Prim's Algorithm:</b> Vertex-based greedy. Grows a single tree from a starting vertex by picking the minimum weight cut-edge. Uses Min-Heap. Time: <b>O(E log V)</b> (or O(E + V log V) with Fibonacci heap).<br/>"
                "• <b>Cut Property:</b> For any cut in graph, the lightest edge crossing the cut MUST belong to the MST."
            ),
            "crucial_rule": "CRUCIAL RULE: If all edge weights in a connected graph are strictly UNIQUE, the Minimum Spanning Tree is GUARANTEED TO BE UNIQUE!"
        },
        {
            "number": "19.3",
            "title": "Shortest Path Algorithms: Dijkstra, Bellman-Ford & Floyd-Warshall",
            "content": (
                "• <b>Dijkstra's Algorithm:</b> Single-source shortest path for <b>NON-NEGATIVE edge weights</b>. Greedy. Time: O((V + E) log V) with binary heap.<br/>"
                "• <b>Bellman-Ford Algorithm:</b> Handles <b>NEGATIVE edge weights</b>. Dynamic Programming. Relaxes all E edges V - 1 times. Detects negative cycles on the V-th pass. Time: <b>O(V × E)</b>.<br/>"
                "• <b>Floyd-Warshall Algorithm:</b> All-Pairs Shortest Path. DP using intermediate vertices: D[i][j] = min(D[i][j], D[i][k] + D[k][j]). Time: <b>O(V³)</b> | Space: O(V²)."
            ),
            "crucial_rule": "CRUCIAL RULE: Dijkstra CANNOT work with negative weight edges, even if there are no negative cycles! A single negative edge can invalidate Dijkstra's greedy finalization step."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: Dijkstra Algorithm Execution Trace",
            "problem": "Given directed graph with edges: (A→B, 4), (A→C, 2), (B→C, 1), (B→D, 5), (C→B, 1), (C→D, 8), (C→E, 10), (D→E, 2). Find the shortest path distance from source A to all vertices.",
            "steps": [
                "Step 1: Initialize distances: dist[A]=0, dist[B]=∞, dist[C]=∞, dist[D]=∞, dist[E]=∞. Visited = {}.",
                "Step 2: Pick minimum unvisited vertex A (dist=0). Relax outgoing edges:<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;A→B (4): dist[B] = min(∞, 0+4) = 4.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;A→C (2): dist[C] = min(∞, 0+2) = 2. Visited = {A}.",
                "Step 3: Pick minimum unvisited vertex C (dist=2). Relax outgoing edges:<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;C→B (1): dist[B] = min(4, 2+1) = 3 (Updated!).<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;C→D (8): dist[D] = min(∞, 2+8) = 10.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;C→E (10): dist[E] = min(∞, 2+10) = 12. Visited = {A, C}.",
                "Step 4: Pick minimum unvisited vertex B (dist=3). Relax outgoing edges:<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;B→D (5): dist[D] = min(10, 3+5) = 8 (Updated!). Visited = {A, C, B}.",
                "Step 5: Pick minimum unvisited vertex D (dist=8). Relax outgoing edges:<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;D→E (2): dist[E] = min(12, 8+2) = 10 (Updated!). Visited = {A, C, B, D}.",
                "Step 6: Pick E (dist=10). All vertices visited."
            ],
            "answer": "Shortest Distances from A: A=0, B=3, C=2, D=8, E=10."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: Adding a Constant to All Edges to Eliminate Negative Weights",
            "warning": "You CANNOT make negative edge weights positive for Dijkstra by adding a large constant C to every edge! Paths with more edges get penalized more heavily by C × (edge_count), changing the true shortest path completely!"
        }
    ]
}
