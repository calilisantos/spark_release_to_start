# Boas vindas ao **spark_release_to_start**!

O objetivo é demonstrar features implementadas à partir da release **3.4.0** do Spark que são fundamentais para o uso do framework no contexto da análise de dados.

Aqui você vai encontrar o comparativo da versão **3.4.0** com a **3.2.4** do Spark em diversos contextos de orquestração de containers:

> **IMPORTANTE: Todos os cenários consideram a execução do projeto à partir da raiz do projeto.
>  Logo após cloná-lo abra a pasta resultado em seu terminal:**
>  ```bash
>  cd spark_release_to_start
>  ```

# <a id='topicos'>Tópicos</a>
- [Sobre a release](#release)
- [Executando comparativo](#pre-requisitos)
  - [Com Dockerfile](#dockerfile)
  - [Com docker-compose](#docker-compose)
  - [Com kubernetes](#kubernetes)
  - [Com helm](#helm)
- [Comandos úteis](#comandos-uteis)

## <a id='release'>[Sobre a release](#topicos)</a>
As releases **3.3.0** e **3.4.0** do Spark trouxeram diversas melhorias e correções de bugs.<br/>Pensando no processamento dos dados, os seguintes métodos se destacam:
* **withColumns**: Com a release **3.3.0**, permite a criação de múltiplas colunas em um único comando.
* **isEmpty**: A partir da release **3.3.0**, verifica se o DataFrame está vazio de forma eficiente.
* **withColumnsRenamed**: Da release **3.4.0**, renomeia várias colunas em um único comando.
* **Vários métodos de datas, estatísticos e de string** foram adicionados ou melhorados.

Os 3 primeiros são exemplificados no arquivo [`features.py`](features.py), demonstrando seus comportamentos nas versões **3.2.4** e **3.4.0** do Spark.

Os registros das releases e novidades sobre o Spark podem ser acessados [aqui](https://spark.apache.org/news/index.html)

## <a id='pre-requisitos'>[Executando comparativo](#topicos)</a>
Para reproduzir as instruções abaixo são necessárias as seguintes ferramentas:

| Ferramenta | Versão Utilizada |
| - | - |
| Docker | 25.0.3 |
| docker-compose | 1.29.2 |
| kubectl | 1.23.8 |
| minikube (ou interface kubernetes) | 1.23.8 |
| helm | 3.15.4 |

## <a id='dockerfile'>[Com Dockerfile](#topicos)</a>
É possível executar o projeto com o Dockerfile disponível na raiz do projeto. Para isso, siga os passos a seguir:

![dockerfile gif](docs/dockerfile.gif)

### 1. Comentar/Descomentar a versão do Spark desejada no Dockerfile:
```Dockerfile
# FROM apache/spark-py:v3.4.0
FROM apache/spark-py:v3.2.4

COPY features.py /app/features.py

# Add spark-submit path
ENV PATH="$PATH:/opt/spark/bin"

CMD ["spark-submit", "/app/features.py"]
```

### 2. Construir a imagem:
```bash
docker build -t spark_release . 
```

### 3. Executar a imagem:
```bash
docker run spark_release
 # ou
docker run -it --rm spark_release # para executar em modo interativo
```

### 4. Listar containers:
```bash
docker ps -la
```

### 5. Acessar logs do container:
```bash
docker logs <container_id>
```

### 6. Acessar terminal do container:
```bash
docker exec -it <container_id> bash
```


## <a id='docker-compose'>[Com docker-compose](#topicos)</a>
Com o docker-compose será executado simultaneamente os dois containers com as diferentes versões do Spark. Para isso, siga os passos a seguir:

![docker-compose gif](docs/docker-compose.gif)

* ### Iniciando containers
```bash
docker-compose up -d
```

* ### Listando containers
```bash
docker-compose ps
```

* ### Visualizando logs do container em tempo real ( spark_to_start ou spark_legacy)
```bash
docker-compose logs -f spark_to_start
```

* ### Acessando terminal de um container ( spark_to_start ou spark_legacy)
```bash
docker exec -it spark_to_start bash
```

* ### Derrubando containers
```bash
docker-compose down -v
```

## <a id='kubernetes'>[Com kubernetes](#topicos)</a>
Com as instruções abaixo também é possível executar simultaneamente as duas versões do Spark com seus serviços kubernetes local ou remoto utilizando o [manifesto](k8s/deployment.yaml) e código fonte do repositório.

>**Tendo o `kubectl` e um cliente kubernetes como o `minikube` instalado**
* ### Iniciar cliente kubernetes (como o minikube)
```bash
minikube start --kubernetes-version=v1.23.8 # versão kubernetes recomendada
```

* ### Criar configmap para mapear código-fonte
```bash
kubectl create configmap pyspark-config --from-file=features.py
```

* ### Aplicar deployment
```bash
kubectl apply -f k8s/deployment.yaml 
```

* ### Verificar pods criados
```bash
kubectl get pods
```

* ### Verificar descrição de um pod
```bash
kubectl describe pod spark-legacy
```

* ### Seguir logs da execução de um pod
```bash
kubectl logs -f spark-to-start
```

## <a id='helm'>[Com helm](#topicos)</a>
O helm adiciona uma camada de abstração para a criação de manifestos kubernetes.

[Aqui](spark_chart) você encontra o chart helm criado para a orquestração dos deployments das versões 3.2.4 e 3.4.0 do Spark, com sua execução descrita a seguir:


* ### [NÃO EXECUTE - Ilustrativo] Criando chart
```bash
helm create spark_chart
```

* ### Testando sintaxe do chart
```bash
helm lint spark_chart
```

* ### Validando manifestos que serão gerados
```bash
helm install spark-release ./spark_chart --dry-run --debug
# ou
helm template spark-release ./spark_chart
```

* ### Criando release
```bash
helm install spark-release ./spark_chart

# ou
helm install --debug --dry-run spark-release ./spark_chart
```

* ### Verificando status de um release
```bash
helm status spark-release
```

* ### Listando releases
```bash
helm list --all
```

* ### Atualizando release
```bash
helm upgrade spark-release ./spark_chart
# ou
helm upgrade --debug --dry-run spark-release ./spark_chart
```

* ### Desinstalando release
```bash
helm uninstall spark-release
```

## <a id='comandos-uteis'>[Comandos úteis](#topicos)</a>


* ### Instalando helm: [link](https://helm.sh/docs/intro/install/#from-apt-debianubuntu)

* ### Iniciando cluster kubernetes com minikube:
```bash
minikube start --kubernetes-version=v1.23.8
```

* ### Passando values para a release (Com install ou upgrade):
```bash
helm install -f myvals.yaml ./mychart
```

* ### Sobrescrendo/Setando valores individuais:
```bash
helm install --set key1=val1,key2=val2 ./mychart
```
