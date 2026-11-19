import React from 'react';
import { 
  BookOpen, 
  FileDown, 
  Clock, 
  Award, 
  Sparkles, 
  TrendingUp, 
  CheckCircle2, 
  ArrowRight,
  ShieldCheck,
  Calendar,
  Layers,
  HelpCircle
} from 'lucide-react';

interface HomeDashboardProps {
  setCurrentTab: (tab: string) => void;
  gateData: any;
  completedTopics: string[];
}

export const HomeDashboard: React.FC<HomeDashboardProps> = ({
  setCurrentTab,
  gateData,
  completedTopics,
}) => {
  const totalSubjects = gateData.subjects.length;
  const totalPdfs = gateData.pdfLibrary.length;
  const totalPyqs = gateData.pyqs.length;
  const totalQuestions = gateData.practiceQuestions.length;

  // Compute coverage percentage
  const totalTopicsCount = gateData.subjects.reduce(
    (acc: number, s: any) => acc + s.chapters.length,
    0
  );
  const coveragePercent = Math.min(
    100,
    Math.round((completedTopics.length / Math.max(1, totalTopicsCount)) * 100)
  );

  return (
    <div className="space-y-8 animate-fadeIn">
      {/* Hero Welcome Banner */}
      <div className="relative overflow-hidden rounded-2xl bg-gradient-to-r from-blue-900 via-indigo-900 to-slate-900 text-white p-8 sm:p-10 shadow-xl">
        <div className="absolute right-0 top-0 -mt-10 -mr-10 w-96 h-96 rounded-full bg-blue-500/10 blur-3xl pointer-events-none" />
        <div className="relative z-10 max-w-3xl">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-500/20 border border-blue-400/30 text-blue-200 text-xs font-semibold mb-4">
            <ShieldCheck className="h-3.5 w-3.5 text-teal-400" />
            Official GATE 2027 Syllabus Compliant | IIT Madras
          </div>
          <h1 className="text-3xl sm:text-4xl font-extrabold tracking-tight text-white mb-3">
            GATE 2027 Computer Science & IT Preparation System
          </h1>
          <p className="text-slate-300 text-sm sm:text-base leading-relaxed mb-6">
            Comprehensive curriculum, 120+ downloadable PDF books and notes, verified previous year questions (2012–2026), interactive 180-minute CBT exam simulator, and personalized daily schedules.
          </p>

          <div className="flex flex-wrap items-center gap-3">
            <button
              onClick={() => setCurrentTab('mock_tests')}
              className="flex items-center gap-2 bg-gradient-to-r from-blue-500 to-teal-400 hover:from-blue-600 hover:to-teal-500 text-slate-950 font-bold px-5 py-2.5 rounded-xl shadow-lg transition"
            >
              <Award className="h-4 w-4" />
              <span>Take Full-Length CBT Mock</span>
            </button>
            <button
              onClick={() => setCurrentTab('subject_library')}
              className="flex items-center gap-2 bg-white/10 hover:bg-white/20 text-white font-semibold px-4 py-2.5 rounded-xl border border-white/20 transition"
            >
              <BookOpen className="h-4 w-4" />
              <span>Browse Subject Library</span>
            </button>
            <button
              onClick={() => setCurrentTab('pdf_library')}
              className="flex items-center gap-2 bg-white/10 hover:bg-white/20 text-white font-semibold px-4 py-2.5 rounded-xl border border-white/20 transition"
            >
              <FileDown className="h-4 w-4" />
              <span>Download 120+ PDFs</span>
            </button>
          </div>
        </div>
      </div>

      {/* Metrics Row */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
        <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-5 shadow-sm">
          <div className="flex items-center justify-between text-slate-500 dark:text-slate-400 text-xs font-semibold mb-1">
            <span>Syllabus Subjects</span>
            <Layers className="h-4 w-4 text-blue-500" />
          </div>
          <div className="text-2xl font-extrabold text-slate-900 dark:text-white">{totalSubjects}</div>
          <p className="text-[11px] text-slate-500 dark:text-slate-400 mt-1">11 Mandatory Sections</p>
        </div>

        <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-5 shadow-sm">
          <div className="flex items-center justify-between text-slate-500 dark:text-slate-400 text-xs font-semibold mb-1">
            <span>Published PDFs</span>
            <FileDown className="h-4 w-4 text-teal-500" />
          </div>
          <div className="text-2xl font-extrabold text-slate-900 dark:text-white">{totalPdfs}</div>
          <p className="text-[11px] text-teal-600 dark:text-teal-400 mt-1">100% Downloadable Offline</p>
        </div>

        <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-5 shadow-sm">
          <div className="flex items-center justify-between text-slate-500 dark:text-slate-400 text-xs font-semibold mb-1">
            <span>Verified PYQs</span>
            <HelpCircle className="h-4 w-4 text-amber-500" />
          </div>
          <div className="text-2xl font-extrabold text-slate-900 dark:text-white">{totalPyqs}+</div>
          <p className="text-[11px] text-slate-500 dark:text-slate-400 mt-1">2012 - 2026 Solved</p>
        </div>

        <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-5 shadow-sm">
          <div className="flex items-center justify-between text-slate-500 dark:text-slate-400 text-xs font-semibold mb-1">
            <span>Study Progress</span>
            <TrendingUp className="h-4 w-4 text-emerald-500" />
          </div>
          <div className="text-2xl font-extrabold text-slate-900 dark:text-white">{coveragePercent}%</div>
          <p className="text-[11px] text-emerald-600 dark:text-emerald-400 mt-1">{completedTopics.length} of {totalTopicsCount} topics done</p>
        </div>
      </div>

      {/* Progress & Quick Links Section */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Left 2 Cols: Subject Grid */}
        <div className="lg:col-span-2 space-y-4">
          <div className="flex items-center justify-between">
            <h2 className="text-lg font-bold text-slate-900 dark:text-white">Curriculum Subject Matrix</h2>
            <button
              onClick={() => setCurrentTab('subject_library')}
              className="text-xs font-semibold text-blue-600 dark:text-blue-400 hover:underline flex items-center gap-1"
            >
              <span>View All Notes</span>
              <ArrowRight className="h-3.5 w-3.5" />
            </button>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            {gateData.subjects.map((sub: any) => (
              <div
                key={sub.id}
                onClick={() => setCurrentTab('subject_library')}
                className="group cursor-pointer bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 hover:border-blue-400 dark:hover:border-blue-600 rounded-xl p-4 transition shadow-sm hover:shadow-md"
              >
                <div className="flex items-start justify-between">
                  <div>
                    <span className="text-[10px] font-bold uppercase tracking-wider text-blue-600 dark:text-blue-400 bg-blue-50 dark:bg-blue-950/60 px-2 py-0.5 rounded">
                      {sub.id} • {sub.weightage}
                    </span>
                    <h3 className="font-bold text-sm text-slate-900 dark:text-white mt-1.5 group-hover:text-blue-600 dark:group-hover:text-blue-400 transition">
                      {sub.name}
                    </h3>
                  </div>
                  <BookOpen className="h-4 w-4 text-slate-400 group-hover:text-blue-500 transition" />
                </div>
                <p className="text-xs text-slate-500 dark:text-slate-400 mt-2 line-clamp-2">
                  {sub.topics.join(' • ')}
                </p>
                <div className="mt-3 flex items-center gap-3 text-[11px] text-slate-500 dark:text-slate-400 pt-2 border-t border-slate-100 dark:border-slate-800">
                  <span>{sub.chapters.length} Detailed Chapters</span>
                  <span>•</span>
                  <span>{sub.questionCount} Practice Qs</span>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Right Col: Official Exam Facts & Quick Tools */}
        <div className="space-y-6">
          {/* Official IIT Madras Card */}
          <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-5 shadow-sm">
            <h3 className="text-sm font-bold text-slate-900 dark:text-white flex items-center gap-2 mb-3">
              <ShieldCheck className="h-4 w-4 text-teal-600 dark:text-teal-400" />
              Official Examination Parameters
            </h3>
            <ul className="space-y-2.5 text-xs text-slate-600 dark:text-slate-300">
              <li className="flex justify-between pb-2 border-b border-slate-100 dark:border-slate-800">
                <span className="text-slate-500 dark:text-slate-400">Organizing Institute:</span>
                <span className="font-semibold text-slate-900 dark:text-white">IIT Madras</span>
              </li>
              <li className="flex justify-between pb-2 border-b border-slate-100 dark:border-slate-800">
                <span className="text-slate-500 dark:text-slate-400">Exam Mode:</span>
                <span className="font-semibold text-slate-900 dark:text-white">Computer Based Test (CBT)</span>
              </li>
              <li className="flex justify-between pb-2 border-b border-slate-100 dark:border-slate-800">
                <span className="text-slate-500 dark:text-slate-400">Exam Dates:</span>
                <span className="font-semibold text-slate-900 dark:text-white">Feb 6, 7, 13, 14, 20, 21, 2027</span>
              </li>
              <li className="flex justify-between pb-2 border-b border-slate-100 dark:border-slate-800">
                <span className="text-slate-500 dark:text-slate-400">Questions:</span>
                <span className="font-semibold text-slate-900 dark:text-white">65 (10 GA + 55 CS/Math)</span>
              </li>
              <li className="flex justify-between pb-2 border-b border-slate-100 dark:border-slate-800">
                <span className="text-slate-500 dark:text-slate-400">Negative Marking:</span>
                <span className="font-semibold text-slate-900 dark:text-white">1/3 (1M) | 2/3 (2M) for MCQs</span>
              </li>
              <li className="flex justify-between">
                <span className="text-slate-500 dark:text-slate-400">MSQ & NAT:</span>
                <span className="font-semibold text-emerald-600 dark:text-emerald-400">ZERO Negative Marking</span>
              </li>
            </ul>
          </div>

          {/* Quick Study Planner Shortcut */}
          <div className="bg-gradient-to-br from-amber-500/10 to-orange-500/10 border border-amber-500/20 rounded-xl p-5">
            <h3 className="text-sm font-bold text-amber-900 dark:text-amber-300 flex items-center gap-2 mb-2">
              <Calendar className="h-4 w-4 text-amber-600 dark:text-amber-400" />
              Preparation Timetable
            </h3>
            <p className="text-xs text-amber-800 dark:text-amber-400 mb-3 leading-relaxed">
              Targeted 16-week study schedule with 2h, 4h, and 6h daily options and automatic backlog recovery.
            </p>
            <button
              onClick={() => setCurrentTab('study_planner')}
              className="w-full bg-amber-600 hover:bg-amber-700 text-white font-semibold text-xs py-2 rounded-lg transition"
            >
              Open Interactive Study Planner
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};
