package com.example.test01.contraller;

import com.example.test01.Response;
import com.example.test01.dao.Student;
import com.example.test01.dto.StudentDTO;
import com.example.test01.service.StudentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
public class StudentContraller {
    @Autowired
    private StudentService studentService;

    @GetMapping("/student/{id}/")
    public Response<StudentDTO> getStudentById(@PathVariable long id){
        return  Response.newSuccess(studentService.getStudentById(id));
    }

    @PostMapping("/student/")
    public  Response<Long> addStudent(@RequestBody StudentDTO studentDTO){
        return  Response.newSuccess(studentService.addNewStudent(studentDTO));
    }
}
