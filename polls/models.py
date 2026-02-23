from datetime import timezone, datetime
from django.db import models

# Tabela Question
class Question(models.Model):
    # Colunas da tabela Question
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    # Método para retornar uma string quando pedirmos para imprimir um objeto da classe Question
    def __str__(self):
        return f"\nId: # {self.id}\nText: {self.question_text}\nPublication Date: {self.pub_date}\n\n"

    # Método para mostrar as perguntas publicadas recentemente
    def was_published_recently(self):
        # Retorna as linhas que têm um dia de vida
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# Tabela Choice
class Choice(models.Model):
    # Colunas da tabela Choice
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # Método para retornar uma string quando pedirmos para imprimir um objeto da classe Choice
    def __str__(self):
        return self.choice_text