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
