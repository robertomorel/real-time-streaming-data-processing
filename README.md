# Streaming de Dados em Tempo Real

## Conceitos ✒️
Também conhecido como Evento de Processamento de Streaming, Streaming de Dados trata do fluxo contínuo de geração de dados à partir de fontes diversas.
Utilizando este tipo de tecnologia, streaming de dados podem ser consumidos, processados, armazenados e analisados conforme estes são gerados em tempo real.

Streaming é o conceito usado para descrever um fluxo contínuo - sem início ou fim - que provê uma contante carga de dados que pode ser utilizada sem a necessidade prévia de download.
Streaming de Dados, de modo semelhante, são gerados por várias fontes e formatos distintos e com volumes variáveis, como por exemplo: aplicações WEB/ERPs; dispositivos de rede; transações bancárias; e dados de localiação (GPS). Todos estes dados poder ser agregados para análise e geração de informação.  

### Como funciona?
"Dados modernos" são gerados por uma infinidade de dispositivos distintos e, considerando estudos como Internet das Coisas, esta questão torna-se exponencial. Deste modo, se torna praticamente impossível a regulamentação ou padronização de estrutura de dados, visando controle de volume e frequência na geração dos dados. 

Aplicações que analisam dados por streaming precisam processá-los individualmente ou por conjunto - segundo regras propostas - e em ordem sequencial. Deixando implícita a relevância destes sistemas serem preparados para tolerância à falhas. Cada parcela de dados gerada tratá sua fonte origem e timestamp, para habilitar aplicações a trabalharem corretamento com o streaming.

#### Funções principais:
- Storage (armazenamento): deve ser capaz de gravar grandes conjuntos de streaming de dadosde modo sequencial e consistente;
- Processing (processamento): deve interagir com o storage, consumir, analisar e rodar lógicas computacionais em cima dos dados.

### Principais desafios:
Para o usuário final, o streaming de dados em tempo real precisa ter tanta qualidade quanto qualquer sistema rodando em batch, com dados já previamente armazenados em disco, cache ou DB. Para tanto, alguns aspectos da aplicação devem ser reconhecidos como obrigatórios.
- Escalabilidade

    - Um exemplo muito prático, é que à medida que falhas acontecem, a quantidade de dados de log podem passar de kilobits para gigabits/seg. Esta exponencialidade exige que a infraestrutura como um todo cresça e se adapte instatâneamente para que não hava nenhum sentido de perda de dados. 

- Ordenação

    - Parte não trivial para streaming em tempo real, principalmente porquê nem sempre a ordem dos dados que é enviada de uma fonte é a mesma ordem que chega ao destino.

- Consistência e durabilidade

    - Também um dos grandes desafios, considerando que qualquer dado gerado à qualquer hora ou volume, pode ser modificado, transferido para outro DC e enviado ao destino em outra parte do mundo.

- Tolerância à falhas e garantias de dados

    - Com dados vindos de inúmeras fontes, localizações, formatos e volumes, o sistema realmente está preparado para prevenir perturbações de um único ponto de falha? 

## KAFKA CLI 🔓
O Apache Kafka veio como uma resposta inteligente e segura aos principais desafios do streaming de dados. 
É um sistema de mensagems distribuídos, com alta vazão e capaz de gerar, analisar e monitorar dados em tempo real. 

Pode ser visto como um sistema de publisher qsubscriber, como o Youtube, mas com mensagens, não vídeos.

> <i>Em resumo, temos os tópicos (streaming específico); as mensagens (associadas a tópicos); producers (geram dados); os consumers (se inscrevem em um ou mais tópicos para consumirem as mensagens); e o Kafka em si (broker que funciona junto ao Zookeeper para gerenciar os tópicos)</i>

### Setup do Kafka
#### 1. Download
```bash
curl http://ftp.unicamp.br/pub/apache/kafka/2.7.0/kafka_2.12-2.7.0.tgz -o ~/Downloads/kafka.tgz
```

#### 2. Criar projeto 
```bash
mkdir kafka
cd kafka
tar -xvzf ~/Downloads/kafka.tgz --strip 1
```

