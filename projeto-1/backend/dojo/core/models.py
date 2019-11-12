from django.db import models

# Create your models here.


# Model == Tabela do banco
class Joke(models.Model):
    text = models.TextField(verbose_name="Piada")
    batata = "oi"


    def get_best_joke(self):
        # TODO: implement
        print(self.batata)


    def __str__(self):
        return self.text

