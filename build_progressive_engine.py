# build_progressive_engine.py
# Generates the Progressive Learning Engine (All 38 Chapters, 5-Level Structure)
# and Subject-Wise Complete Revision Data for all 11 Subjects.

import os
import sys

def generate_progressive_learning_html(title, level1, level2, level3, level4, level5):
    return f"""<div class="progressive-learning-container space-y-6">

  <!-- LEVEL 1: Intuitive Real-World Analogy & Beginner Explanation -->
  <div class="p-4 rounded-xl bg-blue-50/70 dark:bg-blue-950/30 border border-blue-200 dark:border-blue-900/60">
    <div class="flex items-center gap-2 mb-2 font-bold text-blue-900 dark:text-blue-200 text-sm">
      <span class="px-2 py-0.5 rounded bg-blue-600 text-white text-[10px] font-extrabold tracking-wide">LEVEL 1</span>
      <span>🌱 Beginner Intuition & Real-World Analogy (Easy Language)</span>
    </div>
    <div class="text-xs sm:text-sm text-slate-700 dark:text-slate-300 leading-relaxed space-y-1.5">
      {level1}
    </div>
  </div>

  <!-- LEVEL 2: Core Concepts & Essential Theory -->
  <div class="p-4 rounded-xl bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800">
    <div class="flex items-center gap-2 mb-2 font-bold text-slate-900 dark:text-white text-sm">
      <span class="px-2 py-0.5 rounded bg-slate-700 text-white text-[10px] font-extrabold tracking-wide">LEVEL 2</span>
      <span>📘 Core Fundamentals & Essential Theory</span>
    </div>
    <div class="text-xs sm:text-sm text-slate-700 dark:text-slate-300 leading-relaxed space-y-1.5">
      {level2}
    </div>
  </div>

  <!-- LEVEL 3: Step-by-Step Working & Mathematical Formulations -->
  <div class="p-4 rounded-xl bg-emerald-50/60 dark:bg-emerald-950/20 border border-emerald-200 dark:border-emerald-900/50">
    <div class="flex items-center gap-2 mb-2 font-bold text-emerald-900 dark:text-emerald-200 text-sm">
      <span class="px-2 py-0.5 rounded bg-emerald-600 text-white text-[10px] font-extrabold tracking-wide">LEVEL 3</span>
      <span>🚀 Intermediate Mechanics & Step-by-Step Working</span>
    </div>
    <div class="text-xs sm:text-sm text-slate-700 dark:text-slate-300 leading-relaxed space-y-1.5">
      {level3}
    </div>
  </div>

  <!-- LEVEL 4: Advanced GATE Analysis & Exam Traps -->
  <div class="p-4 rounded-xl bg-amber-50/70 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-900/60">
    <div class="flex items-center gap-2 mb-2 font-bold text-amber-900 dark:text-amber-200 text-sm">
      <span class="px-2 py-0.5 rounded bg-amber-600 text-white text-[10px] font-extrabold tracking-wide">LEVEL 4</span>
      <span>⚡ Advanced GATE Nuances & Exam Trap Alerts</span>
    </div>
    <div class="text-xs sm:text-sm text-slate-700 dark:text-slate-300 leading-relaxed space-y-1.5">
      {level4}
    </div>
  </div>

  <!-- LEVEL 5: Step-by-Step Solved Exam Problem -->
  <div class="p-4 rounded-xl bg-purple-50/70 dark:bg-purple-950/30 border border-purple-200 dark:border-purple-900/60">
    <div class="flex items-center gap-2 mb-2 font-bold text-purple-900 dark:text-purple-200 text-sm">
      <span class="px-2 py-0.5 rounded bg-purple-600 text-white text-[10px] font-extrabold tracking-wide">LEVEL 5</span>
      <span>🎯 Step-by-Step Solved Exam Problem (Basic to Advanced)</span>
    </div>
    <div class="text-xs sm:text-sm text-slate-700 dark:text-slate-300 leading-relaxed space-y-2">
      {level5}
    </div>
  </div>

</div>"""

print("Progressive template defined!")
