import React, { useState } from 'react';
import { FileCheck2, FileDown, ShieldCheck, AlertCircle, ExternalLink, ChevronDown, ChevronRight, CheckCircle2 } from 'lucide-react';

interface OfficialSyllabusViewProps {
  gateData: any;
}

export const OfficialSyllabusView: React.FC<OfficialSyllabusViewProps> = ({ gateData }) => {
  const [activeSection, setActiveSection] = useState<string>('EM');
  const metadata = gateData.metadata;

  return (
    <div className="space-y-6 animate-fadeIn">
      {/* Page Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-6 border-b border-slate-200 dark:border-slate-800">
        <div>
          <div className="inline-flex items-center gap-1.5 text-xs font-semibold text-blue-600 dark:text-blue-400 bg-blue-50 dark:bg-blue-950/60 px-2.5 py-1 rounded-full mb-2 border border-blue-200 dark:border-blue-800">
            <ShieldCheck className="h-3.5 w-3.5" />
            Verified Official Document Source
          </div>
          <h1 className="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white">
            Official GATE 2027 CS Syllabus & Exam Pattern
          </h1>
          <p className="text-sm text-slate-500 dark:text-slate-400 mt-1">
            Organized by Indian Institute of Technology Madras (IIT Madras) • Paper Code: CS
          </p>
        </div>

        {/* Download Buttons for Official Syllabi */}
        <div className="flex items-center gap-3">
          <a
            href="/00_Official_Syllabus/CS_GATE2027_Syllabus.pdf"
            download
            className="flex items-center gap-2 bg-blue-600 hover:bg-blue-700 text-white font-semibold text-xs px-3.5 py-2 rounded-lg shadow-sm transition"
          >
            <FileDown className="h-4 w-4" />
            <span>Download CS Syllabus PDF</span>
          </a>
          <a
            href="/00_Official_Syllabus/GA_GATE2027_Syllabus.pdf"
            download
            className="flex items-center gap-2 bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 font-semibold text-xs px-3.5 py-2 rounded-lg border border-slate-300 dark:border-slate-700 transition"
          >
            <FileDown className="h-4 w-4" />
            <span>Download GA Syllabus PDF</span>
          </a>
        </div>
      </div>

      {/* Official Pattern Summary Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
        <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 p-4 rounded-xl">
          <span className="text-xs font-bold text-slate-500 dark:text-slate-400 uppercase">General Aptitude (GA)</span>
          <div className="text-xl font-extrabold text-blue-600 dark:text-blue-400 mt-1">15 Marks (10 Qs)</div>
          <p className="text-xs text-slate-500 dark:text-slate-400 mt-1">5 Qs of 1 Mark + 5 Qs of 2 Marks</p>
        </div>
        <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 p-4 rounded-xl">
          <span className="text-xs font-bold text-slate-500 dark:text-slate-400 uppercase">Engineering Mathematics</span>
          <div className="text-xl font-extrabold text-teal-600 dark:text-teal-400 mt-1">13 Marks</div>
          <p className="text-xs text-slate-500 dark:text-slate-400 mt-1">Discrete Math, Linear Algebra, Calculus, Probability</p>
        </div>
        <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 p-4 rounded-xl">
          <span className="text-xs font-bold text-slate-500 dark:text-slate-400 uppercase">Core Computer Science</span>
          <div className="text-xl font-extrabold text-indigo-600 dark:text-indigo-400 mt-1">72 Marks</div>
          <p className="text-xs text-slate-500 dark:text-slate-400 mt-1">9 Technical Core Computer Science Subjects</p>
        </div>
      </div>

      {/* Notice on GATE 2027 Changes */}
      <div className="bg-amber-50 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-800/60 p-4 rounded-xl flex items-start gap-3">
        <AlertCircle className="h-5 w-5 text-amber-600 dark:text-amber-400 flex-shrink-0 mt-0.5" />
        <div className="text-xs text-amber-900 dark:text-amber-200 leading-relaxed">
          <span className="font-bold">Verified Syllabus Nuances for GATE 2027:</span> The official IIT Madras syllabus specifically highlights <b>Data Flow Analyses</b> (constant propagation, liveness analysis, common subexpression elimination) in Compiler Design, <b>I/O Scheduling</b> alongside CPU scheduling in Operating Systems, and explicitly streamlines Computer Networks to core layers, CIDR, NAT, TCP congestion control, and DNS/HTTP. Spatial Aptitude is tested in General Aptitude.
        </div>
      </div>

      {/* Interactive Section Explorer */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
        {/* Navigation List */}
        <div className="space-y-1 md:col-span-1">
          <p className="text-xs font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500 px-2 mb-2">
            Syllabus Sections
          </p>
          {gateData.sections.map((sec: any) => (
            <button
              key={sec.id}
              onClick={() => setActiveSection(sec.id)}
              className={`w-full flex items-center justify-between text-left px-3 py-2.5 rounded-lg text-xs font-medium transition ${
                activeSection === sec.id
                  ? 'bg-blue-600 text-white font-semibold shadow-sm'
                  : 'bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 border border-slate-200 dark:border-slate-800'
              }`}
            >
              <span>{sec.title}</span>
              <span className={`text-[10px] font-bold px-1.5 py-0.5 rounded ${
                activeSection === sec.id ? 'bg-blue-700 text-white' : 'bg-slate-100 dark:bg-slate-800 text-slate-500'
              }`}>
                {sec.weightage_marks}M
              </span>
            </button>
          ))}
        </div>

        {/* Section Content Pane */}
        <div className="md:col-span-3 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-6 shadow-sm">
          {(() => {
            const currentSec = gateData.sections.find((s: any) => s.id === activeSection) || gateData.sections[0];
            return (
              <div className="space-y-6">
                <div className="flex items-center justify-between pb-4 border-b border-slate-100 dark:border-slate-800">
                  <div>
                    <span className="text-xs font-bold uppercase tracking-wider text-blue-600 dark:text-blue-400">
                      Section {currentSec.section_number}
                    </span>
                    <h2 className="text-xl font-extrabold text-slate-900 dark:text-white mt-1">
                      {currentSec.title}
                    </h2>
                  </div>
                  <div className="text-right">
                    <span className="inline-block bg-teal-50 dark:bg-teal-950/60 border border-teal-200 dark:border-teal-800 text-teal-700 dark:text-teal-300 font-extrabold text-xs px-3 py-1 rounded-full">
                      Weightage: ~{currentSec.weightage_marks} Marks
                    </span>
                  </div>
                </div>

                {/* Subsections & Topics */}
                <div className="space-y-4">
                  {currentSec.subsections.map((sub: any, idx: number) => (
                    <div key={idx} className="p-4 rounded-xl bg-slate-50 dark:bg-slate-800/50 border border-slate-200/80 dark:border-slate-750">
                      <div className="flex items-center justify-between mb-2">
                        <h3 className="text-sm font-bold text-slate-900 dark:text-white flex items-center gap-2">
                          <CheckCircle2 className="h-4 w-4 text-blue-500" />
                          {sub.title}
                        </h3>
                        {sub.importance && (
                          <span className="text-[10px] font-semibold text-amber-700 dark:text-amber-400 bg-amber-50 dark:bg-amber-950/60 px-2 py-0.5 rounded border border-amber-200 dark:border-amber-800">
                            {sub.importance}
                          </span>
                        )}
                      </div>

                      {/* Topic Bullet List */}
                      <ul className="space-y-1.5 mt-2 pl-6 list-disc text-xs text-slate-600 dark:text-slate-300">
                        {sub.topics.map((t: string, tIdx: number) => (
                          <li key={tIdx} className="leading-relaxed">{t}</li>
                        ))}
                      </ul>

                      {sub.prerequisites && (
                        <div className="mt-3 pt-2 border-t border-slate-200 dark:border-slate-700 text-[11px] text-slate-500 dark:text-slate-400">
                          <span className="font-semibold text-slate-700 dark:text-slate-300">Prerequisites:</span> {sub.prerequisites}
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              </div>
            );
          })()}
        </div>
      </div>
    </div>
  );
};
