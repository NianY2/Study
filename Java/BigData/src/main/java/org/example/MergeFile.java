package org.example;

import java.io.IOException;
import java.io.InputStream;
import java.io.PrintStream;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.URL;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.*;
import org.apache.hadoop.hdfs.DistributedFileSystem;


/***
 * 利用FSDataOutputStream和FSDataInputStream合并HDFS中的文件
 */
public class MergeFile {


    public static void main(String[] args) throws IOException, URISyntaxException {
        System.out.println("Compile Over");
        FileSystem fs = FileSystem.get(new URI( "hdfs://192.168.111.131:9000"), new Configuration());

        // 列出根目录下的所有文件和文件夹
        FileStatus[] files =  fs.listStatus(new Path( "/"));
        for (FileStatus f:files){
            System.out.println(f.getPath().toString());
        }
    }
}