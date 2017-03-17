import PipelineSolution.createPipeline
import com.typesafe.config.ConfigFactory
import org.apache.spark.ml.evaluation.MulticlassClassificationEvaluator
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions.{col, udf}

import scala.util.Try

/**
  * Created by pawel on 11.03.17.
  */
object App {

  val takeFirstUDF = udf(takeFirst _)

  def takeFirst(x: Seq[String]): String = Try(x.head).getOrElse("")

  def main(args: Array[String]) = {

    val config = ConfigFactory.load()

    val spark = SparkSession.builder
      .appName(s"Spark example")
      .master("local[*]")
      .getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")

    val df = spark.read.json("../notebooks/data/companies/companies.json")
      .select("description", "industries")
      .withColumn("industry", takeFirstUDF(col("industries")))
      .repartition(8)
      .cache

    val Array(dfTr, dfTe) = df.randomSplit(Array(0.7, 0.3))

    val trainingLabels = dfTr
      .rdd.map(row => row.getAs[String]("industry"))
      .collect()

    val dfTeClean = dfTe.filter(col("industry").isin(trainingLabels: _*))

    println(s"Number of observations ${df.count()}")
    println(df.printSchema())

    val pipeline = createPipeline()

    val pipelineFit = pipeline.fit(dfTr)

    val dfTrPred = pipelineFit.transform(dfTr)
    val dfTePred = pipelineFit.transform(dfTeClean)

    val evaluator = new MulticlassClassificationEvaluator()
      .setLabelCol("label")
      .setPredictionCol("prediction")
      .setMetricName("accuracy")

    println(s"Test accuracy: ${evaluator.evaluate(dfTePred)}")
    println(s"Train accuracy: ${evaluator.evaluate(dfTrPred)}")
  }
}
