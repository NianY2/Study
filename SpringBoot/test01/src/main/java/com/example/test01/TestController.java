package com.example.test01;

import com.example.test01.utils.Response;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@Slf4j
@RestController
public class TestController {
    // 注入 StringRedisTemplate
    @Autowired
    private StringRedisTemplate stringRedisTemplate;

    @GetMapping("/hello")
    public Response<String> hello() {
        // 设置
        this.stringRedisTemplate.opsForValue().set("title", "spring 中文网");
        // 读取
        String val = this.stringRedisTemplate.opsForValue().get("title");
        System.out.println(val);
        log.info("val="+val);

        return  Response.newSuccess("Hello World");
    }
}
