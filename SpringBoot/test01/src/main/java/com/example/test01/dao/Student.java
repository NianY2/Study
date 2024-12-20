package com.example.test01.dao;

import io.swagger.v3.oas.annotations.media.Schema;
import jakarta.persistence.*;
import lombok.Data;

@Data
@Entity
@Table(name = "student")
public class Student {
    @Id
    @Column(name = "id")
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Schema(description = "ID")
    private long id;

    @Schema(description = "用户名")
    @Column(name = "name")
    private String name;

    @Schema(description = "密码")
    @Column(name = "password")
    private String password;

    @Schema(description = "邮箱")
    @Column(name = "email")
    private  String email;

    @Schema(description = "年龄")
    @Column(name = "age")
    private  int age;
}
