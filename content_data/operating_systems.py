# Operating Systems Content Module for GATE 2027 CSE
# Weightage: 8-10 Marks

SUBJECT_META = {
    "id": "OS",
    "name": "Operating System",
    "folder": "08_Operating_Systems",
    "weightage": "9 Marks",
    "topics": [
        "System calls, processes, threads, inter-process communication, concurrency and synchronization",
        "Deadlock: characterization, prevention, avoidance (Banker's algorithm), detection and recovery",
        "CPU and I/O scheduling: Preemptive and non-preemptive algorithms, disk scheduling",
        "Memory management and virtual memory: Paging, TLB, multi-level paging, page replacement algorithms",
        "File systems: File allocation methods, free space management, UNIX Inodes"
    ]
}

CHAPTERS = [
    {
        "title": "Processes, Threads, Concurrency & Synchronization",
        "hinglish": "Synchronization me Critical Section ke teen primary conditions (Mutual Exclusion, Progress, Bounded Waiting) aur Semaphores (wait/signal operations) par har saal tricky code tracing aati hai.",
        "theory": (
            "<b>1. Process & Thread Concepts:</b><br/>"
            "• <b>Process:</b> Program in execution. Contains text (code), data (globals), heap (dynamic), and stack (locals/activation records). PCB (Process Control Block) stores state, PC, registers.<br/>"
            "• <b>Threads (Lightweight Processes):</b> Share text, data, and open files, but have INDEPENDENT stack, registers, and program counter (PC).<br/>"
            "• User-Level Threads (ULT) vs Kernel-Level Threads (KLT): Context switching in ULT is fast (no mode switch), but if one ULT makes a blocking system call, the ENTIRE process blocks. KLT handles blocking calls individually.<br/><br/>"
            "<b>2. Critical Section Problem:</b><br/>"
            "• <b>Mutual Exclusion (Mandatory):</b> If process Pi is executing in critical section, no other process can be executing in CS.<br/>"
            "• <b>Progress (Mandatory):</b> If no process is in CS and some wish to enter, ONLY those processes not in their remainder section can participate in deciding who enters next, and selection cannot be postponed indefinitely.<br/>"
            "• <b>Bounded Waiting (Optional/Desirable):</b> Bound on number of times other processes can enter CS after a process requests entry.<br/><br/>"
            "<b>3. Peterson's Algorithm (2 Processes P0 and P1):</b><br/>"
            "• Shared variables: boolean flag[2] = {false, false}; int turn = 0;<br/>"
            "• Entry section for Pi: flag[i] = true; turn = j; while(flag[j] && turn == j);<br/>"
            "• Satisfies Mutual Exclusion, Progress, and Bounded Waiting on single-core systems!<br/><br/>"
            "<b>4. Semaphores:</b><br/>"
            "• Integer variable accessed ONLY via atomic operations wait() [P()] and signal() [V()].<br/>"
            "• <b>wait(S):</b> while (S <= 0); S--; (Decrements S; blocks if S <= 0).<br/>"
            "• <b>signal(S):</b> S++; (Increments S; unblocks a waiting process).<br/>"
            "• Counting Semaphore initialized to k: Allows at most k processes into CS simultaneously."
        ),
        "callouts": [
            ("Strict Alternation Trap", "A synchronization solution using only a shared 'turn' variable (while(turn != i);) guarantees Mutual Exclusion and Bounded Waiting, but VIOLATES PROGRESS because an idle process can prevent an active one from entering!", "warn"),
            ("Semaphore Value Meaning", "If counting semaphore S has value -k, it indicates that exactly k processes are currently BLOCKED waiting on semaphore S.", "formula")
        ],
        "tables": []
    },
    {
        "title": "CPU Scheduling, I/O Scheduling & Deadlocks",
        "hinglish": "CPU scheduling me Gantt chart draw karke turnaround time aur waiting time nikalte hain. Deadlock me Banker's algorithm se safe sequence determine karna direct numerical hota hai.",
        "theory": (
            "<b>1. Scheduling Metrics:</b><br/>"
            "• Turnaround Time (TAT) = Completion Time (CT) - Arrival Time (AT).<br/>"
            "• Waiting Time (WT) = Turnaround Time (TAT) - Burst Time (BT).<br/>"
            "• Response Time (RT) = Time of First CPU Response - Arrival Time (AT).<br/><br/>"
            "<b>2. CPU Scheduling Algorithms:</b><br/>"
            "• <b>FCFS (First Come First Serve):</b> Non-preemptive. Suffers from Convoy Effect (short processes stuck behind long CPU-bound process).<br/>"
            "• <b>SJF / SRTF (Shortest Job First / Shortest Remaining Time First):</b> Optimal for minimizing average waiting time! Preemptive version is SRTF.<br/>"
            "• <b>Round Robin (RR):</b> Preemptive with time quantum q. If q is very large -> behaves like FCFS. If q is very small -> high context switch overhead.<br/>"
            "• <b>Priority Scheduling:</b> Can cause Starvation of low priority processes. Prevented via <b>Aging</b> (gradually increasing priority of waiting processes).<br/><br/>"
            "<b>3. I/O & Disk Scheduling (Official GATE 2027 Syllabus):</b><br/>"
            "• <b>FCFS:</b> Requests served in arrival order. Fair, but slow.<br/>"
            "• <b>SSTF (Shortest Seek Time First):</b> Services request closest to current head position. Minimizes seek time, but prone to starvation.<br/>"
            "• <b>SCAN (Elevator Algorithm):</b> Head moves in one direction servicing all requests until end of disk, then reverses.<br/>"
            "• <b>C-SCAN (Circular SCAN):</b> Services requests in one direction only. When reaching the end, returns to the start without servicing requests on return trip. More uniform wait time.<br/>"
            "• <b>LOOK and C-LOOK:</b> Like SCAN/C-SCAN, but reverses as soon as last request in current direction is serviced (doesn't travel all the way to disk boundary).<br/><br/>"
            "<b>4. Deadlock Characterization & Handling:</b><br/>"
            "• <b>Coffman Conditions (All 4 must hold simultaneously):</b><br/>"
            "  1. Mutual Exclusion &nbsp; 2. Hold and Wait &nbsp; 3. No Preemption &nbsp; 4. Circular Wait.<br/>"
            "• <b>Banker's Algorithm for Deadlock Avoidance:</b><br/>"
            "  - Need[i, j] = Max[i, j] - Allocation[i, j].<br/>"
            "  - Process Pi can be allocated if Need[i] ≤ Available. If satisfied, new Available = Available + Allocation[i]."
        ),
        "callouts": [
            ("SRTF Minimization", "Shortest Remaining Time First (SRTF) is mathematically provably optimal in yielding the absolute minimum average waiting time among all scheduling algorithms.", "formula"),
            ("Safe State ≠ Deadlock Free Forever", "A safe state guarantees that at least one execution sequence exists that avoids deadlock. An unsafe state is NOT necessarily a deadlock, but it MAY lead to one!", "tip")
        ],
        "tables": []
    },
    {
        "title": "Memory Management, Virtual Memory & File Systems",
        "hinglish": "Multi-level paging me page table size calculate karna, TLB access time formula EMAT, aur page replacement (Belady's anomaly) most scored topics hain.",
        "theory": (
            "<b>1. Paging & Address Translation:</b><br/>"
            "• Logical Address: Page Number (p) | Page Offset (d).<br/>"
            "• Physical Address: Frame Number (f) | Page Offset (d). Page size == Frame size = 2^d bytes.<br/>"
            "• Page Table Size = (Number of pages in logical address space) * (Page Table Entry (PTE) size).<br/>"
            "• <b>Multi-level Paging:</b> Used to avoid keeping huge contiguous page tables in main memory. Outer page table must fit inside exactly ONE frame of memory!<br/><br/>"
            "<b>2. TLB & Effective Memory Access Time (EMAT):</b><br/>"
            "• Single-level Paging with TLB (hit ratio c, TLB access time t, Main Memory access time m):<br/>"
            "  - EMAT = c * (t + m) + (1 - c) * (t + 2m).<br/>"
            "• Two-level Paging with TLB:<br/>"
            "  - EMAT = c * (t + m) + (1 - c) * (t + 3m).<br/><br/>"
            "<b>3. Page Replacement Algorithms:</b><br/>"
            "• <b>FIFO:</b> Evicts the oldest page. Suffers from <b>Belady's Anomaly</b> (page faults can INCREASE when more frames are allocated!).<br/>"
            "• <b>Optimal (MIN / Belady's Optimal):</b> Evicts page that will not be used for the longest future time. Minimum page faults, but impossible to implement in practice.<br/>"
            "• <b>LRU (Least Recently Used):</b> Evicts page not used for the longest past time. Stack algorithm; NEVER suffers from Belady's Anomaly.<br/><br/>"
            "<b>4. UNIX Inodes & File Systems:</b><br/>"
            "• Inode structure contains file metadata and direct/indirect block pointers:<br/>"
            "  - Direct block pointers (e.g. 10 or 12 pointers).<br/>"
            "  - Single indirect block pointer -> points to disk block containing addresses of data blocks.<br/>"
            "  - Double indirect block pointer -> points to block containing single indirect pointers.<br/>"
            "  - Triple indirect block pointer -> points to double indirect blocks."
        ),
        "callouts": [
            ("Belady's Anomaly Exception", "Stack-based page replacement algorithms such as Optimal and LRU are MATHEMATICALLY IMMUNE to Belady's Anomaly. FIFO and Second-Chance can suffer from it!", "tip"),
            ("EMAT TLB Access Order", "Watch if TLB and Memory are searched in parallel or sequentially. Sequential: EMAT = t + m + (1-c)*m. Parallel: EMAT = c*m + (1-c)*(t + 2m).", "warn")
        ],
        "tables": []
    }
]

