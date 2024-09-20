package com.example.test01;

//import lombok.AllArgsConstructor;
//import lombok.Builder;
//import lombok.Getter;
//import lombok.Setter;
//import lombok.extern.slf4j.Slf4j;
//
//@Builder(toBuilder = true)
//@AllArgsConstructor
//@Setter
//@Getter
//@Slf4j

public class Response <T>{
    private T data;
    private boolean success;
    private String errorMsg;
    private int errorCode;

    public int getErrorCode() {
        return errorCode;
    }

    public void setErrorCode(int errorCode) {
        this.errorCode = errorCode;
    }

    public static <K> Response<K>  newSuccess(){
        Response<K> response = new Response<K>();
        response.setSuccess(true);
        return response;
    }

    public static <K> Response<K>  newSuccess(K data){
        Response<K> response = new Response<K>();
        response.setSuccess(true);
        response.setData(data);
        return response;
    }

    public  static  Response<Void> newFail(String errorMsg){
        Response<Void> response = new Response<Void>();
        response.setSuccess(false);
        response.setErrorMsg(errorMsg);
        response.setErrorCode(40000000);
        return response;
    }
    public  static  Response<Void> newFail(String errorMsg,int code){
        Response<Void> response = new Response<Void>();
        response.setSuccess(false);
        response.setErrorMsg(errorMsg);
        response.setErrorCode(code);
        return response;
    }

    public boolean isSuccess() {
        return success;
    }

    public void setSuccess(boolean success) {
        this.success = success;
    }

    public T getData() {
        return data;
    }

    public void setData(T data) {
        this.data = data;
    }

    public String getErrorMsg() {
        return errorMsg;
    }

    public void setErrorMsg(String errorMsg) {
        this.errorMsg = errorMsg;
    }
}
