//1. 定义一个方法，该方法能够找出三个整数中的最大值并返回。在主方法中调用方法测试执行。
public class Test01 {
    public  static  int maxNum(int a,int b,int c){
        return  Math.max(a,Math.max(b,c));
    }
    public static void main(String[] args) {
        System.out.println(maxNum(1,2,3));
    }
}
