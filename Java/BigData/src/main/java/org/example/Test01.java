package org.example;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.*;

import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;

public class Test01 {
    public static void main(String[] args) throws IOException {
        Configuration conf = new Configuration();
        conf.set("fs.defaultFS","hdfs://192.168.111.131:9000");
        conf.set("fs.hdfs.impl","org.apache.hadoop.hdfs.DistributedFileSystem");
        FileSystem fs = FileSystem.get(conf);
        Path file = new Path(".");

        RemoteIterator<LocatedFileStatus> files = fs.listFiles(new Path("/"), true);
        while (files.hasNext()) {
            FileStatus fileStatus = files.next();
            System.out.println(fileStatus.getPath().toString());
        }
//        BufferedReader d = new BufferedReader(new InputStreamReader(getIt));
//        String content = d.readLine(); //读取文件一行
//        System.out.println(content);
//        d.close(); //关闭文件
        fs.close(); //关闭hdfs
    }
}
