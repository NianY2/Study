package Test03;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class  Student{
    private String stuNo;
    private String stuName;
    private  String college;
    private  String speciality;
    private  String stuSex;
    private  String stuPhone;
    private  String QQ;
    private  String weChat;

    public Student() { }

    public Student(String stuNo, String stuName, String college, String speciality, String stuSex, String stuPhone, String QQ, String weChat) {
        this.stuNo = stuNo;
        this.stuName = stuName;
        this.college = college;
        this.speciality = speciality;
        this.stuSex = stuSex;
        this.stuPhone = stuPhone;
        this.QQ = QQ;
        this.weChat = weChat;
    }

    public String getStuNo() {
        return stuNo;
    }

    public void setStuNo(String stuNo) {
        this.stuNo = stuNo;
    }

    public String getStuName() {
        return stuName;
    }

    public void setStuName(String stuName) {
        this.stuName = stuName;
    }

    public String getCollege() {
        return college;
    }

    public void setCollege(String college) {
        this.college = college;
    }

    public String getSpeciality() {
        return speciality;
    }

    public void setSpeciality(String speciality) {
        this.speciality = speciality;
    }

    public String getStuSex() {
        return stuSex;
    }

    public void setStuSex(String stuSex) {
        this.stuSex = stuSex;
    }

    public String getStuPhone() {
        return stuPhone;
    }

    public void setStuPhone(String stuPhone) {
        this.stuPhone = stuPhone;
    }

    public String getQQ() {
        return QQ;
    }

    public void setQQ(String QQ) {
        this.QQ = QQ;
    }

    public String getWeChat() {
        return weChat;
    }

    public void setWeChat(String weChat) {
        this.weChat = weChat;
    }
}

class  StudentInfo{
    private Map<String,Student> studentMap = new HashMap<>();
    public void  add(Student student){
        studentMap.put(student.getStuNo(),student);
    }
    public Student  get(String stuNo){
        return studentMap.get(stuNo);
    }
    public  void  delete(String stuNo){
        studentMap.remove(stuNo);
    }
    public  void  update(String stuNo,Student student){
        studentMap.put(stuNo,student);
    }
    public  List<Student>  all(){
        return  new ArrayList(this.studentMap.entrySet());
    }
    public  void printTable(){
        for (Student student:studentMap.values()){
            System.out.println(student.getStuNo()+"\t"+student.getStuName()+"\t"+student.getCollege()+"\t"+
                    student.getSpeciality()+"\t"+student.getStuSex()+"\t"+student.getStuPhone()+"\t"+student.getQQ()+"\t"+student.getWeChat());
        }
    }
}

public class Test02 {
    public static void main(String[] args) {
        StudentInfo studentInfo = new StudentInfo();
        System.out.println("增加");
        studentInfo.add(new Student("202212390606","陈煜","现代信息产业学院","软件工程","男","16607512918","1871263099","CY1871263099"));
        studentInfo.add(new Student("202212390001","CY2","现代信息产业学院","软件工程","男","16607512918","1871263099","CY1871263099"));
        studentInfo.add(new Student("202212390002","CY3","现代信息产业学院","软件工程","男","16607512918","1871263099","CY1871263099"));
        studentInfo.printTable();

        System.out.println("\n删除");
        studentInfo.delete("202212390001");
        studentInfo.printTable();

        System.out.println("\n修改");
        Student student2 =  studentInfo.get("202212390002");

        student2.setStuName("名字修改了");
        studentInfo.update("202212390002",student2);
        studentInfo.printTable();

        System.out.println("\n查");
        Student student1 =  studentInfo.get("202212390606");
        System.out.println(student1.getStuNo()+"\t"+student1.getStuName());


    }
}
