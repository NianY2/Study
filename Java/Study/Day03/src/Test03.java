//世界最高山峰是珠穆朗玛峰(8848.86米=8848860毫米)，
// 假如我有一张足够大的纸，它的厚度是0.1毫米。请问，折叠多少次，可以折成珠穆朗玛峰的高度。
public class Test03 {
    public static void main(String[] args) {
        int num = 0;
        float height = 1;
        while(height < 88488600){
            height*=2;
            num++;
        }
        System.out.println("折叠"+ num +"次，可以折成珠穆朗玛峰的高度。");
    }
}
