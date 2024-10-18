package Test04.graph;

public class Cuboid extends  Rectangle {
    private double height;

    public Cuboid(double length, double width, double height) {
        super(length, width);
        this.height = height;
    }

    public Cuboid() {}

    @Override
    public double area() {
        return this.height*this.getWidth()*2+
                this.getWidth()*this.getLength()*2+
                this.height*this.getLength()*2;
    }

    @Override
    public double perimeter() {
        return (this.height+this.getWidth()+this.getLength())*4;
    }

    public double volume(){
        return this.height*this.getWidth()*this.getLength();
    }

    public double getHeight() {
        return height;
    }

    public void setHeight(double height) {
        this.height = height;
    }
}
