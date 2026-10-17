import os
import sys
import json

# Add parent directory
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import content_data.engineering_math as em
import content_data.digital_logic as dl
import content_data.computer_org as coa
import content_data.programming_ds as pds
import content_data.algorithms as algo
import content_data.theory_of_computation as toc
import content_data.compiler_design as cd
import content_data.operating_systems as os_mod
import content_data.databases as db
import content_data.computer_networks as cn
import content_data.general_aptitude as ga
import content_data.pyq_repository as pyq_mod
import content_data.mock_tests_data as mock_mod
import content_data.study_plans_data as plan_mod
import content_data.final_revision_data as rev_mod

ALL_SUBJECTS = [em, dl, coa, pds, algo, toc, cd, os_mod, db, cn, ga]

def main():
    os.makedirs(os.path.join("web_platform", "src", "data"), exist_ok=True)

    with open("syllabus_database.json", "r", encoding="utf-8") as f:
        syllabus_db = json.load(f)

    with open("master_pdf_index.json", "r", encoding="utf-8") as f:
        pdf_index = json.load(f)

    subjects_data = []
    all_practice_questions = []

    import chapter_resources_data as cr_mod
    import content_data.practice_bank_generator as pbg
    import content_data.progressive_theory_engine as pte
    import content_data.subject_revision_data as srd

    for sub in ALL_SUBJECTS:
        meta = sub.SUBJECT_META
        chapters = sub.CHAPTERS
        sub_id = meta["id"]

        # Generate 20 high-yield practice questions for this subject
        questions = pbg.generate_practice_for_subject(sub_id, meta["name"])
        all_practice_questions.extend(questions)

        res_list = cr_mod.CHAPTER_RESOURCES.get(sub_id, [])

        enriched_chapters = []
        for idx, chap in enumerate(chapters):
            chap_copy = dict(chap)

            # Progressive 5-Tier learning theory injection in easy language
            if (sub_id, idx) in pte.PROGRESSIVE_THEORY_DICT:
                chap_copy["theory"] = pte.PROGRESSIVE_THEORY_DICT[(sub_id, idx)]

            if idx < len(res_list):
                chap_copy["video_resources"] = res_list[idx].get("videos", [])
                chap_copy["solved_examples"] = res_list[idx].get("solved_examples", [])
            else:
                chap_copy["video_resources"] = [
                    {"title": f"GATE Lecture: {chap['title']}", "channel": "Gate Smashers", "url": cr_mod.yt_link(f"gate cse {meta['name']} {chap['title']}")}
                ]
                chap_copy["solved_examples"] = []
            enriched_chapters.append(chap_copy)

        subjects_data.append({
            "id": meta["id"],
            "name": meta["name"],
            "folder": meta["folder"],
            "weightage": meta["weightage"],
            "topics": meta["topics"],
            "chapters": enriched_chapters,
            "questionCount": len(questions)
        })

    compiled_data = {
        "metadata": syllabus_db["metadata"],
        "sections": syllabus_db["sections"],
        "subjects": subjects_data,
        "pyqs": pyq_mod.VERIFIED_PYQS,
        "mockTests": {
            "meta": mock_mod.MOCK_TEST_META,
            "mock1": mock_mod.FULL_MOCK_1_QUESTIONS
        },
        "studyPlans": plan_mod.STUDY_PLANS,
        "finalRevision": rev_mod.FINAL_REVISION_DATA,
        "subjectRevision": srd.SUBJECT_REVISION_DATA,
        "pdfLibrary": pdf_index,
        "practiceQuestions": all_practice_questions
    }

    # Write as JSON
    json_path = os.path.join("web_platform", "src", "data", "gateData.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(compiled_data, f, indent=2)

    # Write as TypeScript module
    ts_path = os.path.join("web_platform", "src", "data", "gateData.ts")
    with open(ts_path, "w", encoding="utf-8") as f:
        f.write("// Auto-generated Comprehensive GATE 2027 CSE Data Store\n")
        f.write("import data from './gateData.json';\n\n")
        f.write("export const gateData = data;\n")
        f.write("export default gateData;\n")

    print(f"Exported gateData.json ({os.path.getsize(json_path)} bytes) and gateData.ts successfully!")

if __name__ == "__main__":
    main()
