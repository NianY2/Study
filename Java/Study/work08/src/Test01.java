import java.io.*;

public class Test01 {
    public static void main(String[] args) throws IOException {
        FileInputStream fis = new FileInputStream("./img/girl.png");
        FileOutputStream fos = new FileOutputStream("./file/girl.png");
        int n = 0;
        while ((n=fis.read()) != -1){
            char by = (char) n;
            fos.write(by);
        }
        fos.flush();
        fos.close();
    }
}
