import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.SparkConf;
import org.apache.spark.api.java.function.Function;
import org.apache.spark.api.java.function.PairFunction;
import org.apache.spark.api.java.function.Function2;
import scala.Tuple2;

import java.util.List;
import java.util.Scanner;

public class Test03 {

    static class ProductSale {
        public int product_id;
        public String product_name;
        public int total_sales;

        @Override
        public String toString() {
            return product_id + "\t" + product_name + "\t" + total_sales;
        }
    }

    public static void main(String[] args) {
        // 文件路径
        String logFile = "file:///Desktop/spark_test.txt";
        // SparkConf 对象
        SparkConf conf = new SparkConf().setMaster("local").setAppName("TopNSales");
        // JavaSparkContext对象
        JavaSparkContext sc = new JavaSparkContext(conf);
        // 加载文本文件内容并缓存
        JavaRDD<String> logData = sc.textFile(logFile).cache();

        // 用户输入N值
        Scanner scanner = new Scanner(System.in);
        System.out.println("请输入想要查询的前N个销量最高的商品数目：");
        int topN = scanner.nextInt();
        scanner.close();

        // 将每一行转换为 (product_id, sales) 的键值对，并过滤掉标题行
        JavaPairRDD<Integer, Integer> salesData = logData
                .filter(line -> !line.startsWith("product_id")) // 去除标题行
                .mapToPair(new PairFunction<String, Integer, Integer>() {
                    @Override
                    public Tuple2<Integer, Integer> call(String line) throws Exception {
                        String[] parts = line.split(",");
                        return new Tuple2<>(Integer.parseInt(parts[0].trim()), Integer.parseInt(parts[2].trim()));
                    }
                });

        // 对相同商品ID的销售数量进行累加
        JavaPairRDD<Integer, Integer> totalSales = salesData.reduceByKey(new Function2<Integer, Integer, Integer>() {
            @Override
            public Integer call(Integer v1, Integer v2) throws Exception {
                return v1 + v2;
            }
        });

        // 获取完整的ProductSale对象
        JavaPairRDD<Integer, ProductSale> finalResult = totalSales.mapToPair(
                new PairFunction<Tuple2<Integer, Integer>, Integer, ProductSale>() {
                    @Override
                    public Tuple2<Integer, ProductSale> call(Tuple2<Integer, Integer> tuple) throws Exception {
                        // 假设我们有一个辅助方法可以根据product_id获取product_name
                        // 这里简化处理，直接返回"Unknown"
                        return new Tuple2<>(tuple._1(), new ProductSale());
                    }
                });

        // 重新映射以包含product_name
        JavaPairRDD<Integer, ProductSale> enrichedSales = finalResult.mapToPair(
                new PairFunction<Tuple2<Integer, ProductSale>, Integer, ProductSale>() {
                    @Override
                    public Tuple2<Integer, ProductSale> call(Tuple2<Integer, ProductSale> tuple) throws Exception {
                        ProductSale ps = tuple._2();
                        ps.product_id = tuple._1();
                        ps.total_sales = tuple._2().total_sales;
                        ps.product_name = logData.filter(line -> line.contains("" + tuple._1()))
                                .first().split(",")[1];
                        return tuple;
                    }
                });

        // 找出销量最高的前N个商品
        List<Tuple2<Integer, ProductSale>> topNProducts = enrichedSales
                .sortBy(new Function<Tuple2<Integer, ProductSale>, Integer>() {
                    @Override
                    public Integer call(Tuple2<Integer, ProductSale> tuple) throws Exception {
                        return -tuple._2().total_sales; // 按照销量降序排序
                    }
                }, true, 1)
                .take(topN);

        // 输出结果
        for (Tuple2<Integer, ProductSale> tuple : topNProducts) {
            System.out.println(tuple._2());
        }

        // 关闭Spark上下文
        sc.close();
    }
}