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
    @Schema(description = "数据")
    private T data=null;

    @Schema(description = "状态信息")
    private boolean state=true;

    @Schema(description = "返回信息")
    private String msg= "success";

    @Schema(description = "状态码")
    private int code=0;

    public static <K> Response<K>  newSuccess(K data){
        Response<K> response = new Response<K>();
        response.setData(data);
        return response;
    }

    public static <K> Response<K>  newSuccess(K data,String msg){
        Response<K> response = new Response<K>();
        response.setData(data);
        response.setMsg(msg);
        return  response;
    }

    public static <K> Response<K>  newSuccess(K data,String msg,int code){
        Response<K> response = new Response<K>();
        response.setData(data);
        response.setMsg(msg);
        response.setCode(code);
        return  response;
    }

    public static <K> Response<K>  newFail(){
        Response<K> response = new Response<K>();
        response.setState(false);
        response.setMsg("fail");
        response.setCode(500);
        return response;
    }
    public static <K> Response<K>  newFail(String msg){
        Response<K> response = new Response<K>();
        response.setState(false);
        response.setMsg(msg);
        response.setCode(500);
        return response;
    }

    public static <K> Response<K>  newFail(String msg,int code){
        Response<K> response = new Response<K>();
        response.setState(false);
        response.setMsg(msg);
        response.setCode(code);
        return response;
    }

    /**
     * 设置 状态码 和 信息 （二）
     *
     * @param httpCodeEnum 枚举信息
     * @return JsonResult
     */
    public static  <K> Response<K> codeAndMessage(HttpCodeEnum httpCodeEnum) {
        Response<K> response = new Response<K>();
        response.setState(false);
        response.setMsg(httpCodeEnum.getMessage());
        response.setCode(httpCodeEnum.getCode());
        return response;
    }
}
