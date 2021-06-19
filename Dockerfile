FROM python:3.8-alpine
ADD srcs/dependencies.txt /deps.txt
ADD requirements.txt /requirements.txt
RUN pip install -r deps.txt
EXPOSE 8000
COPY srcs /app
WORKDIR /app
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
