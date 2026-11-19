# Master Textbook Module: Databases, Computer Networks & General Aptitude (10 Chapters)
# Auto-generated comprehensive ChatGPT-style point-form guide

CHAPTERS_DB_CN_GA = { ('CN', 0): { 'chapter_number': 32,
               'exam_traps': [ { 'title': 'Bits vs Bytes Unit Conversion Trap',
                                 'warning': 'Packet size is usually given in Bytes (KB), but Bandwidth is given in '
                                            'bits/sec (Mbps). ALWAYS multiply bytes by 8 to convert to bits before '
                                            'computing T_t = L / B!'}],
               'foundations': [ { 'content': '• <b>The 7 OSI Layers & Their Data Units:</b><br/>\n'
                                             "<div class='font-mono text-xs p-3 bg-slate-900 text-slate-100 rounded-xl "
                                             "my-2 leading-relaxed overflow-x-auto'>\n"
                                             'OSI Layer           │ Protocol Data Unit (PDU) │ Core Addressing '
                                             'Used          │ Hardware Devices\n'
                                             '─────────────────────────────────────────────────────────────────────────────────────────────\n'
                                             'Application (7-5)   │ Message / Data           │ Process / Domain Name '
                                             '(DNS)   │ Gateway\n'
                                             'Transport (4)       │ Segment (TCP) / Datagram │ Port Number '
                                             '(16-bit)          │ Firewall / Load Balancer\n'
                                             'Network (3)         │ Packet                   │ IP Address (32 / '
                                             '128-bit)     │ Router / L3 Switch\n'
                                             'Data Link (2)       │ Frame                    │ MAC Address '
                                             '(48-bit)          │ Bridge / L2 Switch / NIC\n'
                                             'Physical (1)        │ Bits                     │ Physical signaling '
                                             '(Volts, Hz)│ Hub / Repeater\n'
                                             '</div>',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: Hub and Repeater work at Layer 1 '
                                                  '(Physical). Bridge and Switch work at Layer 2 (Data Link - '
                                                  'Collision domains separated). Router works at Layer 3 (Network - '
                                                  'Broadcast domains separated).',
                                  'number': '32.1',
                                  'title': 'OSI 7-Layer vs TCP/IP Models & Protocol Stacks'},
                                { 'content': '• <b>The 4 Fundamental Network Delays:</b><br/>\n'
                                             '&nbsp;&nbsp;1. <b>Transmission Delay (Tₜ):</b> Time to push all packet '
                                             'bits onto the wire: <code>Tₜ = Packet Size (L) / Bandwidth '
                                             '(B)</code>.<br/>\n'
                                             '&nbsp;&nbsp;2. <b>Propagation Delay (Tₚ):</b> Time for 1 bit to travel '
                                             'from sender to receiver: <code>Tₚ = Distance (d) / Propagation Speed '
                                             '(v)</code>.<br/>\n'
                                             '&nbsp;&nbsp;3. <b>Queuing Delay:</b> Time waiting in router '
                                             'buffers.<br/>\n'
                                             '&nbsp;&nbsp;4. <b>Processing Delay:</b> Time taken by router to examine '
                                             'packet headers.<br/><br/>\n'
                                             '\n'
                                             '• <b>Bandwidth-Delay Product (BDP):</b><br/>\n'
                                             '&nbsp;&nbsp;<code>BDP = Bandwidth × Propagation Delay</code><br/>\n'
                                             "&nbsp;&nbsp;Represents the maximum volume of bits that can be 'in "
                                             "flight' on the transmission link at any given instant!",
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: Transmission delay depends on bandwidth '
                                                  '(bits/sec), NOT distance! Propagation delay depends on physical '
                                                  'distance and medium speed, NOT bandwidth.',
                                  'number': '32.2',
                                  'title': 'Network Delays & Bandwidth-Delay Product (BDP)'}],
               'real_life_examples': [ { 'text': 'Transmission delay is how fast you pour water into a pipe. '
                                                 'Propagation delay is how long the first drop takes to travel through '
                                                 'the pipe to the other end.',
                                         'title': 'Real-Life Analogy: Pipe Length vs Flow Rate'}],
               'title': 'Layering, Switching & Network Performance Metrics',
               'worked_examples': [ { 'answer': 'Transmission Delay = 0.8 ms, Propagation Delay = 10 ms.',
                                      'problem': 'A 1000-byte packet is sent over a 10 Mbps point-to-point link of '
                                                 'distance 2000 km. The propagation speed is 2 × 10⁸ m/s. Find the '
                                                 'transmission and propagation delays.',
                                      'steps': [ 'Step 1: Transmission delay T_t = L / B = (1000 × 8 bits) / (10 × 10⁶ '
                                                 'bps) = 8000 / 10,000,000 = 0.0008 s = 0.8 ms.',
                                                 'Step 2: Propagation delay T_p = d / v = (2000 × 10³ m) / (2 × 10⁸ '
                                                 'm/s) = 2,000,000 / 200,000,000 = 0.01 s = 10 ms.',
                                                 'Step 3: Notice: T_p (10 ms) is over 12 times larger than T_t (0.8 '
                                                 'ms)! The link is propagation-dominated.'],
                                      'title': 'Worked Example: Transmission Delay vs Propagation Delay'}]},
  ('CN', 1): { 'chapter_number': 33,
               'exam_traps': [ { 'title': 'Round Trip Time Factor 2 Trap',
                                 'warning': 'In CSMA/CD, the factor of 2 (2 × T_p) accounts for the WORST-CASE '
                                            'round-trip collision scenario where collision occurs just before reaching '
                                            'the destination.'}],
               'foundations': [ { 'content': "• <b>Let parameter 'a':</b> <code>a = Propagation Delay (Tₚ) / "
                                             'Transmission Delay (Tₜ)</code>.<br/><br/>\n'
                                             '\n'
                                             '• <b>Master Comparison of Flow Control Protocols:</b><br/>\n'
                                             "<div class='font-mono text-xs p-3 bg-slate-900 text-slate-100 rounded-xl "
                                             "my-2 leading-relaxed overflow-x-auto'>\n"
                                             'Protocol           │ Sender Window (Wₛ) │ Receiver Window (Wᵣ) │ '
                                             'Efficiency (η) Formula        │ Minimum Sequence Bits\n'
                                             '───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n'
                                             'Stop-and-Wait      │ 1                  │ 1                    │ η = 1 / '
                                             '(1 + 2a)              │ 1 bit (Seq 0 and 1)\n'
                                             'Go-Back-N (GBN)    │ N                  │ 1                    │ η = N / '
                                             '(1 + 2a) (max 100%)   │ ⌈log₂(N + 1)⌉ bits\n'
                                             'Selective Repeat   │ N                  │ N                    │ η = N / '
                                             '(1 + 2a) (max 100%)   │ ⌈log₂(2N)⌉ bits\n'
                                             '</div>',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: In Selective Repeat, Sender and Receiver '
                                                  'window sizes must satisfy: W_s + W_r ≤ 2^k (where k is number of '
                                                  'sequence bits). With W_s = W_r = N: N ≤ 2^(k-1)!',
                                  'number': '33.1',
                                  'title': 'Sliding Window Protocol Efficiency & Window Sizes'},
                                { 'content': '• <b>Carrier Sense Multiple Access with Collision Detection '
                                             '(CSMA/CD):</b><br/>\n'
                                             '&nbsp;&nbsp;- Used in classic half-duplex Ethernet.<br/>\n'
                                             '&nbsp;&nbsp;• <b>The Fundamental Collision Detection '
                                             'Condition:</b><br/>\n'
                                             '&nbsp;&nbsp;&nbsp;&nbsp;To detect a collision before transmission '
                                             'completes, the transmission time MUST be at least twice the propagation '
                                             'delay!<br/>\n'
                                             '&nbsp;&nbsp;&nbsp;&nbsp;<code>Tₜ ≥ 2 × Tₚ</code><br/>\n'
                                             '&nbsp;&nbsp;&nbsp;&nbsp;<code>(L_min / Bandwidth) ≥ 2 × (Distance / '
                                             'v)</code><br/>\n'
                                             '&nbsp;&nbsp;&nbsp;&nbsp;<code>L_min = 2 × Bandwidth × Tₚ</code>',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: If a packet is smaller than L_min, sender '
                                                  'finishes transmitting and assumes success before the collision '
                                                  'signal can travel back! This is why Ethernet has a mandatory '
                                                  'minimum frame size of 64 bytes.',
                                  'number': '33.2',
                                  'title': 'CSMA/CD & Minimum Frame Size Condition'}],
               'real_life_examples': [ { 'text': 'CSMA/CD is a room of polite people: listen before speaking (Carrier '
                                                 'Sense); if two people start talking at once, stop immediately and '
                                                 'wait a random delay (Exponential Backoff).',
                                         'title': 'Real-Life Analogy: Polite Group Discussion'}],
               'title': 'Data Link Layer, CRC & Medium Access Control (CSMA/CD)',
               'worked_examples': [ { 'answer': 'Minimum frame size is 1250 bytes (10,000 bits).',
                                      'problem': 'A 1 Gbps CSMA/CD network has a cable length of 1 km with signal '
                                                 'propagation speed 2 × 10⁸ m/s. What is the minimum frame size '
                                                 'required for reliable collision detection?',
                                      'steps': [ 'Step 1: Calculate propagation delay T_p = d / v = 1000 m / (2 × 10⁸ '
                                                 'm/s) = 5 × 10⁻⁶ s = 5 µs.',
                                                 'Step 2: Apply the CSMA/CD condition: T_t ≥ 2 × T_p ⇒ T_t_min = 2 × 5 '
                                                 'µs = 10 µs.',
                                                 'Step 3: Calculate minimum frame length L_min = Bandwidth × T_t_min = '
                                                 '(1 × 10⁹ bps) × (10 × 10⁻⁶ s) = 10,000 bits.',
                                                 'Step 4: Convert to bytes: 10,000 / 8 = 1250 bytes.'],
                                      'title': 'Worked Example: Minimum Frame Size in CSMA/CD'}]},
  ('CN', 2): { 'chapter_number': 34,
               'exam_traps': [ { 'title': 'HLEN 4-Byte Scaling vs Offset 8-Byte Scaling Trap',
                                 'warning': 'HLEN is scaled by 4 bytes (e.g. HLEN=6 means 24 bytes). Fragment Offset '
                                            'is scaled by 8 bytes (e.g. Offset=100 means byte 800). Never mix up these '
                                            'two scaling factors.'}],
               'foundations': [ { 'content': '• <b>CIDR Notation (/n):</b> IP address format <code>a.b.c.d / n</code> '
                                             'where n is the number of Network Prefix bits.<br/>\n'
                                             '&nbsp;&nbsp;• <b>Host bits (h):</b> <code>h = 32 - n</code>.<br/>\n'
                                             '&nbsp;&nbsp;• <b>Total IP Addresses in Subnet:</b> '
                                             '<code>2ʰ</code>.<br/>\n'
                                             '&nbsp;&nbsp;• <b>Usable Host Addresses:</b> <code>2ʰ - 2</code> '
                                             '(Subtract 2: Network ID with all 0 host bits, and Broadcast ID with all '
                                             '1 host bits).<br/><br/>\n'
                                             '\n'
                                             '• <b>Subnetting Example (/26):</b><br/>\n'
                                             '&nbsp;&nbsp;h = 32 - 26 = 6 bits. Total IPs = 2⁶ = 64. Usable hosts = 64 '
                                             '- 2 = 62 hosts per subnet.',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: Longest Prefix Match Rule: When a router '
                                                  'receives a packet, it compares the destination IP against all '
                                                  'routing table entries. If multiple routes match, the router '
                                                  'strictly picks the route with the LONGEST prefix (highest /n '
                                                  'value)!',
                                  'number': '34.1',
                                  'title': 'IPv4 Subnetting, CIDR & Usable Hosts'},
                                { 'content': '• <b>IPv4 Header Fields (Tested in GATE):</b><br/>\n'
                                             '&nbsp;&nbsp;• <b>Header Length (HLEN):</b> 4-bit field, scaled in '
                                             '<b>4-byte words</b>! Minimum HLEN = 5 (20 bytes); Maximum = 15 (60 '
                                             'bytes).<br/>\n'
                                             '&nbsp;&nbsp;• <b>Total Length:</b> 16 bits (max datagram size = 65,535 '
                                             'bytes).<br/>\n'
                                             '&nbsp;&nbsp;• <b>Fragmentation Offset:</b> 13 bits, measured in <b>units '
                                             'of 8 bytes</b>!<br/>\n'
                                             "&nbsp;&nbsp;• <b>Flags:</b> [ Reserved | DF (Don't Fragment) | MF (More "
                                             'Fragments) ].<br/>\n'
                                             '&nbsp;&nbsp;&nbsp;&nbsp;- If MF = 1: More fragments follow.<br/>\n'
                                             '&nbsp;&nbsp;&nbsp;&nbsp;- If MF = 0: Last fragment (or unfragmented '
                                             'packet).',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: The fragmentation offset field stores: '
                                                  '(Original Data Byte Offset) / 8! The payload size of every fragment '
                                                  '(except the last) MUST be a multiple of 8 bytes.',
                                  'number': '34.2',
                                  'title': 'IPv4 Header & Packet Fragmentation'}],
               'real_life_examples': [ { 'text': 'NAT is the receptionist in an office: your laptop, phone, and TV '
                                                 'share 1 public IP address, and the NAT table routes incoming '
                                                 'responses to your device via internal port numbers.',
                                         'title': 'Real-Life Analogy: NAT Router & Home Wi-Fi'}],
               'title': 'Routing Protocols & IPv4 Addressing (CIDR, Fragmentation, NAT)',
               'worked_examples': [ { 'answer': 'Fragment 2: Payload = 1480 bytes, MF = 1, Offset = 185.',
                                      'problem': 'An IPv4 datagram of 4000 bytes (20 bytes header + 3980 bytes '
                                                 'payload) arrives at a router whose outgoing link has an MTU of 1500 '
                                                 'bytes. Find the payload size, MF flag, and Offset of the second '
                                                 'fragment.',
                                      'steps': [ 'Step 1: MTU = 1500 bytes. Including 20 bytes IP header, maximum data '
                                                 'payload per fragment = 1500 - 20 = 1480 bytes.',
                                                 'Step 2: Check multiple of 8: 1480 / 8 = 185 (perfect multiple of '
                                                 '8!).',
                                                 'Step 3: Fragment 1: Payload = 1480 bytes (bytes 0 to 1479). MF = 1. '
                                                 'Offset = 0 / 8 = 0.',
                                                 'Step 4: Fragment 2: Takes next 1480 bytes (bytes 1480 to 2959). MF = '
                                                 '1. Offset = 1480 / 8 = 185.',
                                                 'Step 5: Fragment 3: Remaining data = 3980 - 1480 - 1480 = 1020 bytes '
                                                 '(bytes 2960 to 3979). MF = 0. Offset = 2960 / 8 = 370.'],
                                      'title': 'Worked Example: IPv4 Packet Fragmentation Trace'}]},
  ('CN', 3): { 'chapter_number': 35,
               'exam_traps': [ { 'title': 'TCP Acknowledgment Number Trap',
                                 'warning': "TCP ACK is cumulative: Ack = N means 'I have received all bytes up to N - "
                                            "1 successfully, and I am expecting byte N next'."}],
               'foundations': [ { 'content': '• <b>TCP 3-Way Handshake:</b><br/>\n'
                                             '&nbsp;&nbsp;1. Client → Server: <code>SYN, Seq = x</code>.<br/>\n'
                                             '&nbsp;&nbsp;2. Server → Client: <code>SYN + ACK, Seq = y, Ack = x + '
                                             '1</code>.<br/>\n'
                                             '&nbsp;&nbsp;3. Client → Server: <code>ACK, Seq = x + 1, Ack = y + '
                                             '1</code>.<br/><br/>\n'
                                             '\n'
                                             '• <b>TCP Congestion Control Phases:</b><br/>\n'
                                             '&nbsp;&nbsp;1. <b>Slow Start:</b> <code>cwnd</code> starts at 1 MSS and '
                                             '<b>DOUBLES every RTT</b> (Exponential growth: 1, 2, 4, 8...).<br/>\n'
                                             '&nbsp;&nbsp;2. <b>Congestion Avoidance:</b> When <code>cwnd ≥ Threshold '
                                             '(ssthresh)</code>, growth becomes linear: <b>increases by 1 MSS every '
                                             'RTT</b> (Additive Increase).<br/>\n'
                                             '&nbsp;&nbsp;3. <b>On Timeout (Severe Congestion):</b><br/>\n'
                                             '&nbsp;&nbsp;&nbsp;&nbsp;- <code>ssthresh = cwnd / 2</code>.<br/>\n'
                                             '&nbsp;&nbsp;&nbsp;&nbsp;- <code>cwnd = 1 MSS</code> (Resets back to slow '
                                             'start!).<br/>\n'
                                             '&nbsp;&nbsp;4. <b>On 3 Duplicate ACKs (TCP Tahoe vs Reno):</b><br/>\n'
                                             '&nbsp;&nbsp;&nbsp;&nbsp;- Tahoe: cwnd resets to 1 MSS.<br/>\n'
                                             '&nbsp;&nbsp;&nbsp;&nbsp;- Reno (Fast Recovery): <code>ssthresh = cwnd / '
                                             '2</code>, and <code>cwnd = ssthresh</code> (Skips slow start, continues '
                                             'linear growth!).',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: Sequence number consumes 1 number for SYN '
                                                  'and FIN flags! ACK packets that carry no data do NOT consume '
                                                  'sequence numbers.',
                                  'number': '35.1',
                                  'title': 'TCP 3-Way Handshake & Congestion Control'},
                                { 'content': '• <b>DNS (Domain Name System - Port 53):</b><br/>\n'
                                             '&nbsp;&nbsp;• Uses <b>UDP</b> for standard client queries (fast, low '
                                             'overhead). Uses <b>TCP</b> for zone transfers.<br/>\n'
                                             '&nbsp;&nbsp;• <b>Iterative Query:</b> Server replies with the referral '
                                             'address of next server. Client does the walking.<br/>\n'
                                             '&nbsp;&nbsp;• <b>Recursive Query:</b> Server resolves the full name on '
                                             "client's behalf and returns final IP.<br/><br/>\n"
                                             '\n'
                                             '• <b>HTTP Protocols:</b><br/>\n'
                                             '&nbsp;&nbsp;• <b>HTTP/1.0:</b> Non-persistent (1 TCP handshake per '
                                             'image/file).<br/>\n'
                                             '&nbsp;&nbsp;• <b>HTTP/1.1:</b> Persistent connections (re-uses TCP '
                                             'connection; suffers from Head-of-Line blocking).<br/>\n'
                                             '&nbsp;&nbsp;• <b>HTTP/2:</b> Binary framing, multiplexing multiple '
                                             'streams over a single TCP connection.',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: Persistent HTTP without pipelining takes 1 '
                                                  'RTT per referenced object. Persistent HTTP WITH pipelining takes 1 '
                                                  'RTT total for all referenced objects.',
                                  'number': '35.2',
                                  'title': 'Application Layer: DNS Resolution & HTTP/1.1 vs HTTP/2'}],
               'real_life_examples': [ { 'text': 'TCP slow start rapidly expands your YouTube video buffer during '
                                                 'initial loading, then stabilizes into linear mode once smooth 4K '
                                                 'playback is achieved.',
                                         'title': 'Real-Life Analogy: Video Streaming Buffer'}],
               'title': 'Transport Layer (TCP), Sockets & Application Protocols (DNS, HTTP)',
               'worked_examples': [ { 'answer': 'cwnd in round 7 is 18 MSS.',
                                      'problem': 'A TCP connection has ssthresh = 16 MSS. In round 1, cwnd = 1 MSS. '
                                                 'Assuming no packet loss occurs, what is the size of cwnd in round 7?',
                                      'steps': [ 'Step 1: Round 1: cwnd = 1 MSS (Slow start).',
                                                 'Step 2: Round 2: cwnd = 2 MSS.',
                                                 'Step 3: Round 3: cwnd = 4 MSS.',
                                                 'Step 4: Round 4: cwnd = 8 MSS.',
                                                 'Step 5: Round 5: cwnd = 16 MSS (Hits ssthresh = 16! Switches to '
                                                 'Congestion Avoidance).',
                                                 'Step 6: Round 6: cwnd = 16 + 1 = 17 MSS (Linear growth).',
                                                 'Step 7: Round 7: cwnd = 17 + 1 = 18 MSS.'],
                                      'title': 'Worked Example: TCP Congestion Window Calculation'}]},
  ('DB', 0): { 'chapter_number': 29,
               'exam_traps': [ { 'title': 'SQL NULL Comparison with Equality Trap',
                                 'warning': "In SQL, comparing anything to NULL with '=' (e.g. 'salary = NULL') "
                                            "evaluates to UNKNOWN, never TRUE! Always use 'IS NULL' or 'IS NOT "
                                            "NULL'."}],
               'foundations': [ { 'content': '• <b>Cardinality Ratios & Table Merging Rules:</b><br/>\n'
                                             "<div class='font-mono text-xs p-3 bg-slate-900 text-slate-100 rounded-xl "
                                             "my-2 leading-relaxed overflow-x-auto'>\n"
                                             'Relationship Type │ Cardinality / Participation        │ Minimum '
                                             'Relational Tables Needed\n'
                                             '─────────────────────────────────────────────────────────────────────────────────────────────\n'
                                             'Many-to-Many (M:N)│ Any participation                  │ 3 Tables (Table '
                                             'A, Table B, Table AB)\n'
                                             'One-to-Many (1:N) │ Any participation                  │ 2 Tables '
                                             "(Foreign key placed on the 'MANY' side!)\n"
                                             'One-to-One (1:1)  │ Partial on both sides (0..1, 0..1) │ 2 Tables '
                                             '(Foreign key on either side with UNIQUE constraint)\n'
                                             'One-to-One (1:1)  │ Total on one side (1..1, 0..1)     │ 2 Tables '
                                             '(Foreign key placed on the TOTAL participation side!)\n'
                                             'One-to-One (1:1)  │ Total on BOTH sides (1..1, 1..1)   │ 1 SINGLE MERGED '
                                             'TABLE (Combines both entities!)\n'
                                             '</div>\n'
                                             '\n'
                                             '• <b>Weak Entity Sets:</b><br/>\n'
                                             '&nbsp;&nbsp;- Does not have sufficient attributes to form a primary '
                                             'key.<br/>\n'
                                             '&nbsp;&nbsp;- Depends on an <b>Identifying Strong Entity</b> via an '
                                             '<b>Identifying Relationship</b>.<br/>\n'
                                             '&nbsp;&nbsp;- <b>Primary Key of Weak Entity:</b> <code>Primary Key of '
                                             'Strong Entity + Discriminator (Partial Key)</code>.<br/>\n'
                                             '&nbsp;&nbsp;- Weak entity and its identifying relationship are ALWAYS '
                                             'merged into a single table!',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: In 1:N relationship, NEVER place the '
                                                  'foreign key on the 1-side (causes massive NULL or multivalued '
                                                  'redundancy)! Always place the foreign key on the N-side.',
                                  'number': '29.1',
                                  'title': 'ER to Relational Table Conversion Rules (Minimal Tables)'},
                                { 'content': '• <b>Core Relational Algebra Operators:</b><br/>\n'
                                             '&nbsp;&nbsp;• <b>Selection (σ_condition):</b> Filters rows (horizontal '
                                             'subset).<br/>\n'
                                             '&nbsp;&nbsp;• <b>Projection (π_attributes):</b> Selects columns '
                                             '(vertical subset; eliminates duplicates).<br/>\n'
                                             '&nbsp;&nbsp;• <b>Cross Product (R × S):</b> Combines every tuple of R '
                                             'with every tuple of S.<br/>\n'
                                             '&nbsp;&nbsp;• <b>Natural Join (R ⋈ S):</b> Equi-join on all shared '
                                             'common attributes, eliminating redundant duplicate columns.<br/><br/>\n'
                                             '\n'
                                             '• <b>The Division Operator (R ÷ S):</b><br/>\n'
                                             "&nbsp;&nbsp;- Used to answer queries containing the word <b>'FOR "
                                             "ALL'</b> (e.g. <i>'Find students who have enrolled in ALL courses "
                                             "offered by Prof. Rao'</i>).<br/>\n"
                                             '&nbsp;&nbsp;- Result schema: Attributes in R that are NOT in S: '
                                             '<code>Schema(R ÷ S) = Schema(R) - Schema(S)</code>.<br/>\n'
                                             '&nbsp;&nbsp;- Formal formula: <code>R ÷ S = π_{R-S}(R) - π_{R-S}( '
                                             '(π_{R-S}(R) × S) - R )</code>.',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: Tuple Relational Calculus (TRC) and Domain '
                                                  'Relational Calculus (DRC) are equivalent in expressive power to '
                                                  "Relational Algebra (Codd's Theorem). SQL is declarative, based "
                                                  'directly on TRC.',
                                  'number': '29.2',
                                  'title': 'Relational Algebra: Joins, Division & Calculus'}],
               'real_life_examples': [ { 'text': 'A university database uses M:N relationship tables: Students and '
                                                 "Courses connect through an 'Enrollment' bridge table that stores "
                                                 'grades and semester dates.',
                                         'title': 'Real-Life Analogy: University Enrollment Database'}],
               'title': 'ER-Model, Relational Algebra & SQL',
               'worked_examples': [ { 'answer': 'Minimum 2 tables required.',
                                      'problem': 'An ER diagram has entities Student and Department. A student belongs '
                                                 'to at most one department, and a department can have multiple '
                                                 'students. Both have partial participation. How many minimum '
                                                 'relational tables are needed?',
                                      'steps': [ 'Step 1: Identify cardinality ratio: Department-to-Student is '
                                                 'One-to-Many (1:N).',
                                                 'Step 2: Recall the 1:N table conversion rule: We can merge the '
                                                 "relationship table into the entity table on the 'MANY' side "
                                                 '(Student).',
                                                 'Step 3: Table 1: Department(Dept_ID, Dept_Name) with Dept_ID as '
                                                 'Primary Key.',
                                                 'Step 4: Table 2: Student(Roll_No, Name, Dept_ID) with Roll_No as '
                                                 'Primary Key, and Dept_ID as Foreign Key referencing Department.',
                                                 'Step 5: Minimum tables required = 2.'],
                                      'title': 'Worked Example: Minimum Relational Tables from ER Diagram'}]},
  ('DB', 1): { 'chapter_number': 30,
               'exam_traps': [ { 'title': 'All-Prime Attributes Guarantee 3NF Trap',
                                 'warning': 'If all attributes in a relation are Prime Attributes, the relation is '
                                            'GUARANTEED to be in 3NF! However, it may still violate BCNF.'}],
               'foundations': [ { 'content': '• <b>Attribute Closure (X⁺):</b> The set of all attributes functionally '
                                             'determined by attribute set X.<br/><br/>\n'
                                             '\n'
                                             '• <b>Step-by-Step Candidate Key Finding Algorithm:</b><br/>\n'
                                             '&nbsp;&nbsp;1. <b>Essential Attributes (Must be in every Candidate '
                                             'Key):</b> Attributes that appear ONLY on the LHS of dependencies, or '
                                             'never appear in any dependency.<br/>\n'
                                             '&nbsp;&nbsp;2. <b>Non-Essential Attributes:</b> Attributes that appear '
                                             'ONLY on the RHS can NEVER be part of any minimal candidate key!<br/>\n'
                                             '&nbsp;&nbsp;3. Compute closure of essential attributes. If it derives '
                                             'all attributes, it is the <b>UNIQUE Candidate Key</b>.<br/>\n'
                                             '&nbsp;&nbsp;4. If not, combine with intermediate attributes until '
                                             'closure covers the entire relation schema.',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: Prime Attribute: Any attribute that is a '
                                                  'part of AT LEAST ONE Candidate Key. Non-Prime Attribute: An '
                                                  'attribute that does NOT belong to ANY Candidate Key.',
                                  'number': '30.1',
                                  'title': 'Candidate Keys & Attribute Closure Algorithm'},
                                { 'content': '• <b>Hierarchical Normal Forms Decision Checklist:</b><br/>\n'
                                             "<div class='font-mono text-xs p-3 bg-slate-900 text-slate-100 rounded-xl "
                                             "my-2 leading-relaxed overflow-x-auto'>\n"
                                             'Normal Form │ Violation Condition to Check '
                                             'For                               │ Required Standard\n'
                                             '────────────────────────────────────────────────────────────────────────────────────────────────────────────\n'
                                             '1NF         │ Multi-valued or composite attributes '
                                             'exist                      │ All attribute values are ATOMIC\n'
                                             '2NF         │ Partial Dependency: Proper Subset of Key → Non-Prime '
                                             'Attribute  │ NO Partial Dependencies!\n'
                                             '3NF         │ Transitive Dependency: Non-Prime → Non-Prime '
                                             'Attribute          │ For every X → Y: X is Superkey OR Y is Prime\n'
                                             'BCNF        │ Any functional dependency where LHS is not a '
                                             'Superkey           │ For EVERY X → Y: X MUST be a Superkey!\n'
                                             '</div>\n'
                                             '\n'
                                             '• <b>Decomposition Properties (Lossless vs Dependency '
                                             'Preserving):</b><br/>\n'
                                             '&nbsp;&nbsp;• <b>Lossless Join Condition:</b> R₁ ∩ R₂ → R₁ OR R₁ ∩ R₂ → '
                                             'R₂ (The common attribute must be a Superkey in at least one '
                                             'table!).<br/>\n'
                                             '&nbsp;&nbsp;• <b>Decomposition into 3NF:</b> Always guarantees BOTH '
                                             'Lossless Join AND Dependency Preservation!<br/>\n'
                                             '&nbsp;&nbsp;• <b>Decomposition into BCNF:</b> Always guarantees Lossless '
                                             'Join, but <b>MAY NOT PRESERVE DEPENDENCIES</b>!',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: Any binary decomposition into two tables R₁ '
                                                  'and R₂ is LOSSLESS if and only if their common attribute (R₁ ∩ R₂) '
                                                  'forms a candidate key of R₁ or R₂!',
                                  'number': '30.2',
                                  'title': 'The Step-by-Step Normal Forms Checklist (1NF to BCNF)'}],
               'real_life_examples': [ { 'text': "Normalization eliminates anomalies: if a customer's address is "
                                                 'stored in every invoice row, updating their address requires '
                                                 'updating 1,000 rows (update anomaly) or risks inconsistent data.',
                                         'title': 'Real-Life Analogy: Eliminating Redundant Billing Data'}],
               'title': 'Functional Dependencies & Normalization (1NF to BCNF)',
               'worked_examples': [ { 'answer': 'The relation R is in 3NF, but NOT in BCNF.',
                                      'problem': 'Given relation R(A, B, C, D) with FDs: {AB → C, C → D, D → A}. What '
                                                 'is the highest normal form of R?',
                                      'steps': [ 'Step 1: Find candidate keys. Compute closures: (AB)⁺ = {A, B, C, D}. '
                                                 'Since C → D and D → A: (BC)⁺ = {B, C, D, A}. (BD)⁺ = {B, D, A, C}.',
                                                 'Step 2: Candidate Keys are AB, BC, BD.',
                                                 'Step 3: Prime attributes = {A, B, C, D}. ALL attributes are prime!',
                                                 'Step 4: Check 2NF: No non-prime attributes exist, so no partial '
                                                 'dependencies. Satisfies 2NF.',
                                                 'Step 5: Check 3NF: In every FD X → Y, RHS (Y) is a prime attribute! '
                                                 'Since RHS is prime, 3NF condition is satisfied for ALL FDs. '
                                                 'Satisfies 3NF.',
                                                 'Step 6: Check BCNF: For C → D, C is not a superkey! For D → A, D is '
                                                 'not a superkey! Hence, BCNF is VIOLATED.'],
                                      'title': 'Worked Example: Highest Normal Form Identification'}]},
  ('DB', 2): { 'chapter_number': 31,
               'exam_traps': [ { 'title': 'Two-Phase Locking (2PL) vs Deadlock Trap',
                                 'warning': 'Strict 2PL guarantees Conflict Serializability and prevents Cascading '
                                            'Aborts, but IT DOES NOT PREVENT DEADLOCKS! Systems using 2PL can still '
                                            'deadlock.'}],
               'foundations': [ { 'content': '• <b>Key Structural Differences:</b><br/>\n'
                                             '&nbsp;&nbsp;• <b>B-Tree:</b> Both Internal nodes and Leaf nodes store '
                                             'data records / record pointers.<br/>\n'
                                             '&nbsp;&nbsp;• <b>B+ Tree:</b> Internal nodes store ONLY search keys and '
                                             'child tree pointers. <b>ALL data records / record pointers are stored '
                                             'strictly in the LEAF nodes!</b> Leaf nodes are linked as a Doubly Linked '
                                             'List for blazing fast range queries.<br/><br/>\n'
                                             '\n'
                                             '• <b>B+ Tree Node Order (p) Sizing Equations:</b><br/>\n'
                                             '&nbsp;&nbsp;Given: Block Size = B bytes, Key Size = K bytes, Record '
                                             'Pointer = R bytes, Block/Child Pointer = P bytes.<br/>\n'
                                             '&nbsp;&nbsp;• <b>Internal Node Equation:</b> <code>p · P + (p - 1) · K ≤ '
                                             'B</code>.<br/>\n'
                                             '&nbsp;&nbsp;• <b>Leaf Node Equation:</b> <code>q · (K + R) + P ≤ '
                                             'B</code> (where P is the sibling leaf pointer).',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: In a B+ tree of order p: Root has at least '
                                                  '2 children. Internal nodes have at least ⌈p / 2⌉ children. Leaves '
                                                  'have at least ⌈(p - 1) / 2⌉ keys.',
                                  'number': '31.1',
                                  'title': 'B-Tree vs B+ Tree Node Capacity Calculations'},
                                { 'content': '• <b>Conflict Operations:</b> Two operations on the same data item by '
                                             'different transactions where <b>at least ONE operation is a WRITE</b> '
                                             '(R-W, W-R, W-W).<br/><br/>\n'
                                             '\n'
                                             '• <b>Precedence Graph (Testing Conflict Serializability):</b><br/>\n'
                                             '&nbsp;&nbsp;1. Create a vertex for each transaction Tᵢ.<br/>\n'
                                             '&nbsp;&nbsp;2. Draw directed edge Tᵢ → Tⱼ if an operation of Tᵢ precedes '
                                             'a conflicting operation of Tⱼ.<br/>\n'
                                             '&nbsp;&nbsp;3. <b>The Serializability Theorem:</b> A schedule is '
                                             'Conflict Serializable if and only if the <b>Precedence Graph is ACYCLIC '
                                             '(contains NO cycles)</b>!<br/>\n'
                                             '&nbsp;&nbsp;4. The equivalent serial schedule order is obtained via '
                                             '<b>Topological Sort</b> of the precedence graph.',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: Conflict Serializable ⇒ View Serializable. '
                                                  'But View Serializable does NOT imply Conflict Serializable! View '
                                                  'serializable schedules with cycles require Blind Writes.',
                                  'number': '31.2',
                                  'title': 'Conflict Serializability & Precedence Graphs'}],
               'real_life_examples': [ { 'text': 'ACID Atomicity ensures that if the ATM cash dispenser jams after '
                                                 'your bank balance is deducted, the entire transaction rolls back '
                                                 'automatically so you never lose money.',
                                         'title': 'Real-Life Analogy: ATM Cash Withdrawal & ACID'}],
               'title': 'B/B+ Trees, Transactions & Concurrency Control',
               'worked_examples': [ { 'answer': 'Maximum order p = 57 child pointers.',
                                      'problem': 'A disk block size is 1024 bytes. Data keys are 12 bytes, child tree '
                                                 'pointers are 6 bytes. Find the maximum order (fan-out) p of an '
                                                 'internal node in a B+ tree.',
                                      'steps': [ 'Step 1: Formula for internal node: p · P + (p - 1) · K ≤ Block Size.',
                                                 'Step 2: Substitute values: p(6) + (p - 1)(12) ≤ 1024.',
                                                 'Step 3: Simplify: 6p + 12p - 12 ≤ 1024 ⇒ 18p ≤ 1036.',
                                                 'Step 4: Solve for p: p ≤ 1036 / 18 ≈ 57.55.',
                                                 'Step 5: Since order must be an integer: p = 57.'],
                                      'title': 'Worked Example: B+ Tree Internal Node Order'}]},
  ('GA', 0): { 'chapter_number': 36,
               'exam_traps': [ { 'title': 'The False Friend Relative Pronoun Trap',
                                 'warning': "'One of the students who HAVE passed' vs 'The ONLY one of the students "
                                            "who HAS passed'. In 'one of those who', the antecedent is the plural "
                                            'noun!'}],
               'foundations': [ { 'content': '• <b>Fundamental Concord Rule:</b> A singular subject takes a singular '
                                             'verb; a plural subject takes a plural verb.<br/><br/>\n'
                                             '\n'
                                             '• <b>High-Yield GATE Grammar Rules:</b><br/>\n'
                                             '&nbsp;&nbsp;1. <b>Rule of Proximity (Neither... Nor, Either... Or):</b> '
                                             'The verb agrees with the subject CLOSER to it!<br/>\n'
                                             "&nbsp;&nbsp;&nbsp;&nbsp;- <i>'Neither the manager nor the <u>employees "
                                             "were</u> present.'</i><br/>\n"
                                             "&nbsp;&nbsp;&nbsp;&nbsp;- <i>'Neither the employees nor the <u>manager "
                                             "was</u> present.'</i><br/>\n"
                                             "&nbsp;&nbsp;2. <b>Intervening Phrases:</b> Phrases like <i>'as well "
                                             "as'</i>, <i>'along with'</i>, <i>'together with'</i> DO NOT change "
                                             'subject number!<br/>\n'
                                             "&nbsp;&nbsp;&nbsp;&nbsp;- <i>'The President, along with his advisors, "
                                             "<b>is</b> arriving.'</i> (Subject is singular 'President').<br/>\n"
                                             '&nbsp;&nbsp;3. <b>Collective Nouns:</b> Singular when acting as a '
                                             "unified unit (<i>'The committee <b>has</b> reached a consensus'</i>); "
                                             "Plural when acting individually (<i>'The committee <b>are</b> divided in "
                                             "their opinions'</i>).",
                                  'crucial_rule': "🎯 GOLDEN RULE FOR GATE: In sentences beginning with 'Each of...', "
                                                  "'Either of...', 'Neither of...', the subject is strictly SINGULAR! "
                                                  "Always use singular verb: 'Each of the students IS prepared'.",
                                  'number': '36.1',
                                  'title': 'Subject-Verb Agreement (Concord) Rules'},
                                { 'content': '• <b>Definitions:</b><br/>\n'
                                             '&nbsp;&nbsp;• <b>Fact:</b> Explicitly stated truth in the passage.<br/>\n'
                                             '&nbsp;&nbsp;• <b>Inference:</b> A logical deduction that is 100% '
                                             'guaranteed to be true based on the passage.<br/>\n'
                                             '&nbsp;&nbsp;• <b>Assumption:</b> An UNSTATED premise that the author '
                                             'MUST believe to be true for the conclusion to stand.<br/><br/>\n'
                                             '\n'
                                             '• <b>The Negation Test for Assumptions:</b><br/>\n'
                                             '&nbsp;&nbsp;- To verify if an option is a valid assumption: <b>Negate '
                                             'the option</b>.<br/>\n'
                                             '&nbsp;&nbsp;- If negating the option <b>DESTROYS or INVALIDATES the '
                                             "author's argument</b>, that option is the correct mandatory assumption!",
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: In reading comprehension, beware of extreme '
                                                  "words like 'always', 'never', 'all', 'none'. Unless explicitly "
                                                  'supported by the text, extreme answer choices are almost always '
                                                  'traps.',
                                  'number': '36.2',
                                  'title': 'Critical Reasoning: Assumptions, Inferences & Conclusions'}],
               'real_life_examples': [ { 'text': 'Critical reasoning is courtroom law: an inference is proven forensic '
                                                 'evidence; an assumption is an unproven hypothesis that must hold for '
                                                 "the prosecution's case to make sense.",
                                         'title': 'Real-Life Analogy: Courtroom Evidence vs Hearsay'}],
               'title': 'Verbal Aptitude - Grammar, Vocabulary & Comprehension',
               'worked_examples': [ { 'answer': "Correct verb: 'lends'",
                                      'problem': "Choose the grammatically correct option: 'A bouquet of yellow roses "
                                                 "_____ (lend / lends) a vibrant color to the room.'",
                                      'steps': [ 'Step 1: Identify the grammatical subject. The prepositional phrase '
                                                 "is 'of yellow roses'.",
                                                 "Step 2: The actual head noun of the subject is 'A bouquet' "
                                                 '(Singular).',
                                                 "Step 3: A singular subject requires a singular verb with an 's' "
                                                 "ending ('lends').",
                                                 "Step 4: The plural noun 'roses' is an object of the preposition, not "
                                                 'the subject.'],
                                      'title': 'Worked Example: Subject-Verb Agreement Selection'}]},
  ('GA', 1): { 'chapter_number': 37,
               'exam_traps': [ { 'title': 'Average Speed Arithmetic Mean Trap',
                                 'warning': 'Traveling distance d at 40 km/hr and returning at 60 km/hr gives average '
                                            'speed 2(40)(60)/(40+60) = 48 km/hr, NOT 50 km/hr! Arithmetic mean is '
                                            'strictly wrong.'}],
               'foundations': [ { 'content': '• <b>Fundamental Formula:</b> <code>Distance = Speed × '
                                             'Time</code>.<br/>\n'
                                             '&nbsp;&nbsp;• Conversion: <code>1 km/hr = 5 / 18 m/s</code>.<br/><br/>\n'
                                             '\n'
                                             '• <b>Relative Speed Mechanics:</b><br/>\n'
                                             '&nbsp;&nbsp;• Moving in <b>OPPOSITE</b> directions: <code>S_rel = S₁ + '
                                             'S₂</code>.<br/>\n'
                                             '&nbsp;&nbsp;• Moving in the <b>SAME</b> direction: <code>S_rel = |S₁ - '
                                             'S₂|</code>.<br/><br/>\n'
                                             '\n'
                                             '• <b>Boats and Streams:</b><br/>\n'
                                             '&nbsp;&nbsp;• Let boat speed in still water = u, stream speed = v.<br/>\n'
                                             '&nbsp;&nbsp;• Downstream speed: <code>D = u + v</code>.<br/>\n'
                                             '&nbsp;&nbsp;• Upstream speed: <code>U = u - v</code>.<br/>\n'
                                             '&nbsp;&nbsp;• <code>u = (D + U) / 2</code>, <code>v = (D - U) / '
                                             '2</code>.<br/><br/>\n'
                                             '\n'
                                             '• <b>Average Speed for Equal Distances:</b><br/>\n'
                                             '&nbsp;&nbsp;<code>S_avg = (2 · S₁ · S₂) / (S₁ + S₂)</code> (Harmonic '
                                             'Mean, NOT Arithmetic Mean!).',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: If a train of length L passes a standing '
                                                  'person/pole, distance covered is L. If it passes a platform/bridge '
                                                  'of length P, distance covered is L + P!',
                                  'number': '37.1',
                                  'title': 'Time, Speed, Distance & Relative Speed'},
                                { 'content': '• <b>Work-Rate Equivalence:</b><br/>\n'
                                             "&nbsp;&nbsp;If person A finishes work in X days, A's 1-day work rate = "
                                             '<code>1 / X</code>.<br/>\n'
                                             '&nbsp;&nbsp;• Combined rate of A and B: <code>1/X + 1/Y = (X + Y) / '
                                             '(XY)</code>.<br/>\n'
                                             '&nbsp;&nbsp;• Time taken together: <code>T = (X · Y) / (X + '
                                             'Y)</code>.<br/><br/>\n'
                                             '\n'
                                             '• <b>LCM Method (Fastest Exam Technique):</b><br/>\n'
                                             '&nbsp;&nbsp;1. Assume Total Work = LCM of individual days.<br/>\n'
                                             '&nbsp;&nbsp;2. Calculate individual daily efficiency = Total Work / '
                                             'Individual days.<br/>\n'
                                             '&nbsp;&nbsp;3. Total Time = Total Work / Combined Efficiency.',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: In Pipes and Cisterns, an inlet pipe has '
                                                  'positive efficiency (+E), while an outlet/leak pipe has negative '
                                                  'efficiency (-E)!',
                                  'number': '37.2',
                                  'title': 'Work and Time & Pipes and Cisterns'}],
               'real_life_examples': [ { 'text': 'Work and time calculations mirror software sprint velocity: 3 '
                                                 'developers finishing 15 story points together allows planning '
                                                 'parallel delivery schedules.',
                                         'title': 'Real-Life Analogy: Project Sprints in Tech'}],
               'title': 'Quantitative Aptitude - Arithmetic, Algebra & Mensuration',
               'worked_examples': [ { 'answer': 'Train speeds are 30 m/s and 20 m/s (108 km/hr and 72 km/hr).',
                                      'problem': 'Two trains of length 150 m and 250 m run on parallel tracks. When '
                                                 'running in the same direction, the faster train passes the slower in '
                                                 '40 seconds. When running in opposite directions, they pass each '
                                                 'other in 8 seconds. Find the speeds of both trains.',
                                      'steps': [ 'Step 1: Total distance covered in passing = Sum of lengths = 150 + '
                                                 '250 = 400 m.',
                                                 'Step 2: Same direction relative speed S₁ - S₂ = Distance / Time = '
                                                 '400 m / 40 s = 10 m/s.',
                                                 'Step 3: Opposite direction relative speed S₁ + S₂ = Distance / Time '
                                                 '= 400 m / 8 s = 50 m/s.',
                                                 'Step 4: Solve system: (S₁ + S₂) + (S₁ - S₂) = 50 + 10 ⇒ 2S₁ = 60 ⇒ '
                                                 'S₁ = 30 m/s (108 km/hr).',
                                                 'Step 5: S₂ = 50 - 30 = 20 m/s (72 km/hr).'],
                                      'title': 'Worked Example: Relative Speed Train Crossing'}]},
  ('GA', 2): { 'chapter_number': 38,
               'exam_traps': [ { 'title': 'Reflex Angle vs Interior Angle Trap',
                                 'warning': 'If the question asks for the angle between hands, the standard answer is '
                                            'the interior angle (≤ 180°). If the formula gives > 180°, subtract from '
                                            '360°.'}],
               'foundations': [ { 'content': '• <b>Clock Angle Formula:</b><br/>\n'
                                             '&nbsp;&nbsp;The angle θ between Hour hand and Minute hand at H hours and '
                                             'M minutes is:<br/>\n'
                                             '&nbsp;&nbsp;<code>θ = | 30H - (11 / 2) M |</code><br/>\n'
                                             '&nbsp;&nbsp;• Speed of Minute hand: <code>6° per minute</code>.<br/>\n'
                                             '&nbsp;&nbsp;• Speed of Hour hand: <code>0.5° per minute</code>.<br/>\n'
                                             '&nbsp;&nbsp;• Relative speed of Minute hand over Hour hand: <code>5.5° = '
                                             '(11 / 2)° per minute</code>.<br/><br/>\n'
                                             '\n'
                                             '• <b>Calendar Odd Days:</b><br/>\n'
                                             '&nbsp;&nbsp;• Ordinary Year (365 days): 52 weeks + <b>1 odd '
                                             'day</b>.<br/>\n'
                                             '&nbsp;&nbsp;• Leap Year (366 days): 52 weeks + <b>2 odd days</b>.<br/>\n'
                                             '&nbsp;&nbsp;• Centenary Years: Leap year only if divisible by <b>400</b> '
                                             '(1600, 2000 are leap; 1900 is NOT a leap year!).',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: The hands of a clock coincide (overlap) '
                                                  'exactly 22 times in 24 hours (not 24 times!), because between 11 '
                                                  'and 1 they coincide only once at 12:00.',
                                  'number': '38.1',
                                  'title': 'Clock Angles & Calendar Mathematics'},
                                { 'content': '• <b>Cube & Dice Opposites Rule:</b><br/>\n'
                                             '&nbsp;&nbsp;- On an unfolded standard cross dice: <b>Alternate faces '
                                             'along any straight line are OPPOSITE to each other</b>!<br/>\n'
                                             '&nbsp;&nbsp;- Two opposite faces can NEVER share an edge or vertex, and '
                                             'can NEVER appear simultaneously in any single 2D projection '
                                             'view.<br/><br/>\n'
                                             '\n'
                                             '• <b>Mirror & Water Reflections:</b><br/>\n'
                                             '&nbsp;&nbsp;• <b>Mirror Image:</b> Left and Right swap; Top and Bottom '
                                             'remain unchanged.<br/>\n'
                                             '&nbsp;&nbsp;• <b>Water Reflection:</b> Top and Bottom swap; Left and '
                                             'Right remain unchanged.',
                                  'crucial_rule': '🎯 GOLDEN RULE FOR GATE: In spatial paper folding questions: '
                                                  'Mentally trace the folds in REVERSE order. Each unfolding step '
                                                  'creates a symmetric reflection across the crease line.',
                                  'number': '38.2',
                                  'title': 'Spatial Aptitude: 2D/3D Rotations, Paper Folding & Unfolding'}],
               'real_life_examples': [ { 'text': 'Spatial aptitude tests the mechanical engineering ability to '
                                                 'visualize 3D mechanical components from top, front, and side 2D '
                                                 'technical drawings.',
                                         'title': 'Real-Life Analogy: 3D CAD Modeling & Orthographic Views'}],
               'title': 'Analytical & Spatial Aptitude - Logic, Reasoning & 2D/3D Shapes',
               'worked_examples': [ { 'answer': 'Angle is 130°.',
                                      'problem': 'Find the angle between the hands of a clock at 3:40.',
                                      'steps': [ 'Step 1: Identify values: H = 3, M = 40.',
                                                 'Step 2: Apply clock angle formula: θ = | 30H - (11 / 2)M |.',
                                                 'Step 3: Substitute: θ = | 30(3) - (11 / 2)(40) | = | 90 - 220 | = | '
                                                 '-130 | = 130°.',
                                                 'Step 4: Check if reflex angle is asked. Normal angle = 130°, Reflex '
                                                 'angle = 360° - 130° = 230°.'],
                                      'title': 'Worked Example: Angle Between Clock Hands'}]}}
