import os
import sys
import pypdf
import shutil

sys.path.append(os.path.abspath('.'))
from pdf_generator.builder import GatePdfBuilder
import content_data.study_plans_data as plan_mod

def build_planner():
    fn_plan = os.path.join('16_Study_Plans', 'GATE_2027_Complete_Study_Planner.pdf')
    b_plan = GatePdfBuilder(fn_plan, 'GATE 2027 Personalized Study Planner & Daily Target Roadmaps', 'Study Plans', 'Study Timetable')
    b_plan.add_cover_page({
        'weightage': 'Full Preparation Lifecycle',
        'topics': [
            '3-Month-Early Syllabus Completion Architecture',
            '2h, 4h, and 6h Daily Schedules',
            '100% Syllabus Finish by Nov 1, 2026',
            '90-Day Revision & CBT Mock Test Marathon'
        ]
    })
    b_plan.add_callout(
        '3-MONTH PRE-EXAM BUFFER STRATEGY',
        'Finishing 100% of the entire syllabus 3 months prior to the exam (by November 1, 2026) ensures you enter the final 90 days with zero pending theory. This critical buffer is dedicated entirely to: (1) Month -3 Subject-Wise Revision & Tests, (2) Month -2 All-India CBT Mock Series (10+ Mocks), and (3) Month -1 Weakness Eradication, Formula Drills, and Speed Optimization.'
    )
    b_plan.add_section_header('Daily Study Schedule Models (2h, 4h, 6h Tiers)', 1)
    sched_rows = []
    for k, v in plan_mod.STUDY_PLANS['schedules'].items():
        time_str = f"Concepts: {v['daily_breakdown']['concept_study_mins']}m / Practice: {v['daily_breakdown']['practice_pyq_mins']}m / Revision: {v['daily_breakdown']['revision_mins']}m"
        sched_rows.append([v['title'], time_str, v['strategy']])
    b_plan.add_table(['Schedule Tier', 'Daily Time Allocation', 'Strategic Methodology'], sched_rows, col_widths=[120, 160, 207])
    
    b_plan.add_section_header('Master Calendar: 3-Month-Early Completion & 90-Day Revision Series', 2)
    plan_rows = []
    for item in plan_mod.STUDY_PLANS['weekly_roadmap']:
        plan_rows.append([f"Week {item['week']}", item['phase'], ', '.join(item['subjects']), item['targets']])
    b_plan.add_table(['Week', 'Phase', 'Subjects Covered', 'Weekly Deliverable'], plan_rows, col_widths=[45, 125, 145, 172])
    b_plan.build()
    
    pages = len(pypdf.PdfReader(fn_plan).pages)
    print(f'Successfully regenerated {fn_plan}: {pages} pages, {os.path.getsize(fn_plan)} bytes')

    # Copy to docs
    os.makedirs('docs/16_Study_Plans', exist_ok=True)
    shutil.copy2(fn_plan, 'docs/16_Study_Plans/GATE_2027_Complete_Study_Planner.pdf')
    print('Copied to docs/16_Study_Plans/GATE_2027_Complete_Study_Planner.pdf')

if __name__ == '__main__':
    build_planner()
