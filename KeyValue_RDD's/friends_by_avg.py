from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("FriendsByAge")
sc = SparkContext(conf = conf)

def parseLine(line):
    fields = line.split(',')
    age = int(fields[2])
    numFriends = int(fields[3])
    return(age, numFriends)

Lines = sc.textFile("file:///SparkCourse/fakefriends.xls")
rdd = Lines.map(parseLine)
totalsByAge = rdd.mapValues(lambda x: (x, 1)).reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))
avergeByAge = totalsByAge.mapValues(lambda x: x[0] / x[1])
results = avergeByAge.collect()
for result in results:
    print(result)