PRACTICE_QUESTIONS = [
    {
        "id": "OS-Q01",
        "type": "NAT",
        "marks": 2,
        "text": "A system uses a 32-bit virtual address and 4 KB page size. Each Page Table Entry (PTE) takes 4 bytes. If two-level paging is used such that the outer page table fits exactly into one page frame, how many bits are used for the outer page table index?",
        "answer": "10",
        "explanation": "1. Page size = 4 KB = 2^12 bytes => Offset d = 12 bits.<br/>2. Number of virtual address bits remaining for page numbers = 32 - 12 = 20 bits.<br/>3. A page frame has size 4 KB = 4096 bytes.<br/>4. Each PTE = 4 bytes. Number of entries in one page frame = 4096 / 4 = 1024 entries = 2^10 entries.<br/>5. Since outer page table must fit into exactly one frame, it can hold 2^10 entries => Outer page table index requires 10 bits.<br/>6. Inner page table index = 20 - 10 = 10 bits.",
        "is_pyq": True,
        "year": 2023,
        "difficulty": "Medium"
    },
    {
        "id": "OS-Q02",
        "type": "NAT",
        "marks": 2,
        "text": "Consider a disk queue with requests for I/O to blocks on cylinders: 98, 183, 37, 122, 14, 124, 65, 67. The head is currently at cylinder 53. What is the total head movement (in cylinders) using the SSTF (Shortest Seek Time First) scheduling algorithm?",
        "answer": "236",
        "explanation": "Current head position = 53.<br/>1. Closest to 53 is 65 (diff = 12). Head moves to 65. Distance = 12.<br/>2. Closest to 65 is 67 (diff = 2). Head moves to 67. Distance = 2.<br/>3. Closest to 67 is 37 (diff = 30; vs 98 diff = 31). Head moves to 37. Distance = 30.<br/>4. Closest to 37 is 14 (diff = 23). Head moves to 14. Distance = 23.<br/>5. Now remaining: 98, 122, 124, 183. Closest to 14 is 98 (diff = 84). Head moves to 98. Distance = 84.<br/>6. Closest to 98 is 122 (diff = 24). Head moves to 122. Distance = 24.<br/>7. Closest to 122 is 124 (diff = 2). Head moves to 124. Distance = 2.<br/>8. Finally to 183 (diff = 59). Head moves to 183. Distance = 59.<br/>Total distance = 12 + 2 + 30 + 23 + 84 + 24 + 2 + 59 = 236 cylinders.",
        "is_pyq": True,
        "year": 2021,
        "difficulty": "Medium"
    },
    {
        "id": "OS-Q03",
        "type": "MSQ",
        "marks": 2,
        "text": "Which of the following conditions can lead to BELADY'S ANOMALY in page replacement?",
        "options": {
            "A": "First-In-First-Out (FIFO) algorithm",
            "B": "Least Recently Used (LRU) algorithm",
            "C": "Optimal page replacement algorithm",
            "D": "Second-Chance (Clock) page replacement algorithm"
        },
        "answer": "A, D",
        "explanation": "Belady's Anomaly occurs when increasing the number of page frames results in an INCREASE in the number of page faults.<br/>• FIFO (A) famously suffers from Belady's Anomaly.<br/>• Second-Chance / Clock algorithm (D) is an approximation of FIFO and also exhibits Belady's anomaly.<br/>• LRU (B) and Optimal (C) are strictly STACK algorithms, meaning the set of pages in memory for n frames is always a subset of pages for n+1 frames. Thus they NEVER exhibit Belady's anomaly.",
        "is_pyq": False,
        "year": None,
        "difficulty": "GATE-Level"
    },
    {
        "id": "OS-Q04",
        "type": "MCQ",
        "marks": 1,
        "text": "Suppose a counting semaphore S is initialized to 10. Then, 12 wait() operations and 7 signal() operations are completed on S. What is the current value of S?",
        "answer": "5",
        "explanation": "Initial value = 10.<br/>Each wait() operation decrements the semaphore by 1: -12.<br/>Each signal() operation increments the semaphore by 1: +7.<br/>Current value of S = 10 - 12 + 7 = 5.",
        "options": {
            "A": "3",
            "B": "5",
            "C": "7",
            "D": "-2"
        },
        "is_pyq": True,
        "year": 2020,
        "difficulty": "Easy"
    },
    {
        "id": "OS-Q05",
        "type": "NAT",
        "marks": 2,
        "text": "In a paging system with TLB, the TLB hit ratio is 85%. TLB access time is 20 ns and main memory access time is 100 ns. What is the Effective Memory Access Time (in ns)?",
        "answer": "135",
        "explanation": "Assuming sequential access:<br/>On TLB hit (prob 0.85): time = TLB + Memory = 20 + 100 = 120 ns.<br/>On TLB miss (prob 0.15): time = TLB + Page Table Memory + Actual Memory = 20 + 100 + 100 = 220 ns.<br/>EMAT = 0.85 * 120 + 0.15 * 220 = 102 + 33 = 135 ns.",
        "is_pyq": True,
        "year": 2019,
        "difficulty": "Medium"
    }
]
