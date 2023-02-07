FROM python:3.10-alpine
WORKDIR /app
COPY . .
RUN apk add --update make && make pip
EXPOSE 8000
ENV PYTHONPATH=/app/src/refactoring_service
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]
