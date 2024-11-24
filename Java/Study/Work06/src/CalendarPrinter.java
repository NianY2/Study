import java.time.DayOfWeek;
import java.time.LocalDate;
import java.util.Scanner;

public class CalendarPrinter {
    public  static  void printCalendarTitle(int year,int month){
        System.out.println("--------------------------");
        System.out.println("********"+year+"年"+month+"月"+"********");
        System.out.println("--------------------------");
        System.out.println("一\t二\t三\t四\t五\t六\t七");
    }
    public  static void printCalendarBody(LocalDate localDate){
        DayOfWeek dayOfWeek = localDate.getDayOfWeek();
        int monthDays = localDate.lengthOfMonth();
        int firstDay = dayOfWeek.getValue();
        for (int i = 1; i < firstDay; i++) {
            System.out.print("\t");
        }
        for (int i = 1; i <= monthDays; i++) {
            System.out.print(i+"\t");
            firstDay+=1;
            if(firstDay%8==0){
                firstDay=1;
                System.out.println();
            }
        }
    }
    public static void printCalendar(int year,int month){
        LocalDate localDate = LocalDate.of(year,month,1);
        printCalendarTitle(year,month);
        printCalendarBody(localDate);
    }
    public static void main(String[] args) {
        while (true){
            Scanner sc = new Scanner(System.in);
            System.out.print("请输入年份：");
            int year =  sc.nextInt();
            System.out.print("请输入月份（1~~12）：");
            int month = sc.nextInt();
            try {
                printCalendar(year,month);
                break;
            }catch (Exception e){
                System.out.println("月份输入错误,请重新输入");
            }
        }
    }
}
