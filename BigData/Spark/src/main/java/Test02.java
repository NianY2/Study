import org.apache.spark.api.java.*;
import org.apache.spark.SparkConf;
import scala.Tuple2;

public class Test02 {
    /**
     * 产品销售记录
     */
    static class ProductSale{
        public  int product_id;
        public  String product_name;
        public  int total_sales;

        @Override
        public String toString() {
            return product_id + "/t/t/t/t"+product_name + "/t/t/t/t"+total_sales;
        }
    }
    public static void main(String[] args) {
        // 文件路径
        String logFile = "file:///Desktop/spark_test.txt";
        // SparkConf 对象
        // setMaster("local")表示应用程序将在本地模式下运行
        // setAppName("SimpleApp")设置了应用程序的名称为SimpleApp
        SparkConf conf=new SparkConf().setMaster("local").setAppName("SimpleApp");
        // JavaSparkContext对象，它是与Spark交互的主要入口点。它接收前面创建的SparkConf对象作为参数
        JavaSparkContext sc=new JavaSparkContext(conf);
        // sc.textFile(logFile)加载文本文件内容
        // .cache()方法会将此RDD缓存起来以便后续重复使用时能更快访问
        JavaRDD<String> logData = sc.textFile(logFile).cache();

        JavaPairRDD<Integer, ProductSale> productSales = logData
                .filter(line -> !line.startsWith("product_id")) // 去除标题行
                .mapToPair(line -> {
                    String[] parts = line.split(",");
                    ProductSale productSale = new ProductSale();
                    productSale.product_id = Integer.parseInt(parts[0].trim());
                    productSale.product_name = parts[1].trim();
                    productSale.total_sales = Integer.parseInt(parts[2].trim());
                    return new Tuple2<>(productSale.product_id, productSale);
                });

    }
}