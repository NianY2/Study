import org.apache.spark.api.java.*;
import org.apache.spark.api.java.function.Function;
import org.apache.spark.SparkConf;
import org.apache.spark.api.java.function.PairFunction;
import org.apache.spark.api.java.function.Function2;
import scala.Serializable;
import scala.Tuple2;
import java.util.Scanner;

public class Test04 {
    /*
     * Serializable
     * 标记一个类可以被序列化，
     * 即可以将其状态转换为字节流，
     * 以便进行持久化存储或在网络上传输
     * */
    static class CityFee implements Serializable {
        String city;
        float fee;

        @Override
        public String toString() {
            return String.format("%-10s %-10s", city, fee);
        }
    }
    public static void main(String[] args) {
        // 文件路径
        // 获取用户的主目录并构建绝对路径
        String userHome = System.getProperty("user.home");
//        String logFile = "file://" + userHome + "/Desktop/logistics_cy.jar";
//        读HDFS的文件路径
        String logFile = "hdfs://192.168.111.135:9000/user/hadoop/exam/06_logistics_data/logistics_data.txt";
        // SparkConf 对象
        // setMaster("local")表示应用程序将在本地模式下运行
        // setAppName("SimpleApp")设置了应用程序的名称为SimpleApp
        SparkConf conf=new SparkConf().setMaster("local").setAppName("SimpleApp");
        // JavaSparkContext对象，它是与Spark交互的主要入口点。它接收前面创建的SparkConf对象作为参数
        JavaSparkContext sc=new JavaSparkContext(conf);
        // sc.textFile(logFile)加载文本文件内容
        // .cache()方法会将此RDD缓存起来以便后续重复使用时能更快访问
        JavaRDD<String> linesRDD = sc.textFile(logFile).cache();
        /*
         * 按商品分组
         * JavaPairRDD 键值对
         * PairFunction用于定义将输入对象转换为键值对的逻辑
         * filter 方法对linesRDD中的每一行执行过滤(删除标题行)
         * mapToPair 会对每一行进行处理，生成键值对
         * 以product_name做键，Product对象做值
         * */
        JavaPairRDD<String, CityFee> productRDD = linesRDD.filter(new Function<String, Boolean>() {
            public Boolean call(String line) {
                if(line.equals("")){
                    return false;
                }
                return !line.contains("快");
            }
        }).mapToPair(new PairFunction<String, String, CityFee>(){
            @Override
            public Tuple2<String, CityFee> call(String line) throws Exception {
                String[] fields = line.split(", ");
                CityFee cityFee = new CityFee();

                cityFee.city = fields[1];
                cityFee.fee = Float.parseFloat(fields[2]);
                return new Tuple2<String, CityFee>(cityFee.city, cityFee);
            }
        });

        System.out.printf("%-10s %-10s%n", "城市", "费用");
        productRDD.foreach(tuple -> {
            CityFee value = tuple._2;
            System.out.println(value);
        });
        System.out.println("------------------------------------");

        /*
         * 合并同一商品的数量
         * */
        JavaPairRDD<String, CityFee> productRDD2 = productRDD.reduceByKey(new Function2<CityFee, CityFee, CityFee>(){
            @Override
            public CityFee call(CityFee cityFee, CityFee cityFee2) throws Exception {
                cityFee2.fee += cityFee.fee;
                return cityFee2;
            }
        });
        System.out.printf("%-10s %-10s%n", "城市", "费用");
        productRDD2.foreach(tuple -> {
            CityFee value = tuple._2;
            System.out.println(value);
        });
        System.out.println("------------------------------------");
    }
}
