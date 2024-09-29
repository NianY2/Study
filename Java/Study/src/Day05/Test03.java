package Day05;

import java.util.ArrayList;
import java.util.Random;

public class Test03 {

    public  static  int lottery(ArrayList<Integer>  bonusList){
        Random rd = new Random();
        return  bonusList.remove(rd.nextInt(bonusList.size()));
    }

    public static void main(String[] args) {
        int[] bonus = {2,588,888,1000,10000};
        ArrayList<Integer> bonusList = new ArrayList<>();
        for(var i:bonus){
            bonusList.add(i);
        }
        while (bonusList.size() != 0){
            System.out.println(lottery(bonusList) +"元的奖金被抽出");
        }
    }
}
