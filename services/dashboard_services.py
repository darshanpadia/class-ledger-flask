from repositories.student_record_repo import (
    find_duplicate_record, insert_student_record, update_student_record, fetch_all_student_records,
    delete_student_record_by_id
)

def fetch_all_student_record_service():
    return fetch_all_student_records

def add_student_record_service(student_name, subject, marks, teacher_id):
    existing = find_duplicate_record(student_name, subject)

    if existing:
        total_marks = existing.marks + marks
        if total_marks > 100:
            return{
                "message":"Cannot add with existing record, total exceeding 100",
                "category":"error"
            }
        update_student_record(existing.id, student_name, subject, total_marks)
        return{
            "message": f"Merged with existing record id: {existing.id}, Total marks: {total_marks}",
            "category": "success"
        }
    insert_student_record(student_name, subject, marks, teacher_id)
    return {
        "message": "Student record successfully added",
        "category" : "success"
    }

def delete_student_record_service(record_id):
    """"""
    success = delete_student_record_by_id(record_id)
    if success:
        return{
            "message": "Student record deleted.",
            "category": "info"
        }
    return{
        "message": "Record not found.",
        "category":"error"
    }