package com.example.test01.controller;

import com.example.test01.utils.Config.FileConfig;
import com.example.test01.utils.Response;
import com.example.test01.dto.StudentDTO;
import com.example.test01.service.StudentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import io.swagger.v3.oas.annotations.Operation;
import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.io.IOException;
import java.util.UUID;

@RestController
public class StudentController {
    @Autowired
    private StudentService studentService;

    @Operation(summary = "获取学生信息")
    @GetMapping("/student/{id}/")
    public Response<StudentDTO> getStudentById(@PathVariable long id){
        return  Response.newSuccess(studentService.getStudentById(id));
    }

    @Operation(summary = "创建学生")
    @PostMapping("/student/")
    public  Response<Long> addStudent(@RequestBody StudentDTO studentDTO){
//        throw new BusinessException(HttpCodeEnum.RC403);
        return  Response.newSuccess(studentService.addNewStudent(studentDTO));
    }

    @Operation(summary = "删除学生")
    @DeleteMapping("/student/{id}/")
    public  void deleteStudentByID(@PathVariable long id){
        studentService.deleteStudentByID(id);
    }

    @Operation(summary = "修改学生信息")
    @PutMapping("/student/{id}/")
    public  Response<StudentDTO> updateStudentByID(@PathVariable long id,
                                                   @RequestParam(required = false) String name,
                                                   @RequestParam(required = false) String email){
        return Response.newSuccess(studentService.updateStudentByID(id, name, email));
    }



    @PostMapping("/upload/")
    @ResponseBody
    public  Response upload(MultipartFile file) {
        // 验证是否有文件
        if(file == null || file.isEmpty()){
            return Response.newFail("Upload failed, please select file",400);
        }
        FileConfig fileConfig = new FileConfig();
        // 文件保存目录
        String filePath = fileConfig.getPath();

        // 验证文件夹
        File folder = new File(filePath);
        if (!folder.exists()) {
            folder.mkdirs();
        }

        // 文件名
        String fileName = UUID.randomUUID() + file.getOriginalFilename();
        filePath = filePath  + fileName;
        File saveFile = new File(filePath);
        try {
            file.transferTo(saveFile);
            return  Response.newSuccess("Upload successful");
        } catch (IOException e) {
            e.printStackTrace();
            return  Response.newFail("Upload failed",50001);
        }
    }
}
