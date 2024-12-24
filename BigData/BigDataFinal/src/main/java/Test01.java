import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.*;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Test01 {
    public static void main(String[] args) throws IOException {
        Configuration conf = new Configuration();
//        设置用户名（一定要，不然默认用户名是win的用户名）
        System.setProperty("HADOOP_USER_NAME","hadoop");
        conf.set("fs.defaultFS","hdfs://192.168.111.135:9000");
        conf.set("fs.hdfs.impl","org.apache.hadoop.hdfs.DistributedFileSystem");
//        列出根目录下的所有文件和文件夹
        FileSystem fs = FileSystem.get(conf);
        Path file = new Path("/user/hadoop/exam/06_sales_data/");
        FileStatus[] fileStatuses = fs.listStatus(file);
        for (FileStatus fileStatus : fileStatuses){
            System.out.println(fileStatus.getPath());
        }
        System.out.println("==========================================================================================");
        Path remotePath = new Path("/user/hadoop/exam/06_sales_data/sales_data.txt");
//       读取 sales_data.txt 文件的内容，并打印到控制台。
        FSDataInputStream inputStream = fs.open(remotePath);
        BufferedReader d = new BufferedReader(new InputStreamReader(inputStream));
        String ans = "";
        String line;
        while ((line = d.readLine()) != null)
            ans += line + "\n";
        System.out.print(ans);
//        删除最后一个/n
        ans = ans.substring(0, ans.length() - 1);
        System.out.println("==========================================================================================");
        // 判断目录和文件是否存在，不存在就创建
        Path dirPath = new Path("/user/hadoop/exam/06_sales_data_processed");
        if(!fs.exists(dirPath)){
            fs.mkdirs(dirPath);
        }
        Path remotePath2 = new Path("/user/hadoop/exam/06_sales_data_processed/sales_data.txt");
        FSDataOutputStream outputStream = fs.create(remotePath2);
        outputStream.close();
//        向 sales_data.txt 文件中写入一段指定的文本内容（606，陈煜，123）。
        FSDataOutputStream outputStream2 = fs.create(remotePath2);
        ans += "606, 陈煜, 123\n";
        outputStream2.write(ans.getBytes());
        outputStream2.close();
//        查看 sales_data.txt 文件的内容，并打印到控制台。
        FSDataInputStream inputStream2 = fs.open(remotePath2);
        BufferedReader d2 = new BufferedReader(new InputStreamReader(inputStream2));
        String line2;
        while ((line2 = d2.readLine()) != null)
            System.out.println(line2);
//      关闭与HDFS的连接。
        fs.close();
    }
}

