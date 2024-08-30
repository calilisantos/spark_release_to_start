# Executando o comparativo

> **IMPORTANTE: Todos os comandos devem ser executados na raiz do projeto.
  Logo apõs cloná-lo abra a pasta resultado em seu terminal:**
  ```bash
  cd spark_release_to_start
  ```

## Com docker-compose
* Iniciando containers
```bash
docker-compose up -d
```

* Listando containers
```bash
docker-compose ps
```

* Visualizando logs do container em tempo real ( spark_to_start ou spark_legacy)
```bash
docker-compose logs -f spark_to_start
```

* Acessando terminal de um container ( spark_to_start ou spark_legacy)
```bash
docker exec -it spark_to_start bash
```

* Derrubando containers
```bash
docker-compose down -v
```

## Com kubernetes
>**Tendo o `kubectl` e um cliente kubernetes como o `minikube` instalado**
* Iniciar cliente kubernetes (como o minikube)
```
minikube start --kubernetes-version=v1.23.8 # versão kubernetes recomendada
```

* Criar configmap para mapear código-fonte
```
kubectl create configmap pyspark-config --from-file=features.py
```

* Aplicar deployment
```
kubectl apply -f k8s/deployment.yaml 
```

* Verificar pods criados
```
kubectl get pods
```

* Verificar descrição de um pod
```
kubectl describe pod spark-legacy
```

* Seguir logs da execução de um pod
```
kubectl logs -f spark-to-start
```

## Com helm

* Iniciando projeto com release 3.4.0:
```bash
helm install better-release ./pyspark_chart --dry-run --debug --set env=prod
```

* Iniciando projeto com release 3.2.4:
```bash
helm install good-release ./pyspark_chart --dry-run --debug --set env=prod --set env=dev
```

* Instalando helm: [link](https://helm.sh/docs/intro/install/#from-apt-debianubuntu)

* Iniciando cluster kubernetes com minikube:
```bash
minikube start --kubernetes-version=v1.23.8
```

* Iniciando release do helm:
```bash
helm install --debug --dry-run <nome-da-release> ./<diretorio-do-chart>
```

* Passando values para a release (Com install ou upgrade):
```bash
helm install -f myvals.yaml ./mychart
```

* Passando valores individuais:
```bash
helm install --set key1=val1,key2=val2 ./mychart
```
