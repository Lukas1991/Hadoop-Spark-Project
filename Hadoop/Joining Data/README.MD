Part 1г║

Run the Hadoop streaming command:

 hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
   -input /user/cloudera/input \
   -output /user/cloudera/output_join \   
   -mapper /home/cloudera/join1_mapper.py \   
   -reducer /home/cloudera/join1_reducer.py

Part2:

First generate some datasets using the scripts as follows:

1
> sh make_data_join2.txt
(this is a script that produces 6 files:

python make_join2data.py y 1000 13 > join2_gennumA.txt

python make_join2data.py y 2000 17 > join2_gennumB.txt

бн)

2. Use HDFS commands to copy the 6 files created in step 1 into one HDFS directory, 
   just like step 2 in Part 1 and in the wordcount assignment.

3. Run the Hadoop streaming command just like the above.