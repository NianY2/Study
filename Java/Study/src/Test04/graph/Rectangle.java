package Test04.graph;

public class Rectangle {
    private  double length;
    private  double width;


    public  double area(){
        return this.length*this.width;
    }
    public  double perimeter(){
        return (this.length+this.width)*2;
    }

    public Rectangle(double length, double width) {
        this.length = length;
        this.width = width;
    }

    public Rectangle() {
    }

    public double getLength() {
        return length;
    }

    public void setLength(double length) {
        this.length = length;
    }

    public double getWidth() {
        return width;
    }

    public void setWidth(double width) {
        this.width = width;
    }

}