#### 3. Abrir projeto ([VS Code](https://code.visualstudio.com/download))
```bash
code .
```

#### 4. Iniciando Zookeper
```bash
bin/zookeeper-server-start.sh config/zookeeper.properties
```

#### 5. Iniciando Kafka
```bash
bin/kafka-server-start.sh config/server.properties
```

### Exemplo
Utilizando os comandos (CLI) do Apache KAFKA, vamos criar o seguinte esquema de troca de mensagens via streaming de dados

<img src="https://raw.githubusercontent.com/robertomorel/real-time-streaming-data-processing/master/assets/kafka-cli.jpeg" alt="Esquema, Roberto's header" width="500"/>

#### Criando tópicos
- petr4: `bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --topic petr4`
- vale3: `bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --topic vale3`

> Para listar os tópicos existentes: `bin/kafka-topics.sh --list --zookeeper localhost:2181`

#### Criando produtores
- Produtor 1: `bin/kafka-console-producer.sh --broker-list localhost:9092 --topic petr4`
- Produtor 2: `bin/kafka-console-producer.sh --broker-list localhost:9092 --topic vale3`

#### Criando consumidores
- Consumidor 1: `bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic vale3 --from-beginning`
- Consumidor 2: `bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic vale3 --from-beginning`
- Consumidor 3: `bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic petr4 --from-beginning`

<hr>
<b>
  <p align="center">
    RESULTADO ESPERADO
  </p>
</b>

<div align="center">
  <img src="https://github.com/robertomorel/real-time-streaming-data-processing/blob/master/assets/kafka-zookeeper.gif" width="700"/>
</div>

## Projetos 📥

### [Produtor Consumidor](/produtor-consumidor)
Regras:
- No consumidor (classe Consumer) imprima apenas as tuplas que possuem valores de IMC acima de 35 (IMC = peso/altura²);
- Crie um novo produtor (classe Producer2, por exemplo) o qual gera um streaming contendo “nomes” e “salários” aleatórios no intervalo fixo de 4 segundos. Os nomes aleatórios podem ser gerados pela biblioteca Faker utilizada no curso e os salários devem estar no intervalo entre R$ 1.000,00 e R$ 3.000,00;
- Crie um novo consumidor (classe Consumer2, por exemplo) o qual irá consumir os dados do novo produtor criado e imprimir o valor de cada tupla;
- Altere o consumidor recém criado para imprimir apenas o nome das pessoas que recebem salários maiores que R$ 2.000,00;
- Aumente a frequência de geração das tuplas para 2 segundos no Produtor 1 (classe Producer);
- Gere dados simultâneos de dois Produtores da classe Producer e dois produtores da classe Producer2.

#### Para executar
- Inicie o Zookeeper e o Kafka;
- Entre na pasta do projeto;
- Rode o comando:

  ```bash
  python3 producer_consumer.py
  ```

### [Produtor Consumidor - MongoDB](/produtor-consumidor-mongodb)
Regras:
- Inclua na geração de tuplas o nome das pessoas como primeiro atributo. A estrutura do seu arquivo json gerado via streaming será: nome, idade, altura e peso. O nome pode ser gerado pela biblioteca Faker;
- Pesquise como seria para salvar os dados em um banco de dados MySQL ou algum outro banco de dados relacional de sua preferência. Salve nesse banco (via consumidor) apenas as pessoas com nomes que começam com a letra J.

#### Dependência
Necessário o MySQL na máquina, deste modo, recomendamos o uso do docker.

