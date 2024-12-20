import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class Test04 {
    public static void main(String[] args) throws IOException {
        FileReader fr  = new FileReader("./file/name.txt");
        List<String> names = new ArrayList<>();
        int n = 0;
        String name = "";
        while ((n=fr.read()) != -1){
            if((char) n == '\n'){
                names.add(name);
                name = "";
                continue;
            }
            name += (char) n;
        }
        fr.close();
        System.out.println(names);
        Random random = new Random();
        System.out.println(names.get(random.nextInt(names.size())));

    }
}
