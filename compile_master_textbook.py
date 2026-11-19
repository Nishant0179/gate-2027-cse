# compile_master_textbook.py
# Compiles all 38 textbook chapters across the 4 modules into:
# 1. content_data/master_textbook_data.py (structured data)
# 2. content_data/progressive_theory_engine.py (web HTML + structured data for PDFs)

import os
import sys

from content_data.textbook_modules.textbook_em_dl import CHAPTERS_EM_DL
from content_data.textbook_modules.textbook_coa_pds_algo import CHAPTERS_COA_PDS_ALGO
from content_data.textbook_modules.textbook_toc_cd_os import CHAPTERS_TOC_CD_OS
from content_data.textbook_modules.textbook_db_cn_ga import CHAPTERS_DB_CN_GA

def compile_all():
    all_chapters = {}
    all_chapters.update(CHAPTERS_EM_DL)
    all_chapters.update(CHAPTERS_COA_PDS_ALGO)
    all_chapters.update(CHAPTERS_TOC_CD_OS)
    all_chapters.update(CHAPTERS_DB_CN_GA)

    print(f"Total compiled chapters: {len(all_chapters)}")
    assert len(all_chapters) == 38, f"Expected 38 chapters, but found {len(all_chapters)}!"

    # 1. Generate master_textbook_data.py
    with open(os.path.join("content_data", "master_textbook_data.py"), "w", encoding="utf-8") as f:
        f.write("# Master Textbook Structured Repository for all 38 Chapters\n")
        f.write("MASTER_TEXTBOOK_DATA = " + repr(all_chapters) + "\n")
    print("Successfully wrote content_data/master_textbook_data.py!")

    # 2. Build progressive_theory_engine.py with HTML formatted exactly like User Images 2 & 3
    html_dict = {}
    for key, data in all_chapters.items():
        sub_id, chap_idx = key
        title = data["title"]
        real_life = data.get("real_life_examples", [])
        foundations = data.get("foundations", [])
        worked = data.get("worked_examples", [])
        traps = data.get("exam_traps", [])

        # Section 1: Real life examples
        real_life_boxes = ""
        for ex in real_life:
            real_life_boxes += f"""
      <div class="p-4 sm:p-5 rounded-2xl bg-slate-50/90 dark:bg-slate-800/60 border border-slate-200/80 dark:border-slate-700/70 shadow-xs space-y-2">
        <div class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-100 dark:bg-amber-950/80 text-amber-800 dark:text-amber-300 border border-amber-200 dark:border-amber-800/60">
          <span>💡 Real-Life Analogy</span>
        </div>
        <h4 class="font-bold text-slate-900 dark:text-slate-100 text-sm sm:text-base">
          {ex['title']}
        </h4>
        <p class="text-xs sm:text-sm text-slate-700 dark:text-slate-300 leading-relaxed whitespace-pre-line">
          {ex['text']}
        </p>
      </div>"""

        # Section 2: Foundations
        foundations_content = ""
        for fnd in foundations:
            fnd_num = fnd.get('number', '')
            fnd_title = fnd.get('title', '')
            fnd_text = fnd.get('content', '')
            crucial = fnd.get('crucial_rule', '')

            crucial_html = ""
            if crucial:
                crucial_html = f"""
        <div class="mt-3 p-3.5 rounded-xl bg-emerald-50/90 dark:bg-emerald-950/40 border border-emerald-300/80 dark:border-emerald-700/60 text-emerald-950 dark:text-emerald-200 text-xs sm:text-sm leading-relaxed font-semibold">
          {crucial}
        </div>"""

            foundations_content += f"""
      <div class="p-4 sm:p-5 rounded-2xl bg-slate-50/60 dark:bg-slate-800/40 border border-slate-200/80 dark:border-slate-700/60 space-y-2">
        <h3 class="text-sm sm:text-base font-bold text-blue-700 dark:text-blue-400 flex items-center gap-2">
          <span>{fnd_num} {fnd_title}</span>
        </h3>
        <div class="text-xs sm:text-sm text-slate-700 dark:text-slate-300 leading-relaxed space-y-1.5">
          {fnd_text}
        </div>
        {crucial_html}
      </div>"""

        # Section 3: Worked Examples
        worked_content = ""
        for w in worked:
            w_title = w.get("title", "Worked Problem")
            w_prob = w.get("problem", "")
            w_steps = w.get("steps", [])
            w_ans = w.get("answer", "")

            steps_html = "<br/>".join([f"• {s}" for s in w_steps])
            worked_content += f"""
      <div class="p-4 sm:p-5 rounded-2xl bg-slate-50/80 dark:bg-slate-800/60 border border-slate-200/80 dark:border-slate-700/70 space-y-3">
        <div class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-xs font-bold bg-purple-100 dark:bg-purple-950/80 text-purple-800 dark:text-purple-300 border border-purple-200 dark:border-purple-800/60">
          <span>🔢 Step-by-Step Solved Problem</span>
        </div>
        <h4 class="font-bold text-slate-900 dark:text-slate-100 text-sm sm:text-base">
          {w_title}
        </h4>
        <div class="text-xs sm:text-sm text-slate-900 dark:text-slate-100 bg-white dark:bg-slate-900 p-3.5 rounded-xl border border-slate-200 dark:border-slate-700">
          <b>Problem:</b> {w_prob}
        </div>
        <div class="text-xs sm:text-sm text-slate-700 dark:text-slate-300 leading-relaxed pt-1 space-y-1.5">
          <b>Step-by-Step Solution & Traces:</b><br/>
          {steps_html}
        </div>
        <div class="p-3 rounded-xl bg-emerald-50 dark:bg-emerald-950/50 border border-emerald-300 dark:border-emerald-700 text-emerald-900 dark:text-emerald-200 text-xs sm:text-sm font-bold">
          🎯 {w_ans}
        </div>
      </div>"""

        # Section 4: Exam Traps
        traps_content = ""
        for tr in traps:
            traps_content += f"""
      <div class="p-4 rounded-xl bg-rose-50/80 dark:bg-rose-950/30 border border-rose-200/80 dark:border-rose-900/60 space-y-1.5">
        <h4 class="font-bold text-rose-900 dark:text-rose-200 text-xs sm:text-sm flex items-center gap-1.5">
          <span>⚠️ {tr['title']}</span>
        </h4>
        <p class="text-xs sm:text-sm text-slate-700 dark:text-slate-300 leading-relaxed">
          {tr['warning']}
        </p>
      </div>"""

        full_html = f"""<div class="master-chapter-textbook-container space-y-8">
  <!-- SECTION 1: EVERYDAY REAL-LIFE EXAMPLES (INTUITIVE MENTAL MODELS) -->
  <div class="space-y-3">
    <div class="border-b border-slate-200 dark:border-slate-800 pb-2">
      <h2 class="text-sm sm:text-base md:text-lg font-black text-blue-700 dark:text-blue-400 tracking-wide uppercase flex items-center gap-2">
        <span>1. EVERYDAY REAL-LIFE EXAMPLES (INTUITIVE MENTAL MODELS)</span>
      </h2>
      <p class="text-xs sm:text-sm text-slate-600 dark:text-slate-400 italic mt-0.5">
        These everyday real-life examples illustrate the core concept using familiar situations before diving into theory:
      </p>
    </div>
    <div class="space-y-3">
      {real_life_boxes}
    </div>
  </div>

  <!-- SECTION 2: IN-DEPTH CONCEPTUAL & ARCHITECTURAL FOUNDATIONS -->
  <div class="space-y-4">
    <div class="border-b border-slate-200 dark:border-slate-800 pb-2">
      <h2 class="text-sm sm:text-base md:text-lg font-black text-blue-700 dark:text-blue-400 tracking-wide uppercase flex items-center gap-2">
        <span>2. IN-DEPTH CONCEPTUAL & ARCHITECTURAL FOUNDATIONS</span>
      </h2>
    </div>
    <div class="space-y-4">
      {foundations_content}
    </div>
  </div>

  <!-- SECTION 3: STEP-BY-STEP EXAM WORKED EXAMPLES & PROBLEM TRACES -->
  <div class="space-y-4">
    <div class="border-b border-slate-200 dark:border-slate-800 pb-2">
      <h2 class="text-sm sm:text-base md:text-lg font-black text-blue-700 dark:text-blue-400 tracking-wide uppercase flex items-center gap-2">
        <span>3. STEP-BY-STEP EXAM WORKED EXAMPLES & PROBLEM TRACES</span>
      </h2>
    </div>
    <div class="space-y-3">
      {worked_content}
    </div>
  </div>

  <!-- SECTION 4: COMMON MISCONCEPTIONS & EXAM TRAP WARNINGS -->
  <div class="space-y-3">
    <div class="border-b border-slate-200 dark:border-slate-800 pb-2">
      <h2 class="text-sm sm:text-base md:text-lg font-black text-blue-700 dark:text-blue-400 tracking-wide uppercase flex items-center gap-2">
        <span>4. COMMON MISCONCEPTIONS & EXAM TRAP WARNINGS</span>
      </h2>
    </div>
    <div class="space-y-2.5">
      {traps_content}
    </div>
  </div>
</div>"""
        html_dict[key] = full_html

    with open(os.path.join("content_data", "progressive_theory_engine.py"), "w", encoding="utf-8") as f:
        f.write("# progressive_theory_engine.py\n")
        f.write("# Master textbook explanations for all 38 chapters matching User Images 2 & 3.\n\n")
        f.write("from .master_textbook_data import MASTER_TEXTBOOK_DATA as MASTER_CHAPTER_STRUCTURED_DICT\n\n")
        f.write("PROGRESSIVE_THEORY_DICT = " + repr(html_dict) + "\n")

    print("Successfully built content_data/progressive_theory_engine.py with all 38 master chapters!")

if __name__ == "__main__":
    compile_all()
