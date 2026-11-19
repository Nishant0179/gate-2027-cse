# textbook_db_cn_ga.py
# Simplified, crystal-clear study notes for Databases, Computer Networks, and General Aptitude.
# Written in simple, friendly, easy-to-understand language for GATE 2027 CSE aspirants.

CHAPTERS_DB_CN_GA = {}

# =============================================================================
# DATABASES (DB)
# =============================================================================

# DB Chapter 0: ER-Model, Relational Algebra & SQL
CHAPTERS_DB_CN_GA[("DB", 0)] = {
    "sub_id": "DB",
    "chap_idx": 0,
    "title": "ER-Model, Relational Algebra & SQL",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Hospital Blueprints vs Real Rooms (ER Model to Tables)",
            "text": "Before building a hospital, you draw a sketch of Doctors, Patients, and Rooms (ER Diagram). When building the hospital, you pour real concrete rooms with ID numbers (Relational Tables). Because one Doctor sees many Patients, you don't build a new hospital: you put the Doctor's ID on the Patient's medical chart (Foreign Key on the N-side!)."
        },
        {
            "title": "Real-Life Example 2: Slicing Vegetables (Selection σ vs Projection π)",
            "text": "Imagine a basket of potatoes and carrots. Selection (σ) acts like a filter: it picks only the red carrots and throws away potatoes (filters ROWS horizontally). Projection (π) acts like a peeler: it keeps only the weight tag and throws away the color and farm origin (slices COLUMNS vertically)."
        },
        {
            "title": "Real-Life Example 3: The Mystery Answer on an Exam Sheet (NULL in SQL)",
            "text": "In SQL, `NULL` does NOT mean zero, and it does NOT mean empty text. It means 'UNKNOWN / MISSING'. If a student's marks are NULL, what is `marks > 50`? It is UNKNOWN! In SQL three-valued logic, `NULL = NULL` is NOT True—it is UNKNOWN! That is why writing `WHERE marks = NULL` returns zero rows; you must write `WHERE marks IS NULL`."
        }
    ],
    "foundations": [
        {
            "number": "29.1",
            "title": "ER to Relational Table Conversion Rules",
            "content": (
                "• <b>1:1 Relationship:</b> Combine into 2 tables, or 1 table if total participation.<br/>"
                "• <b>1:N Relationship:</b> Relationship table can be merged into the <b>'N' side table</b> (Foreign key goes to N-side!).<br/>"
                "• <b>M:N Relationship:</b> CANNOT be merged! Requires a <b>separate table</b> with primary keys of both entities.<br/>"
                "• <b>Weak Entity:</b> Always merged with its identifying relationship into 1 table."
            ),
            "crucial_rule": "GOLDEN RULE: In a 1:N relationship, the Foreign Key ALWAYS goes to the 'N' (Many) side, NEVER the '1' side!"
        },
        {
            "number": "29.2",
            "title": "Relational Algebra Core Operators",
            "content": (
                "• <b>Selection (σ):</b> Filters rows based on condition: σ_age>20(Student).<br/>"
                "• <b>Projection (π):</b> Selects columns: π_name,roll(Student). Automatically eliminates duplicate rows!<br/>"
                "• <b>Cartesian Product (R × S):</b> Combines every row of R with every row of S.<br/>"
                "• <b>Natural Join (R ⋈ S):</b> Joins matching common columns."
            ),
            "crucial_rule": "GOLDEN RULE: Relational algebra automatically eliminates duplicate rows (Set semantics). SQL keeps duplicates (Bag semantics) unless you write DISTINCT!"
        },
        {
            "number": "29.3",
            "title": "SQL Rules & NULL Behaviors",
            "content": (
                "• `WHERE` filters rows BEFORE grouping.<br/>"
                "• `HAVING` filters groups AFTER `GROUP BY`.<br/>"
                "• Aggregate functions (SUM, AVG, MIN, MAX) <b>IGNORE NULLs completely</b>.<br/>"
                "• Exception: `COUNT(*)` counts ALL rows, including rows containing NULLs!"
            ),
            "crucial_rule": "GOLDEN RULE: If a subquery inside `NOT IN (SELECT id FROM ...)` returns even ONE NULL, the entire outer query returns ZERO rows!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Minimum Tables for ER Diagram",
            "problem": "Entities E1 and E2 have a 1:N relationship R1. E2 and E3 have an M:N relationship R2. What is the minimum number of relational tables needed?",
            "steps": [
                "Step 1: E1 gets 1 table: Table(E1).",
                "Step 2: 1:N relationship R1 merges into N-side table E2: Table(E2) with E1's key as foreign key.",
                "Step 3: Entity E3 gets 1 table: Table(E3).",
                "Step 4: M:N relationship R2 MUST have its own independent table: Table(R2).",
                "Step 5: Total tables = Table(E1) + Table(E2) + Table(E3) + Table(R2) = 4 tables."
            ],
            "answer": "Minimum tables = 4."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: COUNT(*) vs COUNT(column)",
            "warning": "COUNT(*) counts every row in the table. COUNT(column_name) counts only rows where that specific column is NOT NULL!"
        }
    ]
}

