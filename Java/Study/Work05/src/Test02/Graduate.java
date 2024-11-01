package Test02;

public class Graduate implements StudentManageInterface,TeacherManageInterface{
    private  float free;
    private  float pay;
    private  String name;

    public Graduate( String name,float free, float pay) {
        this.free = free;
        this.pay = pay;
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Graduate() { }

    public boolean isLoan(){
        if(free > pay){
            System.out.println("provide a loan");
            return true;
        }else {
            System.out.println("don’t need a loan");
            return false;
        }
    }

    @Override
    public float getFree() {
        return free;
    }

    @Override
    public void setFree(float free) {
        this.free = free;
    }

    @Override
    public float gePay() {
        return pay;
    }

    @Override
    public void setPay(float pay) {
        this.pay = pay;
    }
}
