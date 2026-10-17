import React, { useState } from 'react';
import { Sparkles, Search, FileDown, Copy, Check } from 'lucide-react';

interface FormulaSheetsViewProps {
  finalRevision: any;
}

export const FormulaSheetsView: React.FC<FormulaSheetsViewProps> = ({ finalRevision }) => {
  const [searchQuery, setSearchQuery] = useState('');
  const [copiedIndex, setCopiedIndex] = useState<string | null>(null);

  const masterFormulas = finalRevision.master_formulas || [];

  const handleCopy = (key: string, text: string) => {
    navigator.clipboard.writeText(text);
    setCopiedIndex(key);
    setTimeout(() => setCopiedIndex(null), 2000);
  };

  return (
    <div className="space-y-6 animate-fadeIn">
      {/* Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-6 border-b border-slate-200 dark:border-slate-800">
        <div>
          <div className="inline-flex items-center gap-1.5 text-xs font-semibold text-amber-600 dark:text-amber-400 bg-amber-50 dark:bg-amber-950/60 px-2.5 py-1 rounded-full mb-2 border border-amber-200 dark:border-amber-800">
            <Sparkles className="h-3.5 w-3.5" />
            High-Yield Memory Aid
          </div>
          <h1 className="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white">
            Official Master Formula & Cheat Sheets
          </h1>
          <p className="text-sm text-slate-500 dark:text-slate-400 mt-1">
            Mathematical definitions, asymptotic bounds, architectural equations, and rapid-fire invariants across all 11 subjects.
          </p>
        </div>

        <div>
          <a
            href="/15_Quick_Revision/Master_Formula_and_Cheat_Sheet.pdf"
            download
            className="flex items-center gap-2 bg-blue-600 hover:bg-blue-700 text-white font-semibold text-xs px-4 py-2.5 rounded-xl shadow-sm transition"
          >
            <FileDown className="h-4 w-4" />
            <span>Download Master Formula Sheet PDF</span>
          </a>
        </div>
      </div>

      {/* Search Input */}
      <div className="relative max-w-md">
        <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-slate-400" />
        <input
          type="text"
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          placeholder="Filter formulas (e.g. Euler, Bayes, Cache, TCP, Pipelining)..."
          className="w-full pl-9 pr-4 py-2 text-xs sm:text-sm rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-slate-900 dark:text-slate-100 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500 shadow-sm"
        />
      </div>

      {/* Subject Formula Sections */}
      <div className="space-y-6">
        {masterFormulas.map((sec: any, secIdx: number) => {
          const matchingFormulas = sec.formulas.filter(
            ([name, val]: any) =>
              name.toLowerCase().includes(searchQuery.toLowerCase()) ||
              val.toLowerCase().includes(searchQuery.toLowerCase()) ||
              sec.subject.toLowerCase().includes(searchQuery.toLowerCase())
          );

          if (matchingFormulas.length === 0) return null;

          return (
            <div
              key={secIdx}
              className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-6 shadow-sm space-y-4"
            >
              <h2 className="text-base font-extrabold text-blue-600 dark:text-blue-400 flex items-center gap-2">
                <span className="h-2 w-2 rounded-full bg-blue-600" />
                {sec.subject}
              </h2>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                {matchingFormulas.map(([name, val]: any, fIdx: number) => {
                  const uniqueKey = `${secIdx}-${fIdx}`;
                  const isCopied = copiedIndex === uniqueKey;
                  return (
                    <div
                      key={fIdx}
                      className="p-3.5 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700/80 flex flex-col justify-between"
                    >
                      <div>
                        <div className="flex items-center justify-between mb-1.5">
                          <span className="text-xs font-bold text-slate-900 dark:text-white">
                            {name}
                          </span>
                          <button
                            onClick={() => handleCopy(uniqueKey, `${name}: ${val}`)}
                            className="text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 p-1"
                            title="Copy Formula"
                          >
                            {isCopied ? <Check className="h-3 w-3 text-emerald-500" /> : <Copy className="h-3 w-3" />}
                          </button>
                        </div>
                        <p className="text-xs font-mono font-semibold text-slate-700 dark:text-slate-300 leading-relaxed bg-white dark:bg-slate-900 p-2 rounded-lg border border-slate-200/60 dark:border-slate-800">
                          {val}
                        </p>
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