# DB Chapter 1: Normalization
CHAPTERS_DB_CN_GA[("DB", 1)] = {
    "sub_id": "DB",
    "chap_idx": 1,
    "title": "Functional Dependencies & Normalization (1NF to BCNF)",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Repeated College Roster Rows (Database Anomalies)",
            "text": "Imagine a college spreadsheet repeating Student Name, HOD Name, and HOD Mobile Number 5,000 times. If the HOD changes their phone number, updating 5,000 rows by hand is crazy (Update Anomaly). If you miss 2 rows, data becomes corrupted. If the last student drops out of a course and you delete the row, you accidentally delete the course from the college (Deletion Anomaly)! Normalization splits data into clean, separate tables."
        },
        {
            "title": "Real-Life Example 2: The Driving License Master Key (Candidate Key)",
            "text": "Your driving license number determines your Name, Blood Group, and Address. Does your Blood Group determine your Name? No! An Attribute Closure (X+) starts with a column and sees how many other columns it unlocks. If X+ unlocks the whole table, X is a Candidate Key."
        },
        {
            "title": "Real-Life Example 3: Disassembling a Lego Car (Lossless Join)",
            "text": "When you split a big table into two smaller tables, you must be able to snap them back together using Natural Join without creating fake ghost rows that never existed (Lossless Join). The common column must be a Superkey in at least one of the tables."
        }
    ],
    "foundations": [
        {
            "number": "30.1",
            "title": "The Normal Forms in 4 Simple Rules",
            "content": (
                "• <b>1NF:</b> Every cell holds a single atomic value (no lists or arrays in cells).<br/>"
                "• <b>2NF:</b> In 1NF and <b>NO PARTIAL DEPENDENCY</b> (no non-key column depends on just half of a composite key).<br/>"
                "• <b>3NF:</b> In 2NF and <b>NO TRANSITIVE DEPENDENCY</b>. For every FD `X → A`: either <b>X is a Superkey</b> OR <b>A is a Prime Attribute</b>.<br/>"
                "• <b>BCNF:</b> For every FD `X → A`, <b>X MUST BE A SUPERKEY</b>."
            ),
            "crucial_rule": "GOLDEN RULE: Any relation with only 2 attributes is ALWAYS in BCNF! (Direct GATE shortcut)."
        },
        {
            "number": "30.2",
            "title": "Lossless Join Decomposition Test",
            "content": (
                "Splitting relation R into R1 and R2 is Lossless if and only if:<br/>"
                "• <b>(R1 ∩ R2) → R1</b> &nbsp;OR&nbsp; <b>(R1 ∩ R2) → R2</b>.<br/>"
                "In plain words: The common attribute must be a Superkey of at least one of the sub-tables!"
            ),
            "crucial_rule": "GOLDEN RULE: 3NF decomposition can ALWAYS achieve BOTH Lossless Join and Dependency Preservation. BCNF guarantees Lossless Join, but may NOT preserve dependencies!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Finding Highest Normal Form",
            "problem": "Relation R(A, B, C) with FDs: { A → B, B → C }. What is the highest normal form of R?",
            "steps": [
                "Step 1: Find candidate keys: (A)+ = {A, B, C} ⇒ Candidate Key is A. Prime attribute = {A}.",
                "Step 2: Check 1NF: Atomic values ✔.",
                "Step 3: Check 2NF: No partial dependency (key A has only 1 attribute) ✔.",
                "Step 4: Check 3NF: In B → C: is B a superkey? No. Is C a prime attribute? No. Both tests fail! Violates 3NF.",
                "Step 5: Therefore, highest normal form is 2NF."
            ],
            "answer": "Highest Normal Form = 2NF."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Prime Attributes Can Save 3NF",
            "warning": "In 3NF, the rule is 'X is superkey OR A is prime'. Even if X is NOT a superkey, as long as RHS attribute A is part of ANY candidate key, 3NF is NOT violated!"
        }
    ]
}

