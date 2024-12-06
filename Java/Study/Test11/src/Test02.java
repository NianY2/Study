
import java.util.ArrayList;
import java.util.List;

public class Test02 {
    static  class  Worker{
        private String name;
        private float wages;

        public Worker(String name, float wages) {
            this.name = name;
            this.wages = wages;
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public float getWages() {
            return wages;
        }

        public void setWages(float wages) {
            this.wages = wages;
        }

        @Override
        public String toString() {
            return "Employee{" +
                    "name='" + name + '\'' +
                    ", wages=" + wages +
                    "}";
        }
    }
    public static void main(String[] args) {
//        姓名：张三，工资：3000
//        姓名：李四，工资：3500
//        姓名：王五，工资：4000
//        姓名：赵六，工资：4500
//        姓名：田七，工资：5000
        List<Worker> employeeArray = new ArrayList<Worker>();
        employeeArray.add(new Worker("张三",3000));
        employeeArray.add(new Worker("李四",3500));
        employeeArray.add(new Worker("王五",4000));
        employeeArray.add(new Worker("赵六",4500));
        employeeArray.add(new Worker("田七",5000));

        for (int i = 0; i < employeeArray.size(); i++) {
            Worker employee = employeeArray.get(i);
            if(employee.name.equals("王五")){
                employee.name = "王小五";
            }else if(employee.name.equals("赵六")){
                employeeArray.remove(i);
                i--;
            }else if(employee.name.equals("田七")){
                employee.wages += 500;
            }
        }
        System.out.println(employeeArray);
    }
}
