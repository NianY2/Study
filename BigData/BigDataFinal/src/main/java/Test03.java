import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.*;
import org.apache.hadoop.hbase.client.*;
import org.apache.hadoop.hbase.filter.CompareFilter;
import org.apache.hadoop.hbase.filter.PrefixFilter;
import org.apache.hadoop.hbase.filter.RowFilter;
import org.apache.hadoop.hbase.filter.SubstringComparator;
import org.apache.hadoop.hbase.util.Bytes;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
/**
  * 学生分数对象
  */
class StudentScore implements Comparable<StudentScore>{
    private String studentId;
    private String studentName;
    private String subject;
    private int score;

    public StudentScore(String studentId, String studentName, String subject, int score) {
        this.studentId = studentId;
        this.studentName = studentName;
        this.subject = subject;
        this.score = score;
    }

    @Override
    public String toString() {
        return "StudentScore{" +
                "学号='" + studentId + '\'' +
                ", 姓名='" + studentName + '\'' +
                ", 科目='" + subject + '\'' +
                ", 分数=" + score +
                '}';
    }

    @Override
    public int compareTo(StudentScore o) {
        return   o.score - this.score;

    }
}
public class Test03 {
    public static Configuration configuration;
    public static Connection connection;
    public static Admin admin;

    public static void init(){
        System.setProperty("HADOOP_USER_NAME","hadoop");
        configuration  = HBaseConfiguration.create();
        // IP 需要修改
        configuration.set("hbase.zookeeper.quorum", "192.168.111.135");
        configuration.set("hbase.zookeeper.property.clientPort", "2181");
        // IP 需要修改
        configuration.set("hbase.rootdir","hdfs://192.168.111.135:9000/hbase");
        try{
            connection = ConnectionFactory.createConnection(configuration);
            admin = connection.getAdmin();
        }catch (IOException e){
            e.printStackTrace();
        }
    }

    /*
     * 打印所有表名称
     * */
    public static  void  tableListPrint() throws IOException {
        TableName[] tableNames = admin.listTableNames();
        for(TableName tableName : tableNames){
            System.out.println(tableName.getNameAsString());
        }
    }


    public static void close(){
        try{
            if(admin != null){admin.close();}
            if(null != connection){connection.close();}
        }catch (IOException e){
            e.printStackTrace();
        }
    }
    /*
    * - RowKey: {student_id}-{subject}（如 1001-Math）。
    * - 列族: info。
    * - 列名: name（姓名）、score（分数）。
    * 查询所有学生的 Math 成绩，并按分数从高到低排序。
    * */
    public static void queryMathScore() throws IOException {
        Table table = connection.getTable(TableName.valueOf("student_scores"));
        Scan scan = new Scan();
        /*
        * 过滤RowKey包含"Math"的行
        * CompareFilter.CompareOp.EQUAL
        *    EQUAL: 列的值必须等于给定的值。
        *    NOT_EQUAL: 列的值不能等于给定的值。
        *    GREATER: 列的值必须大于给定的值。
        *    GREATER_OR_EQUAL: 列的值必须大于或等于给定的值。
        *    LESS: 列的值必须小于给定的值。
        *    LESS_OR_EQUAL: 列的值必须小于或等于给定的值。
        * */
        scan.setFilter(new RowFilter(CompareFilter.CompareOp.EQUAL, new SubstringComparator("Math")));
        ResultScanner rs = table.getScanner(scan);
        List<StudentScore> students  =  new ArrayList<>();
        for(Result r : rs){
            String rowKey = Bytes.toString(r.getRow());
            String studentId = rowKey.split("-")[0];
            String studentName = Bytes.toString(r.getValue(Bytes.toBytes("info"), Bytes.toBytes("name")));
            String subject = rowKey.split("-")[1];
            int score = Integer.parseInt(Bytes.toString(r.getValue(Bytes.toBytes("info"), Bytes.toBytes("score"))));
            students.add(new StudentScore(studentId, studentName, subject, score));

        }
        students.sort(StudentScore::compareTo);
        students.forEach(System.out::println);
    }

    public static void main(String[] args) throws IOException {
        init();
        queryMathScore();
        close();
    }
}