# DB Chapter 2: B+ Trees & Transactions
CHAPTERS_DB_CN_GA[("DB", 2)] = {
    "sub_id": "DB",
    "chap_idx": 2,
    "title": "B/B+ Trees, Transactions & Concurrency Control",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The Library Catalog vs Shelf Books (B+ Trees)",
            "text": "An internal node of a B+ tree is like a catalog sign: 'Books A-F in aisle 1, G-M in aisle 2'. The sign contains NO real books (no data records)—only index pointers! The real books live exclusively on the shelves (Leaf Nodes). All shelves are connected side-by-side with a rope (Doubly Linked List), letting you scan books sequentially without climbing back up to the catalog sign."
        },
        {
            "title": "Real-Life Example 2: ATM Money Transfer (ACID Properties)",
            "text": "You transfer ₹5,000 from Savings to Checking. Atomicity (All or Nothing): if power cuts mid-transfer, money isn't lost—it resets back. Consistency: total money remains invariant. Isolation: your friend checking balance doesn't see partial amounts. Durability: once 'Success' displays, a crash cannot wipe the transaction."
        },
        {
            "title": "Real-Life Example 3: Presidential Motorcade (Strict 2-Phase Locking - 2PL)",
            "text": "Growing Phase: acquire locks on every road ahead, NEVER release any lock. Shrinking Phase: once the car safely arrives and commits, unlock all roads at once. Strict 2PL guarantees Conflict Serializability and prevents Cascading Aborts."
        }
    ],
    "foundations": [
        {
            "number": "31.1",
            "title": "B+ Tree Node Capacity Formulas",
            "content": (
                "• <b>Internal Node of order p:</b> Holds p block pointers and p - 1 search keys.<br/>"
                "&nbsp;&nbsp;<b>p × (Block Pointer Size) + (p - 1) × (Key Size) ≤ Block Size</b>.<br/>"
                "• Data pointers reside <b>EXCLUSIVELY in Leaf Nodes</b>!"
            ),
            "crucial_rule": "GOLDEN RULE: Internal nodes in a B+ Tree contain NO record/data pointers, which allows much higher fan-out and shallower tree height compared to B-Trees."
        },
        {
            "number": "31.2",
            "title": "Conflict Serializability via Precedence Graph",
            "content": (
                "Two actions conflict if they belong to different transactions, access the SAME data, and at least one is a <b>WRITE</b>.<br/>"
                "• Draw edge Ti → Tj if Ti executed conflicting action before Tj.<br/>"
                "• <b>Rule:</b> Schedule is Conflict Serializable <b>IF AND ONLY IF the graph has NO CYCLES</b>."
            ),
            "crucial_rule": "GOLDEN RULE: If the precedence graph has no cycles, doing a Topological Sort gives the equivalent serial schedule order!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Maximum B+ Tree Order",
            "problem": "Block size = 512 bytes, Key size = 10 bytes, Block pointer = 6 bytes. Find maximum order p of an internal node.",
            "steps": [
                "Step 1: Formula: p × 6 + (p - 1) × 10 ≤ 512.",
                "Step 2: Expand: 6p + 10p - 10 ≤ 512 ⇒ 16p ≤ 522.",
                "Step 3: Solve: p ≤ 522 / 16 = 32.625.",
                "Step 4: Take floor integer: p = 32."
            ],
            "answer": "Maximum order p = 32."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Cascadeless vs Recoverable",
            "warning": "Strict ⊂ Cascadeless ⊂ Recoverable. A cascadeless schedule is ALWAYS recoverable, but a recoverable schedule is not necessarily cascadeless!"
        }
    ]
}