Clique [aqui](https://hub.docker.com/_/mysql) para realizar o setup do MySQL a partir de um container do DockerHub.

#### Para executar
- Inicie o Zookeeper e o Kafka;
- Entre na pasta do projeto;
- Rode o comando:

  ```bash
  python3 producer_consumer_mongodb.py
  ```

### [Python Kafka](/python-kafka)
Regras:
- Implementar uma função em Python (ou na linguagem de sua preferência) que gere linhas aleatórias (por exemplo textos de log, ou de mensagens fake) de 10 em 10 segundos em um arquivo txt denominado source.txt. Em seguida crie um conector, utilizando Kafka, que será responsável por copiar tudo que for gerado no arquivo "source.txt" (pela sua função) para um outro arquivo denominado "destination.txt"

#### Dependência
- Abra o projeto do Kafka no [VS Code](https://code.visualstudio.com/download);
- Altere o arquivo <b>config\connect-file-source.properties</b>
```js
name=local-file-source
connector.class=FileStreamSource
tasks.max=1
file=source.txt
topic=connect-od
```
- Altere o arquivo <b>config\connect-file-sink.properties</b>
```js
name=local-file-sink
connector.class=FileStreamSink
tasks.max=1
file=destination.txt
topics=connect-od
```
- Altere o arquivo <b>config\connect-standalone.properties</b>
```js
bootstrap.servers=localhost:9092
key.converter=org.apache.kafka.connect.json.JsonConverter
value.converter=org.apache.kafka.connect.json.JsonConverter
key.converter.schemas.enable=true
value.converter.schemas.enable=true
```

#### Para executar
- Inicie o Zookeeper e o Kafka;
- Entre na pasta do projeto;
- Ainda no projeto do Kafka, iniciar o Source e o Sink connectors:

  ```bash
  ./bin/connect-standalone.sh config/connect-standalone.properties config/connect-file-source.properties config/connect-file-sink.properties
  ```

- Rode o comando:

  ```bash
  python3 write_on_file.py
  ```

> A aplicação irá escrever no arquivo 'source.txt' de 5 em 5s e o Kafka Connect irá se encarregar de pegar o conteúdo gerado e transferí-lo para o arquivo 'destination.txt'   

<hr>
<b>
  <p align="center">
    RESULTADO ESPERADO
  </p>
</b>

<div align="center">
  <img src="https://github.com/robertomorel/real-time-streaming-data-processing/blob/master/assets/kafka-connector.gif" width="850"/>
</div>

### [Streaming Dataframe](/streaming-df)
Regras:
- Média de valor investido nos municípios nos anos de 2010 e 2011
- ID do município do IBGE que recebeu mais aportes, ou seja, mais investimentos ao longo de todos os anos
- 10 municípios que menos receberam aportes ao longo de todos os anos

#### Criando Ambiente
- Baixando Spark Hadoop

  `wget https://downloads.apache.org/spark/spark-3.1.1/spark-3.1.1-bin-hadoop2.7.tgz ~/Downloads/spark-hadoop.tgz`

- Extrair os arquivos

  `tar -xvzf spark-*`

- Mover os arquivos para o diretório ~ opt/spark

  `sudo mv spark-3.1.1-bin-hadoop2.7 /opt/spark`

##### Variáveis de Ambiente
- Configurando variáveis

  `echo "export SPARK_HOME=/opt/spark" >> ~/.profile`
  
  `echo "export PATH=$PATH:/opt/spark/bin:/opt/spark/sbin" >> ~/.profile`
  
  `echo "export PYSPARK_PYTHON=/usr/bin/python3" >> ~/.profile`

- Testando variáveis

  `source ~/.profile`

##### Iniciando Spark
- Master

  `start-master.sh`

- Trabalhador

  `start-slave.sh spark://posgrad-vm:7077`

- Para finalizar o serviço do spark

  `stop-slave.sh`
  
  `stop-master.sh`  

> Acessar localhost:8080 no navegador e visualizar o Worker ativo:

##### Testando o Spark Shell
- Rodar o comando: 

  `pyspark`

- Para sair

  `exit()`

#### Para executar
- Inicie o Spark Master e Worker;
- Entre na pasta do projeto;
- Rode o comando:

  ```bash
  /opt/spark/bin/spark-submit ans_streaming_df.py
  ```

## Bibliotecas 📚
* [ Kafka ](https://kafka.apache.org/documentation/)
* [ Spark ](https://spark.apache.org/docs/latest/)
* [ Python ](https://docs.python.org/pt-br/3/)

----------------------------
## Colaboradores 🧤
[ Roberto Bezerra Morel Lopes ](https://www.linkedin.com/in/roberto-morel-6b9065193/)

[ Lucas Martins Belmino ](https://www.linkedin.com/in/)

[ Venicius Gomes Santiago ](https://www.linkedin.com/)