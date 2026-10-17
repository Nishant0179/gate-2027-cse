import React, { useState } from 'react';
import { 
  Zap, 
  Clock, 
  ShieldAlert, 
  FileDown, 
  CheckCircle2, 
  BookOpen, 
  Sparkles, 
  AlertTriangle, 
  Bookmark,
  ChevronRight,
  Layers
} from 'lucide-react';

interface QuickRevisionViewProps {
  finalRevision: any;
  subjectRevision?: Record<string, any>;
}

export const QuickRevisionView: React.FC<QuickRevisionViewProps> = ({ 
  finalRevision,
  subjectRevision = {} 
}) => {
  const lastMonthStrategy = finalRevision.last_month_strategy || [];
  const finalWeekPack = finalRevision.final_week_pack || [];

  const subjectKeys = Object.keys(subjectRevision);
  const [selectedSubjectId, setSelectedSubjectId] = useState<string>(subjectKeys[0] || 'EM');

  const currentRev = subjectRevision[selectedSubjectId] || subjectRevision['EM'] || null;

  return (
    <div className="space-y-8 animate-fadeIn">
      {/* Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-6 border-b border-slate-200 dark:border-slate-800">
        <div>
          <div className="inline-flex items-center gap-1.5 text-xs font-semibold text-rose-600 dark:text-rose-400 bg-rose-50 dark:bg-rose-950/60 px-2.5 py-1 rounded-full mb-2 border border-rose-200 dark:border-rose-800">
            <Zap className="h-3.5 w-3.5" />
            Subject-Wise Rapid Revision & Final Sprint Packs
          </div>
          <h1 className="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white">
            Complete Subject Revision & Formula Sheets
          </h1>
          <p className="text-sm text-slate-500 dark:text-slate-400 mt-1">
            Subject-wise high-yield formulas, canonical theorems, exam traps, and downloadable complete subject PDF books.
          </p>
        </div>

        <div className="flex flex-wrap items-center gap-2">
          <a
            href="./15_Quick_Revision/Master_Formula_and_Cheat_Sheet.pdf"
            download
            className="flex items-center gap-2 bg-blue-600 hover:bg-blue-700 text-white font-semibold text-xs px-4 py-2.5 rounded-xl shadow-sm transition"
          >
            <FileDown className="h-4 w-4" />
            <span>Master Formula Sheet PDF</span>
          </a>
          <a
            href="./17_Final_Revision/Final_Week_and_Last_Day_Pack.pdf"
            download
            className="flex items-center gap-2 bg-rose-600 hover:bg-rose-700 text-white font-semibold text-xs px-4 py-2.5 rounded-xl shadow-sm transition"
          >
            <FileDown className="h-4 w-4" />
            <span>Final Sprint Pack PDF</span>
          </a>
        </div>
      </div>

      {/* SUBJECT-WISE COMPLETE REVISION SECTION */}
      {currentRev && (
        <div className="space-y-4">
          <div className="flex items-center justify-between">
            <h2 className="text-base sm:text-lg font-extrabold text-slate-900 dark:text-white flex items-center gap-2">
              <Layers className="h-5 w-5 text-blue-600" />
              <span>Select Subject for Complete Rapid Revision</span>
            </h2>
            <span className="text-xs text-slate-500 dark:text-slate-400 font-medium hidden sm:inline">
              11 Subjects • Complete PDF & Formulas Included
            </span>
          </div>

          {/* Subject Pills */}
          <div className="flex items-center gap-2 overflow-x-auto pb-2 scrollbar-none">
            {subjectKeys.map((subId) => {
              const item = subjectRevision[subId];
              const isSelected = subId === selectedSubjectId;
              return (
                <button
                  key={subId}
                  onClick={() => setSelectedSubjectId(subId)}
                  className={`flex-shrink-0 px-3.5 py-2 rounded-xl text-xs font-semibold transition border ${
                    isSelected
                      ? 'bg-blue-600 text-white border-blue-600 shadow-sm'
                      : 'bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-300 border-slate-200 dark:border-slate-800 hover:border-blue-400'
                  }`}
                >
                  <span>{item.name}</span>
                  <span className={`ml-2 text-[10px] px-1.5 py-0.5 rounded-full ${
                    isSelected ? 'bg-blue-700 text-white' : 'bg-slate-100 dark:bg-slate-800 text-slate-500'
                  }`}>
                    {item.weightage}
                  </span>
                </button>
              );
            })}
          </div>

          {/* Selected Subject Revision Card */}
          <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-6 shadow-sm space-y-6">
            {/* Banner with Download Buttons */}
            <div className="p-5 rounded-2xl bg-gradient-to-r from-blue-900 via-indigo-900 to-slate-900 text-white flex flex-col md:flex-row md:items-center justify-between gap-4">
              <div>
                <div className="flex items-center gap-2 mb-1">
                  <span className="text-xs font-bold px-2 py-0.5 rounded bg-blue-500/30 text-blue-200 border border-blue-400/40">
                    {currentRev.weightage}
                  </span>
                  <span className="text-xs text-blue-200 font-medium">Official IIT Syllabus Topic</span>
                </div>
                <h3 className="text-xl sm:text-2xl font-black">{currentRev.name} — Rapid Revision</h3>
                <p className="text-xs text-blue-200/80 mt-1 max-w-xl">
                  Revise high-yield formulas, canonical theorems, and exam traps in under 15 minutes.
                </p>
              </div>

              {/* Direct PDF Download Buttons */}
              <div className="flex flex-wrap items-center gap-2">
                <a
                  href={currentRev.complete_pdf}
                  download
                  className="flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-bold text-xs shadow-sm transition"
                  title="Download Complete Subject Book PDF"
                >
                  <FileDown className="h-4 w-4" />
                  <span>Complete Subject PDF</span>
                </a>
                <a
                  href={currentRev.quick_revision_pdf}
                  download
                  className="flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-white/10 hover:bg-white/20 text-white font-semibold text-xs border border-white/20 transition"
                  title="Download Quick Revision Notes PDF"
                >
                  <Zap className="h-4 w-4 text-amber-400" />
                  <span>Quick Revision PDF</span>
                </a>
                <a
                  href={currentRev.formula_sheet_pdf}
                  download
                  className="flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-white/10 hover:bg-white/20 text-white font-semibold text-xs border border-white/20 transition"
                  title="Download Formula Sheet PDF"
                >
                  <Sparkles className="h-4 w-4 text-emerald-400" />
                  <span>Formula Sheet PDF</span>
                </a>
              </div>
            </div>

            {/* High-Yield Formulas */}
            {currentRev.high_yield_formulas && currentRev.high_yield_formulas.length > 0 && (
              <div className="space-y-3">
                <h4 className="text-sm font-bold text-slate-900 dark:text-white flex items-center gap-2">
                  <Sparkles className="h-4 w-4 text-blue-600" />
                  <span>High-Yield Formulas & Shortcuts for {currentRev.name}</span>
                </h4>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                  {currentRev.high_yield_formulas.map((item: any, fIdx: number) => (
                    <div 
                      key={fIdx}
                      className="p-4 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700/80 space-y-1.5"
                    >
                      <div className="text-xs font-bold text-slate-900 dark:text-white flex items-center gap-1.5">
                        <span className="w-1.5 h-1.5 rounded-full bg-blue-600"></span>
                        <span>{item.name}</span>
                      </div>
                      <div className="p-2.5 rounded-lg bg-white dark:bg-slate-900 border border-blue-200 dark:border-blue-900/60 text-xs font-mono font-bold text-blue-800 dark:text-blue-300">
                        {item.formula}
                      </div>
                      <p className="text-[11px] text-slate-500 dark:text-slate-400 leading-relaxed">
                        {item.notes}
                      </p>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Canonical Theorems & Proof Takeaways */}
            {currentRev.key_theorems && currentRev.key_theorems.length > 0 && (
              <div className="space-y-3 pt-2">
                <h4 className="text-sm font-bold text-slate-900 dark:text-white flex items-center gap-2">
                  <Bookmark className="h-4 w-4 text-emerald-600" />
                  <span>Canonical Theorems & Takeaways</span>
                </h4>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                  {currentRev.key_theorems.map((thm: any, tIdx: number) => (
                    <div 
                      key={tIdx}
                      className="p-4 rounded-xl bg-emerald-50/50 dark:bg-emerald-950/20 border border-emerald-200/80 dark:border-emerald-900/60 space-y-1 text-xs"
                    >
                      <span className="font-extrabold text-emerald-900 dark:text-emerald-200">
                        {thm.title}:
                      </span>
                      <p className="text-slate-700 dark:text-slate-300 leading-relaxed">
                        {thm.statement}
                      </p>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Exam Traps & Negative Marking Warnings */}
            {currentRev.exam_traps && currentRev.exam_traps.length > 0 && (
              <div className="p-4 rounded-xl bg-amber-50/70 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-900/60 space-y-2">
                <div className="flex items-center gap-2 text-xs font-bold text-amber-950 dark:text-amber-200">
                  <AlertTriangle className="h-4 w-4 text-amber-600" />
                  <span>Exam Pitfalls & Negative Marking Warnings for {currentRev.name}</span>
                </div>
                <ul className="space-y-1 text-xs text-slate-700 dark:text-slate-300 list-disc list-inside">
                  {currentRev.exam_traps.map((trap: string, trIdx: number) => (
                    <li key={trIdx} className="leading-relaxed">
                      {trap}
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        </div>
      )}

      {/* Grid: Last Month Strategy vs Final Week Protocol */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 pt-4 border-t border-slate-200 dark:border-slate-800">
        {/* Last Month 30-Day Battle Plan */}
        <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-6 shadow-sm space-y-4">
          <h2 className="text-base font-bold text-slate-900 dark:text-white flex items-center gap-2">
            <Clock className="h-5 w-5 text-blue-600 dark:text-blue-400" />
            Last-Month (30 Days) Countdown Strategy
          </h2>
          <div className="space-y-3">
            {lastMonthStrategy.map((step: string, idx: number) => (
              <div key={idx} className="p-3.5 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200/80 dark:border-slate-700 text-xs sm:text-sm text-slate-700 dark:text-slate-300 flex items-start gap-3">
                <span className="font-extrabold text-blue-600 dark:text-blue-400 mt-0.5">#{idx + 1}</span>
                <span className="leading-relaxed">{step}</span>
              </div>
            ))}
          </div>
        </div>

        {/* Final 7-Day Protocol */}
        <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-6 shadow-sm space-y-4">
          <h2 className="text-base font-bold text-slate-900 dark:text-white flex items-center gap-2">
            <Zap className="h-5 w-5 text-rose-600 dark:text-rose-400" />
            Final-Week (7 Days) Rapid-Fire Protocol
          </h2>
          <div className="space-y-2.5">
            {finalWeekPack.map((day: string, idx: number) => {
              const parts = day.split(':');
              return (
                <div key={idx} className="p-3 rounded-xl bg-rose-50/50 dark:bg-rose-950/20 border border-rose-200/60 dark:border-rose-900/40 text-xs">
                  <span className="font-extrabold text-rose-700 dark:text-rose-400 mr-2">{parts[0]}:</span>
                  <span className="text-slate-700 dark:text-slate-300 font-medium">{parts[1]}</span>
                </div>
              );
            })}
          </div>
        </div>
      </div>

      {/* Last Day Checklist */}
      <div className="bg-gradient-to-r from-amber-500/10 via-orange-500/10 to-red-500/10 border border-amber-500/30 rounded-2xl p-6 space-y-4">
        <h3 className="text-base font-extrabold text-amber-950 dark:text-amber-200 flex items-center gap-2">
          <ShieldAlert className="h-5 w-5 text-amber-600" />
          Last-Day High-Probability Checklist & Exam Protocol
        </h3>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs text-slate-700 dark:text-slate-300">
          <div className="p-3 bg-white/80 dark:bg-slate-900/80 rounded-xl border border-amber-200 dark:border-slate-700">
            <h4 className="font-bold text-slate-900 dark:text-white mb-1">1. Admit Card & Identification</h4>
            <p>Printed color Admit Card, valid original government photo ID (Aadhaar / Passport / Voter ID / PAN) as specified during application.</p>
          </div>
          <div className="p-3 bg-white/80 dark:bg-slate-900/80 rounded-xl border border-amber-200 dark:border-slate-700">
            <h4 className="font-bold text-slate-900 dark:text-white mb-1">2. Mental Conditioning</h4>
            <p>Do NOT attempt new complex unsolved problems on the final day. Only review the master formula sheet and sleep at least 7.5 hours.</p>
          </div>
          <div className="p-3 bg-white/80 dark:bg-slate-900/80 rounded-xl border border-amber-200 dark:border-slate-700">
            <h4 className="font-bold text-slate-900 dark:text-white mb-1">3. CBT Exam Strategy</h4>
            <p>Start with General Aptitude (first 25-30 mins). Mark easy 1-mark questions first. Avoid guessing on 2-mark MCQs (-0.67 penalty!).</p>
          </div>
        </div>
      </div>
    </div>
  );
};
