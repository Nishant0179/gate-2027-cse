import React from 'react';
import { Zap, Clock, ShieldAlert, FileDown, CheckCircle2 } from 'lucide-react';

interface QuickRevisionViewProps {
  finalRevision: any;
}

export const QuickRevisionView: React.FC<QuickRevisionViewProps> = ({ finalRevision }) => {
  const lastMonthStrategy = finalRevision.last_month_strategy || [];
  const finalWeekPack = finalRevision.final_week_pack || [];

  return (
    <div className="space-y-6 animate-fadeIn">
      {/* Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-6 border-b border-slate-200 dark:border-slate-800">
        <div>
          <div className="inline-flex items-center gap-1.5 text-xs font-semibold text-rose-600 dark:text-rose-400 bg-rose-50 dark:bg-rose-950/60 px-2.5 py-1 rounded-full mb-2 border border-rose-200 dark:border-rose-800">
            <Zap className="h-3.5 w-3.5" />
            High-Impact Final Sprint
          </div>
          <h1 className="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white">
            Quick Revision Center & Final Sprint Packs
          </h1>
          <p className="text-sm text-slate-500 dark:text-slate-400 mt-1">
            Last-month, final-week, and last-day high-probability topic checklists and memory anchors.
          </p>
        </div>

        <div>
          <a
            href="./17_Final_Revision/Final_Week_and_Last_Day_Pack.pdf"
            download
            className="flex items-center gap-2 bg-rose-600 hover:bg-rose-700 text-white font-semibold text-xs px-4 py-2.5 rounded-xl shadow-sm transition"
          >
            <FileDown className="h-4 w-4" />
            <span>Download Final Sprint Pack PDF</span>
          </a>
        </div>
      </div>

      {/* Grid: Last Month Strategy vs Final Week Protocol */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
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
