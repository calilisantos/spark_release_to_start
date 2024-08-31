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

* Criando chart
```bash
helm create spark_chart
```

* Testando sintaxe do chart
```bash
helm lint spark_chart
```

* Validando manifestos que serão gerados
```bash
helm install spark-release ./spark_chart --dry-run --debug
# ou
helm template spark-release ./spark_chart

* Criando release
```bash
helm install spark-release ./spark_chart

# ou
helm install --debug --dry-run spark-release ./spark_chart
```

* Verificando status de um release
```bash
helm status spark-release
```

* Listando releases
```bash
helm list --all
```

* Atualizando release
```bash
helm upgrade spark-release ./spark_chart
# ou
helm upgrade --debug --dry-run spark-release ./spark_chart
```

* Desinstalando release
```bash
helm uninstall spark-release
```

## Comandos úteis:


* Instalando helm: [link](https://helm.sh/docs/intro/install/#from-apt-debianubuntu)

* Iniciando cluster kubernetes com minikube:
```bash
minikube start --kubernetes-version=v1.23.8
```

* Passando values para a release (Com install ou upgrade):
```bash
helm install -f myvals.yaml ./mychart
```

* Passando valores individuais:
```bash
helm install --set key1=val1,key2=val2 ./mychart
```
