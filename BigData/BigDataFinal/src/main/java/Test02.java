import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

import java.io.IOException;
import java.util.Iterator;


public class Test02 {
    public Test02() {
    }
    public static void main(String[] args) throws Exception {
        // 创建一个Configuration对象，用于配置MapReduce作业
        Configuration conf = new Configuration();
        // 使用GenericOptionsParser解析命令行参数并判断
        String[] otherArgs = (new GenericOptionsParser(conf, args)).getRemainingArgs();
        if(otherArgs.length < 2) {
            System.err.println("Usage: Test02 <in> [<in>...] <out>");
            System.exit(2);
        }
        // 创建一个MapReduce作业实例，并设置作业名称。
        Job job = Job.getInstance(conf, "Test02");
        //  指定包含作业类的jar文件
        job.setJarByClass(Test02.class);
        //  设置Mapper类。
        job.setMapperClass(Test02.TokenizerMapper.class);
        // 设置Combiner类，Combiner是Map端的一个可选优化步骤，可以减少传输到Reduce端的数据量。
        job.setCombinerClass(Test02.IntSumReducer.class);
        // 设置Reducer类
        job.setReducerClass(Test02.IntSumReducer.class);
        // 设置作业输出键和值的类型。
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        // 为作业添加输入路径。
        FileInputFormat.addInputPath(job, new Path(otherArgs[0]));
        // 设置作业的输出路径。
        FileOutputFormat.setOutputPath(job, new Path(otherArgs[1]));
        // 等待作业完成，并根据作业是否成功来设置退出状态。
        System.exit(job.waitForCompletion(true)?0:1);
    }
    /*
     *定义了一个名为TokenizerMapper的Mapper类，
     * 它继承自Hadoop的Mapper类，
     * 并指定了输入键、输入值、输出键和输出值的类型。
     * 获得每个部门的工资
     * */
    public static class TokenizerMapper extends Mapper<Object, Text, Text, IntWritable> {
        // one用于在map方法中输出计数为1
        private static final IntWritable one = new IntWritable(1);
        // 每个部门
        private Text department = new Text();
        public TokenizerMapper() {
        }
        // 接收输入键值对和上下文对象，
        // 会得到每一行
        public void map(Object key, Text value, Mapper<Object, Text, Text, IntWritable>.Context context) throws IOException, InterruptedException {
            String line_str = value.toString();
            // 过滤标题行和空行
            if(line_str.equals("") || line_str.indexOf("部门") != -1){
                return;
            };
            String[] strs = line_str.split(",");
            this.department.set(strs[0]);
            // 获得工资,删除空格
            int num =  Integer.parseInt(strs[2].trim());
            context.write(this.department, new IntWritable(num));
        }
    }
    /*
     * 定义了一个名为IntSumReducer的Reducer类，
     * 它继承自Hadoop的Reducer类，
     * 并指定了输入键、输入值、输出键和输出值的类型。
     * */
    public static class IntSumReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
        // 存储单词的总计数
        private IntWritable result = new IntWritable();
        public IntSumReducer() {
        }
        // reduce方法，它接收输入键、值的集合和上下文对象
        // 将相同的结果进行相加
        public void reduce(Text key, Iterable<IntWritable> values, Reducer<Text, IntWritable, Text, IntWritable>.Context context) throws IOException, InterruptedException {
            // 遍历值的集合，每个部门的工资。
            int sum = 0;
            IntWritable val;
            for(Iterator i$ = values.iterator(); i$.hasNext(); sum += val.get()) {
                val = (IntWritable)i$.next();
            }
            // 设置结果并输出。
            this.result.set(sum);
            context.write(key, this.result);
        }
    }
}
