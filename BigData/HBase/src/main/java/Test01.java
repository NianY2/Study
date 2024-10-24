import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.*;
import org.apache.hadoop.hbase.client.*;
import java.io.IOException;

public class Test01 {
    public static Configuration configuration;
    public static Connection connection;
    public static Admin admin;

    public static void init(){
        System.setProperty("HADOOP_USER_NAME","hadoop");
        configuration  = HBaseConfiguration.create();
        configuration.set("hbase.zookeeper.quorum", "192.168.111.135");
        configuration.set("hbase.zookeeper.property.clientPort", "2181");
        configuration.set("hbase.rootdir","hdfs://localhost:9000/hbase");
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


    public static void main(String[] args) throws IOException {
        init();
        tableListPrint();
        close();
    }
}
