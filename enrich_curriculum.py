# Script to enrich curriculum with curated YouTube video links, solved exam examples, and detailed 7-day daily plans
import os
import sys
import json
import urllib.parse

sys.path.append(os.path.abspath('.'))

def yt_search(query):
    return "https://www.youtube.com/results?search_query=" + urllib.parse.quote_plus(query)

# 1. Update study_plans_data.py with comprehensive daily_plan for all weeks
import content_data.study_plans_data as plan_mod

# Subject & Chapter Mapping helper
SUBJECT_TOPIC_MAP = {
    1: {"sub": "EM", "chap": 0, "title": "Discrete Math: Logic & Set Theory", "query": "gate cse discrete mathematics mathematical logic gate smashers"},
    2: {"sub": "EM", "chap": 1, "title": "Discrete Math: Graph Theory & Combinatorics", "query": "gate cse graph theory planar graphs gate smashers"},
    3: {"sub": "DL", "chap": 1, "title": "Digital Logic: Boolean Algebra & K-Maps", "query": "gate cse digital logic k-map gate smashers"},
    4: {"sub": "DL", "chap": 3, "title": "Digital Logic: Sequential Circuits & Counters", "query": "gate cse digital logic sequential circuits flip flops gate smashers"},
    5: {"sub": "COA", "chap": 2, "title": "COA: Memory Hierarchy & Cache Mapping", "query": "gate cse cache memory mapping amat gate smashers"},
    6: {"sub": "COA", "chap": 3, "title": "COA: Pipelining & Hazards", "query": "gate cse instruction pipelining hazards gate smashers"},
    7: {"sub": "PDS", "chap": 0, "title": "Programming in C: Pointers & Recursion", "query": "gate cse c programming pointers recursion gate smashers"},
    8: {"sub": "PDS", "chap": 2, "title": "Data Structures: Trees, BST & Heaps", "query": "gate cse binary search tree heap abdul bari"},
    9: {"sub": "ALGO", "chap": 2, "title": "Algorithms: Greedy & Dynamic Programming", "query": "gate cse dynamic programming 0 1 knapsack abdul bari"},
    10: {"sub": "ALGO", "chap": 3, "title": "Algorithms: Graph Algorithms (Dijkstra, MST)", "query": "gate cse graph algorithms dijkstra prim kruskal abdul bari"},
    11: {"sub": "TOC", "chap": 0, "title": "TOC: Finite Automata & Regular Languages", "query": "gate cse dfa nfa minimization gate smashers"},
    12: {"sub": "CD", "chap": 1, "title": "Compiler Design: Parsing & Syntax Analysis", "query": "gate cse compiler design ll1 lr parsing gate smashers"},
    13: {"sub": "OS", "chap": 1, "title": "Operating Systems: CPU Scheduling & Synchronization", "query": "gate cse cpu scheduling semaphores gate smashers"},
    14: {"sub": "OS", "chap": 2, "title": "Operating Systems: Virtual Memory & Paging", "query": "gate cse paging tlb virtual memory gate smashers"},
    15: {"sub": "DB", "chap": 1, "title": "Databases: Normalization & Functional Dependencies", "query": "gate cse functional dependency normalization gate smashers"},
    16: {"sub": "CN", "chap": 1, "title": "Computer Networks: Subnetting & IP Addressing", "query": "gate cse ipv4 subnetting cidr gate smashers"},
    # Revision and Mocks Weeks
    17: {"sub": "EM", "chap": 0, "title": "Engg Math & Digital Logic Revision", "query": "gate cse discrete mathematics revision gate smashers"},
    18: {"sub": "PDS", "chap": 0, "title": "Programming & Algorithms Revision", "query": "gate cse algorithms revision abdul bari"},
    19: {"sub": "TOC", "chap": 0, "title": "TOC, Compiler & OS Revision", "query": "gate cse toc compiler revision gate smashers"},
    20: {"sub": "DB", "chap": 0, "title": "DBMS, Networks & Aptitude Revision", "query": "gate cse dbms networks revision gate smashers"},
    21: {"sub": "EM", "chap": 0, "title": "Full CBT Mock Test 1 & 2 Diagnostic", "query": "gate cse full mock test strategy time management"},
    22: {"sub": "COA", "chap": 2, "title": "Full CBT Mock Test 3 & 4 Speed Tuning", "query": "gate cse virtual calculator speed practice"},
    23: {"sub": "ALGO", "chap": 2, "title": "Full CBT Mock Test 5 & 6 MSQ Mastery", "query": "gate cse msq multi select questions strategy"},
    24: {"sub": "OS", "chap": 1, "title": "Full CBT Mock Test 7 & 8 Negative Mark Control", "query": "gate cse avoid negative marking silly mistakes"},
    25: {"sub": "EM", "chap": 0, "title": "Final Sprint: High-Yield Top 25 Concepts", "query": "gate cse top 25 high weightage topics revision"},
    26: {"sub": "COA", "chap": 2, "title": "Final Sprint: Master Formula Sheet Drills", "query": "gate cse all formulas revision marathon"},
    27: {"sub": "PDS", "chap": 0, "title": "Final Sprint: Recent 5-Year PYQs (2022-2026)", "query": "gate 2026 cs paper solution discussion"},
    28: {"sub": "OS", "chap": 2, "title": "Final Sprint: 30-Day Battle Plan & Weakness Clearance", "query": "gate cse last month revision strategy"},
    29: {"sub": "EM", "chap": 0, "title": "Exam Week: Final-Day Pack & Mindset Calibration", "query": "gate exam day instructions tips dos and don'ts"}
}