# =============================================================================
# COMPUTER NETWORKS (CN)
# =============================================================================

# CN Chapter 0: Layering & Performance
CHAPTERS_DB_CN_GA[("CN", 0)] = {
    "sub_id": "CN",
    "chap_idx": 0,
    "title": "Layering, Switching & Network Performance Metrics",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Mailing an Overseas Birthday Gift (Layering)",
            "text": "• Application: You write a birthday greeting note.\n• Transport: Put a parcel tracking code on it.\n• Network: Write the destination Country and PIN code (IP Address routing).\n• Data Link: Truck driver reads the license plate of the next regional warehouse (MAC address).\n• Physical: The asphalt highway road."
        },
        {
            "title": "Real-Life Example 2: Wide River Pipe vs Fast Jet Speed (Bandwidth vs Latency)",
            "text": "Bandwidth is the width of a water pipe (how many liters flow per second). Propagation delay is how fast the water flows through the hose (speed of light). A huge cargo ship has massive bandwidth (can carry 1,000,000 hard drives), but high latency (takes 2 weeks). Playing online games needs low latency, not giant bandwidth."
        },
        {
            "title": "Real-Life Example 3: Cars on a Long Highway (Bandwidth-Delay Product - BDP)",
            "text": "If 100 cars enter a 500-km highway every minute, there are thousands of cars driving on the road at any given instant. Bandwidth-Delay Product (Bandwidth × Propagation Delay) measures how many data bits can fill the entire length of the cable pipe at once!"
        }
    ],
    "foundations": [
        {
            "number": "32.1",
            "title": "Transmission Delay vs Propagation Delay",
            "content": (
                "• <b>Transmission Delay (T_trans):</b> Time to push packet onto wire = <b>Packet Size (L) / Bandwidth (B)</b>.<br/>"
                "• <b>Propagation Delay (T_prop):</b> Time for bit to travel across physical distance = <b>Distance (d) / Speed (v)</b>.<br/>"
                "• Total Latency = T_trans + T_prop + Queueing + Processing."
            ),
            "crucial_rule": "GOLDEN RULE: Bandwidth NEVER affects propagation speed! Propagation speed depends only on the speed of light in the cable."
        },
        {
            "number": "32.2",
            "title": "Store-and-Forward Packet Switching Delay",
            "content": (
                "For M packets of size L traveling over N router hops with bandwidth B:<br/>"
                "• <b>Total Time = (N + M - 1) × (L / B) + N × T_prop</b>."
            ),
            "crucial_rule": "GOLDEN RULE: Bandwidth is ALWAYS in bits per second (bps, Mbps). If packet size is given in Bytes, multiply by 8 first!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Packet Transmission Delay",
            "problem": "A 1000-byte packet is sent over a 1 Mbps link. What is the transmission delay?",
            "steps": [
                "Step 1: Convert bytes to bits: 1000 Bytes × 8 = 8000 bits.",
                "Step 2: Bandwidth = 1 Mbps = 1,000,000 bits/sec.",
                "Step 3: T_trans = 8000 / 1,000,000 = 0.008 seconds = 8 milliseconds."
            ],
            "answer": "Transmission Delay = 8 ms."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Bits vs Bytes",
            "warning": "Forgetting to multiply Bytes by 8 before dividing by Mbps will make your answer 8 times too small!"
        }
    ]
}

