# SF-Crime-Statistics

1. How did changing values on the SparkSession property parameters affect the throughput and latency of the data?
`processedRowsPerSecond` seems to be the key metric which indicates the streaming throughput of our spark application

2. What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?
The goal was to maximize the throughput by observing `processROwsPerSecond`. The following configurations were chosen:

`spark.sql.shuffle.partitions                10`
Depends on input dataset size and partition size. I had to estimate this by trial and error

`spark.streaming.kafka.maxRatePerPartition   100`
Prevent spark to be overwhelmed with a significant number of unprocessed messages

`spark.default.parallelism                   12`
Good rule of thumb is 3 per CPU core