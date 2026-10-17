import React from 'react';
import { TrendingUp, AlertTriangle, CheckCircle2, Award, BookOpen, Layers } from 'lucide-react';

interface AnalyticsViewProps {
  gateData: any;
  completedTopics: string[];
}

export const AnalyticsView: React.FC<AnalyticsViewProps> = ({ gateData, completedTopics }) => {
  const subjects = gateData.subjects;
  const totalTopics = subjects.reduce((acc: number, s: any) => acc + s.chapters.length, 0);
  const completedCount = completedTopics.length;
  const overallPercent = Math.min(100, Math.round((completedCount / Math.max(1, totalTopics)) * 100));

  return (
    <div className="space-y-6 animate-fadeIn">
      {/* Header */}
      <div className="pb-6 border-b border-slate-200 dark:border-slate-800">
        <div className="inline-flex items-center gap-1.5 text-xs font-semibold text-emerald-600 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-950/60 px-2.5 py-1 rounded-full mb-2 border border-emerald-200 dark:border-emerald-800">
          <TrendingUp className="h-3.5 w-3.5" />
          Progress & Performance Dashboard
        </div>
        <h1 className="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white">
          Preparation Readiness & Weak Topic Analysis
        </h1>
        <p className="text-sm text-slate-500 dark:text-slate-400 mt-1">
          Real-time metrics, syllabus coverage, and automated diagnostic recommendations.
        </p>
      </div>

      {/* Overview Stat Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
        <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-5 shadow-sm">
          <span className="text-xs font-semibold text-slate-500 dark:text-slate-400">Overall Syllabus Progress</span>
          <div className="text-2xl font-extrabold text-blue-600 dark:text-blue-400 mt-1">{overallPercent}%</div>
          <div className="w-full bg-slate-100 dark:bg-slate-800 h-2 rounded-full overflow-hidden mt-3">
            <div className="bg-blue-600 h-full rounded-full transition-all" style={{ width: `${overallPercent}%` }} />
          </div>
        </div>

        <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-5 shadow-sm">
          <span className="text-xs font-semibold text-slate-500 dark:text-slate-400">Chapters Completed</span>
          <div className="text-2xl font-extrabold text-teal-600 dark:text-teal-400 mt-1">{completedCount} / {totalTopics}</div>
          <p className="text-xs text-slate-400 mt-2">Tracked via interactive checkboxes</p>
        </div>

        <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-5 shadow-sm">
          <span className="text-xs font-semibold text-slate-500 dark:text-slate-400">Estimated Exam Readiness</span>
          <div className="text-2xl font-extrabold text-indigo-600 dark:text-indigo-400 mt-1">
            {overallPercent >= 75 ? 'AIR Top 500 Zone' : overallPercent >= 40 ? 'On Track' : 'Foundational Stage'}
          </div>
          <p className="text-xs text-slate-400 mt-2">Target: &gt;65 Marks for IIT admission</p>
        </div>
      </div>

      {/* Subject-Wise Completion Matrix */}
      <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-6 shadow-sm space-y-4">
        <h2 className="text-base font-bold text-slate-900 dark:text-white">
          Subject Completion Breakdown
        </h2>

        <div className="space-y-4">
          {subjects.map((sub: any) => {
            const subDoneCount = sub.chapters.filter((_: any, idx: number) =>
              completedTopics.includes(`${sub.id}-${idx}`)
            ).length;
            const subPercent = Math.round((subDoneCount / sub.chapters.length) * 100);

            return (
              <div key={sub.id} className="space-y-1.5">
                <div className="flex items-center justify-between text-xs font-semibold">
                  <span className="text-slate-800 dark:text-slate-200">{sub.name} ({sub.weightage})</span>
                  <span className="text-slate-500">{subDoneCount} of {sub.chapters.length} chapters ({subPercent}%)</span>
                </div>
                <div className="w-full bg-slate-100 dark:bg-slate-800 h-2 rounded-full overflow-hidden">
                  <div
                    className={`h-full rounded-full transition-all ${
                      subPercent === 100 ? 'bg-emerald-500' : subPercent > 0 ? 'bg-blue-600' : 'bg-transparent'
                    }`}
                    style={{ width: `${subPercent}%` }}
                  />
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Weak Area Diagnostic Guidance */}
      <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-6 shadow-sm space-y-4">
        <h2 className="text-base font-bold text-slate-900 dark:text-white flex items-center gap-2">
          <AlertTriangle className="h-5 w-5 text-amber-500" />
          High-Priority Conceptual Traps to Watch
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs text-slate-600 dark:text-slate-300">
          <div className="p-3.5 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700">
            <h4 className="font-bold text-slate-900 dark:text-white mb-1">COA: Pipeline Stall vs Forwarding</h4>
            <p>Remember ALU-to-ALU forwarding eliminates stalls completely, but Load-to-Use dependencies ALWAYS incur exactly 1 stall cycle in a 5-stage RISC pipeline!</p>
          </div>
          <div className="p-3.5 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700">
            <h4 className="font-bold text-slate-900 dark:text-white mb-1">OS: Belady's Anomaly Algorithms</h4>
            <p>LRU and Optimal page replacement algorithms NEVER suffer from Belady's Anomaly because they are mathematically proven stack algorithms.</p>
          </div>
          <div className="p-3.5 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700">
            <h4 className="font-bold text-slate-900 dark:text-white mb-1">TOC: Pumping Lemma Misconception</h4>
            <p>Pumping lemma CANNOT be used to prove a language is regular or context-free. It is only a tool for proving NON-regularity or NON-context-freeness.</p>
          </div>
          <div className="p-3.5 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700">
            <h4 className="font-bold text-slate-900 dark:text-white mb-1">DBMS: BCNF vs 3NF Dependency Preservation</h4>
            <p>3NF decomposition is ALWAYS lossless and dependency-preserving. BCNF decomposition is always lossless, but may sacrifice functional dependencies.</p>
          </div>
        </div>
      </div>
    </div>
  );
};
