import React, { useState, useMemo } from 'react';
import { 
  CalendarCheck, 
  Clock, 
  CheckCircle2, 
  Circle, 
  FileDown, 
  AlertCircle, 
  Sparkles, 
  Target, 
  Award,
  Filter,
  CheckCircle,
  ChevronDown,
  ChevronUp,
  Play,
  Youtube,
  BookOpen,
  ExternalLink,
  ArrowRight
} from 'lucide-react';

interface StudyPlannerViewProps {
  studyPlans: any;
  completedTasks: string[];
  toggleTaskCompletion: (taskId: string) => void;
  navigateToTopic?: (subjectId: string, chapterIndex?: number) => void;
}

export const StudyPlannerView: React.FC<StudyPlannerViewProps> = ({
  studyPlans,
  completedTasks,
  toggleTaskCompletion,
  navigateToTopic,
}) => {
  const [selectedTier, setSelectedTier] = useState<string>('4_hours');
  const [phaseFilter, setPhaseFilter] = useState<string>('all');
  const [expandedWeek, setExpandedWeek] = useState<number | null>(1); // Week 1 expanded by default

  const schedules = studyPlans.schedules;
  const currentSchedule = schedules[selectedTier];
  const roadmap = studyPlans.weekly_roadmap;

  // Filtered roadmap
  const filteredRoadmap = useMemo(() => {
    if (phaseFilter === 'all') return roadmap;
    return roadmap.filter((w: any) => w.phase_category === phaseFilter);
  }, [roadmap, phaseFilter]);

  // Overall progress
  const completedCount = completedTasks.filter((t: string) => t.startsWith('week-')).length;
  const progressPercent = Math.min(100, Math.round((completedCount / roadmap.length) * 100));

  const toggleExpand = (weekNum: number) => {
    setExpandedWeek(prev => (prev === weekNum ? null : weekNum));
  };

  return (
    <div className="space-y-6 animate-fadeIn">
      {/* Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-6 border-b border-slate-200 dark:border-slate-800">
        <div>
          <div className="inline-flex items-center gap-1.5 text-xs font-semibold text-emerald-600 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-950/60 px-3 py-1 rounded-full mb-2 border border-emerald-200 dark:border-emerald-800">
            <Sparkles className="h-3.5 w-3.5 text-amber-500" />
            <span>3-Month Early Completion Masterplan: Finish 100% by Nov 1, 2026</span>
          </div>
          <h1 className="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white">
            Personalized Study Timetable & Daily Targets
          </h1>
          <p className="text-sm text-slate-500 dark:text-slate-400 mt-1 max-w-3xl">
            Structured roadmap engineered to complete 100% of all 11 GATE CSE subjects <b>3 months prior to the exam</b>, with detailed 7-day daily plans, direct topic explanations, and curated YouTube video lectures.
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

      {/* 3-Month Buffer Strategy Banner */}
      <div className="bg-gradient-to-r from-blue-500/10 via-emerald-500/10 to-teal-500/10 border border-blue-200/80 dark:border-blue-800/60 rounded-2xl p-5 shadow-sm">
        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
          <div className="space-y-1">
            <div className="flex items-center gap-2">
              <Award className="h-5 w-5 text-amber-500" />
              <h3 className="font-extrabold text-sm sm:text-base text-slate-900 dark:text-white">
                The 3-Month Pre-Exam Buffer Strategy
              </h3>
            </div>
            <p className="text-xs text-slate-600 dark:text-slate-300">
              <b>Milestone 1 (Weeks 1–16):</b> 100% syllabus completed by <b>November 1, 2026</b>.
              <span className="mx-2 hidden sm:inline">•</span>
              <b>Milestone 2 (Nov–Jan):</b> 90 days of dedicated Subject Tests, 10 Full CBT Mocks, and Weakness Elimination.
            </p>
          </div>
          <div className="flex items-center gap-3 w-full sm:w-auto">
            <div className="text-right hidden md:block">
              <div className="text-xs text-slate-500 dark:text-slate-400 font-medium">Preparation Progress</div>
              <div className="text-lg font-black text-emerald-600 dark:text-emerald-400">{progressPercent}%</div>
            </div>
            <div className="w-full sm:w-32 bg-slate-200 dark:bg-slate-700 h-2.5 rounded-full overflow-hidden">
              <div 
                className="bg-emerald-500 h-full rounded-full transition-all duration-500"
                style={{ width: `${progressPercent}%` }}
              />
            </div>
          </div>
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

      {/* Master Calendar Roadmap */}
      <div className="space-y-4">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div>
            <h2 className="text-lg font-bold text-slate-900 dark:text-white">
              Master Preparation Roadmap & Daily Plans
            </h2>
            <p className="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
              Click any week to open its <b>Detailed 7-Day Plan</b> with direct topic explanations and YouTube lectures.
            </p>
          </div>
          <span className="text-xs text-slate-500 font-semibold self-start sm:self-auto">
            {completedCount} of {roadmap.length} weeks checked off
          </span>
        </div>

        {/* Phase Filter Buttons */}
        <div className="flex flex-wrap items-center gap-1.5 pt-1">
          {[
            { id: 'all', label: 'All Weeks (Full Plan)' },
            { id: 'syllabus', label: '100% Syllabus (Weeks 1–16)' },
            { id: 'revision', label: 'Month -3: Revision (Nov)' },
            { id: 'mocks', label: 'Month -2: CBT Mocks (Dec)' },
            { id: 'final_sprint', label: 'Month -1: Final Sprint (Jan)' },
            { id: 'exam_week', label: 'Exam Week (Feb)' },
          ].map((tab) => {
            const isActive = phaseFilter === tab.id;
            return (
              <button
                key={tab.id}
                onClick={() => setPhaseFilter(tab.id)}
                className={`text-xs px-3 py-1.5 rounded-lg font-medium transition ${
                  isActive
                    ? 'bg-blue-600 text-white shadow-xs font-bold'
                    : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700'
                }`}
              >
                {tab.label}
              </button>
            );
          })}
        </div>

        {/* Roadmap Items List */}
        <div className="space-y-3">
          {filteredRoadmap.map((weekItem: any) => {
            const taskId = `week-${weekItem.week}`;
            const isDone = completedTasks.includes(taskId);
            const isMilestoneWeek = weekItem.week === 16;
            const isExpanded = expandedWeek === weekItem.week;

            // Mapping for quick jump
            const defaultSubId = weekItem.daily_plan?.[0]?.subject_id || 'EM';
            const defaultChapIdx = weekItem.daily_plan?.[0]?.chapter_index || 0;

            return (
              <div
                key={weekItem.week}
                className={`rounded-2xl border transition overflow-hidden shadow-xs ${
                  isMilestoneWeek
                    ? 'bg-amber-50/50 dark:bg-amber-950/20 border-amber-400 dark:border-amber-700 ring-2 ring-amber-400/20'
                    : isDone
                    ? 'bg-emerald-50/30 dark:bg-emerald-950/10 border-emerald-300 dark:border-emerald-800'
                    : 'bg-white dark:bg-slate-900 border-slate-200 dark:border-slate-800'
                }`}
              >
                {/* Week Header Row */}
                <div 
                  onClick={() => toggleExpand(weekItem.week)}
                  className="p-5 cursor-pointer hover:bg-slate-50/80 dark:hover:bg-slate-800/40 transition flex items-start justify-between gap-4"
                >
                  <div className="flex items-start gap-3">
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        toggleTaskCompletion(taskId);
                      }}
                      className="mt-0.5 text-slate-400 hover:text-emerald-600 transition flex-shrink-0"
                      title={isDone ? 'Mark as Incomplete' : 'Mark as Completed'}
                    >
                      {isDone ? (
                        <CheckCircle2 className="h-5 w-5 text-emerald-500" />
                      ) : (
                        <Circle className="h-5 w-5" />
                      )}
                    </button>

                    <div className="space-y-1.5">
                      <div className="flex flex-wrap items-center gap-2">
                        <span className={`text-xs font-extrabold px-2 py-0.5 rounded ${
                          isMilestoneWeek
                            ? 'bg-amber-500 text-white'
                            : 'bg-blue-100 dark:bg-blue-950 text-blue-700 dark:text-blue-300'
                        }`}>
                          Week {weekItem.week}
                        </span>
                        <h3 className="text-sm font-bold text-slate-900 dark:text-white">
                          {weekItem.phase}
                        </h3>
                        <span className="text-xs text-slate-500 dark:text-slate-400">
                          ({weekItem.subjects.join(', ')})
                        </span>
                      </div>

                      {/* Clickable Topics Pills */}
                      <div className="flex flex-wrap items-center gap-1.5 pt-0.5">
                        <span className="text-xs font-semibold text-slate-500 dark:text-slate-400">Topics:</span>
                        {weekItem.topics.map((t: string, tIdx: number) => (
                          <button
                            key={tIdx}
                            onClick={(e) => {
                              e.stopPropagation();
                              if (navigateToTopic) {
                                navigateToTopic(defaultSubId, defaultChapIdx);
                              }
                            }}
                            className="inline-flex items-center gap-1 text-[11px] font-semibold text-blue-700 dark:text-blue-300 bg-blue-50 dark:bg-blue-950/60 hover:bg-blue-100 dark:hover:bg-blue-900/60 px-2.5 py-0.5 rounded-md border border-blue-200 dark:border-blue-900/60 transition group"
                            title="Click to view detailed explanation & notes"
                          >
                            <BookOpen className="h-3 w-3 text-blue-500 group-hover:scale-110 transition" />
                            <span>{t}</span>
                          </button>
                        ))}
                      </div>

                      <div className="text-xs text-slate-500 dark:text-slate-400 pt-0.5">
                        <b>Weekly Target:</b> {weekItem.targets}
                      </div>

                      {isMilestoneWeek && (
                        <div className="mt-2 inline-flex items-center gap-1.5 bg-amber-100 dark:bg-amber-900/60 text-amber-900 dark:text-amber-200 text-xs font-bold px-2.5 py-1 rounded-lg border border-amber-300 dark:border-amber-700">
                          <Target className="h-3.5 w-3.5 text-amber-600" />
                          <span>CRITICAL GOAL: 100% Complete Syllabus finished 3 months prior to GATE exam!</span>
                        </div>
                      )}
                    </div>
                  </div>

                  <div className="flex items-center gap-2 flex-shrink-0">
                    <span className={`text-[11px] font-semibold px-2.5 py-1 rounded-lg border hidden sm:inline-block ${
                      isMilestoneWeek
                        ? 'bg-amber-500 text-white border-amber-600'
                        : 'text-amber-700 dark:text-amber-400 bg-amber-50 dark:bg-amber-950/60 border-amber-200 dark:border-amber-800'
                    }`}>
                      {weekItem.buffer_day}
                    </span>

                    <button
                      className="p-1.5 rounded-lg text-slate-400 hover:text-slate-700 dark:hover:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800 transition"
                      title={isExpanded ? 'Collapse Daily Plan' : 'Expand Detailed 7-Day Plan'}
                    >
                      {isExpanded ? <ChevronUp className="h-4 w-4" /> : <ChevronDown className="h-4 w-4" />}
                    </button>
                  </div>
                </div>

                {/* EXPANDED DETAILED DAILY PLAN */}
                {isExpanded && weekItem.daily_plan && (
                  <div className="border-t border-slate-100 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-950/50 p-5 space-y-3">
                    <div className="flex items-center justify-between pb-2">
                      <div className="flex items-center gap-2">
                        <CalendarCheck className="h-4 w-4 text-blue-600" />
                        <h4 className="text-xs font-extrabold uppercase tracking-wider text-slate-700 dark:text-slate-300">
                          Detailed 7-Day Daily Study Schedule & Lectures
                        </h4>
                      </div>
                      <span className="text-[11px] text-slate-500 dark:text-slate-400">
                        Click topic to read notes • Click YouTube to watch video
                      </span>
                    </div>

                    <div className="grid grid-cols-1 gap-2.5">
                      {weekItem.daily_plan.map((dayItem: any) => {
                        const dayTaskId = `day-w${weekItem.week}-d${dayItem.day}`;
                        const isDayDone = completedTasks.includes(dayTaskId);

                        return (
                          <div
                            key={dayItem.day}
                            className={`p-3.5 rounded-xl border transition flex flex-col sm:flex-row sm:items-center justify-between gap-3 ${
                              isDayDone
                                ? 'bg-emerald-50/40 dark:bg-emerald-950/20 border-emerald-300 dark:border-emerald-800'
                                : 'bg-white dark:bg-slate-900 border-slate-200 dark:border-slate-800'
                            }`}
                          >
                            <div className="flex items-start sm:items-center gap-3">
                              <button
                                onClick={() => toggleTaskCompletion(dayTaskId)}
                                className="mt-0.5 sm:mt-0 text-slate-400 hover:text-emerald-600 transition flex-shrink-0"
                                title={isDayDone ? 'Mark Day Incomplete' : 'Mark Day Completed'}
                              >
                                {isDayDone ? (
                                  <CheckCircle2 className="h-4 w-4 text-emerald-500" />
                                ) : (
                                  <Circle className="h-4 w-4" />
                                )}
                              </button>

                              <div className="space-y-0.5">
                                <div className="flex flex-wrap items-center gap-2">
                                  <span className="text-[10px] font-bold text-slate-500 dark:text-slate-400 bg-slate-100 dark:bg-slate-800 px-2 py-0.5 rounded">
                                    {dayItem.day_name}
                                  </span>

                                  {/* Direct Clickable Topic Button */}
                                  <button
                                    onClick={() => {
                                      if (navigateToTopic) {
                                        navigateToTopic(dayItem.subject_id, dayItem.chapter_index);
                                      }
                                    }}
                                    className="text-xs font-bold text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300 hover:underline flex items-center gap-1 text-left"
                                    title="Click to open Topic Detail Explanation & Notes"
                                  >
                                    <BookOpen className="h-3.5 w-3.5 flex-shrink-0" />
                                    <span>{dayItem.topic}</span>
                                  </button>
                                </div>

                                <p className="text-xs text-slate-600 dark:text-slate-300">
                                  {dayItem.task}
                                </p>
                              </div>
                            </div>

                            {/* Direct Actions: Read Theory & Watch YouTube Video */}
                            <div className="flex items-center gap-2 self-start sm:self-auto pl-7 sm:pl-0 flex-shrink-0">
                              <button
                                onClick={() => {
                                  if (navigateToTopic) {
                                    navigateToTopic(dayItem.subject_id, dayItem.chapter_index);
                                  }
                                }}
                                className="inline-flex items-center gap-1 px-2.5 py-1 rounded-lg text-[11px] font-semibold bg-blue-50 hover:bg-blue-600 text-blue-600 hover:text-white dark:bg-blue-950/60 dark:text-blue-300 dark:hover:bg-blue-600 dark:hover:text-white border border-blue-200 dark:border-blue-800 transition"
                              >
                                <BookOpen className="h-3 w-3" />
                                <span>Read Theory</span>
                              </button>

                              <a
                                href={dayItem.video_url}
                                target="_blank"
                                rel="noopener noreferrer"
                                className="inline-flex items-center gap-1 px-2.5 py-1 rounded-lg text-[11px] font-semibold bg-red-50 hover:bg-red-600 text-red-600 hover:text-white dark:bg-red-950/60 dark:text-red-300 dark:hover:bg-red-600 dark:hover:text-white border border-red-200 dark:border-red-900 transition"
                                title="Watch curated video lecture on YouTube"
                              >
                                <Play className="h-3 w-3 fill-current" />
                                <span>Watch Video</span>
                              </a>
                            </div>
                          </div>
                        );
                      })}
                    </div>
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};