day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for w_item in plan_mod.STUDY_PLANS["weekly_roadmap"]:
    w_num = w_item["week"]
    mapping = SUBJECT_TOPIC_MAP.get(w_num, {"sub": "EM", "chap": 0, "title": "General CSE Revision", "query": "gate cse preparation"})
    sub_id = mapping["sub"]
    chap_idx = mapping["chap"]
    
    daily_list = []
    topics = w_item["topics"]
    
    for d_idx in range(1, 8):
        d_name = day_names[d_idx - 1]
        if d_idx <= len(topics):
            topic_str = topics[d_idx - 1]
            task_str = f"Study theory notes on {topic_str}. Solve 12-15 practice problems and note down any errors."
            v_title = f"Lecture: {topic_str}"
            v_url = yt_search(f"gate cse {sub_id} {topic_str} lecture")
        elif d_idx == 6:
            topic_str = "Weekly Practice Drill & PYQ Solving"
            task_str = f"Solve 25 verified previous year GATE questions on {w_item['phase']} under timed conditions."
            v_title = f"PYQ Solving Session: {w_item['phase']}"
            v_url = yt_search(f"gate cse pyq solutions {w_item['phase']}")
        else: # Sunday
            topic_str = w_item["buffer_day"]
            task_str = f"{w_item['buffer_day']}. Audit error log notebook and revise formula sheets."
            v_title = f"Revision & Weekly Assessment: {w_item['phase']}"
            v_url = yt_search(f"gate cse revision quiz {w_item['phase']}")
            
        daily_list.append({
            "day": d_idx,
            "day_name": f"Day {d_idx} ({d_name})",
            "topic": topic_str,
            "subject_id": sub_id,
            "chapter_index": chap_idx,
            "task": task_str,
            "video_title": v_title,
            "video_url": v_url
        })
        
    w_item["daily_plan"] = daily_list

print("Enriched all 29 weeks with 7-day daily plans!")

# Save back to content_data/study_plans_data.py
with open("content_data/study_plans_data.py", "w", encoding="utf-8") as f:
    f.write("# GATE 2027 Study Timetable and Personalized Study Planner Module\n")
    f.write("# 3-Month-Early Completion Architecture with Detailed 7-Day Plans\n\n")
    f.write("STUDY_PLANS = " + repr(plan_mod.STUDY_PLANS) + "\n")

print("Saved enriched study_plans_data.py successfully!")
