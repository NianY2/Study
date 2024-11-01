package management.Person;

public class Teacher extends  Person{
    private String num;
    private String research_office;

    public Teacher() { }

    public Teacher(String name, int age, String collage, String major, String num, String research_office) {
        super(name, age, collage, major);
        this.num = num;
        this.research_office = research_office;
    }

    public void  study(){
        System.out.println("学习");
    }

    public String getNum() {
        return num;
    }

    public void setNum(String num) {
        this.num = num;
    }

    public String getResearch_office() {
        return research_office;
    }

    public void setResearch_office(String research_office) {
        this.research_office = research_office;
    }
}
