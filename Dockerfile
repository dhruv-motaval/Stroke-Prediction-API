FROM continuumio/miniconda3

WORKDIR /app

COPY requirements.txt .

RUN conda create -y --name stroke_env python=3.9 && \
    /opt/conda/envs/stroke_env/bin/pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 7860

CMD ["/opt/conda/envs/stroke_env/bin/uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
