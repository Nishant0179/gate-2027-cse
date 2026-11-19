import React, { useState, useMemo } from 'react';
import { 
  BookOpen, 
  FileDown, 
  CheckCircle, 
  Circle, 
  AlertTriangle, 
  Lightbulb, 
  Sparkles, 
  ChevronRight,
  ChevronLeft,
  ChevronDown,
  ChevronUp,
  Bookmark,
  Share2,
  Table as TableIcon,
  Play,
  Youtube,
  ExternalLink,
  HelpCircle,
  CheckCircle2,
  XCircle,
  ArrowRight,
  Filter,
  Zap,
  Layers
} from 'lucide-react';

interface SubjectLibraryViewProps {
  gateData: any;
  completedTopics: string[];
  toggleTopicCompletion: (topicId: string) => void;
  selectedSubjectId?: string;
  setSelectedSubjectId?: (id: string) => void;
  activeChapterIndex?: number;
  setActiveChapterIndex?: (idx: number) => void;
  setCurrentTab?: (tab: string) => void;
}

export const SubjectLibraryView: React.FC<SubjectLibraryViewProps> = ({
  gateData,
  completedTopics,
  toggleTopicCompletion,
  selectedSubjectId: propSubjectId,
  setSelectedSubjectId: propSetSubjectId,
  activeChapterIndex: propChapterIndex,
  setActiveChapterIndex: propSetChapterIndex,
  setCurrentTab,
}) => {
  const [internalSubjectId, setInternalSubjectId] = useState<string>(gateData.subjects[0]?.id || 'EM');
  const [internalChapterIndex, setInternalChapterIndex] = useState<number>(0);

  const selectedSubjectId = propSubjectId !== undefined ? propSubjectId : internalSubjectId;
  const setSelectedSubjectId = propSetSubjectId !== undefined ? propSetSubjectId : setInternalSubjectId;

  const activeChapterIndex = propChapterIndex !== undefined ? propChapterIndex : internalChapterIndex;
  const setActiveChapterIndex = propSetChapterIndex !== undefined ? propSetChapterIndex : setInternalChapterIndex;

  // Interactive practice states on page
  const [selectedAnswers, setSelectedAnswers] = useState<Record<string, string>>({});
  const [revealedSolutions, setRevealedSolutions] = useState<Record<string, boolean>>({});
  const [practiceTypeFilter, setPracticeTypeFilter] = useState<'All' | 'MCQ' | 'MSQ' | 'NAT'>('All');
  const [practiceLimit, setPracticeLimit] = useState<number>(10);
  const [natInputs, setNatInputs] = useState<Record<string, string>>({});
  const [subjectViewMode, setSubjectViewMode] = useState<'chapters' | 'revision'>('chapters');
  const [readerSectionFilter, setReaderSectionFilter] = useState<'all' | 'stories' | 'foundations' | 'solved' | 'traps' | 'videos' | 'practice'>('all');
  const [readerFontSize, setReaderFontSize] = useState<'normal' | 'large' | 'xlarge'>('normal');

  const fontSizeClasses = {
    normal: { body: 'text-xs sm:text-sm', heading: 'text-sm sm:text-base', title: 'text-base sm:text-lg' },
    large: { body: 'text-sm sm:text-base', heading: 'text-base sm:text-lg', title: 'text-lg sm:text-xl' },
    xlarge: { body: 'text-base sm:text-lg', heading: 'text-lg sm:text-xl', title: 'text-xl sm:text-2xl' },
  }[readerFontSize];

  const handlePrevChapter = () => {
    if (activeChapterIndex > 0) {
      setActiveChapterIndex(activeChapterIndex - 1);
      setReaderSectionFilter('all');
      window.scrollTo({ top: 220, behavior: 'smooth' });
    }
  };

  const handleNextChapter = () => {
    if (activeChapterIndex < subject.chapters.length - 1) {
      setActiveChapterIndex(activeChapterIndex + 1);
      setReaderSectionFilter('all');
      window.scrollTo({ top: 220, behavior: 'smooth' });
    }
  };

  const subject = gateData.subjects.find((s: any) => s.id === selectedSubjectId) || gateData.subjects[0];
  const currentRev = gateData.subjectRevision ? gateData.subjectRevision[subject.id] : null;
  const chapter = subject.chapters[activeChapterIndex] || subject.chapters[0];
  const topicUniqueId = `${subject.id}-${activeChapterIndex}`;
  const isCompleted = completedTopics.includes(topicUniqueId);

  // Subject practice questions
  const subjectQuestions = gateData.practiceQuestions.filter(
    (q: any) => q.subject === subject.name || q.id.startsWith(subject.id)
  );

  const filteredSubjectQuestions = useMemo(() => {
    return subjectQuestions.filter((q: any) => {
      if (practiceTypeFilter === 'All') return true;
      return q.type === practiceTypeFilter;
    });
  }, [subjectQuestions, practiceTypeFilter]);

  const handleSelectOption = (qId: string, optKey: string) => {
    setSelectedAnswers(prev => ({ ...prev, [qId]: optKey }));
  };

  const toggleReveal = (qId: string) => {
    setRevealedSolutions(prev => ({ ...prev, [qId]: !prev[qId] }));
  };

  return (
    <div className="space-y-6 animate-fadeIn">
      {/* Subject Selector Bar */}
      <div className="flex items-center gap-2 overflow-x-auto pb-2 scrollbar-none">
        {gateData.subjects.map((sub: any) => {
          const isSelected = sub.id === selectedSubjectId;
          return (
            <button
              key={sub.id}
              onClick={() => {
                setSelectedSubjectId(sub.id);
                setActiveChapterIndex(0);
                setSubjectViewMode('chapters');
              }}
              className={`flex-shrink-0 px-3.5 py-2 rounded-xl text-xs font-semibold transition border ${
                isSelected
                  ? 'bg-blue-600 text-white border-blue-600 shadow-sm'
                  : 'bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-300 border-slate-200 dark:border-slate-800 hover:border-blue-400'
              }`}
            >
              <span>{sub.name}</span>
              <span className={`ml-2 text-[10px] px-1.5 py-0.5 rounded-full ${
                isSelected ? 'bg-blue-700 text-white' : 'bg-slate-100 dark:bg-slate-800 text-slate-500'
              }`}>
                {sub.weightage}
              </span>
            </button>
          );
        })}
      </div>

      {/* Prominent Subject Header & Complete Subject PDF Download Banner */}
      <div className="p-5 rounded-2xl bg-gradient-to-r from-blue-900 via-indigo-900 to-slate-900 text-white shadow-md flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <div className="flex items-center gap-2 mb-1">
            <span className="text-xs font-bold px-2.5 py-0.5 rounded bg-blue-500/30 text-blue-200 border border-blue-400/40">
              {subject.weightage}
            </span>
            <span className="text-xs text-blue-200 font-medium">
              {subject.chapters.length} In-Depth Chapters • 20 Practice Problems
            </span>
          </div>
          <h2 className="text-xl sm:text-2xl font-black tracking-tight">{subject.name}</h2>
          <p className="text-xs text-blue-200/80 mt-1 max-w-xl">
            Complete IIT Madras syllabus coverage from fundamentals to exam-level numericals.
          </p>
        </div>

        {/* Action / Download Buttons */}
        <div className="flex flex-wrap items-center gap-2">
          <a
            href={`./${subject.folder}/Subject_Complete_Notes.pdf`}
            download
            className="flex items-center gap-1.5 px-3.5 py-2.5 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-bold text-xs shadow-sm transition"
            title="Download Complete Subject PDF Book"
          >
            <FileDown className="h-4 w-4" />
            <span>Complete Subject PDF</span>
          </a>
          <a
            href={`./${subject.folder}/Quick_Revision_Notes.pdf`}
            download
            className="flex items-center gap-1.5 px-3.5 py-2.5 rounded-xl bg-white/10 hover:bg-white/20 text-white font-semibold text-xs border border-white/20 transition"
            title="Download Quick Revision Notes PDF"
          >
            <Zap className="h-4 w-4 text-amber-400" />
            <span>Quick Revision PDF</span>
          </a>
          <a
            href={`./${subject.folder}/Formula_Sheet.pdf`}
            download
            className="flex items-center gap-1.5 px-3.5 py-2.5 rounded-xl bg-white/10 hover:bg-white/20 text-white font-semibold text-xs border border-white/20 transition"
            title="Download Formula Sheet PDF"
          >
            <Sparkles className="h-4 w-4 text-emerald-400" />
            <span>Formula Sheet PDF</span>
          </a>
        </div>
      </div>

      {/* Mode Switcher Pills: In-Depth Chapter Study vs Subject Complete Quick Revision */}
      <div className="flex items-center gap-2 border-b border-slate-200 dark:border-slate-800 pb-2">
        <button
          onClick={() => setSubjectViewMode('chapters')}
          className={`px-4 py-2 rounded-xl text-xs font-bold transition flex items-center gap-2 ${
            subjectViewMode === 'chapters'
              ? 'bg-blue-600 text-white shadow-sm'
              : 'bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200'
          }`}
        >
          <BookOpen className="h-4 w-4" />
          <span>In-Depth Chapter Notes (Basic to Advanced)</span>
        </button>

        <button
          onClick={() => setSubjectViewMode('revision')}
          className={`px-4 py-2 rounded-xl text-xs font-bold transition flex items-center gap-2 ${
            subjectViewMode === 'revision'
              ? 'bg-blue-600 text-white shadow-sm'
              : 'bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200'
          }`}
        >
          <Zap className="h-4 w-4 text-amber-400" />
          <span>Subject Complete Revision & Formula Sheet</span>
        </button>
      </div>

      {/* RENDER SUBJECT COMPLETE REVISION VIEW IF ACTIVE */}
      {subjectViewMode === 'revision' && currentRev && (
        <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-6 sm:p-8 shadow-sm space-y-6">
          <div className="pb-4 border-b border-slate-100 dark:border-slate-800 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
            <div>
              <div className="inline-flex items-center gap-1.5 text-xs font-bold text-amber-600 dark:text-amber-400 bg-amber-50 dark:bg-amber-950/60 px-2.5 py-0.5 rounded-full mb-1 border border-amber-200 dark:border-amber-800">
                <Zap className="h-3 w-3" />
                15-Minute Complete Rapid Revision
              </div>
              <h3 className="text-xl sm:text-2xl font-black text-slate-900 dark:text-white">
                {currentRev.name} — Formulas, Theorems & Traps
              </h3>
            </div>

            <div className="flex items-center gap-2">
              <a
                href={currentRev.complete_pdf}
                download
                className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs shadow-xs transition"
              >
                <FileDown className="h-3.5 w-3.5" />
                <span>Complete Subject PDF</span>
              </a>
              <a
                href={currentRev.formula_sheet_pdf}
                download
                className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 text-slate-700 dark:text-slate-300 font-semibold text-xs transition"
              >
                <Sparkles className="h-3.5 w-3.5 text-emerald-500" />
                <span>Formula Sheet PDF</span>
              </a>
            </div>
          </div>

          {/* High Yield Formulas */}
          {currentRev.high_yield_formulas && (
            <div className="space-y-3">
              <h4 className="text-sm font-bold text-slate-900 dark:text-white flex items-center gap-2">
                <Sparkles className="h-4 w-4 text-blue-600" />
                <span>High-Yield Formulas & Exam Shortcuts</span>
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

          {/* Canonical Theorems */}
          {currentRev.key_theorems && (
            <div className="space-y-3 pt-2">
              <h4 className="text-sm font-bold text-slate-900 dark:text-white flex items-center gap-2">
                <Bookmark className="h-4 w-4 text-emerald-600" />
                <span>Canonical Theorems Tested by IITs</span>
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

          {/* Exam Traps */}
          {currentRev.exam_traps && (
            <div className="p-4 rounded-xl bg-amber-50/70 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-900/60 space-y-2">
              <div className="flex items-center gap-2 text-xs font-bold text-amber-950 dark:text-amber-200">
                <AlertTriangle className="h-4 w-4 text-amber-600" />
                <span>Common Exam Pitfalls & Negative Marking Warnings</span>
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
      )}

      {/* Main Content Layout (Chapters Mode) */}
      {subjectViewMode === 'chapters' && (
      <div className="grid grid-cols-1 lg:grid-cols-4 gap-6">
        {/* Chapters Navigation List */}
        <div className="space-y-2 lg:col-span-1">
          <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-4 shadow-sm">
            <h3 className="text-xs font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500 mb-3">
              Chapters in {subject.name}
            </h3>
            <div className="space-y-1.5">
              {subject.chapters.map((chap: any, idx: number) => {
                const isActive = activeChapterIndex === idx;
                const cId = `${subject.id}-${idx}`;
                const done = completedTopics.includes(cId);
                return (
                  <button
                    key={idx}
                    onClick={() => setActiveChapterIndex(idx)}
                    className={`w-full text-left p-2.5 rounded-lg text-xs font-medium transition flex items-start gap-2.5 ${
                      isActive
                        ? 'bg-blue-50 dark:bg-blue-900/30 text-blue-700 dark:text-blue-300 font-semibold border border-blue-200 dark:border-blue-800'
                        : 'text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800'
                    }`}
                  >
                    <div 
                      onClick={(e) => {
                        e.stopPropagation();
                        toggleTopicCompletion(cId);
                      }} 
                      className="mt-0.5 flex-shrink-0 cursor-pointer"
                    >
                      {done ? (
                        <CheckCircle className="h-3.5 w-3.5 text-emerald-500" />
                      ) : (
                        <Circle className="h-3.5 w-3.5 text-slate-400 hover:text-blue-500" />
                      )}
                    </div>
                    <span className="line-clamp-2">{chap.title}</span>
                  </button>
                );
              })}
            </div>
          </div>

          {/* Quick PDF Download Box */}
          <div className="bg-blue-50/50 dark:bg-blue-950/20 border border-blue-200 dark:border-blue-900/60 rounded-xl p-4 shadow-sm">
            <h4 className="text-xs font-bold text-blue-900 dark:text-blue-200 mb-1 flex items-center gap-1.5">
              <FileDown className="h-4 w-4 text-blue-600 dark:text-blue-400" />
              Download Subject PDF Book
            </h4>
            <p className="text-[11px] text-blue-800/80 dark:text-blue-300/80 mb-3">
              High-resolution printable PDF with complete proofs and diagrams.
            </p>
            <a
              href={`./${subject.folder}/Subject_Complete_Notes.pdf`}
              download
              className="block text-center w-full py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg text-xs font-semibold shadow-sm transition"
            >
              Download Complete Notes PDF
            </a>
          </div>
        </div>

        {/* Reader Area */}
        <div className="lg:col-span-3 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-6 sm:p-8 shadow-sm">
          {/* Chapter Header */}
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-6 border-b border-slate-100 dark:border-slate-800">
            <div>
              <span className="text-xs font-bold uppercase tracking-wider text-blue-600 dark:text-blue-400">
                Chapter {activeChapterIndex + 1} of {subject.chapters.length}
              </span>
              <h2 className="text-xl sm:text-2xl font-extrabold text-slate-900 dark:text-white mt-1">
                {chapter.title}
              </h2>
            </div>

            <div className="flex items-center gap-2">
              <button
                onClick={() => toggleTopicCompletion(topicUniqueId)}
                className={`flex items-center gap-1.5 text-xs font-semibold px-3.5 py-1.5 rounded-lg border transition ${
                  isCompleted
                    ? 'bg-emerald-50 dark:bg-emerald-950/50 text-emerald-700 dark:text-emerald-300 border-emerald-300 dark:border-emerald-800'
                    : 'bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 border-slate-300 dark:border-slate-700 hover:bg-emerald-50 hover:text-emerald-700'
                }`}
              >
                {isCompleted ? <CheckCircle className="h-3.5 w-3.5 text-emerald-500" /> : <Circle className="h-3.5 w-3.5" />}
                <span>{isCompleted ? 'Completed' : 'Mark as Done'}</span>
              </button>

              <a
                href={`./${subject.folder}/Topic_${activeChapterIndex + 1 < 10 ? '0' : ''}${activeChapterIndex + 1}_Notes.pdf`}
                download
                className="flex items-center gap-1.5 text-xs font-semibold px-3 py-1.5 rounded-lg bg-blue-50 dark:bg-blue-950/40 text-blue-700 dark:text-blue-300 border border-blue-200 dark:border-blue-800 hover:bg-blue-100 dark:hover:bg-blue-900/60 transition shadow-xs"
                title="Download Chapter PDF"
              >
                <FileDown className="h-3.5 w-3.5" />
                <span>Chapter PDF</span>
              </a>
            </div>
          </div>

          {/* Chapter Content Body */}
          <div className="mt-6 space-y-6">
            {/* Interactive Reader Toolbar: Section Filters & Font Size Adjuster */}
            <div className="flex flex-wrap items-center justify-between gap-3 p-3 rounded-2xl bg-slate-100/90 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-800 shadow-xs">
              <div className="flex flex-wrap items-center gap-1.5">
                <button
                  onClick={() => setReaderSectionFilter('all')}
                  className={`px-3 py-1.5 rounded-xl text-xs font-bold transition ${
                    readerSectionFilter === 'all'
                      ? 'bg-blue-600 text-white shadow-xs'
                      : 'text-slate-600 dark:text-slate-300 hover:bg-white dark:hover:bg-slate-700'
                  }`}
                >
                  ✨ All Sections
                </button>
                {chapter.structured_content?.foundations && (
                  <button
                    onClick={() => setReaderSectionFilter('foundations')}
                    className={`px-3 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5 ${
                      readerSectionFilter === 'foundations'
                        ? 'bg-blue-600 text-white shadow-xs'
                        : 'text-slate-600 dark:text-slate-300 hover:bg-white dark:hover:bg-slate-700'
                    }`}
                  >
                    <span>📖 Core Foundations</span>
                    <span className={`text-[10px] px-1.5 py-0.2 rounded-full ${
                      readerSectionFilter === 'foundations' ? 'bg-blue-700 text-white' : 'bg-slate-200 dark:bg-slate-700 text-slate-700 dark:text-slate-300'
                    }`}>
                      {chapter.structured_content.foundations.length}
                    </span>
                  </button>
                )}
                {chapter.structured_content?.worked_examples && (
                  <button
                    onClick={() => setReaderSectionFilter('solved')}
                    className={`px-3 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5 ${
                      readerSectionFilter === 'solved'
                        ? 'bg-purple-600 text-white shadow-xs'
                        : 'text-slate-600 dark:text-slate-300 hover:bg-white dark:hover:bg-slate-700'
                    }`}
                  >
                    <span>🔢 Solved Numericals</span>
                    <span className={`text-[10px] px-1.5 py-0.2 rounded-full ${
                      readerSectionFilter === 'solved' ? 'bg-purple-700 text-white' : 'bg-slate-200 dark:bg-slate-700 text-slate-700 dark:text-slate-300'
                    }`}>
                      {chapter.structured_content.worked_examples.length}
                    </span>
                  </button>
                )}
                {chapter.structured_content?.exam_traps && (
                  <button
                    onClick={() => setReaderSectionFilter('traps')}
                    className={`px-3 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5 ${
                      readerSectionFilter === 'traps'
                        ? 'bg-rose-600 text-white shadow-xs'
                        : 'text-slate-600 dark:text-slate-300 hover:bg-white dark:hover:bg-slate-700'
                    }`}
                  >
                    <span>⚠️ GATE Traps</span>
                    <span className={`text-[10px] px-1.5 py-0.2 rounded-full ${
                      readerSectionFilter === 'traps' ? 'bg-rose-700 text-white' : 'bg-slate-200 dark:bg-slate-700 text-slate-700 dark:text-slate-300'
                    }`}>
                      {chapter.structured_content.exam_traps.length}
                    </span>
                  </button>
                )}
                {chapter.structured_content?.real_life_examples && (
                  <button
                    onClick={() => setReaderSectionFilter('stories')}
                    className={`px-3 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5 ${
                      readerSectionFilter === 'stories'
                        ? 'bg-amber-600 text-white shadow-xs'
                        : 'text-slate-600 dark:text-slate-300 hover:bg-white dark:hover:bg-slate-700'
                    }`}
                  >
                    <span>💡 Mental Models</span>
                    <span className={`text-[10px] px-1.5 py-0.2 rounded-full ${
                      readerSectionFilter === 'stories' ? 'bg-amber-700 text-white' : 'bg-slate-200 dark:bg-slate-700 text-slate-700 dark:text-slate-300'
                    }`}>
                      {chapter.structured_content.real_life_examples.length}
                    </span>
                  </button>
                )}
                {chapter.video_resources && chapter.video_resources.length > 0 && (
                  <button
                    onClick={() => setReaderSectionFilter('videos')}
                    className={`px-3 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5 ${
                      readerSectionFilter === 'videos'
                        ? 'bg-red-600 text-white shadow-xs'
                        : 'text-slate-600 dark:text-slate-300 hover:bg-white dark:hover:bg-slate-700'
                    }`}
                  >
                    <span>🎥 Video Classes</span>
                  </button>
                )}
                <button
                  onClick={() => setReaderSectionFilter('practice')}
                  className={`px-3 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5 ${
                    readerSectionFilter === 'practice'
                      ? 'bg-emerald-600 text-white shadow-xs'
                      : 'text-slate-600 dark:text-slate-300 hover:bg-white dark:hover:bg-slate-700'
                  }`}
                >
                  <span>📝 Practice ({subjectQuestions.length})</span>
                </button>
              </div>

              {/* Text Size Control */}
              <div className="flex items-center gap-1 bg-white dark:bg-slate-900 px-2 py-1 rounded-xl border border-slate-200 dark:border-slate-700 text-xs shadow-2xs">
                <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500 mr-1">
                  Font:
                </span>
                <button
                  onClick={() => setReaderFontSize('normal')}
                  className={`px-2 py-0.5 rounded-md font-bold text-xs transition ${
                    readerFontSize === 'normal'
                      ? 'bg-blue-600 text-white'
                      : 'text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800'
                  }`}
                  title="Normal Text Size"
                >
                  A-
                </button>
                <button
                  onClick={() => setReaderFontSize('large')}
                  className={`px-2 py-0.5 rounded-md font-bold text-xs transition ${
                    readerFontSize === 'large'
                      ? 'bg-blue-600 text-white'
                      : 'text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800'
                  }`}
                  title="Large Text Size"
                >
                  A
                </button>
                <button
                  onClick={() => setReaderFontSize('xlarge')}
                  className={`px-2 py-0.5 rounded-md font-bold text-xs transition ${
                    readerFontSize === 'xlarge'
                      ? 'bg-blue-600 text-white'
                      : 'text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800'
                  }`}
                  title="Extra Large Text Size"
                >
                  A+
                </button>
              </div>
            </div>

            {/* Curated YouTube Video Lectures */}
            {chapter.video_resources && chapter.video_resources.length > 0 && (readerSectionFilter === 'all' || readerSectionFilter === 'videos') && (
              <div className="p-4 sm:p-5 rounded-2xl bg-gradient-to-r from-red-50/70 via-rose-50/50 to-orange-50/40 dark:from-red-950/20 dark:via-rose-950/20 dark:to-slate-900 border border-red-200 dark:border-red-900/60 shadow-xs">
                <div className="flex items-center gap-2 mb-3">
                  <div className="p-1.5 rounded-lg bg-red-600 text-white">
                    <Youtube className="h-4 w-4 fill-current" />
                  </div>
                  <div>
                    <h3 className="text-xs sm:text-sm font-bold text-slate-900 dark:text-white">
                      Curated Video Lectures on YouTube for this Topic
                    </h3>
                    <p className="text-[11px] text-slate-500 dark:text-slate-400">
                      Top-rated official lectures from verified educators for deep conceptual understanding.
                    </p>
                  </div>
                </div>

                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
                  {chapter.video_resources.map((v: any, vIdx: number) => (
                    <a
                      key={vIdx}
                      href={v.url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="group p-3 rounded-xl bg-white dark:bg-slate-900 border border-red-100 dark:border-slate-800 hover:border-red-500 hover:shadow-sm transition flex items-center justify-between gap-3"
                    >
                      <div className="flex items-center gap-2.5 min-w-0">
                        <div className="p-2 rounded-lg bg-red-50 dark:bg-red-950/60 text-red-600 group-hover:bg-red-600 group-hover:text-white transition flex-shrink-0">
                          <Play className="h-3.5 w-3.5 fill-current" />
                        </div>
                        <div className="min-w-0">
                          <h4 className="text-xs font-bold text-slate-900 dark:text-white group-hover:text-red-600 transition truncate">
                            {v.title}
                          </h4>
                          <span className="text-[10px] font-semibold text-slate-400 uppercase tracking-wider">
                            {v.channel}
                          </span>
                        </div>
                      </div>
                      <ExternalLink className="h-3.5 w-3.5 text-slate-400 group-hover:text-red-500 flex-shrink-0" />
                    </a>
                  ))}
                </div>
              </div>
            )}

            {/* SECTION 1: IN-DEPTH FOUNDATIONS & THEOREMS (POINT-BY-POINT STUDY GUIDE) */}
            {chapter.structured_content?.foundations && (readerSectionFilter === 'all' || readerSectionFilter === 'foundations') && (
              <div className="space-y-4 pt-1">
                <div className="border-b border-slate-200 dark:border-slate-800 pb-2">
                  <h3 className="text-sm sm:text-base font-extrabold text-blue-700 dark:text-blue-400 uppercase tracking-wide flex items-center gap-2">
                    <BookOpen className="h-4 w-4" />
                    <span>1. Core Concept Foundations (Point-by-Point Study Guide)</span>
                  </h3>
                  <p className="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
                    Crystal-clear bullet points, step-by-step logic, code, and key exam rules tested in GATE:
                  </p>
                </div>

                <div className="space-y-4">
                  {chapter.structured_content.foundations.map((fnd: any, fIdx: number) => (
                    <div
                      key={fIdx}
                      className="p-4 sm:p-5 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-xs space-y-3"
                    >
                      <div className="flex items-center gap-2.5">
                        <span className="text-xs font-mono font-extrabold px-2 py-0.5 rounded bg-blue-100 dark:bg-blue-950 text-blue-700 dark:text-blue-300 border border-blue-200 dark:border-blue-800">
                          {fnd.number}
                        </span>
                        <h4 className={`font-bold text-slate-900 dark:text-slate-100 ${fontSizeClasses.heading}`}>
                          {fnd.title}
                        </h4>
                      </div>

                      <div
                        className={`${fontSizeClasses.body} text-slate-700 dark:text-slate-300 leading-relaxed space-y-2`}
                        dangerouslySetInnerHTML={{ __html: fnd.content }}
                      />

                      {fnd.crucial_rule && (
                        <div className="mt-3 p-3.5 rounded-xl bg-emerald-50/90 dark:bg-emerald-950/40 border border-emerald-300/80 dark:border-emerald-700/60 text-emerald-950 dark:text-emerald-200 text-xs sm:text-sm font-semibold flex items-start gap-2.5 shadow-2xs">
                          <Sparkles className="h-4 w-4 text-emerald-600 dark:text-emerald-400 flex-shrink-0 mt-0.5" />
                          <div className="leading-relaxed">{fnd.crucial_rule}</div>
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* SECTION 2: STEP-BY-STEP EXAM WORKED EXAMPLES */}
            {chapter.structured_content?.worked_examples && (readerSectionFilter === 'all' || readerSectionFilter === 'solved') && (
              <div className="space-y-4 pt-2">
                <div className="border-b border-slate-200 dark:border-slate-800 pb-2">
                  <h3 className="text-sm sm:text-base font-extrabold text-purple-700 dark:text-purple-400 uppercase tracking-wide flex items-center gap-2">
                    <Sparkles className="h-4 w-4" />
                    <span>2. Step-by-Step Exam Worked Examples & Problem Traces</span>
                  </h3>
                  <p className="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
                    Authentic exam-pattern numerical and conceptual problems solved with detailed step-by-step derivations:
                  </p>
                </div>

                <div className="space-y-4">
                  {chapter.structured_content.worked_examples.map((w: any, wIdx: number) => (
                    <div
                      key={wIdx}
                      className="p-4 sm:p-5 rounded-2xl bg-slate-50/80 dark:bg-slate-800/50 border border-slate-200/80 dark:border-slate-700/70 shadow-xs space-y-3"
                    >
                      <div className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-xs font-bold bg-purple-100 dark:bg-purple-950/80 text-purple-800 dark:text-purple-300 border border-purple-200 dark:border-purple-800/60">
                        <Sparkles className="h-3 w-3" />
                        <span>Solved Problem {wIdx + 1}</span>
                      </div>
                      <h4 className={`font-bold text-slate-900 dark:text-slate-100 ${fontSizeClasses.heading}`}>
                        {w.title}
                      </h4>
                      <div className="text-xs sm:text-sm text-slate-900 dark:text-slate-100 bg-white dark:bg-slate-900 p-3.5 rounded-xl border border-slate-200 dark:border-slate-700">
                        <span className="text-blue-600 dark:text-blue-400 font-bold block mb-1">Problem Statement:</span>
                        {w.problem}
                      </div>
                      <div className="space-y-1.5 pt-1">
                        <span className="text-xs font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400">
                          Step-by-Step Solution & Traces:
                        </span>
                        <div className="space-y-1.5">
                          {w.steps.map((st: string, sIdx: number) => (
                            <div key={sIdx} className="flex items-start gap-2 text-xs sm:text-sm text-slate-700 dark:text-slate-300">
                              <span className="flex-shrink-0 w-5 h-5 rounded-full bg-blue-100 dark:bg-blue-950 text-blue-700 dark:text-blue-300 font-bold text-[10px] flex items-center justify-center mt-0.5">
                                {sIdx + 1}
                              </span>
                              <span className="leading-relaxed">{st}</span>
                            </div>
                          ))}
                        </div>
                      </div>
                      <div className="p-3 rounded-xl bg-emerald-50 dark:bg-emerald-950/40 border border-emerald-300 dark:border-emerald-700 text-emerald-900 dark:text-emerald-200 text-xs sm:text-sm font-bold flex items-center gap-2">
                        <CheckCircle2 className="h-4 w-4 text-emerald-600 dark:text-emerald-400 flex-shrink-0" />
                        <span>{w.answer}</span>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* SECTION 3: COMMON MISCONCEPTIONS & EXAM TRAPS */}
            {chapter.structured_content?.exam_traps && (readerSectionFilter === 'all' || readerSectionFilter === 'traps') && (
              <div className="space-y-3.5 pt-2">
                <div className="border-b border-slate-200 dark:border-slate-800 pb-2">
                  <h3 className="text-sm sm:text-base font-extrabold text-rose-700 dark:text-rose-400 uppercase tracking-wide flex items-center gap-2">
                    <AlertTriangle className="h-4 w-4" />
                    <span>3. Common Misconceptions & Exam Trap Warnings</span>
                  </h3>
                  <p className="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
                    Critical negative-marking traps designed by IIT professors to catch unprepared candidates:
                  </p>
                </div>

                <div className="space-y-3">
                  {chapter.structured_content.exam_traps.map((tr: any, trIdx: number) => {
                    const trapTitle = typeof tr === 'object' && tr !== null ? tr.title : 'GATE Exam Trap';
                    const trapWarning = typeof tr === 'object' && tr !== null ? tr.warning : String(tr);
                    return (
                      <div
                        key={trIdx}
                        className="p-4 rounded-xl bg-rose-50/80 dark:bg-rose-950/30 border border-rose-200/80 dark:border-rose-900/60 shadow-xs space-y-1.5"
                      >
                        <h4 className="font-bold text-rose-900 dark:text-rose-200 text-xs sm:text-sm flex items-center gap-1.5">
                          <AlertTriangle className="h-4 w-4 text-rose-600 dark:text-rose-400 flex-shrink-0" />
                          <span>⚠️ {trapTitle}</span>
                        </h4>
                        <p className={`${fontSizeClasses.body} text-slate-700 dark:text-slate-300 leading-relaxed`}>
                          {trapWarning}
                        </p>
                      </div>
                    );
                  })}
                </div>
              </div>
            )}

            {/* SECTION 4: QUICK INTUITIVE MENTAL MODELS (REAL-LIFE ANALOGIES) */}
            {chapter.structured_content?.real_life_examples && (readerSectionFilter === 'all' || readerSectionFilter === 'stories') && (
              <div className="space-y-4 pt-2">
                <div className="border-b border-slate-200 dark:border-slate-800 pb-2">
                  <h3 className="text-sm sm:text-base font-extrabold text-amber-700 dark:text-amber-400 uppercase tracking-wide flex items-center gap-2">
                    <Lightbulb className="h-4 w-4" />
                    <span>4. Quick Intuitive Mental Models (Real-Life Analogies)</span>
                  </h3>
                  <p className="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
                    Simple everyday analogies to connect technical concepts with natural intuition:
                  </p>
                </div>

                <div className="space-y-3.5">
                  {chapter.structured_content.real_life_examples.map((ex: any, exIdx: number) => (
                    <div
                      key={exIdx}
                      className="p-4 sm:p-5 rounded-2xl bg-slate-50/90 dark:bg-slate-800/50 border border-slate-200/80 dark:border-slate-700/70 shadow-xs space-y-2 transition hover:border-amber-400/60"
                    >
                      <div className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-100 dark:bg-amber-950/70 text-amber-800 dark:text-amber-300 border border-amber-200 dark:border-amber-800/60">
                        <Lightbulb className="h-3 w-3" />
                        <span>Analogy {exIdx + 1}</span>
                      </div>
                      <h4 className={`font-bold text-slate-900 dark:text-slate-100 ${fontSizeClasses.heading}`}>
                        {ex.title}
                      </h4>
                      <p className={`${fontSizeClasses.body} text-slate-700 dark:text-slate-300 leading-relaxed whitespace-pre-line`}>
                        {ex.text}
                      </p>
                    </div>
                  ))}
                </div>
              </div>
            )}
            {/* Fallback to HTML Theory if structured_content is absent */}
            {!chapter.structured_content && chapter.theory && (
              <div className="space-y-3">
                <div className="flex flex-wrap items-center justify-between gap-2">
                  <h3 className="text-sm font-bold text-slate-900 dark:text-white flex items-center gap-2">
                    <BookOpen className="h-4 w-4 text-blue-600" />
                    <span>Comprehensive Master Textbook Chapter</span>
                  </h3>
                </div>
                <div 
                  className="prose dark:prose-invert max-w-none text-xs sm:text-sm text-slate-700 dark:text-slate-300 leading-relaxed bg-white dark:bg-slate-900/60 p-5 sm:p-7 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-xs"
                  dangerouslySetInnerHTML={{ __html: chapter.theory }}
                />
              </div>
            )}

            {/* Solved Exam-Level Examples */}
            {chapter.solved_examples && chapter.solved_examples.length > 0 && (
              <div className="space-y-4 pt-2">
                <h3 className="text-sm font-bold text-slate-900 dark:text-white flex items-center gap-2">
                  <Sparkles className="h-4 w-4 text-emerald-500" />
                  <span>Step-by-Step Solved Exam Numerical Examples</span>
                </h3>

                <div className="space-y-3">
                  {chapter.solved_examples.map((ex: any, exIdx: number) => (
                    <div 
                      key={exIdx}
                      className="p-5 rounded-2xl bg-white dark:bg-slate-950 border border-emerald-200/80 dark:border-emerald-900/60 shadow-xs space-y-3"
                    >
                      <div className="flex items-start gap-2">
                        <span className="text-[10px] font-bold uppercase tracking-wider text-emerald-700 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-200 dark:border-emerald-800 flex-shrink-0 mt-0.5">
                          Problem {exIdx + 1}
                        </span>
                        <div className="text-xs sm:text-sm font-bold text-slate-900 dark:text-white whitespace-pre-line">
                          {ex.question}
                        </div>
                      </div>

                      <div className="p-3.5 rounded-xl bg-slate-50 dark:bg-slate-900/80 border border-slate-100 dark:border-slate-800 text-xs text-slate-700 dark:text-slate-300 font-mono whitespace-pre-line leading-relaxed">
                        <div className="text-slate-400 uppercase text-[10px] font-sans font-bold tracking-wider mb-1">
                          Step-by-Step Solution:
                        </div>
                        {ex.solution}
                      </div>

                      {ex.takeaway && (
                        <div className="text-xs text-emerald-800 dark:text-emerald-300 bg-emerald-50/50 dark:bg-emerald-950/30 p-2.5 rounded-lg border border-emerald-100 dark:border-emerald-900/50">
                          <b>Key Exam Takeaway:</b> {ex.takeaway}
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Tables if present */}
            {chapter.tables && chapter.tables.length > 0 && (
              <div className="space-y-4 pt-2">
                {chapter.tables.map((tbl: any, tIdx: number) => (
                  <div key={tIdx} className="overflow-x-auto rounded-xl border border-slate-200 dark:border-slate-800">
                    <table className="min-w-full divide-y divide-slate-200 dark:divide-slate-800 text-xs">
                      <thead className="bg-slate-100 dark:bg-slate-800/80">
                        <tr>
                          {tbl.header.map((h: string, hIdx: number) => (
                            <th key={hIdx} className="px-4 py-2.5 text-left font-bold text-slate-700 dark:text-slate-200">
                              {h}
                            </th>
                          ))}
                        </tr>
                      </thead>
                      <tbody className="divide-y divide-slate-200 dark:divide-slate-800 bg-white dark:bg-slate-900">
                        {tbl.rows.map((row: string[], rIdx: number) => (
                          <tr key={rIdx} className="hover:bg-slate-50 dark:hover:bg-slate-800/50">
                            {row.map((cell: string, cIdx: number) => (
                              <td key={cIdx} className="px-4 py-2 text-slate-600 dark:text-slate-300">
                                {cell}
                              </td>
                            ))}
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                ))}
              </div>
            )}

            {/* DIRECT TOPIC PRACTICE SECTION */}
            {(readerSectionFilter === 'all' || readerSectionFilter === 'practice') && (
            <div className="pt-6 border-t border-slate-200 dark:border-slate-800 space-y-4">
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                <div>
                  <h3 className="text-base font-extrabold text-slate-900 dark:text-white flex items-center gap-2">
                    <HelpCircle className="h-5 w-5 text-blue-600" />
                    <span>Practice Questions for {subject.name}</span>
                    <span className="text-xs font-bold px-2 py-0.5 rounded-full bg-blue-100 dark:bg-blue-950 text-blue-700 dark:text-blue-300">
                      {subjectQuestions.length} Problems
                    </span>
                  </h3>
                  <p className="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
                    Read the theory above, then test your understanding directly below with instant answer verification.
                  </p>
                </div>

                {setCurrentTab && (
                  <button
                    onClick={() => setCurrentTab('practice_banks')}
                    className="inline-flex items-center gap-1.5 text-xs font-bold text-blue-600 dark:text-blue-400 hover:underline self-start sm:self-auto"
                  >
                    <span>Open Full Practice Simulator</span>
                    <ArrowRight className="h-3.5 w-3.5" />
                  </button>
                )}
              </div>

              {/* Filter Pills */}
              <div className="flex flex-wrap items-center gap-2 pt-1 pb-1">
                {(['All', 'MCQ', 'MSQ', 'NAT'] as const).map((type) => {
                  const count = type === 'All' 
                    ? subjectQuestions.length 
                    : subjectQuestions.filter((q: any) => q.type === type).length;
                  const isActive = practiceTypeFilter === type;
                  return (
                    <button
                      key={type}
                      onClick={() => setPracticeTypeFilter(type)}
                      className={`px-3 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5 ${
                        isActive
                          ? 'bg-blue-600 text-white shadow-xs'
                          : 'bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700'
                      }`}
                    >
                      <span>{type === 'All' ? 'All Types' : type}</span>
                      <span className={`text-[10px] px-1.5 py-0.2 rounded-full ${
                        isActive ? 'bg-blue-700 text-white' : 'bg-slate-200 dark:bg-slate-700 text-slate-600 dark:text-slate-300'
                      }`}>
                        {count}
                      </span>
                    </button>
                  );
                })}

                <span className="text-xs font-medium text-slate-500 dark:text-slate-400 ml-auto">
                  Showing {Math.min(filteredSubjectQuestions.length, practiceLimit)} of {filteredSubjectQuestions.length}
                </span>
              </div>

              {/* List of practice questions */}
              <div className="space-y-4">
                {filteredSubjectQuestions.slice(0, practiceLimit).map((q: any) => {
                  const selectedOpt = selectedAnswers[q.id];
                  const isRevealed = revealedSolutions[q.id];
                  const isCorrect = String(selectedOpt || '').trim().toLowerCase() === String(q.answer || '').trim().toLowerCase();
                  const isNat = q.type === 'NAT' || !q.options || Object.keys(q.options).length === 0;

                  return (
                    <div
                      key={q.id}
                      className="p-5 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-3 shadow-xs"
                    >
                      <div className="flex items-center justify-between gap-2">
                        <div className="flex items-center gap-2">
                          <span className="text-[10px] font-bold px-2 py-0.5 rounded bg-blue-100 dark:bg-blue-950 text-blue-700 dark:text-blue-300">
                            {q.id}
                          </span>
                          <span className="text-[10px] font-bold px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 uppercase">
                            {q.type} • {q.marks} Mark{q.marks > 1 ? 's' : ''}
                          </span>
                        </div>
                      </div>

                      <p className="text-xs sm:text-sm font-semibold text-slate-900 dark:text-white leading-relaxed">
                        {q.text}
                      </p>

                      {/* Options or NAT Input */}
                      {!isNat ? (
                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 pt-1">
                          {Object.entries(q.options).map(([optKey, optVal]: any) => {
                            const isPicked = selectedOpt === optKey;
                            const isAnswer = q.answer === optKey;
                            
                            let optStyle = 'border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-800/60 text-slate-700 dark:text-slate-300 hover:border-blue-400';
                            if (isRevealed) {
                              if (isAnswer) {
                                optStyle = 'border-emerald-500 bg-emerald-50 dark:bg-emerald-950/60 text-emerald-800 dark:text-emerald-200 font-bold';
                              } else if (isPicked) {
                                optStyle = 'border-rose-500 bg-rose-50 dark:bg-rose-950/60 text-rose-800 dark:text-rose-200';
                              }
                            } else if (isPicked) {
                              optStyle = 'border-blue-500 bg-blue-50 dark:bg-blue-950/60 text-blue-800 dark:text-blue-200 font-semibold ring-1 ring-blue-500';
                            }

                            return (
                              <button
                                key={optKey}
                                onClick={() => handleSelectOption(q.id, optKey)}
                                className={`text-left p-3 rounded-xl border text-xs transition flex items-start gap-2.5 ${optStyle}`}
                              >
                                <span className="font-bold flex-shrink-0 w-4">{optKey}.</span>
                                <span>{optVal}</span>
                              </button>
                            );
                          })}
                        </div>
                      ) : (
                        <div className="pt-1 pb-1">
                          <div className="flex flex-wrap items-center gap-2 max-w-md">
                            <input
                              type="text"
                              placeholder="Enter exact numerical answer..."
                              value={natInputs[q.id] || ''}
                              onChange={(e) => setNatInputs(prev => ({ ...prev, [q.id]: e.target.value }))}
                              onKeyDown={(e) => {
                                if (e.key === 'Enter') {
                                  handleSelectOption(q.id, (natInputs[q.id] || '').trim());
                                }
                              }}
                              className="px-3 py-2 text-xs rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-900 dark:text-white font-mono flex-1 focus:ring-2 focus:ring-blue-500"
                            />
                            <button
                              onClick={() => handleSelectOption(q.id, (natInputs[q.id] || '').trim())}
                              className="px-4 py-2 rounded-xl bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs transition shadow-xs"
                            >
                              Check NAT
                            </button>
                          </div>
                        </div>
                      )}

                      {/* Action Bar */}
                      <div className="pt-2 flex items-center justify-between">
                        <button
                          onClick={() => toggleReveal(q.id)}
                          className="text-xs font-bold text-blue-600 dark:text-blue-400 hover:underline flex items-center gap-1"
                        >
                          <span>{isRevealed ? 'Hide Explanation' : 'Show Step-by-Step Solution'}</span>
                        </button>

                        {selectedOpt && (
                          <div className="flex items-center gap-1.5 text-xs font-bold">
                            {isCorrect ? (
                              <span className="text-emerald-600 dark:text-emerald-400 flex items-center gap-1">
                                <CheckCircle2 className="h-4 w-4" /> Correct Answer!
                              </span>
                            ) : isRevealed ? (
                              <span className="text-rose-600 dark:text-rose-400 flex items-center gap-1">
                                <XCircle className="h-4 w-4" /> Incorrect (Correct: {q.answer})
                              </span>
                            ) : (
                              <span className="text-rose-600 dark:text-rose-400 flex items-center gap-1">
                                <XCircle className="h-4 w-4" /> Incorrect, try again or view solution
                              </span>
                            )}
                          </div>
                        )}
                      </div>

                      {/* Revealed Explanation */}
                      {isRevealed && (
                        <div className="p-3.5 rounded-xl bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-800 text-xs text-slate-700 dark:text-slate-300 space-y-1.5 leading-relaxed">
                          <div className="font-bold text-slate-900 dark:text-white flex items-center gap-1.5">
                            <CheckCircle2 className="h-3.5 w-3.5 text-emerald-500" />
                            <span>Correct Answer: {q.answer}</span>
                          </div>
                          <p>{q.explanation}</p>
                        </div>
                      )}
                    </div>
                  );
                })}
              </div>

              {/* Expansion / Load More Controls */}
              {filteredSubjectQuestions.length > 10 && (
                <div className="pt-2 flex items-center justify-center gap-3">
                  {practiceLimit < filteredSubjectQuestions.length ? (
                    <button
                      onClick={() => setPracticeLimit(prev => prev + 10)}
                      className="px-4 py-2 rounded-xl bg-blue-50 dark:bg-blue-950/60 hover:bg-blue-100 dark:hover:bg-blue-900 border border-blue-200 dark:border-blue-800 text-xs font-bold text-blue-700 dark:text-blue-300 transition shadow-xs"
                    >
                      Load More Questions ({filteredSubjectQuestions.length - practiceLimit} remaining)
                    </button>
                  ) : (
                    <button
                      onClick={() => setPracticeLimit(10)}
                      className="px-4 py-2 rounded-xl bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 text-xs font-bold text-slate-700 dark:text-slate-300 transition"
                    >
                      Show Less (Top 10)
                    </button>
                  )}
                  {practiceLimit < filteredSubjectQuestions.length && (
                    <button
                      onClick={() => setPracticeLimit(filteredSubjectQuestions.length)}
                      className="px-4 py-2 rounded-xl bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 text-xs font-bold text-slate-700 dark:text-slate-300 transition"
                    >
                      Show All {filteredSubjectQuestions.length} Questions
                    </button>
                  )}
                </div>
              )}
            </div>
            )}

            {/* Chapter Sequential Navigation Footer */}
            <div className="pt-6 border-t border-slate-200 dark:border-slate-800 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
              <button
                onClick={handlePrevChapter}
                disabled={activeChapterIndex === 0}
                className={`flex items-center gap-2 px-4 py-2.5 rounded-xl text-xs font-semibold border transition ${
                  activeChapterIndex === 0
                    ? 'opacity-40 cursor-not-allowed border-slate-200 dark:border-slate-800 text-slate-400'
                    : 'bg-white dark:bg-slate-900 hover:bg-slate-50 dark:hover:bg-slate-800 border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-200 shadow-2xs'
                }`}
              >
                <ChevronLeft className="h-4 w-4" />
                <span>Previous Chapter</span>
              </button>

              <button
                onClick={() => toggleTopicCompletion(topicUniqueId)}
                className={`flex items-center justify-center gap-2 px-5 py-2.5 rounded-xl text-xs font-bold border transition ${
                  isCompleted
                    ? 'bg-emerald-600 text-white border-emerald-600 shadow-sm'
                    : 'bg-blue-50 dark:bg-blue-950/40 text-blue-700 dark:text-blue-300 border-blue-200 dark:border-blue-800 hover:bg-blue-100'
                }`}
              >
                {isCompleted ? <CheckCircle className="h-4 w-4 text-white" /> : <Circle className="h-4 w-4" />}
                <span>{isCompleted ? 'Chapter Completed ✓' : 'Mark Chapter as Done'}</span>
              </button>

              <button
                onClick={handleNextChapter}
                disabled={activeChapterIndex === subject.chapters.length - 1}
                className={`flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl text-xs font-semibold border transition ${
                  activeChapterIndex === subject.chapters.length - 1
                    ? 'opacity-40 cursor-not-allowed border-slate-200 dark:border-slate-800 text-slate-400'
                    : 'bg-blue-600 hover:bg-blue-700 border-blue-600 text-white shadow-sm'
                }`}
              >
                <span>Next Chapter</span>
                <ChevronRight className="h-4 w-4" />
              </button>
            </div>
          </div>
        </div>
      </div>
      )}
    </div>
  );
};
