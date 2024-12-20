import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class Test02 {
    public static void main(String[] args) throws IOException {
        FileReader fr = new FileReader("./img/data.txt");
        FileWriter fw = new FileWriter("./file/data.txt");
        int n = 0;
        while ((n=fr.read()) != -1){
            fw.write((char) n);
        }
        fw.flush();
        fw.close();
    }
}