# CN Chapter 1: Data Link Layer & MAC
CHAPTERS_DB_CN_GA[("CN", 1)] = {
    "sub_id": "CN",
    "chap_idx": 1,
    "title": "Data Link Layer, CRC & Medium Access Control (CSMA/CD)",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Talking at a Dinner Party (CSMA/CD)",
            "text": "At a crowded dinner table, you listen before speaking (Carrier Sense). If someone is talking, you wait. If the room is quiet, you speak. If you and another person start speaking at the exact same instant, you collide! You both stop, yell 'Oops!' (Jamming signal), and wait a random number of seconds (Backoff) before trying again."
        },
        {
            "title": "Real-Life Example 2: Walkie-Talkie vs Phone Call (Stop-and-Wait vs Sliding Window)",
            "text": "In Stop-and-Wait, you say: 'Roger, over' and wait 30 seconds for a reply. Channel sits idle! In a Sliding Window protocol (Go-Back-N), you send 7 packets in a continuous stream without waiting, sliding the window forward as ACKs return."
        },
        {
            "title": "Real-Life Example 3: The Tamper-Proof Seal (Cyclic Redundancy Check - CRC)",
            "text": "CRC treats data bits like a polynomial and divides it by a generator code using binary XOR division. The remainder is attached to the packet. If even one bit flips during transit, the receiver's division fails, catching the error instantly."
        }
    ],
    "foundations": [
        {
            "number": "33.1",
            "title": "Sliding Window Window Sizes",
            "content": (
                "With k sequence bits:<br/>"
                "• <b>Go-Back-N (GBN):</b> Sender window = <b>2^k - 1</b>, Receiver window = 1.<br/>"
                "• <b>Selective Repeat (SR):</b> Sender window = <b>2^(k-1)</b>, Receiver window = <b>2^(k-1)</b>."
            ),
            "crucial_rule": "GOLDEN RULE: Stop-and-Wait efficiency η = 1 / (1 + 2a), where a = T_prop / T_trans."
        },
        {
            "number": "33.2",
            "title": "CSMA/CD Minimum Frame Size Rule",
            "content": (
                "For Ethernet CSMA/CD to detect collisions before finishing transmission:<br/>"
                "• <b>T_trans ≥ 2 × T_prop</b>.<br/>"
                "• <b>Minimum Frame Size: L_min ≥ 2 × (d / v) × Bandwidth</b>."
            ),
            "crucial_rule": "GOLDEN RULE: Remember the factor of 2! The collision signal has to travel all the way back across the cable: Round-Trip Time = 2 × T_prop."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Minimum Frame Size in CSMA/CD",
            "problem": "A 10 Mbps Ethernet cable has propagation delay T_prop = 20 µs. What is the minimum frame size?",
            "steps": [
                "Step 1: Formula: L_min = 2 × T_prop × Bandwidth.",
                "Step 2: Plug in: L_min = 2 × (20 × 10^-6 s) × (10 × 10^6 bps).",
                "Step 3: L_min = 40 × 10 = 400 bits.",
                "Step 4: Convert to bytes: 400 / 8 = 50 Bytes."
            ],
            "answer": "Minimum frame size = 50 Bytes (400 bits)."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: CRC Check Bits",
            "warning": "If the generator polynomial G(x) has degree r (e.g. x^3 + x + 1 has degree 3), append exactly r zeros (3 zeros), NOT 4 zeros!"
        }
    ]
}

