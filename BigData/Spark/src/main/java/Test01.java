import org.apache.spark.api.java.*;
import org.apache.spark.api.java.function.Function;
import org.apache.spark.SparkConf;

public class Test01 {
    public static void main(String[] args) {
        // 文件路径
        String logFile = "file:///usr/local/spark/README.md";
        // SparkConf 对象
        // setMaster("local")表示应用程序将在本地模式下运行
        // setAppName("SimpleApp")设置了应用程序的名称为SimpleApp
        SparkConf conf=new SparkConf().setMaster("local").setAppName("SimpleApp");
        // JavaSparkContext对象，它是与Spark交互的主要入口点。它接收前面创建的SparkConf对象作为参数
        JavaSparkContext sc=new JavaSparkContext(conf);
        // sc.textFile(logFile)加载文本文件内容
        // .cache()方法会将此RDD缓存起来以便后续重复使用时能更快访问
        JavaRDD<String> logData = sc.textFile(logFile).cache();
        // 通过filter方法对logData中的每一行执行过滤
        // 只保留包含字符'a'的那些行
        // count()方法统计符合条件的元素数量
        long numAs = logData.filter(new Function<String, Boolean>() {
            public Boolean call(String s) { return s.contains("a"); }
        }).count();
        long numBs = logData.filter(new Function<String, Boolean>() {
            public Boolean call(String s) { return s.contains("b"); }
        }).count();
        System.out.println("Lines with a: " + numAs + ", lines with b: " + numBs);
    }
}