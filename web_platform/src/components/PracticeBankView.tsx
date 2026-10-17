import React, { useState, useMemo } from 'react';
import { HelpCircle, Filter, CheckCircle2, XCircle, ChevronDown, ChevronUp, Award } from 'lucide-react';
import { Question } from '../types';

interface PracticeBankViewProps {
  questions: Question[];
  subjects: any[];
}

export const PracticeBankView: React.FC<PracticeBankViewProps> = ({ questions, subjects }) => {
  const [selectedSubject, setSelectedSubject] = useState<string>('All');
  const [selectedType, setSelectedType] = useState<string>('All');
  const [userAnswers, setUserAnswers] = useState<Record<number, any>>({});
  const [revealedSolutions, setRevealedSolutions] = useState<Record<number, boolean>>({});

  const filteredQuestions = useMemo(() => {
    return questions.filter((q, idx) => {
      const matchSub = selectedSubject === 'All' || q.id?.startsWith(selectedSubject);
      const matchType = selectedType === 'All' || q.type === selectedType;
      return matchSub && matchType;
    });
  }, [questions, selectedSubject, selectedType]);

  const toggleSolution = (idx: number) => {
    setRevealedSolutions((prev) => ({ ...prev, [idx]: !prev[idx] }));
  };

  const handleSelectOption = (idx: number, optKey: string) => {
    setUserAnswers((prev) => ({ ...prev, [idx]: optKey }));
  };

  return (
    <div className="space-y-6 animate-fadeIn">
      {/* Header */}
      <div className="pb-6 border-b border-slate-200 dark:border-slate-800">
        <div className="inline-flex items-center gap-1.5 text-xs font-semibold text-blue-600 dark:text-blue-400 bg-blue-50 dark:bg-blue-950/60 px-2.5 py-1 rounded-full mb-2 border border-blue-200 dark:border-blue-800">
          <HelpCircle className="h-3.5 w-3.5" />
          Interactive Practice Mode
        </div>
        <h1 className="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white">
          Topic-Wise & Subject-Wise Practice Question Bank
        </h1>
        <p className="text-sm text-slate-500 dark:text-slate-400 mt-1">
          Solve original GATE-standard questions with progressive difficulty and instant detailed solutions.
        </p>
      </div>

      {/* Filter Row */}
      <div className="flex flex-wrap gap-3">
        <select
          value={selectedSubject}
          onChange={(e) => setSelectedSubject(e.target.value)}
          className="px-3 py-2 text-xs sm:text-sm rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-slate-900 dark:text-slate-100 font-medium shadow-sm"
        >
          <option value="All">All Subjects</option>
          {subjects.map((s) => (
            <option key={s.id} value={s.id}>{s.name}</option>
          ))}
        </select>

        <select
          value={selectedType}
          onChange={(e) => setSelectedType(e.target.value)}
          className="px-3 py-2 text-xs sm:text-sm rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-slate-900 dark:text-slate-100 font-medium shadow-sm"
        >
          <option value="All">All Question Types</option>
          <option value="MCQ">MCQ</option>
          <option value="MSQ">MSQ</option>
          <option value="NAT">NAT</option>
        </select>
      </div>

      {/* Questions List */}
      <div className="space-y-4">
        {filteredQuestions.map((q, idx) => {
          const userAns = userAnswers[idx];
          const isRevealed = revealedSolutions[idx] || false;
          const isChecked = userAns !== undefined;
          const isCorrect = userAns === q.answer;

          return (
            <div
              key={idx}
              className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-5 sm:p-6 shadow-sm"
            >
              <div className="flex items-center justify-between gap-2 mb-3">
                <span className="text-xs font-bold text-slate-500 dark:text-slate-400">
                  Question {idx + 1} • {q.type} • {q.marks} Mark{q.marks > 1 ? 's' : ''}
                </span>
                {q.difficulty && (
                  <span className="text-[10px] font-bold px-2 py-0.5 rounded bg-blue-50 dark:bg-blue-950 text-blue-700 dark:text-blue-300">
                    {q.difficulty}
                  </span>
                )}
              </div>

              {/* Statement */}
              <div 
                className="text-xs sm:text-sm text-slate-800 dark:text-slate-200 leading-relaxed font-medium mb-4"
                dangerouslySetInnerHTML={{ __html: q.text }}
              />

              {/* Options */}
              {q.options && (
                <div className="space-y-2 mb-4 pl-2 max-w-xl">
                  {Object.entries(q.options).map(([k, val]: any) => {
                    const isSelected = userAns === k;
                    return (
                      <div
                        key={k}
                        onClick={() => handleSelectOption(idx, k)}
                        className={`cursor-pointer p-2.5 rounded-lg border text-xs sm:text-sm flex items-start gap-2.5 transition ${
                          isSelected
                            ? 'bg-blue-50 dark:bg-blue-900/30 border-blue-500 text-blue-900 dark:text-blue-200 font-semibold'
                            : 'bg-white dark:bg-slate-800/60 border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 hover:border-slate-400'
                        }`}
                      >
                        <span className="font-bold">({k})</span>
                        <span dangerouslySetInnerHTML={{ __html: val }} />
                      </div>
                    );
                  })}
                </div>
              )}

              {/* Card Footer */}
              <div className="pt-3 border-t border-slate-100 dark:border-slate-800 flex items-center justify-between">
                <button
                  onClick={() => toggleSolution(idx)}
                  className="text-xs font-bold text-blue-600 dark:text-blue-400 hover:underline flex items-center gap-1"
                >
                  <span>{isRevealed ? 'Hide Explanation' : 'Check Answer & Explanation'}</span>
                  {isRevealed ? <ChevronUp className="h-3.5 w-3.5" /> : <ChevronDown className="h-3.5 w-3.5" />}
                </button>

                {isChecked && (
                  <span className={`text-xs font-bold flex items-center gap-1 ${
                    isCorrect ? 'text-emerald-600' : 'text-rose-600'
                  }`}>
                    {isCorrect ? <CheckCircle2 className="h-4 w-4" /> : <XCircle className="h-4 w-4" />}
                    <span>{isCorrect ? 'Correct!' : 'Incorrect'}</span>
                  </span>
                )}
              </div>

              {/* Solution Box */}
              {isRevealed && (
                <div className="mt-4 p-4 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700 space-y-2 animate-fadeIn">
                  <div className="flex items-center gap-2">
                    <span className="text-xs font-bold text-slate-500 dark:text-slate-400">Correct Answer:</span>
                    <span className="text-xs font-extrabold text-emerald-600 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-200 dark:border-emerald-800">
                      {q.answer}
                    </span>
                  </div>
                  <div 
                    className="text-xs text-slate-700 dark:text-slate-300 leading-relaxed pt-2 border-t border-slate-200/60 dark:border-slate-700/60"
                    dangerouslySetInnerHTML={{ __html: q.explanation || '' }}
                  />
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
};
