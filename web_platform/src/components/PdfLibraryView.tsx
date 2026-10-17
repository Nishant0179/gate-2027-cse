import React, { useState, useMemo } from 'react';
import { 
  FileDown, 
  Search, 
  Filter, 
  BookOpen, 
  CheckCircle2, 
  FolderDown, 
  ExternalLink,
  Layers,
  Sparkles
} from 'lucide-react';
import { PdfDocument } from '../types';

interface PdfLibraryViewProps {
  pdfLibrary: PdfDocument[];
}

export const PdfLibraryView: React.FC<PdfLibraryViewProps> = ({ pdfLibrary }) => {
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState<string>('All');
  const [selectedSubject, setSelectedSubject] = useState<string>('All');

  // Categories list
  const categories = ['All', 'Complete Notes', 'Topic Notes', 'Quick Revision', 'Formula Sheet', 'Practice Questions', 'Solutions', 'Mock Tests', 'Study Plans', 'Final Revision'];
  
  // Extract unique subjects
  const subjects = useMemo(() => {
    const set = new Set(pdfLibrary.map((p) => p.subject));
    return ['All', ...Array.from(set)];
  }, [pdfLibrary]);

  // Filtered PDFs
  const filteredPdfs = useMemo(() => {
    return pdfLibrary.filter((pdf) => {
      const matchesSearch = 
        pdf.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
        pdf.subject.toLowerCase().includes(searchQuery.toLowerCase()) ||
        pdf.topics_covered.some((t) => t.toLowerCase().includes(searchQuery.toLowerCase()));

      const matchesCat = selectedCategory === 'All' || pdf.category === selectedCategory;
      const matchesSub = selectedSubject === 'All' || pdf.subject === selectedSubject;

      return matchesSearch && matchesCat && matchesSub;
    });
  }, [pdfLibrary, searchQuery, selectedCategory, selectedSubject]);

  return (
    <div className="space-y-6 animate-fadeIn">
      {/* Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-6 border-b border-slate-200 dark:border-slate-800">
        <div>
          <div className="inline-flex items-center gap-1.5 text-xs font-semibold text-teal-600 dark:text-teal-400 bg-teal-50 dark:bg-teal-950/60 px-2.5 py-1 rounded-full mb-2 border border-teal-200 dark:border-teal-800">
            <CheckCircle2 className="h-3.5 w-3.5" />
            105 Real Formatted Documents Generated
          </div>
          <h1 className="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white">
            Downloadable Study Library (PDFs)
          </h1>
          <p className="text-sm text-slate-500 dark:text-slate-400 mt-1">
            Download high-yield subject complete books, topic notes, formula sheets, practice sets, and mock tests for offline preparation.
          </p>
        </div>

        {/* Global Download Pack Button */}
        <div className="flex items-center gap-2">
          <a
            href="./00_Official_Syllabus/CS_GATE2027_Syllabus.pdf"
            download
            className="flex items-center gap-2 bg-blue-600 hover:bg-blue-700 text-white font-semibold text-xs px-4 py-2.5 rounded-xl shadow-sm transition"
          >
            <FolderDown className="h-4 w-4" />
            <span>Official Syllabus PDF</span>
          </a>
        </div>
      </div>

      {/* Filter and Search Controls */}
      <div className="flex flex-col sm:flex-row gap-3">
        <div className="relative flex-1">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-slate-400" />
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Search within 105+ PDFs by title, subject, or topic..."
            className="w-full pl-9 pr-4 py-2 text-xs sm:text-sm rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-slate-900 dark:text-slate-100 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500 shadow-sm"
          />
        </div>

        {/* Category Dropdown */}
        <select
          value={selectedCategory}
          onChange={(e) => setSelectedCategory(e.target.value)}
          className="px-3 py-2 text-xs sm:text-sm rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-slate-900 dark:text-slate-100 focus:outline-none focus:ring-2 focus:ring-blue-500 shadow-sm font-medium"
        >
          {categories.map((c) => (
            <option key={c} value={c}>{c}</option>
          ))}
        </select>

        {/* Subject Dropdown */}
        <select
          value={selectedSubject}
          onChange={(e) => setSelectedSubject(e.target.value)}
          className="px-3 py-2 text-xs sm:text-sm rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-slate-900 dark:text-slate-100 focus:outline-none focus:ring-2 focus:ring-blue-500 shadow-sm font-medium"
        >
          {subjects.map((s) => (
            <option key={s} value={s}>{s}</option>
          ))}
        </select>
      </div>

      {/* Results Header */}
      <div className="flex items-center justify-between text-xs font-semibold text-slate-500 dark:text-slate-400 px-1">
        <span>Showing {filteredPdfs.length} of {pdfLibrary.length} downloadable PDFs</span>
        <span>Vector & Printable A4 Format</span>
      </div>

      {/* Grid of PDF Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4">
        {filteredPdfs.map((pdf) => {
          const fileSizeKb = Math.round(pdf.file_size_bytes / 1024);
          const cleanPath = pdf.file_path.replace(/\\/g, '/').replace(/^\/+/, '');
          const relativeDownloadUrl = `./${cleanPath}`;

          return (
            <div
              key={pdf.pdf_id}
              className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 hover:border-blue-400 dark:hover:border-blue-600 rounded-xl p-5 shadow-sm hover:shadow-md transition flex flex-col justify-between"
            >
              <div>
                <div className="flex items-start justify-between gap-2 mb-2">
                  <span className="text-[10px] font-bold uppercase tracking-wider text-blue-600 dark:text-blue-400 bg-blue-50 dark:bg-blue-950/60 px-2 py-0.5 rounded border border-blue-200 dark:border-blue-800">
                    {pdf.category}
                  </span>
                  <span className="text-[11px] font-semibold text-slate-500 dark:text-slate-400">
                    {pdf.page_count} pages
                  </span>
                </div>

                <h3 className="text-sm font-bold text-slate-900 dark:text-white leading-snug line-clamp-2">
                  {pdf.title}
                </h3>
                <p className="text-xs text-slate-500 dark:text-slate-400 mt-1 font-medium">
                  {pdf.subject}
                </p>

                <div className="mt-3 flex flex-wrap gap-1">
                  {pdf.topics_covered.slice(0, 2).map((t, idx) => (
                    <span key={idx} className="text-[10px] text-slate-600 dark:text-slate-300 bg-slate-100 dark:bg-slate-800 px-2 py-0.5 rounded line-clamp-1">
                      {t}
                    </span>
                  ))}
                </div>
              </div>

              {/* Card Footer with Download Button */}
              <div className="mt-4 pt-3 border-t border-slate-100 dark:border-slate-800 flex items-center justify-between">
                <span className="text-[11px] text-slate-400 dark:text-slate-500 font-medium">
                  {fileSizeKb} KB
                </span>
                <a
                  href={relativeDownloadUrl}
                  download
                  className="inline-flex items-center gap-1.5 bg-blue-50 hover:bg-blue-600 text-blue-700 hover:text-white dark:bg-blue-950/50 dark:hover:bg-blue-600 dark:text-blue-300 dark:hover:text-white text-xs font-semibold px-3 py-1.5 rounded-lg border border-blue-200 dark:border-blue-800 transition"
                >
                  <FileDown className="h-3.5 w-3.5" />
                  <span>Download PDF</span>
                </a>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
