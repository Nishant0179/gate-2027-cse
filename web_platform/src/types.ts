export type QuestionType = 'MCQ' | 'MSQ' | 'NAT' | string;
export type Difficulty = 'Easy' | 'Medium' | 'GATE-Level' | string;

export interface Question {
  id?: string;
  q_num?: number;
  section?: string;
  type: QuestionType;
  marks: number;
  text: string;
  options?: Record<string, string>;
  answer?: string;
  explanation?: string;
  is_pyq?: boolean;
  year?: number | null;
  difficulty?: Difficulty;
}

export interface Chapter {
  title: string;
  hinglish: string;
  theory: string;
  callouts?: Array<[string, string, string]>;
  tables?: Array<{
    header: string[];
    rows: string[][];
  }>;
}

export interface Subject {
  id: string;
  name: string;
  folder: string;
  weightage: string;
  topics: string[];
  chapters: Chapter[];
  questionCount: number;
}

export interface PdfDocument {
  pdf_id: string;
  title: string;
  subject: string;
  topics_covered: string[];
  page_count: number;
  file_path: string;
  file_size_bytes: number;
  generation_status: string;
  validation_status: string;
  category: string;
}

export interface PYQItem {
  id: string;
  year: number;
  subject: string;
  topic: string;
  type: QuestionType;
  marks: number;
  text: string;
  options?: Record<string, string>;
  answer: string;
  explanation: string;
  source_url: string;
  verification_status: string;
}

export interface StudyPlanTier {
  title: string;
  daily_breakdown: {
    concept_study_mins: number;
    practice_pyq_mins: number;
    revision_mins: number;
  };
  strategy: string;
}

export interface WeeklyRoadmapItem {
  week: number;
  phase: string;
  subjects: string[];
  topics: string[];
  targets: string;
  buffer_day: string;
}