# CN Chapter 2: Routing & IPv4
CHAPTERS_DB_CN_GA[("CN", 2)] = {
    "sub_id": "CN",
    "chap_idx": 2,
    "title": "Routing Protocols & IPv4 Addressing (CIDR, Fragmentation, NAT)",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Apartment Building Chutes (CIDR Subnetting)",
            "text": "An IP block `192.168.1.0/24` has 256 addresses. The /24 tells the mail carrier that the first 24 bits are the building's street address (Network ID). The remaining 8 bits are the individual room numbers (Host ID)."
        },
        {
            "title": "Real-Life Example 2: Moving a Huge Sofa Through a Narrow Door (IPv4 Fragmentation)",
            "text": "If a delivery sofa is 8 feet long, but the doorway (MTU) only fits 3-foot boxes, you must unscrew the sofa into 3 numbered boxes with offset tags: Box 1 (Offset 0), Box 2 (Offset 185), Box 3 (Offset 370). In IPv4, Fragment Offset is measured in 8-byte blocks."
        },
        {
            "title": "Real-Life Example 3: Whispering Rumors (Distance Vector Count-to-Infinity)",
            "text": "In Distance Vector (RIP), routers whisper route distances to neighbors every 30 seconds. If a link breaks, routers keep updating each other in circles (2, 3, 4... up to 16!). Split Horizon and Poisoned Reverse stop these loops."
        }
    ],
    "foundations": [
        {
            "number": "34.1",
            "title": "IPv4 Fragmentation & Offset Rules",
            "content": (
                "• <b>Fragment Offset:</b> 13 bits. Measures byte offset in <b>units of 8 bytes</b>: `Offset = (Payload bytes) / 8`.<br/>"
                "• Fragment payload size MUST be a multiple of 8 (except the last fragment).<br/>"
                "• <b>MF bit (More Fragments):</b> 1 if more fragments follow; 0 for the last fragment."
            ),
            "crucial_rule": "GOLDEN RULE: Offset is ALWAYS divided by 8! If byte offset is 800, the offset field stores 800 / 8 = 100."
        },
        {
            "number": "34.2",
            "title": "Longest Prefix Match in Routing",
            "content": (
                "When an IP matches multiple entries in a routing table, the router ALWAYS routes packet through the entry with the <b>LONGEST SUBNET MASK (most specific prefix)</b>."
            ),
            "crucial_rule": "GOLDEN RULE: If a packet matches both /16 and /24, route according to /24!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: IPv4 Usable Hosts",
            "problem": "How many usable host IP addresses are in a /26 subnet?",
            "steps": [
                "Step 1: Total bits = 32. Host bits h = 32 - 26 = 6 bits.",
                "Step 2: Total IP addresses = 2^6 = 64.",
                "Step 3: Subtract 2 addresses (Network ID and Direct Broadcast Address).",
                "Step 4: Usable hosts = 64 - 2 = 62."
            ],
            "answer": "Usable hosts = 62."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: First and Last IP Addresses",
            "warning": "Always subtract 2 for usable hosts! The all-zeros host address is Network ID; the all-ones host address is Broadcast."
        }
    ]
}

# CN Chapter 3: Transport Layer & Applications
CHAPTERS_DB_CN_GA[("CN", 3)] = {
    "sub_id": "CN",
    "chap_idx": 3,
    "title": "Transport Layer (TCP), Sockets & Application Protocols (DNS, HTTP)",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The Three-Way Hello Handshake (TCP 3-Way Handshake)",
            "text": "Before two people talk on a phone: 'Can you hear me?' (SYN) -> 'Yes, I hear you, can you hear me?' (SYN+ACK) -> 'Yes, loud and clear!' (ACK). Connection established! Now data can flow reliably."
        },
        {
            "title": "Real-Life Example 2: Squeezing a Water Hose (TCP Congestion Control)",
            "text": "TCP starts sending slowly (Slow Start: doubles window every round). When it reaches a threshold, it increases gently by +1 packet per round (Additive Increase). If a packet drops (congestion!), it immediately cuts its speed in HALF (Multiplicative Decrease - AIMD)."
        },
        {
            "title": "Real-Life Example 3: Phone Contact List (DNS)",
            "text": "You don't memorize 142.250.190.46; you type 'google.com'. The Domain Name System (DNS) looks up the name like a global phonebook and returns the numerical IP address using fast, lightweight UDP (port 53)."
        }
    ],
    "foundations": [
        {
            "number": "35.1",
            "title": "TCP Handshake & Sequence Numbers",
            "content": (
                "• <b>3-Way Handshake:</b> SYN -> SYN+ACK -> ACK.<br/>"
                "• <b>Sequence numbers:</b> SYN and FIN packets <b>CONSUME 1 SEQUENCE NUMBER</b> even if they have 0 bytes of payload!"
            ),
            "crucial_rule": "GOLDEN RULE: Plain ACK packets consume 0 sequence numbers."
        },
        {
            "number": "35.2",
            "title": "TCP Congestion Window Growth",
            "content": (
                "• <b>Slow Start:</b> Window doubles every RTT (1, 2, 4, 8...).<br/>"
                "• <b>Congestion Avoidance:</b> Increases by +1 MSS per RTT.<br/>"
                "• <b>On Timeout:</b> ssthresh = cwnd / 2, and <b>cwnd resets to 1 MSS</b>.<br/>"
                "• <b>On 3 Duplicate ACKs (TCP Reno):</b> cwnd drops to ssthresh (Fast Recovery, does not reset to 1!)."
            ),
            "crucial_rule": "GOLDEN RULE: Common Port Numbers to memorize: DNS (53), HTTP (80), HTTPS (443), SMTP (25), POP3 (110)."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: TCP Window Growth",
            "problem": "TCP starts Slow Start with cwnd = 1 MSS, ssthresh = 8 MSS. How big is cwnd after 4 RTTs (no loss)?",
            "steps": [
                "Step 1: Start: cwnd = 1.",
                "Step 2: RTT 1: cwnd = 2.",
                "Step 3: RTT 2: cwnd = 4.",
                "Step 4: RTT 3: cwnd = 8 (Hits ssthresh = 8! Switches to Congestion Avoidance).",
                "Step 5: RTT 4: Linear increase (+1) ⇒ cwnd = 8 + 1 = 9 MSS."
            ],
            "answer": "After 4 RTTs, cwnd = 9 MSS."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: HTTP Statelessness",
            "warning": "HTTP is stateless by design. Websites use Cookies and Session tokens to remember who you are."
        }
    ]
}

