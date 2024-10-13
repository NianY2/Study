package hdfs;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.*;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Test01 {
//    /*  输出某个目录的目录或文件 */
//    public  static  void  lsDir(Configuration conf, String remoteDir) throws IOException{
//        FileSystem fs = FileSystem.get(conf);
//        Path file = new Path(remoteDir);
//        FileStatus[] fileStatuses = fs.listStatus(file);
//        for (FileStatus fileStatus : fileStatuses){
//            System.out.println(fileStatus.getPath());
//        }
//        fs.close();
//    }
//
//    /* 验证文件是否存在 */
//    public  static  boolean exists(Configuration conf, String path) throws IOException  {
//        FileSystem fs = FileSystem.get(conf);
//        boolean flag = fs.exists(new Path(path));
//        fs.close();
//        return flag;
//    }
//
//
//    /*  创建文件夹 */
//    public  static  boolean mkdir(Configuration conf, String remoteDir) throws IOException {
//        FileSystem fs = FileSystem.get(conf);
//        Path dirPath = new Path(remoteDir);
//        boolean result = fs.mkdirs(dirPath);
//        fs.close();
//        return result;
//    }
//
//    /* 创建文件 */
//    public static void touchz(Configuration conf, String remoteFilePath) throws IOException {
//        FileSystem fs = FileSystem.get(conf);
//        Path remotePath = new Path(remoteFilePath);
//        FSDataOutputStream outputStream = fs.create(remotePath);
//        outputStream.close();
//        fs.close();
//    }


    public static void main(String[] args) throws IOException {
        Configuration conf = new Configuration();
//        设置用户名
        System.setProperty("HADOOP_USER_NAME","hadoop");
        conf.set("fs.defaultFS","hdfs://localhost:9000");
        conf.set("fs.hdfs.impl","org.apache.hadoop.hdfs.DistributedFileSystem");
//        列出根目录下的所有文件和文件夹
        FileSystem fs = FileSystem.get(conf);
        Path file = new Path("/");
        FileStatus[] fileStatuses = fs.listStatus(file);
        for (FileStatus fileStatus : fileStatuses){
            System.out.println(fileStatus.getPath());
        }
//        创建一个新的文件 test.txt 在HDFS的 /user/hadoop/test 目录下（如果目录不存在，则先创建目录）。
        Path dirPath = new Path("/user/hadoop/test");
        if(!fs.exists(dirPath)){
            fs.mkdirs(dirPath);
        }
        Path remotePath = new Path("/user/hadoop/test/test.txt");
        FSDataOutputStream outputStream = fs.create(remotePath);
        outputStream.close();
//        向 test.txt 文件中写入一段指定的文本内容（如“Hello, HDFS!”）。
        FSDataOutputStream outputStream2 = fs.create(remotePath);
        String s = "Hello, HDFS!";
        outputStream2.write(s.getBytes());
        outputStream2.close();
//       读取 test.txt 文件的内容，并打印到控制台。
        FSDataInputStream inputStream = fs.open(remotePath);
        BufferedReader d = new BufferedReader(new InputStreamReader(inputStream));
        String line = null;
        while ((line = d.readLine()) != null)
            System.out.println(line);
//      关闭与HDFS的连接。
        fs.close();
    }
}
