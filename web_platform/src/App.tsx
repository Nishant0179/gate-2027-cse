import React, { useState, useEffect } from 'react';
import { gateData } from './data/gateData';
import { Navbar } from './components/Navbar';
import { Sidebar } from './components/Sidebar';
import { HomeDashboard } from './components/HomeDashboard';
import { OfficialSyllabusView } from './components/OfficialSyllabusView';
import { SubjectLibraryView } from './components/SubjectLibraryView';
import { PdfLibraryView } from './components/PdfLibraryView';
import { PyqExplorerView } from './components/PyqExplorerView';
import { PracticeBankView } from './components/PracticeBankView';
import { MockTestSimulator } from './components/MockTestSimulator';
import { FormulaSheetsView } from './components/FormulaSheetsView';
import { StudyPlannerView } from './components/StudyPlannerView';
import { QuickRevisionView } from './components/QuickRevisionView';
import { AnalyticsView } from './components/AnalyticsView';

export function App() {
  const [currentTab, setCurrentTab] = useState<string>('home');
  const [darkMode, setDarkMode] = useState<boolean>(() => {
    return localStorage.getItem('gate_theme') === 'dark';
  });
  const [searchQuery, setSearchQuery] = useState<string>('');

  // Persisted completed topics
  const [completedTopics, setCompletedTopics] = useState<string[]>(() => {
    const saved = localStorage.getItem('gate_completed_topics');
    return saved ? JSON.parse(saved) : [];
  });

  // Persisted completed planner tasks
  const [completedTasks, setCompletedTasks] = useState<string[]>(() => {
    const saved = localStorage.getItem('gate_completed_tasks');
    return saved ? JSON.parse(saved) : [];
  });

  // Active Subject and Chapter for deep-linking
  const [selectedSubjectId, setSelectedSubjectId] = useState<string>(gateData.subjects[0]?.id || 'EM');
  const [activeChapterIndex, setActiveChapterIndex] = useState<number>(0);

  const navigateToTopic = (subjectId: string, chapterIndex: number = 0) => {
    setSelectedSubjectId(subjectId);
    setActiveChapterIndex(chapterIndex);
    setCurrentTab('subject_library');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add('dark');
      localStorage.setItem('gate_theme', 'dark');
    } else {
      document.documentElement.classList.remove('dark');
      localStorage.setItem('gate_theme', 'light');
    }
  }, [darkMode]);

  const toggleTopicCompletion = (topicId: string) => {
    setCompletedTopics((prev) => {
      const updated = prev.includes(topicId)
        ? prev.filter((id) => id !== topicId)
        : [...prev, topicId];
      localStorage.setItem('gate_completed_topics', JSON.stringify(updated));
      return updated;
    });
  };

  const toggleTaskCompletion = (taskId: string) => {
    setCompletedTasks((prev) => {
      const updated = prev.includes(taskId)
        ? prev.filter((id) => id !== taskId)
        : [...prev, taskId];
      localStorage.setItem('gate_completed_tasks', JSON.stringify(updated));
      return updated;
    });
  };

  return (
    <div className="min-h-screen bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-slate-100 flex flex-col font-sans transition-colors">
      <Navbar
        currentTab={currentTab}
        setCurrentTab={setCurrentTab}
        darkMode={darkMode}
        setDarkMode={setDarkMode}
        searchQuery={searchQuery}
        setSearchQuery={setSearchQuery}
      />

      <div className="flex-1 max-w-7xl w-full mx-auto flex">
        <Sidebar
          currentTab={currentTab}
          setCurrentTab={setCurrentTab}
          pdfCount={gateData.pdfLibrary.length}
        />

        <main className="flex-1 p-4 sm:p-6 lg:p-8 overflow-x-hidden">
          {currentTab === 'home' && (
            <HomeDashboard
              setCurrentTab={setCurrentTab}
              gateData={gateData}
              completedTopics={completedTopics}
            />
          )}

          {currentTab === 'syllabus' && (
            <OfficialSyllabusView gateData={gateData} />
          )}

          {currentTab === 'subject_library' && (
            <SubjectLibraryView
              gateData={gateData}
              completedTopics={completedTopics}
              toggleTopicCompletion={toggleTopicCompletion}
              selectedSubjectId={selectedSubjectId}
              setSelectedSubjectId={setSelectedSubjectId}
              activeChapterIndex={activeChapterIndex}
              setActiveChapterIndex={setActiveChapterIndex}
              setCurrentTab={setCurrentTab}
            />
          )}

          {currentTab === 'pdf_library' && (
            <PdfLibraryView pdfLibrary={gateData.pdfLibrary} />
          )}

          {currentTab === 'pyq_explorer' && (
            <PyqExplorerView pyqs={gateData.pyqs} />
          )}

          {currentTab === 'practice_banks' && (
            <PracticeBankView
              questions={gateData.practiceQuestions}
              subjects={gateData.subjects}
            />
          )}

          {currentTab === 'mock_tests' && (
            <MockTestSimulator gateData={gateData} />
          )}

          {currentTab === 'quick_revision' && (
            <QuickRevisionView 
              finalRevision={gateData.finalRevision} 
              subjectRevision={gateData.subjectRevision} 
            />
          )}

          {currentTab === 'formula_sheets' && (
            <FormulaSheetsView finalRevision={gateData.finalRevision} />
          )}

          {currentTab === 'study_planner' && (
            <StudyPlannerView
              studyPlans={gateData.studyPlans}
              completedTasks={completedTasks}
              toggleTaskCompletion={toggleTaskCompletion}
              navigateToTopic={navigateToTopic}
            />
          )}

          {currentTab === 'analytics' && (
            <AnalyticsView
              gateData={gateData}
              completedTopics={completedTopics}
            />
          )}
        </main>
      </div>

      {/* Footer */}
      <footer className="mt-auto border-t border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 py-6 text-center text-xs text-slate-500 dark:text-slate-400">
        <div className="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-2">
          <span>GATE 2027 CSE Preparation Platform • Verified against IIT Madras Official Guidelines</span>
          <span>Target Exam: 6th February 2027 • 105 Downloadable Study PDFs</span>
        </div>
      </footer>
    </div>
  );
}

export default App;
