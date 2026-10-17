import React, { useState } from 'react';
import { 
  BookOpen, 
  FileDown, 
  CheckCircle, 
  Circle, 
  AlertTriangle, 
  Lightbulb, 
  Sparkles, 
  ChevronRight,
  Bookmark,
  Share2,
  Table as TableIcon
} from 'lucide-react';

interface SubjectLibraryViewProps {
  gateData: any;
  completedTopics: string[];
  toggleTopicCompletion: (topicId: string) => void;
}

export const SubjectLibraryView: React.FC<SubjectLibraryViewProps> = ({
  gateData,
  completedTopics,
  toggleTopicCompletion,
}) => {
  const [selectedSubjectId, setSelectedSubjectId] = useState<string>(gateData.subjects[0]?.id || 'EM');
  const [activeChapterIndex, setActiveChapterIndex] = useState<number>(0);

  const subject = gateData.subjects.find((s: any) => s.id === selectedSubjectId) || gateData.subjects[0];
  const chapter = subject.chapters[activeChapterIndex] || subject.chapters[0];
  const topicUniqueId = `${subject.id}-${activeChapterIndex}`;
  const isCompleted = completedTopics.includes(topicUniqueId);

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

      {/* Main Content Layout */}
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
          <div className="bg-blue-50 dark:bg-blue-950/40 border border-blue-200 dark:border-blue-800 rounded-xl p-4">
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
                className="p-2 rounded-lg bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-600 dark:text-slate-300 transition"
                title="Download Chapter PDF"
              >
                <FileDown className="h-4 w-4" />
              </a>
            </div>
          </div>

          {/* Chapter Content Body */}
          <div className="mt-6 space-y-6">
            {/* Hinglish Concept Intuition Box */}
            {chapter.hinglish && (
              <div className="p-4 rounded-xl bg-gradient-to-r from-blue-50/80 to-indigo-50/80 dark:from-slate-800/80 dark:to-slate-800/40 border border-blue-200/60 dark:border-slate-700">
                <div className="flex items-center gap-2 mb-1.5">
                  <Lightbulb className="h-4 w-4 text-amber-500" />
                  <span className="text-xs font-bold text-slate-900 dark:text-white">Intuitive Concept Breakdown (Hinglish)</span>
                </div>
                <p className="text-xs sm:text-sm text-slate-700 dark:text-slate-300 leading-relaxed italic">
                  "{chapter.hinglish}"
                </p>
              </div>
            )}

            {/* Core Technical Theory */}
            <div 
              className="prose dark:prose-invert max-w-none text-xs sm:text-sm text-slate-700 dark:text-slate-300 leading-relaxed"
              dangerouslySetInnerHTML={{ __html: chapter.theory }}
            />

            {/* Callouts (Tips, Traps, Formulas) */}
            {chapter.callouts && chapter.callouts.length > 0 && (
              <div className="space-y-3 pt-2">
                {chapter.callouts.map(([cTitle, cText, cType]: any, cIdx: number) => {
                  const isWarn = cType === 'warn';
                  const isFormula = cType === 'formula';
                  return (
                    <div
                      key={cIdx}
                      className={`p-4 rounded-xl border ${
                        isWarn
                          ? 'bg-rose-50 dark:bg-rose-950/30 border-rose-200 dark:border-rose-900/60 text-rose-950 dark:text-rose-200'
                          : isFormula
                          ? 'bg-amber-50 dark:bg-amber-950/30 border-amber-200 dark:border-amber-900/60 text-amber-950 dark:text-amber-200'
                          : 'bg-emerald-50 dark:bg-emerald-950/30 border-emerald-200 dark:border-emerald-900/60 text-emerald-950 dark:text-emerald-200'
                      }`}
                    >
                      <div className="flex items-center gap-2 mb-1">
                        {isWarn ? (
                          <AlertTriangle className="h-4 w-4 text-rose-600 dark:text-rose-400" />
                        ) : isFormula ? (
                          <Sparkles className="h-4 w-4 text-amber-600 dark:text-amber-400" />
                        ) : (
                          <Lightbulb className="h-4 w-4 text-emerald-600 dark:text-emerald-400" />
                        )}
                        <span className="text-xs font-bold tracking-tight">
                          {isWarn ? 'COMMON EXAM TRAP / PITFALL:' : isFormula ? 'KEY FORMULA / RESULT:' : 'PRO STRATEGY:'} {cTitle}
                        </span>
                      </div>
                      <p className="text-xs leading-relaxed">{cText}</p>
                    </div>
                  );
                })}
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
          </div>
        </div>
      </div>
    </div>
  );
};
