# FROM apache/spark-py:v3.4.0
FROM apache/spark-py:v3.2.4

COPY features.py /app/features.py
# COPY old_features.py /app/old_features.py

# Adicione o caminho do spark-submit se necessário
ENV PATH="$PATH:/opt/spark/bin"

CMD ["spark-submit", "/app/features.py"]
# CMD ["spark-submit", "/app/old_features.py"]
