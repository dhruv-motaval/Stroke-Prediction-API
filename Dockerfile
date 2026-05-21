# ✅ Use Miniconda as the base image
FROM continuumio/miniconda3

# ✅ Set working directory
WORKDIR /app

# ✅ Copy requirements and model files
COPY requirements.txt .
COPY best_stroke_model.pkl scaler.pkl app.py /app/

# ✅ Create and activate a Conda environment with Python 3.9
RUN conda create --name stroke_env python=3.9 -c conda-forge && \
    conda run -n stroke_env pip install --no-cache-dir -r requirements.txt

# ✅ Set Conda environment as default
SHELL ["/bin/bash", "-c"]

# ✅ Expose the Hugging Face Spaces default port (7860)
EXPOSE 7860

# ✅ Run FastAPI inside the Conda environment
CMD ["conda", "run", "--no-capture-output", "-n", "stroke_env", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
