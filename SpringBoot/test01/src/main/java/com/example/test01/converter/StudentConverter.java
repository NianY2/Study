package com.example.test01.converter;

import com.example.test01.dao.Student;
import com.example.test01.dto.StudentDTO;

public class StudentConverter {
    public  static StudentDTO converterStudent(Student student){
        StudentDTO studentDTO = new StudentDTO();
        studentDTO.setId(student.getId());
        studentDTO.setName(student.getName());
        studentDTO.setEmail(student.getEmail());
        studentDTO.setAge(student.getAge());
        return  studentDTO;
    }

    public  static Student converterStudent(StudentDTO studentDTO){
        Student student = new Student();
//        student.setId(studentDTO.getId());
        student.setName(studentDTO.getName());
        student.setEmail(studentDTO.getEmail());
        student.setAge(studentDTO.getAge());
        return  student;
    }
}
