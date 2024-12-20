import java.io.FileWriter;
import java.io.IOException;
import java.util.HashSet;

public class Test03 {
    public static void main(String[] args) throws IOException {
        HashSet<String> names = new HashSet<>();
        names.add("陈煜");
        names.add("CY1");
        names.add("CY2");
        names.add("CY3");
        names.add("CY4");
        FileWriter fw = new FileWriter("./file/name.txt");
        names.forEach((String s)-> {
            try {
                fw.write(s);
                fw.write('\n');
            } catch (IOException e) {
                e.printStackTrace();
            }
        });
        fw.flush();
        fw.close();
    }
}
