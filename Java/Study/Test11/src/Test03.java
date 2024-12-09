import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class  Book{
//    编号，书名，作者，价格
    private  String id = null;
    private  String name;
    private  String author;
    private  double price;

    public Book(String id, String name, String author, double price) {
        this.id = id;
        this.name = name;
        this.author = author;
        this.price = price;
    }

    public Book() {
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    @Override
    public String toString() {
        return "Book{" +
                "id='" + id + '\'' +
                ", name='" + name + '\'' +
                ", author='" + author + '\'' +
                ", price=" + price +
                '}';
    }
}
class  Books{
    static List<Book> bookList = new ArrayList<>();
    static Scanner sc = new Scanner(System.in);
    static  {
        bookList.add(new Book("1","哈哈","CY",20.90));
    }
    static public void add(){
        Book book = new Book();
        System.out.print("编号：");
        book.setId(sc.nextLine());
        while (findByID(book.getId()) != null){
            System.out.println("编号重复");
            System.out.print("编号：");
            book.setId(sc.nextLine());
        }
        System.out.print("书名：");
        book.setName(sc.nextLine());
        System.out.print("作者：");
        book.setAuthor(sc.nextLine());
        System.out.print("价格：");
        book.setPrice(sc.nextFloat());
        sc.nextLine();
        bookList.add(book);
        System.out.println("添加成功");

    }
    static public Book findByID(String id){
        for (Book book:bookList){
            if(book.getId().equals(id)){
                return book;
            }
        }
        return null;
    }
    static public Book findByName(){
        System.out.print("书名：");
        String name = sc.nextLine();
        for (Book book:bookList){
            if(book.getName().equals(name)){
                return book;
            }
        }
        return null;
    }
    static public boolean remove(){
        System.out.print("编号：");
        String id = sc.nextLine();
        for (int i = 0; i < bookList.size(); i++) {
            Book book = bookList.get(i);
            if(book.getId().equals(id)){
                bookList.remove(i);
                System.out.println("删除成功");
                return true;
            }
        }
        System.out.println("删除失败");
        return false;
    }
    static public void update(){
        System.out.print("编号：");
        String id = sc.nextLine();
        Book book = findByID(id);
        if(book == null){
            System.out.println("书本不存在");
            System.out.print("编号：");
            book = findByID(sc.nextLine());
        }
        System.out.print("书名：");
        book.setName(sc.nextLine());
        System.out.print("作者：");
        book.setAuthor(sc.nextLine());
        System.out.print("价格：");
        book.setPrice(sc.nextFloat());
        sc.nextLine();
        System.out.println("修改成功");
    }
    static public void println(){
        for (Book book:bookList) {
            System.out.println(book);
        }
    }
}
public class Test03 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true){
            System.out.println("=======================================");
            System.out.println("1 添加图书\n" +
                    "2 查询图书，显示所有图书信息\n" +
                    "3 根据书名，查询单本图书信息\n" +
                    "4 删除图书，通过编号删除\n" +
                    "5 修改图书的信息\n" +
                    "6 退出系统，结束程序运行。");
            System.out.println("=======================================");
            System.out.print("请输入编号：");
            int n = sc.nextInt();
            // 消化换行符
            sc.nextLine();
            switch (n){
                case 1:
                    Books.add();
                    break;
                case 2:
                    Books.println();
                    break;
                case 3:
                    Book book =  Books.findByName();
                    if(book!=null){
                        System.out.println(book);
                    }else {
                        System.out.println("图书不存在");
                    }
                    break;
                case 4:
                    Books.remove();
                    break;
                case 5:
                    Books.update();
                    break;
                case 6:
                    System.exit(0);
                    break;
            }
        }

    }
}
