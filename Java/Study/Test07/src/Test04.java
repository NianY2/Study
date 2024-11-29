import java.util.regex.Matcher;
import java.util.regex.Pattern;

/*
* 4.完成如下需求：
现有如下文本：
* "Java语言是面向对象的，Java语言是健壮的，Java语言是安全的，Java是高性能的，Java语言是跨平台的"。
* 请编写程序，统计该文本中"Java"一词出现的次数。
* */
public class Test04 {
    public static void main(String[] args) {
        String s = "Java语言是面向对象的，Java语言是健壮的，Java语言是安全的，Java是高性能的，Java语言是跨平台的";
        Pattern pattern = Pattern.compile("Java");
        Matcher matcher = pattern.matcher(s);
        int cnt = 0;
        while (matcher.find()){
            cnt+=1;
        }
        System.out.println(cnt);
    }
}
