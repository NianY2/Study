package com.example.blog;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;


// 注解说明：处理 Http 请求
@RestController
public class HelloController {

    //    路由请求 可以设置各种操作方法
    @RequestMapping(value="/hello",method = RequestMethod.GET)
    // @GetMapping、@PostMapping、@PutMapping、@DeleteMapping 是 @RequestMapping 的子集
    // 选择一种使用
    // @GetMapping("/hello")
    public String hello() {
        return  "Hello World!";
    }
}
