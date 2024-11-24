import java.util.Random;

/*
* 1.  随机生成n位数字和字母的组合。
* */
public class TestRandom {
    public String getRandom(){
        Random random = new Random();
        String allChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        int num =  random.nextInt(allChars.length());
        StringBuilder stringBuilder = new  StringBuilder();
        stringBuilder.append(allChars.charAt(num));
        return  stringBuilder.toString();
    }
    public String getRandom(int len){
        StringBuilder stringBuilder = new StringBuilder();
        for (int i = 0; i < len; i++) {
            stringBuilder.append(getRandom());
        }
        return  stringBuilder.toString();
    }
    public static void main(String[] args) {
        TestRandom testRandom = new TestRandom();
        System.out.println(testRandom.getRandom());
        System.out.println(testRandom.getRandom(4));
    }
}
