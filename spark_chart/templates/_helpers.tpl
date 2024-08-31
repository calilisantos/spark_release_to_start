{{/*
Create the common deployments containers specifications
*/}}
{{- define "spark_chart.commonContainerSpecs" -}}
env:
  - name: PATH
    value: "/opt/spark/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
command: ["/bin/bash", "-c"]
args:
  - |
    echo [INFO] Source code
    cat /app/features.py
    spark-submit --version
    spark-submit /app/features.py
    tail -f /dev/null
{{- end }}
