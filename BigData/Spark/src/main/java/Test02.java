import org.apache.spark.api.java.*;
import org.apache.spark.api.java.function.Function;
import org.apache.spark.SparkConf;
import org.apache.spark.api.java.function.PairFunction;
import org.apache.spark.api.java.function.Function2;
import scala.Serializable;
import scala.Tuple2;
import java.util.Scanner;

public class Test02 {
    /*
    * Serializable
    * 标记一个类可以被序列化，
    * 即可以将其状态转换为字节流，
    * 以便进行持久化存储或在网络上传输
    * */
    static  class  Product implements Serializable{
        int product_id;
        String product_name;
        int quantity;

        @Override
        public String toString() {
            return  String.format("%-10s %-20s %-10s", product_id, product_name, quantity);
        }
    }
    public static void main(String[] args) {
        // 文件路径
        // 获取用户的主目录并构建绝对路径
        String userHome = System.getProperty("user.home");
        String logFile = "file://" + userHome + "/Desktop/spark_test.txt";
//        String logFile = "file:///Desktop/spark_test.txt";
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
        JavaPairRDD<Integer, Product> productRDD = linesRDD.filter(new Function<String, Boolean>() {
            public Boolean call(String line) {
                return !line.contains("product_id");
            }
        }).mapToPair(new PairFunction<String, Integer, Product>(){
            @Override
            public Tuple2<Integer, Product> call(String line) throws Exception {
                String[] fields = line.split(", ");
                Product product = new Product();
                product.product_id = Integer.parseInt(fields[0]);
                product.product_name = fields[1].replace("\"", "");
                product.quantity = Integer.parseInt(fields[2]);
                return new Tuple2<Integer, Product>(product.product_id, product);
            }
        });

        System.out.printf("%-10s %-20s %-10s%n", "product_id", "product_name", "total_sales");
        productRDD.foreach(tuple -> {
            Product value = tuple._2;
            System.out.println(value);
        });
        System.out.println("------------------------------------");

        /*
        * 合并同一商品的数量
        * */
        JavaPairRDD<Integer, Product> productRDD2 = productRDD.reduceByKey(new Function2<Product, Product, Product>(){
            @Override
            public Product call(Product product, Product product2) throws Exception {
                product2.quantity += product.quantity;
                return product2;
            }
        });
        // 按照商品id升序排序
        JavaPairRDD<Integer, Product> fourproductRankDescRDD = productRDD2.sortByKey(true);

        System.out.printf("%-10s %-20s %-10s%n", "product_id", "product_name", "total_sales");
        fourproductRankDescRDD.foreach(tuple -> {
            Product value = tuple._2;
            System.out.println(value);
        });
        // 将 JavaPairRDD 转换为 JavaRDD<Product>
        JavaRDD<Product> productRDD3 = productRDD2.values();
        // 按照 quantity 降序排序
        JavaRDD<Product> sortedByQuantityRDD = productRDD3.sortBy(product -> product.quantity, false, 1);
        Scanner scanner = new Scanner(System.in);
        System.out.print("请输入要显示的前N名商品：");
        int N =  scanner.nextInt();
        System.out.printf("%-10s %-20s %-10s%n", "product_id", "product_name", "total_sales");
        sortedByQuantityRDD.take(N).forEach(product -> System.out.println(product));
    }
}