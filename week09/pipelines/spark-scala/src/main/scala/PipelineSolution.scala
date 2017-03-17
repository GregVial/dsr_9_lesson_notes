import org.apache.spark.ml.Pipeline
import org.apache.spark.ml.classification.NaiveBayes
import org.apache.spark.ml.feature.{CountVectorizer, RegexTokenizer, StopWordsRemover, StringIndexer}

/**
  * Created by pawel on 12.03.17.
  */
object PipelineSolution {
  def createPipeline() = {

    val tokenizer = new RegexTokenizer()
      .setToLowercase(true)
      .setPattern("(?u)\\b\\w\\w+\\b") // default scikit-learn
      .setGaps(false)
      .setInputCol("description")
      .setOutputCol("rawTokens")

    val stopWordsRemover = new StopWordsRemover()
      .setInputCol("rawTokens")
      .setOutputCol("tokens")
    stopWordsRemover.setStopWords(stopWordsRemover.getStopWords)

    val countVectorizer = new CountVectorizer()
      .setVocabSize(5000)
      .setMinDF(10)
      .setInputCol("tokens")
      .setOutputCol("features")

    val stringindexer = new StringIndexer()
      .setInputCol("industry")
      .setOutputCol("label")

    val nb = new NaiveBayes()

    val pipeline = new Pipeline()
      .setStages(Array(tokenizer, stopWordsRemover, countVectorizer, stringindexer, nb))

    pipeline
  }
}
