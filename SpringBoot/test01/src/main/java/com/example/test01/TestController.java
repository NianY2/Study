package com.example.test01;

import com.example.test01.utils.Response;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class TestController {
    @GetMapping("/hello")
    public Response<String> hello() {
        return Response.newSuccess("Hello World");
    }
}
