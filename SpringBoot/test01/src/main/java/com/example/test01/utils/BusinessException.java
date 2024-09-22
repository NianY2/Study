package com.example.test01.utils;

import lombok.Getter;

/**
 * 业务异常处理类
 */
@Getter
public class BusinessException extends RuntimeException {

    /**
     * 状态码
     */
    private final Integer code;

    /**
     * 报错信息
     */
    private final String message;

    /**
     * 全参构造方法
     */
    public BusinessException(Integer code, String message) {
        this.code = code;
        this.message = message;
    }

    /**
     * 构造方法
     */
    public BusinessException(String message) {
        this(HttpCodeEnum.ERROR.getCode(), message);
    }

    /**
     * 构造方法
     */
    public BusinessException(HttpCodeEnum httpCodeEnum) {
        this(httpCodeEnum.getCode(), httpCodeEnum.getMessage());
    }

}