# =============================================================================
# GENERAL APTITUDE (GA)
# =============================================================================

# GA Chapter 0: Verbal Aptitude
CHAPTERS_DB_CN_GA[("GA", 0)] = {
    "sub_id": "GA",
    "chap_idx": 0,
    "title": "Verbal Aptitude - Grammar, Vocabulary & Comprehension",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The Misleading Group (Subject-Verb Agreement)",
            "text": "Sentence: 'The teacher, along with 50 students, (was/were) present'. Many pick 'were' because they see 50 students. But phrases with 'along with' or 'as well as' don't change the subject! The true subject is 'The teacher' (singular), so the verb MUST be 'was'."
        },
        {
            "title": "Real-Life Example 2: The Attacking Door (Dangling Modifier)",
            "text": "A sign says: 'Walking into the bank, the door hit Alice'. That means the door was walking! Correct: 'While Alice was walking into the bank, she was hit by the door'."
        },
        {
            "title": "Real-Life Example 3: Word Roots (Etymology)",
            "text": "'Bene' means good (Benefit, Benevolent). 'Mal' means bad (Malfunction, Malevolent). Knowing root prefixes lets you guess hundreds of unfamiliar words in 5 seconds."
        }
    ],
    "foundations": [
        {
            "number": "36.1",
            "title": "Subject-Verb & Either/Neither Rules",
            "content": (
                "• In 'Neither A nor B' / 'Either A or B': Verb agrees with the <b>SUBJECT CLOSEST TO IT</b>.<br/>"
                "• Words like 'Each', 'Everyone', 'Neither of' are STRICTLY SINGULAR ('Each of the boys <b>is</b> ready')."
            ),
            "crucial_rule": "GOLDEN RULE: 'Complement' means something that completes (Wine complements cheese). 'Compliment' means praise (She gave a nice compliment)."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Sentence Correction",
            "problem": "Select the correct sentence:\n(A) Neither the teacher nor the students was present.\n(B) Neither the teacher nor the students were present.",
            "steps": [
                "Step 1: Check subject closest to the verb: 'students' (plural).",
                "Step 2: Plural subject requires plural verb 'were'.",
                "Step 3: Option (B) is grammatically correct."
            ],
            "answer": "Sentence (B) is correct."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Third Conditional Form",
            "warning": "Formula: 'If + had + V3, would have + V3'. Example: 'If he had studied, he would have passed' (Never write 'If he would have studied'!)."
        }
    ]
}

