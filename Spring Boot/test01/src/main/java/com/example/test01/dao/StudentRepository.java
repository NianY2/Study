package com.example.test01.dao;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public class StudentRepository  extends JpaRepository<Student,long>{
}
