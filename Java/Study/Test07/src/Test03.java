import java.util.regex.Matcher;
import java.util.regex.Pattern;

/*
*
请从下列的网页内容中，爬取出电话号码和邮箱，并在控制台输出结果。
网页内容如：“欢迎来到广州商学院学习,电话020-82876193，或者联系邮箱" +
        "gzcc@16.com,电话18762832633，0203232323" +
        "邮箱bozai@gcc.edu.cn，400-100-3233 ，4001003232”+
“电话95333，95588”。
* */
public class Test03 {
    public static void main(String[] args) {
        String s = "欢迎来到广州商学院学习,电话020-82876193，或者联系邮箱" +
                "gzcc@16.com,电话18762832633，0203232323" +
                "邮箱bozai@gcc.edu.cn，400-100-3233 ，4001003232"+
                "电话95333，95588。";
        Pattern pattern = Pattern.compile(
                "(\\w{1,}@\\w{2,10}(\\.\\w{2,10}){1,2})|" +
                        "(1[3-9]\\d{9})|(0\\d{2,5}-?\\d{5,15})|400-?\\d{3,8}-?\\d{3,8}"
        );
        Matcher matcher = pattern.matcher(s);
        while (matcher.find()){
            System.out.println(matcher.group());
        }
    }
}
