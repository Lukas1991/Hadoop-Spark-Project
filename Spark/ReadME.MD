## commands

show_views_file = sc.textFile("/user/cloudera/input/join2_gennum?.txt")

show_views_file.take(2)

show_channel_file = sc.textFile("/user/cloudera/input/join2_genchan?.txt")

show_channel_file.take(2)

show_views = show_views_file.map(split_show_views).reduceByKey(some_function)

show_channel = show_channel_file.map(split_show_channel).reduceByKey(concat_function).flatMap(unique_values)

show_channel.collect()

joined_dataset = show_channel.join(show_views)

joined_dataset.collect()

joined_dist = joined_dataset.distinct()

channel_views = joined_dist.map(extract_channel_views)

channel_views.reduceByKey(some_function).collect()

