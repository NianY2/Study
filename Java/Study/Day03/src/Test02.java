//2.求1-10之间的偶数和，并把求和结果在控制台输出。
public class Test02 {
    public static void main(String[] args) {
        int res = 0;
        for (int i = 2; i <= 10; i+=2) {
            res+=i;
        }
        System.out.println("1-10之间的偶数和为："+res);
    }
}
