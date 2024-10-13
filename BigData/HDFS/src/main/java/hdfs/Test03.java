package hdfs;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.*;

import java.io.IOException;

public class Test03 {
    public static void main(String[] args) throws IOException {
        Configuration conf = new Configuration();
        //  设置用户名（一定要，不然默认用户名是win的用户名）
        System.setProperty("HADOOP_USER_NAME","hadoop");
        // 	IP地址修改成虚拟机的ip
        conf.set("fs.defaultFS","hdfs://localhost:9000");
        conf.set("fs.hdfs.impl","org.apache.hadoop.hdfs.DistributedFileSystem");
        FileSystem fs = FileSystem.get(conf);

        RemoteIterator<LocatedFileStatus> files = fs.listFiles(new Path("/"), true);
        while (files.hasNext()) {
            FileStatus fileStatus = files.next();
            System.out.println(fileStatus.getPath().toString());
        }
        fs.close(); //关闭hdfs
    }
}
