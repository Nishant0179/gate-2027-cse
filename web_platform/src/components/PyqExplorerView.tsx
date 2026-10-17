import React, { useState, useMemo } from 'react';
import { 
  History, 
  Search, 
  Filter, 
  CheckCircle, 
  HelpCircle, 
  ExternalLink,
  ChevronDown,
  ChevronUp,
  Award,
  Sparkles
} from 'lucide-react';
import { PYQItem } from '../types';

interface PyqExplorerViewProps {
  pyqs: PYQItem[];
}

export const PyqExplorerView: React.FC<PyqExplorerViewProps> = ({ pyqs }) => {
  const [selectedYear, setSelectedYear] = useState<string>('All');
  const [selectedSubject, setSelectedSubject] = useState<string>('All');
  const [selectedType, setSelectedType] = useState<string>('All');
  const [expandedSolutions, setExpandedSolutions] = useState<Record<string, boolean>>({});

  const years = useMemo(() => {
    const set = new Set(pyqs.map((q) => q.year.toString()));
    return ['All', ...Array.from(set).sort((a, b) => Number(b) - Number(a))];
  }, [pyqs]);

  const subjects = useMemo(() => {
    const set = new Set(pyqs.map((q) => q.subject));
    return ['All', ...Array.from(set)];
  }, [pyqs]);

  const filteredPyqs = useMemo(() => {
    return pyqs.filter((q) => {
      const matchYear = selectedYear === 'All' || q.year.toString() === selectedYear;
      const matchSub = selectedSubject === 'All' || q.subject === selectedSubject;
      const matchType = selectedType === 'All' || q.type === selectedType;
      return matchYear && matchSub && matchType;
    });
  }, [pyqs, selectedYear, selectedSubject, selectedType]);

  const toggleSolution = (id: string) => {
    setExpandedSolutions((prev) => ({ ...prev, [id]: !prev[id] }));
  };

  return (
    <div className="space-y-6 animate-fadeIn">
      {/* Header */}
      <div className="pb-6 border-b border-slate-200 dark:border-slate-800">
        <div className="inline-flex items-center gap-1.5 text-xs font-semibold text-amber-600 dark:text-amber-400 bg-amber-50 dark:bg-amber-950/60 px-2.5 py-1 rounded-full mb-2 border border-amber-200 dark:border-amber-800">
          <Award className="h-3.5 w-3.5" />
          Authentic Officially Released Papers
        </div>
        <h1 className="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white">
          Verified GATE CSE Previous Year Questions (PYQs)
        </h1>
        <p className="text-sm text-slate-500 dark:text-slate-400 mt-1">
          Historical exam questions cross-verified with official answer keys released by organizing IITs.
        </p>
      </div>

      {/* Filter Row */}
      <div className="flex flex-wrap gap-3">
        <select
          value={selectedYear}
          onChange={(e) => setSelectedYear(e.target.value)}
          className="px-3 py-2 text-xs sm:text-sm rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-slate-900 dark:text-slate-100 font-medium shadow-sm"
        >
          <option value="All">All Years (2012 - 2026)</option>
          {years.filter((y) => y !== 'All').map((y) => (
            <option key={y} value={y}>GATE {y}</option>
          ))}
        </select>

        <select
          value={selectedSubject}
          onChange={(e) => setSelectedSubject(e.target.value)}
          className="px-3 py-2 text-xs sm:text-sm rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-slate-900 dark:text-slate-100 font-medium shadow-sm"
        >
          <option value="All">All Subjects</option>
          {subjects.filter((s) => s !== 'All').map((s) => (
            <option key={s} value={s}>{s}</option>
          ))}
        </select>

        <select
          value={selectedType}
          onChange={(e) => setSelectedType(e.target.value)}
          className="px-3 py-2 text-xs sm:text-sm rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-slate-900 dark:text-slate-100 font-medium shadow-sm"
        >
          <option value="All">All Question Types</option>
          <option value="MCQ">MCQ (Multiple Choice)</option>
          <option value="MSQ">MSQ (Multiple Select)</option>
          <option value="NAT">NAT (Numerical Answer)</option>
        </select>

        <button
          onClick={() => {
            const allOpen: Record<string, boolean> = {};
            filteredPyqs.forEach((q) => { allOpen[q.id] = true; });
            setExpandedSolutions(allOpen);
          }}
          className="px-3 py-2 text-xs rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 font-semibold hover:bg-slate-200"
        >
          Expand All Solutions
        </button>
      </div>

      {/* Results Count */}
      <div className="text-xs font-semibold text-slate-500 dark:text-slate-400">
        Showing {filteredPyqs.length} verified previous year questions
      </div>

      {/* Question List */}
      <div className="space-y-4">
        {filteredPyqs.map((q) => {
          const isOpen = expandedSolutions[q.id] || false;
          return (
            <div
              key={q.id}
              className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-5 sm:p-6 shadow-sm"
            >
              <div className="flex flex-wrap items-center justify-between gap-2 mb-3">
                <div className="flex items-center gap-2">
                  <span className="text-xs font-extrabold px-2.5 py-0.5 rounded bg-blue-100 dark:bg-blue-950 text-blue-800 dark:text-blue-300 border border-blue-200 dark:border-blue-800">
                    GATE {q.year}
                  </span>
                  <span className="text-xs font-bold px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300">
                    {q.subject}
                  </span>
                  <span className="text-xs text-slate-500 dark:text-slate-400 font-medium">
                    {q.topic}
                  </span>
                </div>

                <div className="flex items-center gap-2">
                  <span className="text-xs font-bold text-slate-500 dark:text-slate-400">
                    {q.type} • {q.marks} Mark{q.marks > 1 ? 's' : ''}
                  </span>
                </div>
              </div>

              {/* Question Statement */}
              <div 
                className="text-xs sm:text-sm text-slate-800 dark:text-slate-200 leading-relaxed font-medium mb-3"
                dangerouslySetInnerHTML={{ __html: q.text }}
              />

              {/* Options for MCQ / MSQ */}
              {q.options && (
                <div className="space-y-2 mb-4 pl-2">
                  {Object.entries(q.options).map(([optKey, optVal]) => (
                    <div key={optKey} className="flex items-start gap-2 text-xs sm:text-sm text-slate-700 dark:text-slate-300">
                      <span className="font-bold text-slate-500">({optKey})</span>
                      <span dangerouslySetInnerHTML={{ __html: optVal }} />
                    </div>
                  ))}
                </div>
              )}

              {/* Toggle Solution Button */}
              <div className="pt-3 border-t border-slate-100 dark:border-slate-800 flex items-center justify-between">
                <button
                  onClick={() => toggleSolution(q.id)}
                  className="inline-flex items-center gap-1.5 text-xs font-bold text-blue-600 dark:text-blue-400 hover:underline"
                >
                  <span>{isOpen ? 'Hide Official Solution' : 'View Verified Solution & Explanation'}</span>
                  {isOpen ? <ChevronUp className="h-3.5 w-3.5" /> : <ChevronDown className="h-3.5 w-3.5" />}
                </button>

                <span className="text-[11px] text-teal-600 dark:text-teal-400 font-semibold flex items-center gap-1">
                  <CheckCircle className="h-3 w-3" />
                  {q.verification_status}
                </span>
              </div>

              {/* Collapsible Solution Box */}
              {isOpen && (
                <div className="mt-4 p-4 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700 space-y-2 animate-fadeIn">
                  <div className="flex items-center gap-2">
                    <span className="text-xs font-bold text-slate-500 dark:text-slate-400">Official Correct Answer:</span>
                    <span className="text-xs font-extrabold text-emerald-600 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-950/60 px-2.5 py-0.5 rounded border border-emerald-200 dark:border-emerald-800">
                      {q.answer}
                    </span>
                  </div>
                  <div 
                    className="text-xs text-slate-700 dark:text-slate-300 leading-relaxed pt-2 border-t border-slate-200/60 dark:border-slate-700/60"
                    dangerouslySetInnerHTML={{ __html: q.explanation }}
                  />
                  <div className="text-[10px] text-slate-400 dark:text-slate-500 pt-1">
                    Source: {q.source_url}
                  </div>
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
};
