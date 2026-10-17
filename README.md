# GATE 2027 Computer Science and Information Technology (CS) Preparation Platform & Downloadable Study Library

**Organizing Institute:** Indian Institute of Technology Madras (IIT Madras)  
**Target Examination Dates:** February 6, 7, 13, 14, 20, 21, 2027  
**Official Portal:** [https://gate2027.iitm.ac.in/](https://gate2027.iitm.ac.in/)  
**Verification Date:** October 17, 2026  

---

## 1. Project Overview & Deliverables
This platform is an authentic, production-grade offline and online preparation system for B.Tech CSE students preparing for GATE 2027. Built directly from the official IIT Madras curriculum and question paper patterns.

### Key Highlights
* **Official Syllabus Downloaded:** Original official PDFs directly retrieved from IIT Madras (`00_Official_Syllabus/CS_GATE2027_Syllabus.pdf` and `00_Official_Syllabus/GA_GATE2027_Syllabus.pdf`).
* **105 Vector-Typeset Downloadable PDFs:** 269 pages of comprehensive notes, chapter deep-dives, formula sheets, practice questions with solutions, and subject mock tests across all 11 subjects.
* **Verified Previous Year Questions (PYQs):** Authentic historical questions (2012–2026) verified against official answer keys released by organizing IITs.
* **Full-Length 180-Minute CBT Mock Simulator:** Exact GATE 2027 examination interface with 65 questions (10 General Aptitude + 55 CS & Math), question palette, timer, virtual numeric keypad for NAT, and negative marking calculator (-1/3 for 1M MCQ, -2/3 for 2M MCQ, zero negative for MSQ and NAT).
* **Personalized 16-Week Study Planner:** Selectable schedules for 2h, 4h, and 6h daily study routines with persistent progress tracking in `localStorage`.
* **Quick Revision & Formula Matrix:** Comprehensive master formula sheet, high-yield traps, last-month 30-day battle plan, and final-week protocol.

---

## 2. Directory Structure

```
E:\Gate\
├── 00_Official_Syllabus/
│   ├── CS_GATE2027_Syllabus.pdf                   <- Official IIT Madras CS Syllabus PDF
│   ├── GA_GATE2027_Syllabus.pdf                   <- Official IIT Madras GA Syllabus PDF
│   └── GATE_2027_Syllabus_Analysis_and_Changes.pdf <- Comparative Analysis & Weightages
├── 01_Engineering_Mathematics/                    <- 8 standard PDFs (Notes, Topics, Formulas, Tests)
├── 02_Digital_Logic/                              <- 8 standard PDFs
├── 03_Computer_Organization/                      <- 8 standard PDFs
├── 04_Programming_Data_Structures/                <- 8 standard PDFs
├── 05_Algorithms/                                 <- 8 standard PDFs
├── 06_Theory_of_Computation/                      <- 8 standard PDFs
├── 07_Compiler_Design/                            <- 8 standard PDFs
├── 08_Operating_Systems/                          <- 8 standard PDFs
├── 09_Databases/                                  <- 8 standard PDFs
├── 10_Computer_Networks/                          <- 8 standard PDFs
├── 11_General_Aptitude/                           <- 8 standard PDFs
├── 12_Previous_Year_Questions/                    <- Verified PYQs 2012-2026 Compendium
├── 13_Practice_Question_Banks/                    <- Comprehensive Practice Question Banks
├── 14_Mock_Tests/                                 <- Full-Length 100-Mark Mock Tests
├── 15_Quick_Revision/                             <- Master Formula & Cheat Sheet
├── 16_Study_Plans/                                <- 16-Week Complete Study Planner
├── 17_Final_Revision/                             <- Final Week & Last Day Revision Pack
├── content_data/                                  <- Structured educational data modules (Python)
├── pdf_generator/                                 <- ReportLab Platypus PDF Publishing Engine
├── web_platform/                                  <- React + TypeScript + Tailwind Web Application
├── master_pdf_index.json                          <- Master Index of all 105 Generated PDFs
├── syllabus_database.json                         <- Structured Official Syllabus Database
├── qa_audit_report.json                           <- Automated QA Audit Results (20/20 Passed)
└── start_platform.bat                             <- One-Click Web Platform Launcher
```

---

## 3. How to Launch and Use the Web Platform

### Option A: One-Click Launch (Recommended)
Double-click `start_platform.bat` in `E:\Gate\`.  
It automatically starts the web platform on `http://localhost:3000`.

### Option B: Manual Command Line
```powershell
cd E:\Gate\web_platform
$env:Path = "C:\Program Files\nodejs;" + $env:Path
npm run preview -- --port 3000
```
Open your browser at `http://localhost:3000`.

---

## 4. Quality Assurance Summary
* **Total Automated Checks:** 20 / 20 Passed (100% Success).
* **Corrupt or Zero-Byte PDFs:** 0 (All 105 PDFs are verified valid and readable via PyPDF).
* **Question Uniqueness:** All question identifiers are verified unique.
* **Negative Marking Conformity:** Strictly implements the IIT Madras GATE 2027 rules.
