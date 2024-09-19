# Use a imagem oficial do Python como base
FROM python:3.11-slim

# Crie um diretório para a aplicação
WORKDIR /app

# Copie o arquivo de requisitos e instale as dependências
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código da aplicação
COPY . .

# Defina as variáveis de ambiente
ENV DJANGO_SETTINGS_MODULE=ireApp.settings
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN python manage.py collectstatic --noinput
# Exponha a porta que a API usará
EXPOSE 8000

# Execute o Gunicorn para rodar o servidor
CMD ["gunicorn", "ireApp.wsgi:application", "--bind", "0.0.0.0:8000"]
