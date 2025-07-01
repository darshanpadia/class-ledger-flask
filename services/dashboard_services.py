from repositories.student_record_repo import (
    find_duplicate_record, insert_student_record, update_student_record, fetch_all_student_records,
    delete_student_record_by_id, fetch_student_by_id
)
from repositories.edit_log_repo import create_edit_log
from repositories.teacher_repo import fetch_teacher_by_id

def fetch_all_student_record_service():
    """
    Return all student records from the database.
    """
    return fetch_all_student_records

def add_student_record_service(student_name, subject, marks, teacher_id):
    """
    Add a new student record or merge with an existing one if duplicate found.
    """
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
    """
    Delete a student record by ID.
    """
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

def update_student_record_service(record_id, name, subject, marks, teacher_id):
    """
    Update an existing student record if valid and authorized.
    Also logs the update.
    """
    if not name or not subject or not str(marks).isdigit():
        return{
            "message": "Invalid input",
            "category":"error"
        }
    
    marks = int(marks)
    current_record = fetch_student_by_id(record_id)
    if not current_record:
        return {
            "message": "Record not found.",
            "category": "error"
        }
    
    # Check if the teacher owns the record
    if current_record.teacher_id != teacher_id:
        return{
            "message": "You do not have permission to edit this record.",
            "category": "error"
        }
    
    # Check for duplicate entry
    duplicate = find_duplicate_record(name, subject)
    if duplicate and duplicate.id != record_id:
        return {
            "message": "Another record with the same name and subject exists.",
            "category": "error"
        }
    
    # Update the record
    update_student_record(record_id, name, subject, marks)

    teacher = fetch_teacher_by_id(teacher_id)
    if teacher:
        create_edit_log(teacher.username, record_id)
        
    return{
        "message": "Student record updated successfully.",
        "category": "success"
    }