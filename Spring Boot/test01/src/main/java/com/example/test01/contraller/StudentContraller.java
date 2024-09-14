package com.example.test01.contraller;

import com.example.test01.dao.Student;
import com.example.test01.service.StudentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class StudentContraller {
    @Autowired
    private StudentService studentService;

    @GetMapping("/student/{id}")
    public Student  getStudentById(@PathVariable long id){
        
        return studentService.getStudentById(id);
    }
}
