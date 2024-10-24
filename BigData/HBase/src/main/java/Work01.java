import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.*;
import org.apache.hadoop.hbase.client.*;
import org.apache.hadoop.hbase.util.Bytes;
import java.io.IOException;


public class Work01 {
    public static Configuration configuration;
    public static Connection connection;
    public static Admin admin;

    public static void main(String[] args) throws IOException {
        init();
        // 删除表 第一次运行请注释
//        deleteTable("EmployeeRecords");
        tableListPrint();
        createTable("EmployeeRecords",new String[]{"Info","Salary"});
        tableListPrint();
        insertData("EmployeeRecords","606","Info","Name","CY");
        insertData("EmployeeRecords","606","Info","Department","现代信息产业学院");
        insertData("EmployeeRecords","606","Info","Monthly","50000");
        getData("EmployeeRecords","606");
        updateData("EmployeeRecords","606","60000");
        getData("EmployeeRecords","606");
        deleteData("EmployeeRecords","606");
        close();
    }


    public static void init(){
        System.setProperty("HADOOP_USER_NAME","hadoop");
        configuration  = HBaseConfiguration.create();
        configuration.set("hbase.zookeeper.quorum", "192.168.111.135");
        configuration.set("hbase.zookeeper.property.clientPort", "2181");
        configuration.set("hbase.rootdir","hdfs://localhost:9000/hbase");
        // 避免乱码问题
        configuration.set("hbase.client.encoding.fallback", "UTF-8");
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
        System.out.print("所有表:");
        for(TableName tableName : tableNames){
            System.out.print(tableName.getNameAsString() + "\t");
        }
        System.out.println();
    }

    public static void createTable(String myTableName,String[] colFamily) throws IOException {
        TableName tableName = TableName.valueOf(myTableName);
        if(admin.tableExists(tableName)){
            System.out.println("talbe is exists!");
        }else {
            TableDescriptorBuilder tableDescriptor = TableDescriptorBuilder.newBuilder(tableName);
            for(String str:colFamily){
                ColumnFamilyDescriptor family =
                        ColumnFamilyDescriptorBuilder.newBuilder(Bytes.toBytes(str)).build();
                tableDescriptor.setColumnFamily(family);
            }
            admin.createTable(tableDescriptor.build());
        }
    }

    public static void deleteTable(String myTableName) throws IOException {
        TableName tableName = TableName.valueOf(myTableName);
        admin.disableTable(tableName);
        admin.deleteTable(tableName);
    }

    public static void insertData(String tableName,String rowKey,String colFamily,String col,String val) throws IOException {
        Table table = connection.getTable(TableName.valueOf(tableName));
        Put put = new Put(rowKey.getBytes());
        put.addColumn(colFamily.getBytes(),col.getBytes(), val.getBytes());
        table.put(put);
        table.close();
    }

    public static void updateData(String tableName,String rowKey,String val) throws IOException {
        Table table = connection.getTable(TableName.valueOf(tableName));
        Put put = new Put(rowKey.getBytes());
        put.addColumn("Info".getBytes(),"Monthly".getBytes(), val.getBytes());
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

    public static void deleteData(String tableName,String rowKey)throws  IOException{
        Table table = connection.getTable(TableName.valueOf(tableName));
        Delete delete = new Delete(rowKey.getBytes());
        table.delete(delete);
        System.out.println("删除成功");
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
