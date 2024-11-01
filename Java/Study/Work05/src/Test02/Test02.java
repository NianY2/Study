package Test02;

public class Test02 {
    public static void main(String[] args) {
        Graduate graduate = new Graduate("zhangsan",9999,100);
        graduate.isLoan();
        Graduate graduate2 = new Graduate("zhangsan",9999,1000000000);
        graduate2.isLoan();
    }
}
