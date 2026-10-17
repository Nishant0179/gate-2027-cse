import React from 'react';
import {
  LayoutDashboard,
  FileCheck2,
  BookOpenCheck,
  FileDown,
  History,
  HelpCircle,
  Clock,
  Sparkles,
  CalendarCheck,
  TrendingUp,
  BookmarkCheck,
  Zap
} from 'lucide-react';

interface SidebarProps {
  currentTab: string;
  setCurrentTab: (tab: string) => void;
  pdfCount: number;
}

export const Sidebar: React.FC<SidebarProps> = ({ currentTab, setCurrentTab, pdfCount }) => {
  const menuItems = [
    { id: 'home', label: 'Dashboard', icon: LayoutDashboard },
    { id: 'syllabus', label: 'Official Syllabus', icon: FileCheck2 },
    { id: 'subject_library', label: 'Subject Library', icon: BookOpenCheck },
    { id: 'pdf_library', label: 'Downloadable PDFs', icon: FileDown, badge: `${pdfCount}` },
    { id: 'pyq_explorer', label: 'Verified PYQs', icon: History, badge: '2012-26' },
    { id: 'practice_banks', label: 'Question Bank', icon: HelpCircle },
    { id: 'mock_tests', label: 'CBT Exam Simulator', icon: Clock, highlight: true },
    { id: 'quick_revision', label: 'Quick Revision', icon: Zap },
    { id: 'formula_sheets', label: 'Formula Sheets', icon: Sparkles },
    { id: 'study_planner', label: 'Study Planner', icon: CalendarCheck },
    { id: 'analytics', label: 'Progress & Weak Areas', icon: TrendingUp },
  ];

  return (
    <aside className="w-64 flex-shrink-0 hidden lg:block border-r border-slate-200 dark:border-slate-800 bg-white/70 dark:bg-slate-900/70 p-4 sticky top-16 h-[calc(100vh-4rem)] overflow-y-auto">
      <div className="space-y-1">
        <p className="px-3 text-[11px] font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500 mb-2">
          Curriculum & Study
        </p>
        {menuItems.slice(0, 4).map((item) => {
          const Icon = item.icon;
          const isActive = currentTab === item.id;
          return (
            <button
              key={item.id}
              onClick={() => setCurrentTab(item.id)}
              className={`w-full flex items-center justify-between px-3 py-2 rounded-lg text-sm font-medium transition ${
                isActive
                  ? 'bg-blue-50 dark:bg-blue-900/30 text-blue-700 dark:text-blue-400 font-semibold shadow-sm'
                  : 'text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800/60'
              }`}
            >
              <div className="flex items-center gap-3">
                <Icon className={`h-4 w-4 ${isActive ? 'text-blue-600 dark:text-blue-400' : 'text-slate-400'}`} />
                <span>{item.label}</span>
              </div>
              {item.badge && (
                <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">
                  {item.badge}
                </span>
              )}
            </button>
          );
        })}

        <div className="pt-4">
          <p className="px-3 text-[11px] font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500 mb-2">
            Practice & Evaluation
          </p>
          {menuItems.slice(4, 7).map((item) => {
            const Icon = item.icon;
            const isActive = currentTab === item.id;
            return (
              <button
                key={item.id}
                onClick={() => setCurrentTab(item.id)}
                className={`w-full flex items-center justify-between px-3 py-2 rounded-lg text-sm font-medium transition ${
                  isActive
                    ? 'bg-blue-50 dark:bg-blue-900/30 text-blue-700 dark:text-blue-400 font-semibold shadow-sm'
                    : item.highlight
                    ? 'text-blue-600 dark:text-blue-400 hover:bg-blue-50/50 dark:hover:bg-blue-950/20'
                    : 'text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800/60'
                }`}
              >
                <div className="flex items-center gap-3">
                  <Icon className={`h-4 w-4 ${isActive ? 'text-blue-600 dark:text-blue-400' : item.highlight ? 'text-blue-600 dark:text-blue-400' : 'text-slate-400'}`} />
                  <span>{item.label}</span>
                </div>
                {item.badge && (
                  <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-blue-100 dark:bg-blue-900/60 text-blue-700 dark:text-blue-300">
                    {item.badge}
                  </span>
                )}
              </button>
            );
          })}
        </div>

        <div className="pt-4">
          <p className="px-3 text-[11px] font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500 mb-2">
            Revision & Planning
          </p>
          {menuItems.slice(7).map((item) => {
            const Icon = item.icon;
            const isActive = currentTab === item.id;
            return (
              <button
                key={item.id}
                onClick={() => setCurrentTab(item.id)}
                className={`w-full flex items-center justify-between px-3 py-2 rounded-lg text-sm font-medium transition ${
                  isActive
                    ? 'bg-blue-50 dark:bg-blue-900/30 text-blue-700 dark:text-blue-400 font-semibold shadow-sm'
                    : 'text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800/60'
                }`}
              >
                <div className="flex items-center gap-3">
                  <Icon className={`h-4 w-4 ${isActive ? 'text-blue-600 dark:text-blue-400' : 'text-slate-400'}`} />
                  <span>{item.label}</span>
                </div>
              </button>
            );
          })}
        </div>
      </div>

      {/* IIT Madras Compliant Badge */}
      <div className="mt-8 p-3 rounded-xl bg-gradient-to-br from-blue-50 to-teal-50 dark:from-slate-800 dark:to-slate-800/60 border border-blue-100 dark:border-slate-700">
        <div className="flex items-center gap-2 mb-1">
          <BookmarkCheck className="h-4 w-4 text-teal-600 dark:text-teal-400" />
          <span className="text-xs font-bold text-slate-900 dark:text-white">100% Verified</span>
        </div>
        <p className="text-[11px] text-slate-600 dark:text-slate-400 leading-snug">
          Curriculum mapped directly to the official GATE 2027 syllabus published by IIT Madras.
        </p>
      </div>
    </aside>
  );
};
