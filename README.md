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

#### Resultado esperado

<div align="center">
<img src="https://github.com/robertomorel/real-time-streaming-data-processing/blob/master/assets/kafka-zookeeper.gif" width="500"/>
</div>

## Projetos 📥

### [Produtor Consumidor](/produtor-consumidor)
- 

### [Produtor Consumidor - MongoDB](/produtor-consumidor-mongodb)
- 

### [Python Kafka](/python-kafka)
- 

## Bibliotecas 📚
* [ Kafka ](https://kafka.apache.org/documentation/)
* [ Spark ](https://spark.apache.org/docs/latest/)
* [ Python ](https://docs.python.org/pt-br/3/)

----------------------------
## Colaboradores 🧤
[ Roberto Bezerra Morel Lopes ](https://www.linkedin.com/in/roberto-morel-6b9065193/)

[ Lucas Martins Belmino ](https://www.linkedin.com/in/)

[ Venicius Gomes Santiago ](https://www.linkedin.com/)