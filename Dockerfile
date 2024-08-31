# FROM apache/spark-py:v3.4.0
FROM apache/spark-py:v3.2.4

COPY features.py /app/features.py

# Add spark-submit path
ENV PATH="$PATH:/opt/spark/bin"

CMD ["spark-submit", "/app/features.py"]
