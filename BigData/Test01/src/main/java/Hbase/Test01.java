package Hbase;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.*;
import org.apache.hadoop.hbase.client.*;
import org.apache.hadoop.hbase.util.Bytes;
import java.io.IOException;


public class Test01 {
    public static Configuration configuration;
    public static Connection connection;
    public static Admin admin;

    public static void main(String[] args) throws IOException {
        init();
        insertData("Student","scofeld","Score","English","55");
        insertData("Student","scofeld","Score","Math","89");
        insertData("Student","scofeld","Score","Computer","100");
        getData("Student","scofeld","Score","Computer");
        close();
    }


    public static void init(){
        System.setProperty("HADOOP_USER_NAME","hadoop");
        configuration  = HBaseConfiguration.create();
        configuration.set("hbase.zookeeper.quorum", "192.168.111.135");
        configuration.set("hbase.zookeeper.property.clientPort", "2181");
        configuration.set("hbase.rootdir","hdfs://192.168.111.135:9000/hbase");
        // 避免乱码问题
        configuration.set("hbase.client.encoding.fallback", "UTF-8");
        try{
            connection = ConnectionFactory.createConnection(configuration);
            admin = connection.getAdmin();
        }catch (IOException e){
            e.printStackTrace();
        }
    }

    public static void insertData(String tableName,String rowKey,String colFamily,String col,String val) throws IOException {
        Table table = connection.getTable(TableName.valueOf(tableName));
        Put put = new Put(rowKey.getBytes());
        put.addColumn(colFamily.getBytes(),col.getBytes(), val.getBytes());
        table.put(put);
        table.close();
    }


    public static void getData(String tableName,String rowKey)throws  IOException{
        Table table = connection.getTable(TableName.valueOf(tableName));
        Get get = new Get(rowKey.getBytes());
        Result result = table.get(get);
        Cell[] cells = result.rawCells();
        System.out.print("行键:"+rowKey);
        for (Cell cell : cells) {
            //获取列名
            String colName = Bytes.toString(cell.getQualifierArray(),cell.getQualifierOffset(),cell.getQualifierLength());
            String value = Bytes.toString(cell.getValueArray(), cell.getValueOffset(), cell.getValueLength());
            System.out.print("\t"+colName+":"+value);
        }
        System.out.println();
        table.close();
    }

    public static void getData(String tableName,String rowKey,String colFamily, String col)throws  IOException{
        Table table = connection.getTable(TableName.valueOf(tableName));
        Get get = new Get(rowKey.getBytes());
        get.addColumn(colFamily.getBytes(),col.getBytes());
        Result result = table.get(get);
        System.out.println(new String(result.getValue(colFamily.getBytes(),col==null?null:col.getBytes())));
        table.close();
    }
    public static void close(){
        try{
            if(admin != null){admin.close();}
            if(null != connection){connection.close();}
        }catch (IOException e){
            e.printStackTrace();
        }
    }
}
