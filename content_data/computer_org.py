# Computer Organization & Architecture Content Module for GATE 2027 CSE
# Weightage: 8-10 Marks

SUBJECT_META = {
    "id": "COA",
    "name": "Computer Organization and Architecture",
    "folder": "03_Computer_Organization",
    "weightage": "9 Marks",
    "topics": [
        "Machine instructions and addressing modes",
        "Design of ALU, datapath, and control unit (hardwired and microprogrammed)",
        "Memory interfacing and hierarchy: performance, cache memory mapping",
        "I/O interface: interrupt and DMA mode",
        "Instruction pipelining, pipeline hazards, branch penalty and speedup"
    ]
}

CHAPTERS = [
    {
        "title": "Machine Instructions & Addressing Modes",
        "hinglish": "Addressing modes se numericals me Effective Address (EA) calculate karne ke questions aate hain. Direct, Indirect, Indexed, aur Relative addressing modes sabse zyada important hain.",
        "theory": (
            "<b>1. Machine Instructions & Instruction Formats:</b><br/>"
            "• An instruction consists of Opcode (operation to perform) and Operands/Addresses.<br/>"
            "• <b>3-Address:</b> Opcode R1, R2, R3 (R1 <- R2 op R3). Compact code, large instruction size.<br/>"
            "• <b>2-Address:</b> Opcode R1, R2 (R1 <- R1 op R2). Destructive read/overwrite.<br/>"
            "• <b>1-Address:</b> Opcode Address (Implicit Accumulator AC <- AC op M[Address]).<br/>"
            "• <b>0-Address:</b> Opcode (Implicit Stack: TOS <- TOS op SOS, e.g. ADD pops two operands and pushes result).<br/><br/>"
            "<b>2. Common Addressing Modes & Effective Address (EA):</b><br/>"
            "• <b>Immediate:</b> Operand is part of instruction itself (no memory reference). Example: MOV R1, #5.<br/>"
            "• <b>Direct (Absolute):</b> EA = Address field of instruction (1 memory access).<br/>"
            "• <b>Indirect:</b> EA = M[Address field] (2 memory accesses). Useful for pointers.<br/>"
            "• <b>Register Direct:</b> Operand is in register Ri (0 memory access).<br/>"
            "• <b>Register Indirect:</b> EA = Contents of register Ri (1 memory access).<br/>"
            "• <b>PC-Relative:</b> EA = PC + Offset. Crucial for position-independent branch instructions.<br/>"
            "• <b>Base Register:</b> EA = Base Register + Offset. Facilitates program relocation in memory.<br/>"
            "• <b>Indexed Addressing:</b> EA = Index Register + Constant. Ideal for array traversal (A[i]).<br/>"
            "• <b>Auto-increment / Auto-decrement:</b> EA = (R)+ or -(R). Ideal for loops and stack operations."
        ),
        "callouts": [
            ("PC-Relative Incremented Value", "When computing PC-Relative EA = PC + Offset, remember that the PC has ALREADY BEEN INCREMENTED to point to the next sequential instruction during the fetch phase!", "warn"),
            ("Immediate vs Direct", "Immediate addressing requires 0 memory accesses to fetch the operand (it is fetched with the instruction). Direct addressing requires 1 memory access to fetch the operand.", "tip")
        ],
        "tables": [
            {
                "header": ["Addressing Mode", "Effective Address (EA)", "Primary Purpose / Use Case"],
                "rows": [
                    ["Immediate", "Operand = Value in instruction", "Constants and counter initialization"],
                    ["Register", "Operand = R[i]", "High-speed temporary variable access"],
                    ["Direct", "EA = Address", "Global static variables"],
                    ["Indirect", "EA = M[Address]", "Pointers and reference parameter passing"],
                    ["PC-Relative", "EA = Updated PC + Offset", "Short branches, position-independent code"],
                    ["Indexed", "EA = R_index + Displacement", "Array indexing and table lookups"]
                ]
            }
        ]
    },
    {
        "title": "ALU, Control Unit & Memory Interfacing",
        "hinglish": "Control unit design me Hardwired (fast, combinatorial) aur Microprogrammed (flexible, ROM based) ka comparison aur control word size calculation standard questions hain.",
        "theory": (
            "<b>1. Datapath and Control Unit:</b><br/>"
            "• <b>Hardwired Control Unit:</b> Implemented using logic gates, decoders, and counters. Fast, consumes less area, but inflexible (modifications require hardware redesign). Used in RISC.<br/>"
            "• <b>Microprogrammed Control Unit:</b> Control signals stored as microinstructions in Control Memory (ROM). Flexible, easier to update, but slower due to ROM access time. Used in CISC.<br/>"
            "• <b>Horizontal Microprogramming:</b> Each bit in the control word directly represents one control signal. Maximum parallelism, no decoding needed, but very wide control words.<br/>"
            "• <b>Vertical Microprogramming:</b> Mutually exclusive signals are grouped and encoded (e.g. k signals encoded in ⌈log2(k+1)⌉ bits). Requires decoder, slower, but much narrower control words.<br/><br/>"
            "<b>2. Control Memory Size Calculation:</b><br/>"
            "• Control word size = Sum of encoded field bits + branch/condition bits + next-address bits.<br/>"
            "• Total control ROM capacity = (Number of microinstructions) * (Control word width in bits)."
        ),
        "callouts": [
            ("Vertical Encoding Trick", "When grouping k mutually exclusive control signals, always add 1 for the 'no operation / inactive' state before taking ceil(log2(k+1))!", "tip"),
            ("RISC vs CISC", "RISC architectures use hardwired control, load/store model, and fixed instruction lengths. CISC architectures use microprogrammed control and variable instruction lengths.", "formula")
        ],
        "tables": []
    },
    {
        "title": "Memory Hierarchy, Cache Mapping & AMAT",
        "hinglish": "Cache memory mapping (Direct, Set-Associative, Fully Associative) aur Average Memory Access Time (AMAT) ke numericals GATE CSE ke most repeated questions me se hain.",
        "theory": (
            "<b>1. Cache Memory Mapping Techniques:</b><br/>"
            "• Let Main Memory = 2^m bytes (m-bit physical address), Cache = 2^c bytes, Block size (Line size) = 2^w bytes.<br/>"
            "• <b>Direct Mapped Cache:</b> Cache line index = (Block Address) mod (Total Lines).<br/>"
            "  - Address breakdown: Tag | Line Index (c - w bits) | Word Offset (w bits).<br/>"
            "  - Tag size = m - c bits. Simple hardware, but highest conflict misses.<br/>"
            "• <b>Fully Associative Cache:</b> Block can go to ANY cache line.<br/>"
            "  - Address breakdown: Tag (m - w bits) | Word Offset (w bits).<br/>"
            "  - Tag size = m - w bits. Zero conflict misses, but requires expensive parallel comparators.<br/>"
            "• <b>k-Way Set Associative Cache:</b> Cache has S sets, where S = (Total Lines) / k.<br/>"
            "  - Block maps to set = (Block Address) mod S.<br/>"
            "  - Address breakdown: Tag | Set Index (log2 S bits) | Word Offset (w bits).<br/>"
            "  - Requires k parallel comparators (one per line in the set).<br/><br/>"
            "<b>2. Cache Performance & AMAT (Average Memory Access Time):</b><br/>"
            "• Single-level Cache: AMAT = T_cache + (Miss Rate * Miss Penalty).<br/>"
            "• Multi-level Cache (L1 and L2):<br/>"
            "  - AMAT = T_L1 + MissRate_L1 * [ T_L2 + MissRate_L2 * T_MainMem ].<br/>"
            "  - Global Miss Rate of L2 = MissRate_L1 * MissRate_L2.<br/><br/>"
            "<b>3. Write Policies:</b><br/>"
            "• <b>Write-Through:</b> Both cache and main memory updated simultaneously. (Consistent, but slower writes; mitigated using write buffers).<br/>"
            "• <b>Write-Back (Copy-Back):</b> Updates only cache; main memory updated when dirty line is evicted. Requires 'Dirty / Modified Bit'."
        ),
        "callouts": [
            ("Tag Directory Size Formula", "Total Cache Size = Data Capacity + Tag Directory Size.<br/>Tag Directory Size = (Number of lines) * [Tag bits + Valid bit + Dirty bit (if write-back) + Replacement bits (LRU)].", "formula"),
            ("Simultaneous vs Hierarchical Access", "Watch the wording! If CPU accesses L1 and L2 hierarchically: AMAT = H1*T1 + (1-H1)*(T1 + T2). If accessed simultaneously: AMAT = H1*T1 + (1-H1)*T2.", "warn")
        ],
        "tables": []
    },
    {
        "title": "Instruction Pipelining, Hazards & Performance",
        "hinglish": "Pipelining me Speedup = (Non-pipelined time) / (Pipelined time) aur Data Hazards (RAW dependencies) ko identify karke stalls calculate karna crucial hota hai.",
        "theory": (
            "<b>1. Pipelining Principles:</b><br/>"
            "• For a k-stage pipeline with clock cycle time τ (where τ = max(stage delays) + register delay):<br/>"
            "  - Time for 1 instruction = k * τ.<br/>"
            "  - Time for n instructions = [k + (n - 1)] * τ.<br/>"
            "  - Speedup S_k = (n * k * τ) / ([k + (n - 1)] * τ) -> As n -> ∞, Ideal Speedup S_max = k.<br/>"
            "  - Efficiency η = Speedup / k = n / [k + (n - 1)].<br/>"
            "  - Throughput = n / ([k + (n - 1)] * τ) instructions per second.<br/><br/>"
            "<b>2. Pipeline Hazards & Resolution:</b><br/>"
            "• <b>Structural Hazard (Resource conflict):</b> Two instructions need same hardware simultaneously (e.g. single-port memory for Instruction Fetch and Data Access). Resolved by separate Harvard cache (I-cache and D-cache).<br/>"
            "• <b>Data Hazards:</b><br/>"
            "  - <b>RAW (Read After Write - True Dependency):</b> Instruction j tries to read a source before instruction i writes to it. Resolved by: Operand Forwarding / Bypassing, Stall insertion (bubbles), or Compiler code reordering.<br/>"
            "  - <b>WAR (Write After Read - Anti-dependency):</b> Cannot happen in standard in-order pipelines.<br/>"
            "  - <b>WAW (Write After Write - Output dependency):</b> Happens with variable execution latency.<br/>"
            "• <b>Control Hazards (Branch hazards):</b> Branch instruction alters PC; target unknown until decode or execute stage.<br/>"
            "  - Branch Penalty = Number of clock cycles lost when branch is taken.<br/>"
            "  - Effective CPI = Ideal CPI + (Branch frequency * Branch penalty)."
        ),
        "callouts": [
            ("Operand Forwarding Impact", "With full operand forwarding from ALU-to-ALU, an instruction following an ALU operation has ZERO stall cycles. But with Load-Use dependency (Load followed by ALU), exactly 1 stall cycle remains!", "tip"),
            ("Stage Delay Clock Cycle", "Clock period in a pipeline is ALWAYS governed by the SLOWEST stage delay plus pipeline register overhead!", "formula")
        ],
        "tables": []
    }
]

