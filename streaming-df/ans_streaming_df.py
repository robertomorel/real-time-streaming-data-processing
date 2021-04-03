from pyspark.sql import SparkSession
from pyspark.sql.functions import desc, asc
from pyspark.sql.functions import sum

if __name__ == "__main__":
  spark = SparkSession.builder.appName("ANS-Streaming").getOrCreate()

  df = spark.read.json("file:///home/rober/workspace/real-time-streaming-data-processing/streaming-df/mocks/ans.json", multiLine = "true")
  #df.take(3)

  # Qual a média de valor investido nos municípios nos anos de 2010 e 2011?
  df_2010_2011 = df.filter((df["ano"] == "2010") | (df["ano"] == "2011"))  
  valorInvestido = df_2010_2011.select(sum("valor")).withColumnRenamed("sum(valor)", "sum").take(1)[0]["sum"]
  totalRegistros = df_2010_2011.count()
  media = valorInvestido / totalRegistros
  print("A média dos valores investidos entre 2021 e 2011 é de '{}'.".format(media)) 

  # Qual o ID do município do IBGE que recebeu mais aportes, ou seja, mais investimentos ao longo de todos os anos?
  max_aportes = df.groupBy("municipio_ibge") \
                  .sum("valor").withColumnRenamed("sum(valor)", "total_valor") \
                  .sort(desc("total_valor")) \
                  .limit(1).take(1) 
  print("O ID do município do IBGE que recebeu mais aportes é o '{}'.".format(max_aportes[0]["municipio_ibge"]))                

  # Quais os 10 municípios que menos receberam aportes ao longo de todos os anos?
  min_aportes = df.groupBy("municipio_ibge") \
                  .sum("valor").withColumnRenamed("sum(valor)", "total_valor") \
                  .sort(asc("total_valor")) \
                  .select("municipio_ibge") \
                  .limit(10).take(10)

  print("IDs dos 10 municípios que menos receberam aportes:")
  for i in range(len(min_aportes)):
    print("ID: '{}'".format(min_aportes[i]["municipio_ibge"]))

  spark.stop()