# GA Chapter 1: Quantitative Aptitude
CHAPTERS_DB_CN_GA[("GA", 1)] = {
    "sub_id": "GA",
    "chap_idx": 1,
    "title": "Quantitative Aptitude - Arithmetic, Algebra & Mensuration",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The Escalator Run (Relative Speed)",
            "text": "An escalator moves up at 1 m/s. If you stand still, you take 60 seconds. If you run up at 2 m/s, your speeds add: (2 + 1) = 3 m/s, taking just 20 seconds! Moving in same direction adds speeds; moving against subtracts."
        },
        {
            "title": "Real-Life Example 2: Painting a Room Together (Time and Work)",
            "text": "Alice paints a room in 10 days (1/10th per day). Bob paints it in 15 days (1/15th per day). Working together, daily work = 1/10 + 1/15 = 5/30 = 1/6th per day. Together they finish the whole room in 6 days!"
        },
        {
            "title": "Real-Life Example 3: Diwali Sale 50% + 50% Off! (Successive Percentages)",
            "text": "Does 50% + 50% off mean clothes are free? No! ₹1000 shirt - 50% becomes ₹500. The second 50% off ₹500 makes it ₹250. Real discount is 75%, not 100%! Formula: Net = a + b + (ab/100)."
        }
    ],
    "foundations": [
        {
            "number": "37.1",
            "title": "Key Arithmetic Formulas to Memorize",
            "content": (
                "• <b>Average Speed for equal distances:</b> <b>2 v1 v2 / (v1 + v2)</b> (Harmonic mean!).<br/>"
                "• <b>Difference between CI and SI for 2 years:</b> <b>P × (R / 100)²</b>.<br/>"
                "• <b>Boats & Streams:</b> Downstream = u + v &nbsp;|&nbsp; Upstream = u - v."
            ),
            "crucial_rule": "GOLDEN RULE: If price rises by R%, consumption must drop by [ R / (100 + R) ] × 100% to keep spending unchanged."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Time and Work Alternate Days",
            "problem": "A completes work in 10 days, B in 15 days. They work alternate days starting with A. How many days will it take?",
            "steps": [
                "Step 1: Total work LCM(10, 15) = 30 units.",
                "Step 2: A does 30/10 = 3 units/day. B does 30/15 = 2 units/day.",
                "Step 3: In 2 days (A + B), work done = 3 + 2 = 5 units.",
                "Step 4: Cycles needed: 30 / 5 = 6 cycles.",
                "Step 5: Total days = 6 cycles × 2 days = 12 days."
            ],
            "answer": "Total time = 12 days."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Average Speed is NOT Simple Average",
            "warning": "If distance is equal, Average Speed is 2v1v2 / (v1 + v2), NOT (v1 + v2)/2!"
        }
    ]
}

# GA Chapter 2: Analytical & Spatial Aptitude
CHAPTERS_DB_CN_GA[("GA", 2)] = {
    "sub_id": "GA",
    "chap_idx": 2,
    "title": "Analytical & Spatial Aptitude - Logic, Reasoning & 2D/3D Shapes",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Folding Paper & Punching a Hole (Spatial Aptitude)",
            "text": "Fold a paper in half, then half again, and punch 1 hole. When you unfold it, the crease lines act as mirrors. That 1 punched hole reflects symmetrically into 4 holes in the opened paper!"
        },
        {
            "title": "Real-Life Example 2: Folding a Cardboard Cube (Cube Nets)",
            "text": "In any straight strip of squares on a flat cube net, alternate squares (separated by 1 square in between) will ALWAYS end up on opposite sides when folded into a 3D box!"
        },
        {
            "title": "Real-Life Example 3: Blood Relations Clue Tree",
            "text": "'His mother is the only daughter of my mother'. Start from 'My mother': Only daughter of my mother is my sister. 'His mother is my sister'. So the boy is my nephew! Always draw a simple tree diagram."
        }
    ],
    "foundations": [
        {
            "number": "38.1",
            "title": "Syllogisms & Validity Rules",
            "content": (
                "• A conclusion is valid ONLY if it holds in <b>EVERY POSSIBLE Venn diagram</b>.<br/>"
                "• 'Some' in logic means 'At least one, and possibly all'."
            ),
            "crucial_rule": "GOLDEN RULE: In a folded 3D cube, two OPPOSITE faces can NEVER touch or appear adjacent to each other!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Cube Net Opposite Faces",
            "problem": "In a vertical cube net strip [1, 2, 3, 4], which faces are opposite?",
            "steps": [
                "Step 1: Alternate faces in a straight line are opposite.",
                "Step 2: Face 1 is opposite to Face 3.",
                "Step 3: Face 2 is opposite to Face 4."
            ],
            "answer": "Opposite pairs: (1, 3) and (2, 4)."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: 'Some' vs 'All'",
            "warning": "If 'All dogs are animals' is true, then 'Some dogs are animals' is also mathematically 100% TRUE!"
        }
    ]
}
