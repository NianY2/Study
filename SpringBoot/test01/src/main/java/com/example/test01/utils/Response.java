package com.example.test01.utils;

import io.swagger.v3.oas.annotations.media.Schema;
import lombok.Data;

/**
 * <p>
 * 统一结果集处理类
 * </p>
 *
 * @author CY
 * @email 1871263099@qq.com
 * @since 2024-09-21
 */
@Data
public class Response <T>{
    private static final int DEFAULT_FAIL_CODE = 500; // 定义默认失败状态码
    private static final String DEFAULT_FAIL_MSG = "fail"; // 定义默认失败信息

    @Schema(description = "数据")
    private T data=null;

    @Schema(description = "状态信息")
    private boolean state=true;

    @Schema(description = "返回信息")
    private String msg= "success";

    @Schema(description = "状态码")
    private int code=0;


    private Response<T> set(T data, String msg, int code, boolean state) {
        this.data = data;
        this.msg = msg;
        this.code = code;
        this.state = state;
        return this;
    }

    public static <K> Response<K> newSuccess(K data) {
        return new Response<K>().set(data, "success", 0, true);
    }

    public static <K> Response<K> newSuccess(K data, String msg) {
        return new Response<K>().set(data, msg, 0, true);
    }

    public static <K> Response<K> newSuccess(K data, String msg, int code) {
        return new Response<K>().set(data, msg, code, true);
    }

    public static <K> Response<K> newFail() {
        return new Response<K>().set(null, DEFAULT_FAIL_MSG, DEFAULT_FAIL_CODE, false);
    }

    public static <K> Response<K> newFail(String msg) {
        return new Response<K>().set(null, msg, DEFAULT_FAIL_CODE, false);
    }

    public static <K> Response<K> newFail(String msg, int code) {
        return new Response<K>().set(null, msg, code, false);
    }

    /**
     * 设置 状态码 和 信息 （二）
     *
     * @param httpCodeEnum 枚举信息
     * @return JsonResult
     */
    public static <K> Response<K> codeAndMessage(HttpCodeEnum httpCodeEnum) {
        return new Response<K>().set(null, httpCodeEnum.getMessage(), httpCodeEnum.getCode(), false);
    }
}
