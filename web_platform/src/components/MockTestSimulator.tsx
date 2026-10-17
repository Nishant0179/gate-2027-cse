import React, { useState, useEffect } from 'react';
import { 
  Clock, 
  CheckCircle, 
  AlertCircle, 
  RotateCcw, 
  Award, 
  HelpCircle, 
  ChevronLeft, 
  ChevronRight, 
  Send,
  BarChart2,
  BookmarkCheck,
  Check,
  X
} from 'lucide-react';
import confetti from 'canvas-confetti';

interface MockTestSimulatorProps {
  gateData: any;
}

type QuestionStatus = 'not_visited' | 'not_answered' | 'answered' | 'marked_review' | 'answered_marked_review';

export const MockTestSimulator: React.FC<MockTestSimulatorProps> = ({ gateData }) => {
  const testMeta = gateData.mockTests.meta;
  const questions: any[] = gateData.mockTests.mock1;

  const [activeQuestionIndex, setActiveQuestionIndex] = useState<number>(0);
  const [activeSection, setActiveSection] = useState<string>('General Aptitude');
  
  // Timer: 180 minutes = 10800 seconds
  const [secondsRemaining, setSecondsRemaining] = useState<number>(10800);
  const [testSubmitted, setTestSubmitted] = useState<boolean>(false);
  const [showSubmitModal, setShowSubmitModal] = useState<boolean>(false);

  // User responses: question index -> user answer (string for MCQ/NAT, string[] for MSQ)
  const [responses, setResponses] = useState<Record<number, any>>({});
  const [questionStatuses, setQuestionStatuses] = useState<Record<number, QuestionStatus>>({
    0: 'not_answered'
  });

  // Score analysis result
  const [scoreResult, setScoreResult] = useState<any>(null);

  // Timer interval
  useEffect(() => {
    if (testSubmitted) return;
    const timer = setInterval(() => {
      setSecondsRemaining((prev) => {
        if (prev <= 1) {
          clearInterval(timer);
          handleSubmitTest();
          return 0;
        }
        return prev - 1;
      });
    }, 1000);
    return () => clearInterval(timer);
  }, [testSubmitted]);

  const currentQ = questions[activeQuestionIndex];

  // Helper to format time HH:MM:SS
  const formatTime = (secs: number) => {
    const h = Math.floor(secs / 3600);
    const m = Math.floor((secs % 3600) / 60);
    const s = secs % 60;
    return `${h.toString().padStart(2, '0')}:${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  };

  // Switch question
  const goToQuestion = (idx: number) => {
    // If not answered yet, mark as not_answered
    if (!questionStatuses[idx]) {
      setQuestionStatuses((prev) => ({ ...prev, [idx]: 'not_answered' }));
    }
    setActiveQuestionIndex(idx);
    if (questions[idx].section !== activeSection) {
      setActiveSection(questions[idx].section);
    }
  };

  // Handle MCQ selection
  const handleSelectOption = (optKey: string) => {
    setResponses((prev) => ({ ...prev, [activeQuestionIndex]: optKey }));
  };

  // Handle MSQ checkbox toggle
  const handleToggleMsqOption = (optKey: string) => {
    const current = (responses[activeQuestionIndex] as string[]) || [];
    const updated = current.includes(optKey)
      ? current.filter((k) => k !== optKey)
      : [...current, optKey].sort();
    setResponses((prev) => ({ ...prev, [activeQuestionIndex]: updated }));
  };

  // Handle NAT text input
  const handleNatInput = (val: string) => {
    setResponses((prev) => ({ ...prev, [activeQuestionIndex]: val }));
  };

  // Clear current response
  const handleClearResponse = () => {
    setResponses((prev) => {
      const copy = { ...prev };
      delete copy[activeQuestionIndex];
      return copy;
    });
    setQuestionStatuses((prev) => ({ ...prev, [activeQuestionIndex]: 'not_answered' }));
  };

  // Save & Next
  const handleSaveAndNext = () => {
    const hasAnswer = responses[activeQuestionIndex] !== undefined && responses[activeQuestionIndex] !== '';
    const newStatus = hasAnswer ? 'answered' : 'not_answered';
    setQuestionStatuses((prev) => ({ ...prev, [activeQuestionIndex]: newStatus }));

    if (activeQuestionIndex < questions.length - 1) {
      goToQuestion(activeQuestionIndex + 1);
    }
  };

  // Mark for Review & Next
  const handleMarkForReviewAndNext = () => {
    const hasAnswer = responses[activeQuestionIndex] !== undefined && responses[activeQuestionIndex] !== '';
    const newStatus = hasAnswer ? 'answered_marked_review' : 'marked_review';
    setQuestionStatuses((prev) => ({ ...prev, [activeQuestionIndex]: newStatus }));

    if (activeQuestionIndex < questions.length - 1) {
      goToQuestion(activeQuestionIndex + 1);
    }
  };

  // Calculate Final Score
  const handleSubmitTest = () => {
    setShowSubmitModal(false);
    setTestSubmitted(true);

    let totalMarksObtained = 0;
    let correctCount = 0;
    let incorrectCount = 0;
    let unattemptedCount = 0;
    let gaScore = 0;
    let csScore = 0;

    const detailedEval = questions.map((q, idx) => {
      const userAns = responses[idx];
      let isCorrect = false;
      let marksAwarded = 0;

      if (userAns === undefined || userAns === '' || (Array.isArray(userAns) && userAns.length === 0)) {
        unattemptedCount++;
      } else {
        if (q.type === 'MCQ') {
          if (userAns === q.answer) {
            isCorrect = true;
            marksAwarded = q.marks;
            correctCount++;
          } else {
            // Negative marking for MCQs
            marksAwarded = q.marks === 1 ? -1 / 3 : -2 / 3;
            incorrectCount++;
          }
        } else if (q.type === 'MSQ') {
          // Zero negative, zero partial marking
          const correctArr = q.answer.split(',').map((s: string) => s.trim()).sort();
          const userArr = ((userAns as string[]) || []).sort();
          if (JSON.stringify(correctArr) === JSON.stringify(userArr)) {
            isCorrect = true;
            marksAwarded = q.marks;
            correctCount++;
          } else {
            marksAwarded = 0;
            incorrectCount++;
          }
        } else if (q.type === 'NAT') {
          // Zero negative marking
          const expected = parseFloat(q.answer);
          const entered = parseFloat(userAns);
          if (!isNaN(expected) && !isNaN(entered) && Math.abs(expected - entered) <= 0.05) {
            isCorrect = true;
            marksAwarded = q.marks;
            correctCount++;
          } else {
            marksAwarded = 0;
            incorrectCount++;
          }
        }
      }

      totalMarksObtained += marksAwarded;
      if (q.section === 'General Aptitude') {
        gaScore += marksAwarded;
      } else {
        csScore += marksAwarded;
      }

      return {
        ...q,
        userAns,
        isCorrect,
        marksAwarded
      };
    });

    const result = {
      totalMarks: Math.max(0, Math.round(totalMarksObtained * 100) / 100),
      gaScore: Math.round(gaScore * 100) / 100,
      csScore: Math.round(csScore * 100) / 100,
      correctCount,
      incorrectCount,
      unattemptedCount,
      accuracy: correctCount + incorrectCount > 0 
        ? Math.round((correctCount / (correctCount + incorrectCount)) * 100)
        : 0,
      detailedEval
    };

    setScoreResult(result);
    try {
      confetti({ particleCount: 80, spread: 60, origin: { y: 0.6 } });
    } catch (e) {}
  };

  // Question counts by status for palette
  const statusCounts = {
    answered: Object.values(questionStatuses).filter((s) => s === 'answered').length,
    not_answered: Object.values(questionStatuses).filter((s) => s === 'not_answered').length,
    marked_review: Object.values(questionStatuses).filter((s) => s === 'marked_review').length,
    answered_marked_review: Object.values(questionStatuses).filter((s) => s === 'answered_marked_review').length,
    not_visited: questions.length - Object.keys(questionStatuses).length,
  };

  // If Test is Submitted, show the comprehensive Review Screen
  if (testSubmitted && scoreResult) {
    return (
      <div className="space-y-6 animate-fadeIn">
        {/* Results Hero Card */}
        <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-6 sm:p-8 shadow-sm">
          <div className="text-center max-w-xl mx-auto space-y-3">
            <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-blue-50 dark:bg-blue-950 text-blue-700 dark:text-blue-300 font-bold text-xs border border-blue-200 dark:border-blue-800">
              <Award className="h-4 w-4" />
              GATE 2027 Mock Test 01 Result
            </div>
            <h2 className="text-3xl font-extrabold text-slate-900 dark:text-white">
              Score: <span className="text-blue-600 dark:text-blue-400">{scoreResult.totalMarks}</span> / 100
            </h2>
            <p className="text-sm text-slate-500 dark:text-slate-400">
              Official scoring applied: Negative marking for MCQs (1/3 & 2/3), zero negative for MSQ & NAT.
            </p>
          </div>

          {/* Breakdown Pills */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 mt-8">
            <div className="bg-slate-50 dark:bg-slate-800/50 p-4 rounded-xl text-center border border-slate-200/80 dark:border-slate-700/80">
              <span className="text-xs font-semibold text-slate-500 dark:text-slate-400">Accuracy</span>
              <div className="text-xl font-extrabold text-slate-900 dark:text-white mt-1">{scoreResult.accuracy}%</div>
            </div>
            <div className="bg-emerald-50 dark:bg-emerald-950/30 p-4 rounded-xl text-center border border-emerald-200 dark:border-emerald-800">
              <span className="text-xs font-semibold text-emerald-700 dark:text-emerald-400">Correct Answers</span>
              <div className="text-xl font-extrabold text-emerald-600 dark:text-emerald-400 mt-1">{scoreResult.correctCount}</div>
            </div>
            <div className="bg-rose-50 dark:bg-rose-950/30 p-4 rounded-xl text-center border border-rose-200 dark:border-rose-800">
              <span className="text-xs font-semibold text-rose-700 dark:text-rose-400">Incorrect Answers</span>
              <div className="text-xl font-extrabold text-rose-600 dark:text-rose-400 mt-1">{scoreResult.incorrectCount}</div>
            </div>
            <div className="bg-slate-50 dark:bg-slate-800/50 p-4 rounded-xl text-center border border-slate-200/80 dark:border-slate-700/80">
              <span className="text-xs font-semibold text-slate-500 dark:text-slate-400">Unattempted</span>
              <div className="text-xl font-extrabold text-slate-700 dark:text-slate-300 mt-1">{scoreResult.unattemptedCount}</div>
            </div>
          </div>

          <div className="mt-6 flex justify-center">
            <button
              onClick={() => {
                setTestSubmitted(false);
                setResponses({});
                setQuestionStatuses({ 0: 'not_answered' });
                setActiveQuestionIndex(0);
                setSecondsRemaining(10800);
              }}
              className="flex items-center gap-2 bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs px-5 py-2.5 rounded-xl shadow-sm transition"
            >
              <RotateCcw className="h-4 w-4" />
              <span>Retake Mock Exam</span>
            </button>
          </div>
        </div>

        {/* Detailed Question Review List */}
        <div className="space-y-4">
          <h3 className="text-lg font-bold text-slate-900 dark:text-white">
            Question-by-Question Solution Review
          </h3>
          {scoreResult.detailedEval.map((q: any, idx: number) => (
            <div
              key={idx}
              className={`p-5 rounded-xl border bg-white dark:bg-slate-900 ${
                q.isCorrect
                  ? 'border-emerald-300 dark:border-emerald-800'
                  : q.userAns !== undefined
                  ? 'border-rose-300 dark:border-rose-800'
                  : 'border-slate-200 dark:border-slate-800'
              }`}
            >
              <div className="flex items-center justify-between gap-2 mb-2">
                <div className="flex items-center gap-2">
                  <span className="text-xs font-extrabold px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-800 dark:text-slate-200">
                    Q{q.q_num}
                  </span>
                  <span className="text-xs font-semibold text-slate-500">
                    {q.section} • {q.type} • {q.marks} Mark{q.marks > 1 ? 's' : ''}
                  </span>
                </div>
                <div className="flex items-center gap-2">
                  {q.isCorrect ? (
                    <span className="inline-flex items-center gap-1 text-xs font-bold text-emerald-600 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-950/60 px-2 py-0.5 rounded">
                      <Check className="h-3 w-3" /> +{q.marksAwarded} Marks
                    </span>
                  ) : q.userAns !== undefined ? (
                    <span className="inline-flex items-center gap-1 text-xs font-bold text-rose-600 dark:text-rose-400 bg-rose-50 dark:bg-rose-950/60 px-2 py-0.5 rounded">
                      <X className="h-3 w-3" /> {q.marksAwarded} Marks
                    </span>
                  ) : (
                    <span className="text-xs font-semibold text-slate-400 bg-slate-100 dark:bg-slate-800 px-2 py-0.5 rounded">
                      Unattempted (0 Marks)
                    </span>
                  )}
                </div>
              </div>

              <div 
                className="text-xs sm:text-sm text-slate-800 dark:text-slate-200 leading-relaxed font-medium mb-3"
                dangerouslySetInnerHTML={{ __html: q.text }}
              />

              {q.options && (
                <div className="space-y-1.5 mb-3 pl-2">
                  {Object.entries(q.options).map(([k, val]: any) => (
                    <div 
                      key={k}
                      className={`text-xs p-2 rounded-lg flex items-start gap-2 ${
                        k === q.answer
                          ? 'bg-emerald-50 dark:bg-emerald-950/40 text-emerald-900 dark:text-emerald-300 font-semibold'
                          : k === q.userAns
                          ? 'bg-rose-50 dark:bg-rose-950/40 text-rose-900 dark:text-rose-300 line-through'
                          : 'text-slate-600 dark:text-slate-400'
                      }`}
                    >
                      <span className="font-bold">({k})</span>
                      <span dangerouslySetInnerHTML={{ __html: val }} />
                    </div>
                  ))}
                </div>
              )}

              <div className="p-3 rounded-lg bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700 text-xs space-y-1">
                <div className="flex items-center gap-2">
                  <span className="font-bold text-slate-500">Official Correct Answer:</span>
                  <span className="font-extrabold text-emerald-600 dark:text-emerald-400">{q.answer}</span>
                  {q.userAns !== undefined && (
                    <span className="font-semibold text-slate-500 ml-3">
                      Your Response: <b>{Array.isArray(q.userAns) ? q.userAns.join(', ') : q.userAns}</b>
                    </span>
                  )}
                </div>
                <div 
                  className="text-slate-700 dark:text-slate-300 leading-relaxed pt-1"
                  dangerouslySetInnerHTML={{ __html: q.explanation }}
                />
              </div>
            </div>
          ))}
        </div>
      </div>
    );
  }

  // Active Live CBT Interface
  return (
    <div className="space-y-4 animate-fadeIn select-none">
      {/* Top CBT Status Bar */}
      <div className="bg-slate-900 text-white rounded-xl p-3 sm:p-4 flex items-center justify-between shadow-md">
        <div className="flex items-center gap-3">
          <div className="h-8 w-8 rounded-lg bg-blue-600 flex items-center justify-center font-black text-sm">
            CBT
          </div>
          <div>
            <h2 className="text-sm font-bold tracking-tight">GATE 2027 CSE Mock Examination 01</h2>
            <p className="text-[11px] text-slate-400">Section: <b>{currentQ.section}</b></p>
          </div>
        </div>

        <div className="flex items-center gap-4">
          <div className="flex items-center gap-2 bg-slate-800 px-3 py-1.5 rounded-lg border border-slate-700">
            <Clock className="h-4 w-4 text-amber-400 animate-pulse" />
            <span className="font-mono text-sm font-bold text-amber-300">{formatTime(secondsRemaining)}</span>
          </div>

          <button
            onClick={() => setShowSubmitModal(true)}
            className="bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs px-3.5 py-2 rounded-lg transition"
          >
            Submit Exam
          </button>
        </div>
      </div>

      {/* Main Examination Grid: Question Area (Left) + Palette (Right) */}
      <div className="grid grid-cols-1 lg:grid-cols-4 gap-4">
        {/* Left 3 Cols: Question & Options */}
        <div className="lg:col-span-3 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-6 flex flex-col justify-between shadow-sm min-h-[500px]">
          <div>
            {/* Question Meta Row */}
            <div className="flex items-center justify-between pb-3 border-b border-slate-100 dark:border-slate-800 mb-4">
              <div className="flex items-center gap-2">
                <span className="text-xs font-bold text-blue-700 dark:text-blue-400 bg-blue-50 dark:bg-blue-950 px-2 py-0.5 rounded">
                  Question No. {currentQ.q_num}
                </span>
                <span className="text-xs font-bold text-slate-600 dark:text-slate-300">
                  {currentQ.type}
                </span>
              </div>
              <div className="text-xs font-semibold text-slate-500">
                Marking: <span className="text-emerald-600 dark:text-emerald-400 font-bold">+{currentQ.marks}</span> / <span className="text-rose-600 dark:text-rose-400 font-bold">{currentQ.type === 'MCQ' ? (currentQ.marks === 1 ? '-0.33' : '-0.67') : '0.00'}</span>
              </div>
            </div>

            {/* Question Statement */}
            <div 
              className="text-sm sm:text-base text-slate-900 dark:text-slate-100 leading-relaxed font-medium mb-6"
              dangerouslySetInnerHTML={{ __html: currentQ.text }}
            />

            {/* Option Input Area */}
            {currentQ.type === 'MCQ' && currentQ.options && (
              <div className="space-y-2.5 max-w-xl">
                {Object.entries(currentQ.options).map(([k, val]: any) => {
                  const isSelected = responses[activeQuestionIndex] === k;
                  return (
                    <div
                      key={k}
                      onClick={() => handleSelectOption(k)}
                      className={`cursor-pointer p-3 rounded-xl border text-xs sm:text-sm flex items-start gap-3 transition ${
                        isSelected
                          ? 'bg-blue-50 dark:bg-blue-900/30 border-blue-500 text-blue-900 dark:text-blue-200 font-semibold shadow-sm'
                          : 'bg-white dark:bg-slate-800/60 border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 hover:border-slate-400'
                      }`}
                    >
                      <div className={`h-4 w-4 mt-0.5 rounded-full border flex items-center justify-center flex-shrink-0 ${
                        isSelected ? 'border-blue-600 bg-blue-600 text-white' : 'border-slate-400'
                      }`}>
                        {isSelected && <div className="h-1.5 w-1.5 rounded-full bg-white" />}
                      </div>
                      <div>
                        <span className="font-bold mr-2">({k})</span>
                        <span dangerouslySetInnerHTML={{ __html: val }} />
                      </div>
                    </div>
                  );
                })}
              </div>
            )}

            {currentQ.type === 'MSQ' && currentQ.options && (
              <div className="space-y-2.5 max-w-xl">
                <p className="text-xs text-amber-700 dark:text-amber-400 font-semibold mb-2">
                  * Multiple Select Question: One or more options can be correct. No partial marking.
                </p>
                {Object.entries(currentQ.options).map(([k, val]: any) => {
                  const selectedArr = (responses[activeQuestionIndex] as string[]) || [];
                  const isChecked = selectedArr.includes(k);
                  return (
                    <div
                      key={k}
                      onClick={() => handleToggleMsqOption(k)}
                      className={`cursor-pointer p-3 rounded-xl border text-xs sm:text-sm flex items-start gap-3 transition ${
                        isChecked
                          ? 'bg-blue-50 dark:bg-blue-900/30 border-blue-500 text-blue-900 dark:text-blue-200 font-semibold shadow-sm'
                          : 'bg-white dark:bg-slate-800/60 border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 hover:border-slate-400'
                      }`}
                    >
                      <div className={`h-4 w-4 mt-0.5 rounded border flex items-center justify-center flex-shrink-0 ${
                        isChecked ? 'border-blue-600 bg-blue-600 text-white' : 'border-slate-400'
                      }`}>
                        {isChecked && <Check className="h-3 w-3 stroke-[3]" />}
                      </div>
                      <div>
                        <span className="font-bold mr-2">({k})</span>
                        <span dangerouslySetInnerHTML={{ __html: val }} />
                      </div>
                    </div>
                  );
                })}
              </div>
            )}

            {currentQ.type === 'NAT' && (
              <div className="max-w-xs space-y-2 mt-4">
                <label className="block text-xs font-bold text-slate-600 dark:text-slate-300">
                  Enter Numerical Value (Virtual Keypad):
                </label>
                <input
                  type="text"
                  value={responses[activeQuestionIndex] || ''}
                  onChange={(e) => handleNatInput(e.target.value)}
                  placeholder="e.g. 15 or 2.4"
                  className="w-full text-base font-mono font-bold px-4 py-2.5 rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-900 dark:text-slate-100 focus:outline-none focus:ring-2 focus:ring-blue-500 shadow-sm"
                />
                <span className="text-[11px] text-slate-400">Zero negative marking for NAT questions.</span>
              </div>
            )}
          </div>

          {/* Action Buttons Row */}
          <div className="pt-6 border-t border-slate-100 dark:border-slate-800 flex flex-wrap items-center justify-between gap-3 mt-8">
            <div className="flex items-center gap-2">
              <button
                onClick={handleSaveAndNext}
                className="bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs px-4 py-2.5 rounded-xl shadow-sm transition"
              >
                Save & Next
              </button>
              <button
                onClick={handleMarkForReviewAndNext}
                className="bg-purple-600 hover:bg-purple-700 text-white font-bold text-xs px-4 py-2.5 rounded-xl shadow-sm transition"
              >
                Mark for Review & Next
              </button>
              <button
                onClick={handleClearResponse}
                className="bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 font-semibold text-xs px-3.5 py-2.5 rounded-xl transition"
              >
                Clear Response
              </button>
            </div>

            <div className="flex items-center gap-2">
              <button
                disabled={activeQuestionIndex === 0}
                onClick={() => goToQuestion(activeQuestionIndex - 1)}
                className="disabled:opacity-40 p-2 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 transition"
              >
                <ChevronLeft className="h-4 w-4" />
              </button>
              <button
                disabled={activeQuestionIndex === questions.length - 1}
                onClick={() => goToQuestion(activeQuestionIndex + 1)}
                className="disabled:opacity-40 p-2 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 transition"
              >
                <ChevronRight className="h-4 w-4" />
              </button>
            </div>
          </div>
        </div>

        {/* Right 1 Col: Question Palette */}
        <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-5 shadow-sm space-y-4">
          <h3 className="text-xs font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500">
            Question Palette
          </h3>

          {/* Legend */}
          <div className="grid grid-cols-2 gap-2 text-[10px] font-semibold text-slate-600 dark:text-slate-300">
            <div className="flex items-center gap-1.5">
              <div className="h-3 w-3 rounded-full bg-emerald-500" />
              <span>Answered ({statusCounts.answered})</span>
            </div>
            <div className="flex items-center gap-1.5">
              <div className="h-3 w-3 rounded-full bg-rose-500" />
              <span>Not Answered ({statusCounts.not_answered})</span>
            </div>
            <div className="flex items-center gap-1.5">
              <div className="h-3 w-3 rounded-full bg-purple-500" />
              <span>Marked Review ({statusCounts.marked_review})</span>
            </div>
            <div className="flex items-center gap-1.5">
              <div className="h-3 w-3 rounded-full bg-slate-200 dark:bg-slate-700" />
              <span>Not Visited ({statusCounts.not_visited})</span>
            </div>
          </div>

          {/* Section Filter Pills */}
          <div className="flex gap-2 pt-2 border-t border-slate-100 dark:border-slate-800">
            <button
              onClick={() => {
                setActiveSection('General Aptitude');
                goToQuestion(0);
              }}
              className={`flex-1 py-1 text-[11px] font-bold rounded-lg ${
                activeSection === 'General Aptitude' ? 'bg-blue-600 text-white' : 'bg-slate-100 dark:bg-slate-800 text-slate-600'
              }`}
            >
              GA (1-10)
            </button>
            <button
              onClick={() => {
                setActiveSection('Computer Science & Engineering Mathematics');
                goToQuestion(10);
              }}
              className={`flex-1 py-1 text-[11px] font-bold rounded-lg ${
                activeSection === 'Computer Science & Engineering Mathematics' ? 'bg-blue-600 text-white' : 'bg-slate-100 dark:bg-slate-800 text-slate-600'
              }`}
            >
              CS/Math (11-65)
            </button>
          </div>

          {/* Palette Grid */}
          <div className="grid grid-cols-5 gap-2 max-h-72 overflow-y-auto pr-1">
            {questions.map((q, idx) => {
              const status = questionStatuses[idx] || 'not_visited';
              const isCurrent = activeQuestionIndex === idx;

              let bgClass = 'bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300';
              if (status === 'answered') bgClass = 'bg-emerald-500 text-white font-bold';
              else if (status === 'not_answered') bgClass = 'bg-rose-500 text-white font-bold';
              else if (status === 'marked_review') bgClass = 'bg-purple-600 text-white font-bold';
              else if (status === 'answered_marked_review') bgClass = 'bg-purple-600 text-white font-bold ring-2 ring-emerald-400';

              return (
                <button
                  key={idx}
                  onClick={() => goToQuestion(idx)}
                  className={`h-9 w-9 rounded-lg text-xs font-bold transition flex items-center justify-center relative ${bgClass} ${
                    isCurrent ? 'ring-2 ring-blue-500 ring-offset-2 dark:ring-offset-slate-900 scale-105' : ''
                  }`}
                >
                  {q.q_num}
                </button>
              );
            })}
          </div>
        </div>
      </div>

      {/* Confirmation Modal */}
      {showSubmitModal && (
        <div className="fixed inset-0 z-50 bg-black/60 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="bg-white dark:bg-slate-900 rounded-2xl max-w-md w-full p-6 shadow-2xl border border-slate-200 dark:border-slate-800 animate-scaleUp">
            <h3 className="text-lg font-bold text-slate-900 dark:text-white mb-2">
              Ready to submit your examination?
            </h3>
            <p className="text-xs text-slate-500 dark:text-slate-400 mb-4 leading-relaxed">
              You still have <b>{formatTime(secondsRemaining)}</b> remaining. Once submitted, your score will be computed according to official GATE negative marking rules.
            </p>

            <div className="grid grid-cols-2 gap-2 text-xs mb-6 p-3 rounded-xl bg-slate-50 dark:bg-slate-800">
              <div>Answered: <b>{statusCounts.answered + statusCounts.answered_marked_review}</b></div>
              <div>Marked for Review: <b>{statusCounts.marked_review}</b></div>
              <div>Not Answered: <b>{statusCounts.not_answered}</b></div>
              <div>Not Visited: <b>{statusCounts.not_visited}</b></div>
            </div>

            <div className="flex items-center justify-end gap-3">
              <button
                onClick={() => setShowSubmitModal(false)}
                className="px-4 py-2 text-xs font-semibold text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 rounded-lg"
              >
                Resume Test
              </button>
              <button
                onClick={handleSubmitTest}
                className="px-4 py-2 text-xs font-bold bg-emerald-600 hover:bg-emerald-700 text-white rounded-lg shadow-sm"
              >
                Yes, Submit Now
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
