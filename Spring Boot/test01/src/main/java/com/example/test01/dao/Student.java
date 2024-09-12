package com.example.test01.dao;

import jakarta.persistence.*;
import jdk.jfr.Enabled;

@Enabled
@Table(name = "studet")
public class Student {
    @Id
    @Column(name = "id")
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;

    @Column(name = "name")
    private String name;

    @Column(name = "email")
    private  String email;

    @Column(name = "age")
    private  int age;
}
