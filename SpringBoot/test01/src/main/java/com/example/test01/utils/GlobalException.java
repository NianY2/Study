package com.example.test01.utils;

import jakarta.servlet.http.HttpServletRequest;
import org.springframework.http.HttpStatus;
import org.springframework.web.HttpRequestMethodNotSupportedException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.multipart.MaxUploadSizeExceededException;
import org.springframework.web.servlet.NoHandlerFoundException;

/**
 * 全局异常信息处理类
 */
//@Slf4j
@RestControllerAdvice
public class GlobalException {


    /**
    * @Description 处理业务异常
    * @return Response
    * @Author CY
    * @Date 2024/9/21
    */
    @ExceptionHandler(value = BusinessException.class)
    public Response businessException(BusinessException e) {
        System.out.println(e.getMessage());
        return Response.newFail(e.getMessage(),e.getCode());
    }

    /**
    * @Description  处理未知(600)异常
    * @Author CY
    * @Date 2024/9/21
    */
    @ExceptionHandler(value = Exception.class)
    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
    public Response globalException(Exception e) {
        System.out.println("服务器错误："+e.getMessage());
        e.printStackTrace();
        return Response.codeAndMessage(HttpCodeEnum.RC600);
    }

    /**
    * @Description 404错误
    * @Author CY
    * @Date 2024/9/21
    */
    @ExceptionHandler(value = NoHandlerFoundException.class)
    @ResponseStatus(HttpStatus.NOT_FOUND)
    public Response noHandlerFoundException(HttpServletRequest e) {
        return Response.codeAndMessage(HttpCodeEnum.RC404);
    }


    /**
    * @Description 超过最大上传文件大小错误(413)
    * @Author CY
    * @Date 2024/9/21
    */
    @ExceptionHandler(value = MaxUploadSizeExceededException.class)
    @ResponseStatus(HttpStatus.PAYLOAD_TOO_LARGE)
    public Response maxUploadSizeExceededException(HttpServletRequest e) {
        return Response.codeAndMessage(HttpCodeEnum.RC413);
    }

    /**
     * @Description 请求方式错误(405)
     * @Author CY
     * @Date 2024/9/21
     */
    @ExceptionHandler(value = HttpRequestMethodNotSupportedException.class)
    @ResponseStatus(HttpStatus.METHOD_NOT_ALLOWED)
    public Response httpRequestMethodNotSupportedException(HttpServletRequest e) {
        return Response.codeAndMessage(HttpCodeEnum.RC405);
    }
}

