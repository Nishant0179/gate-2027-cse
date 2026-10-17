import React, { useState, useEffect } from 'react';
import { BookOpen, Moon, Sun, Search, Clock, Award, Download } from 'lucide-react';

interface NavbarProps {
  currentTab: string;
  setCurrentTab: (tab: string) => void;
  darkMode: boolean;
  setDarkMode: (val: boolean) => void;
  searchQuery: string;
  setSearchQuery: (query: string) => void;
}

export const Navbar: React.FC<NavbarProps> = ({
  currentTab,
  setCurrentTab,
  darkMode,
  setDarkMode,
  searchQuery,
  setSearchQuery,
}) => {
  const [timeLeft, setTimeLeft] = useState<{ days: number; hours: number; mins: number }>({ days: 0, hours: 0, mins: 0 });

  useEffect(() => {
    const examDate = new Date('2027-02-06T09:30:00+05:30').getTime();
    const updateCountdown = () => {
      const now = new Date().getTime();
      const diff = examDate - now;
      if (diff > 0) {
        const days = Math.floor(diff / (1000 * 60 * 60 * 24));
        const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const mins = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
        setTimeLeft({ days, hours, mins });
      }
    };
    updateCountdown();
    const interval = setInterval(updateCountdown, 60000);
    return () => clearInterval(interval);
  }, []);

  return (
    <header className="sticky top-0 z-40 bg-white/95 dark:bg-slate-900/95 backdrop-blur border-b border-slate-200 dark:border-slate-800 transition-colors">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-4">
        {/* Brand */}
        <div 
          onClick={() => setCurrentTab('home')} 
          className="flex items-center gap-3 cursor-pointer select-none"
        >
          <div className="h-10 w-10 rounded-xl bg-gradient-to-tr from-blue-700 to-teal-500 flex items-center justify-center text-white shadow-md shadow-blue-500/20">
            <BookOpen className="h-5 w-5" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <span className="font-extrabold text-lg text-slate-900 dark:text-white tracking-tight">GATE 2027 CS</span>
              <span className="text-[10px] font-bold uppercase tracking-wider bg-blue-100 dark:bg-blue-950 text-blue-700 dark:text-blue-300 px-2 py-0.5 rounded-full border border-blue-200 dark:border-blue-800">
                IIT Madras
              </span>
            </div>
            <p className="text-xs text-slate-500 dark:text-slate-400 font-medium">Preparation Platform & Study Library</p>
          </div>
        </div>

        {/* Global Search Bar */}
        <div className="hidden md:flex flex-1 max-w-md relative">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-slate-400" />
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Search subjects, topics, formulas, PYQs..."
            className="w-full pl-9 pr-4 py-1.5 text-sm rounded-lg bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-900 dark:text-slate-100 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>

        {/* Countdown & Quick Actions */}
        <div className="flex items-center gap-3">
          {/* Exam Countdown Pill */}
          <div className="hidden sm:flex items-center gap-2 bg-amber-50 dark:bg-amber-950/40 border border-amber-200 dark:border-amber-800/60 px-3 py-1 rounded-full text-xs font-semibold text-amber-800 dark:text-amber-300">
            <Clock className="h-3.5 w-3.5 text-amber-600 dark:text-amber-400 animate-pulse" />
            <span>Target Exam: <b>{timeLeft.days}d {timeLeft.hours}h {timeLeft.mins}m</b></span>
          </div>

          {/* Quick Mock CBT Button */}
          <button
            onClick={() => setCurrentTab('mock_tests')}
            className="flex items-center gap-1.5 bg-blue-600 hover:bg-blue-700 text-white text-xs font-semibold px-3 py-2 rounded-lg shadow-sm transition"
          >
            <Award className="h-4 w-4" />
            <span className="hidden sm:inline">Start CBT Mock</span>
          </button>

          {/* Dark Mode Toggle */}
          <button
            onClick={() => setDarkMode(!darkMode)}
            className="p-2 rounded-lg bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-600 dark:text-slate-300 transition"
            title="Toggle Dark Mode"
          >
            {darkMode ? <Sun className="h-4 w-4 text-amber-400" /> : <Moon className="h-4 w-4 text-slate-600" />}
          </button>
        </div>
      </div>
    </header>
  );
};
