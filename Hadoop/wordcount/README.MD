
Type in the following to open a text editor, and then cut and paste the above lines for wordcount_mapper.py into the text editor, save, and exit. Repeat for wordcount_reducer.py

> gedit wordcount_mapper.py

> gedit wordcount_reducer.py

Enter the following to see that the indentations line up as above

> more wordcount_mapper.py

> more wordcount_reducer.py

Enter the following to make it executable

> chmod +x wordcount_mapper.py

> chmod +x wordcount_reducer.py

Enter the following to see what directory you are in

> pwd

It should be /user/cloudera , or something like that.

3. Create some data:

> echo "A long time ago in a galaxy far far away" > /home/cloudera/testfile1

> echo "Another episode of Star Wars" > /home/cloudera/testfile2

4. Create a directory on the HDFS file system (if already exists that¡¯s OK):

hdfs dfs -mkdir /user/cloudera/input

5. Copy the files from local filesystem to the HDFS filesystem:

hdfs dfs -put /home/cloudera/testfile1 /user/cloudera/input

hdfs dfs -put /home/cloudera/testfile2 /user/cloudera/input

6. You can see your files on HDFS

hdfs dfs -ls /user/cloudera/input

7. Run the Hadoop WordCount example with the input and output specified.

Note that your file paths may differ. The ¡®\¡¯ just means the command continues on next line.

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
   -input /user/cloudera/input \
   -output /user/cloudera/output_new \
   -mapper /home/cloudera/wordcount_mapper.py \
   -reducer /home/cloudera/wordcount_reducer.py
Hadoop prints out a whole lot of logging or error information. If it runs you will see something like the following on the screen scroll by:

....

INFO mapreduce.Job: map 0% reduce 0%

INFO mapreduce.Job: map 67% reduce 0%

INFO mapreduce.Job: map 100% reduce 0%

INFO mapreduce.Job: map 100% reduce 100%

INFO mapreduce.Job: Job job_1442937183788_0003 completed successfully

...

8. Check the output file to see the results:

hdfs dfs -cat /user/cloudera/output_new/part-00000

9. View the output directory:

hdfs dfs -ls /user/cloudera/output_new

Look at the files there and check out the contents, e.g.:

hdfs dfs -cat /user/cloudera/output_new/part-00000