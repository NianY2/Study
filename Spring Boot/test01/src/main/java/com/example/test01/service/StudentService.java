package com.example.test01.service;

import com.example.test01.dao.Student;
import com.example.test01.dto.StudentDTO;

public interface StudentService {
    StudentDTO getStudentById(long id);
    Long addNewStudent(StudentDTO studentDTO);
}