PRACTICE_QUESTIONS = [
    {
        "id": "COA-Q01",
        "type": "NAT",
        "marks": 2,
        "text": "A 4-way set associative cache has a total size of 64 KB and a block size of 32 bytes. The CPU generates a 32-bit physical address. What is the number of TAG bits?",
        "answer": "18",
        "explanation": "1. Block size = 32 bytes = 2^5 bytes => Offset bits w = 5.<br/>2. Total cache size = 64 KB = 2^16 bytes.<br/>3. Total lines = (2^16 bytes) / (2^5 bytes) = 2^11 = 2048 lines.<br/>4. For 4-way set associative, Number of sets S = 2048 / 4 = 512 sets = 2^9 sets => Set Index bits s = 9.<br/>5. Address breakdown: Tag | Set Index (9) | Word Offset (5).<br/>6. Tag bits = 32 - (9 + 5) = 32 - 14 = 18 bits.",
        "is_pyq": True,
        "year": 2021,
        "difficulty": "GATE-Level"
    },
    {
        "id": "COA-Q02",
        "type": "NAT",
        "marks": 2,
        "text": "A 5-stage instruction pipeline has stage delays of 150 ps, 120 ps, 160 ps, 140 ps, and 110 ps. The pipeline register overhead delay is 10 ps between stages. Assuming no stalls or branch hazards, what is the total time (in nanoseconds) required to execute 100 instructions?",
        "answer": "17.68",
        "explanation": "1. Pipeline cycle time τ = max(stage delays) + register delay = 160 ps + 10 ps = 170 ps = 0.170 ns.<br/>2. For k = 5 stages and n = 100 instructions, total clock cycles = k + (n - 1) = 5 + 99 = 104 cycles.<br/>3. Total time = 104 * 0.170 ns = 17.68 ns.",
        "is_pyq": True,
        "year": 2019,
        "difficulty": "Medium"
    },
    {
        "id": "COA-Q03",
        "type": "MCQ",
        "marks": 1,
        "text": "In a computer system, which DMA transfer mode releases the system bus after transferring each single byte or word of data?",
        "options": {
            "A": "Burst mode",
            "B": "Cycle stealing mode",
            "C": "Block transfer mode",
            "D": "Transparent mode"
        },
        "answer": "B",
        "explanation": "In Cycle Stealing mode, the DMA controller acquires the bus for transferring one single data unit (byte/word), steals one bus cycle from the CPU, and immediately releases the bus back to the CPU.",
        "is_pyq": True,
        "year": 2020,
        "difficulty": "Easy"
    },
    {
        "id": "COA-Q04",
        "type": "MSQ",
        "marks": 2,
        "text": "Which of the following techniques can effectively reduce DATA HAZARDS in an instruction pipeline?",
        "options": {
            "A": "Operand Forwarding / Bypassing",
            "B": "Compiler instruction scheduling / code reordering",
            "C": "Hardware Branch Prediction",
            "D": "Inserting NOPs (bubbles)"
        },
        "answer": "A, B, D",
        "explanation": "Operand Forwarding (A), Compiler code scheduling (B), and NOP insertion (D) directly resolve data dependencies (RAW hazards). Branch Prediction (C) is used for CONTROL/BRANCH hazards, not data hazards.",
        "is_pyq": False,
        "year": None,
        "difficulty": "GATE-Level"
    },
    {
        "id": "COA-Q05",
        "type": "NAT",
        "marks": 2,
        "text": "A CPU has a 2-level cache hierarchy. L1 cache has a hit rate of 90% and access time of 1 ns. L2 cache has a hit rate of 80% and access time of 5 ns. Main memory access time is 50 ns. What is the Average Memory Access Time (in ns), assuming simultaneous access?",
        "answer": "2.4",
        "explanation": "Simultaneous AMAT = H1 * T1 + (1 - H1) * [ H2 * T2 + (1 - H2) * T_MM ].<br/>Here H1 = 0.90, T1 = 1 ns; Miss1 = 0.10.<br/>H2 = 0.80, T2 = 5 ns; Miss2 = 0.20.<br/>AMAT = 0.90 * 1 + 0.10 * [ 0.80 * 5 + 0.20 * 50 ] = 0.90 + 0.10 * [ 4 + 10 ] = 0.90 + 0.10 * 14 = 0.90 + 1.40 = 2.30 to 2.40 ns (hierarchical: 1 + 0.10 * (5 + 0.20 * 50) = 1 + 0.10 * 15 = 2.5 ns; simultaneous: 2.3 ns).",
        "is_pyq": False,
        "year": None,
        "difficulty": "GATE-Level"
    }
]
