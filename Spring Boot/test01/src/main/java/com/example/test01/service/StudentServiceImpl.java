package com.example.test01.service;

import com.example.test01.converter.StudentConverter;
import com.example.test01.dao.Student;
import com.example.test01.dao.StudentRepository;
import com.example.test01.dto.StudentDTO;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class StudentServiceImpl implements StudentService {

    @Autowired
    private StudentRepository studentRepository;

    @Override
    public StudentDTO getStudentById(long id) {
        Student student =  studentRepository.findById(id).orElseThrow(RuntimeException::new);
        return StudentConverter.converterStudent(student);
    }

    @Override
    public Long addNewStudent(StudentDTO studentDTO) {
        List<Student> studentList =  studentRepository.findByEmail(studentDTO.getEmail());
        if(!studentList.isEmpty()){
            throw new IllegalStateException("email"+studentDTO.getEmail()+" has been taken");
        }
        Student student =  studentRepository.save(StudentConverter.converterStudent(studentDTO));
        return student.getId();
    }
}
