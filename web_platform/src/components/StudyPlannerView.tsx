import React, { useState } from 'react';
import { CalendarCheck, Clock, CheckCircle2, Circle, FileDown, AlertCircle, ArrowRight } from 'lucide-react';

interface StudyPlannerViewProps {
  studyPlans: any;
  completedTasks: string[];
  toggleTaskCompletion: (taskId: string) => void;
}

export const StudyPlannerView: React.FC<StudyPlannerViewProps> = ({
  studyPlans,
  completedTasks,
  toggleTaskCompletion,
}) => {
  const [selectedTier, setSelectedTier] = useState<string>('4_hours');
  const schedules = studyPlans.schedules;
  const currentSchedule = schedules[selectedTier];
  const roadmap = studyPlans.weekly_roadmap;

  return (
    <div className="space-y-6 animate-fadeIn">
      {/* Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-6 border-b border-slate-200 dark:border-slate-800">
        <div>
          <div className="inline-flex items-center gap-1.5 text-xs font-semibold text-emerald-600 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-950/60 px-2.5 py-1 rounded-full mb-2 border border-emerald-200 dark:border-emerald-800">
            <CalendarCheck className="h-3.5 w-3.5" />
            16-Week Target Roadmap
          </div>
          <h1 className="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white">
            Personalized Study Timetable & Daily Targets
          </h1>
          <p className="text-sm text-slate-500 dark:text-slate-400 mt-1">
            Tailored schedules for working professionals, college students, and full-time aspirants targeting Feb 6, 2027.
          </p>
        </div>

        <div>
          <a
            href="./16_Study_Plans/GATE_2027_Complete_Study_Planner.pdf"
            download
            className="flex items-center gap-2 bg-blue-600 hover:bg-blue-700 text-white font-semibold text-xs px-4 py-2.5 rounded-xl shadow-sm transition"
          >
            <FileDown className="h-4 w-4" />
            <span>Download Complete Planner PDF</span>
          </a>
        </div>
      </div>

      {/* Schedule Selector Cards (2h, 4h, 6h) */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
        {[
          { key: '2_hours', title: '2 Hours / Day', desc: 'Working Professionals / College Final Year', badge: 'Light Tier' },
          { key: '4_hours', title: '4 Hours / Day', desc: 'Standard Balanced Preparation Plan', badge: 'Recommended' },
          { key: '6_hours', title: '6 Hours / Day', desc: 'Full-Time Dropper / Rank Booster', badge: 'Intensive Tier' }
        ].map((item) => {
          const isSelected = selectedTier === item.key;
          return (
            <div
              key={item.key}
              onClick={() => setSelectedTier(item.key)}
              className={`cursor-pointer p-5 rounded-2xl border transition shadow-sm ${
                isSelected
                  ? 'bg-blue-50/70 dark:bg-blue-950/40 border-blue-500 ring-2 ring-blue-500/20'
                  : 'bg-white dark:bg-slate-900 border-slate-200 dark:border-slate-800 hover:border-slate-300'
              }`}
            >
              <div className="flex items-center justify-between mb-2">
                <span className={`text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded ${
                  isSelected ? 'bg-blue-600 text-white' : 'bg-slate-100 dark:bg-slate-800 text-slate-500'
                }`}>
                  {item.badge}
                </span>
                <Clock className={`h-4 w-4 ${isSelected ? 'text-blue-600' : 'text-slate-400'}`} />
              </div>
              <h3 className="font-extrabold text-base text-slate-900 dark:text-white">{item.title}</h3>
              <p className="text-xs text-slate-500 dark:text-slate-400 mt-1">{item.desc}</p>
            </div>
          );
        })}
      </div>

      {/* Active Daily Breakdown */}
      <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-6 shadow-sm space-y-4">
        <h2 className="text-base font-bold text-slate-900 dark:text-white">
          Daily Routine & Strategy ({currentSchedule.title})
        </h2>

        <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
          <div className="p-4 rounded-xl bg-blue-50/60 dark:bg-blue-950/30 border border-blue-100 dark:border-blue-900/60">
            <span className="text-xs font-semibold text-blue-700 dark:text-blue-400">Concept Study & Notes</span>
            <div className="text-xl font-extrabold text-blue-900 dark:text-blue-200 mt-1">
              {currentSchedule.daily_breakdown.concept_study_mins} Minutes
            </div>
          </div>
          <div className="p-4 rounded-xl bg-teal-50/60 dark:bg-teal-950/30 border border-teal-100 dark:border-teal-900/60">
            <span className="text-xs font-semibold text-teal-700 dark:text-teal-400">Practice & PYQs</span>
            <div className="text-xl font-extrabold text-teal-900 dark:text-teal-200 mt-1">
              {currentSchedule.daily_breakdown.practice_pyq_mins} Minutes
            </div>
          </div>
          <div className="p-4 rounded-xl bg-amber-50/60 dark:bg-amber-950/30 border border-amber-100 dark:border-amber-900/60">
            <span className="text-xs font-semibold text-amber-700 dark:text-amber-400">Rapid Revision</span>
            <div className="text-xl font-extrabold text-amber-900 dark:text-amber-200 mt-1">
              {currentSchedule.daily_breakdown.revision_mins} Minutes
            </div>
          </div>
        </div>

        <p className="text-xs text-slate-600 dark:text-slate-300 leading-relaxed pt-2">
          <b>Strategy Guideline:</b> {currentSchedule.strategy}
        </p>
      </div>

      {/* 16-Week Roadmap Checklist */}
      <div className="space-y-4">
        <div className="flex items-center justify-between">
          <h2 className="text-lg font-bold text-slate-900 dark:text-white">
            16-Week Master Calendar (October 2026 – February 2027)
          </h2>
          <span className="text-xs text-slate-500 font-semibold">
            {completedTasks.length} of {roadmap.length} weeks checked off
          </span>
        </div>

        <div className="space-y-3">
          {roadmap.map((weekItem: any) => {
            const taskId = `week-${weekItem.week}`;
            const isDone = completedTasks.includes(taskId);

            return (
              <div
                key={weekItem.week}
                className={`p-5 rounded-xl border transition ${
                  isDone
                    ? 'bg-emerald-50/40 dark:bg-emerald-950/20 border-emerald-300 dark:border-emerald-800'
                    : 'bg-white dark:bg-slate-900 border-slate-200 dark:border-slate-800'
                }`}
              >
                <div className="flex items-start justify-between gap-3">
                  <div className="flex items-start gap-3">
                    <button
                      onClick={() => toggleTaskCompletion(taskId)}
                      className="mt-0.5 text-slate-400 hover:text-emerald-600 transition"
                    >
                      {isDone ? (
                        <CheckCircle2 className="h-5 w-5 text-emerald-500" />
                      ) : (
                        <Circle className="h-5 w-5" />
                      )}
                    </button>
                    <div>
                      <div className="flex flex-wrap items-center gap-2">
                        <span className="text-xs font-extrabold px-2 py-0.5 rounded bg-blue-100 dark:bg-blue-950 text-blue-700 dark:text-blue-300">
                          Week {weekItem.week}
                        </span>
                        <span className="text-xs font-bold text-slate-900 dark:text-white">
                          {weekItem.phase}
                        </span>
                        <span className="text-xs text-slate-500">
                          ({weekItem.subjects.join(', ')})
                        </span>
                      </div>

                      <div className="mt-2 text-xs text-slate-600 dark:text-slate-300">
                        <b>Topics:</b> {weekItem.topics.join(' • ')}
                      </div>
                      <div className="mt-1 text-xs text-slate-500 dark:text-slate-400">
                        <b>Target:</b> {weekItem.targets}
                      </div>
                    </div>
                  </div>

                  <span className="text-[11px] font-semibold text-amber-700 dark:text-amber-400 bg-amber-50 dark:bg-amber-950/60 px-2.5 py-1 rounded-lg border border-amber-200 dark:border-amber-800 flex-shrink-0 hidden sm:inline-block">
                    {weekItem.buffer_day}
                  </span>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};
