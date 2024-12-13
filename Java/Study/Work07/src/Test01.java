import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.Random;
import java.util.TreeSet;

public class Test01 {
    public static void main(String[] args) {
        Random random = new Random();
        TreeSet<Integer> red_ball = new TreeSet<>();
        while(red_ball.size() < 6){
            int n = random.nextInt(33)+1;
            if(!red_ball.contains(n)){
                red_ball.add(n);
            }
        }
        System.out.print("红：");
        red_ball.forEach(ball-> System.out.print(ball+" "));
        System.out.println();
        System.out.print("蓝：");
        System.out.print(random.nextInt(16)+1);
    }
}
