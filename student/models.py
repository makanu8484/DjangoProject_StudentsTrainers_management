from django.db import models


from trainer.models import Trainer


class Student(models.Model):

    gender_options = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    first_name = models.CharField(max_length=50)              # puteti stoca maxim 255 de caractere;
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    description = models.TextField(max_length=400)            # numar nelimitat de caractere;
    active = models.BooleanField(default=True)
    start_date = models.DateField()
    end_date = models.DateField()
    gender = models.CharField(choices=gender_options, max_length=1)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True)
     #campuri auxiliare;
    created_at = models.DateTimeField(auto_now_add=True)      # stocam data si ora curenta iar informatia NU va mai fi schimbata;
    updated_at = models.DateTimeField(auto_now=True)          # stocam data si ora. Valoarea va fi schimbata de fiecare data
                                                              # cand actualizati informatiile pentru studentul respectiv;


    def __str__(self):
        return f'{self.first_name} {self.last_name}'



# PENTRU ORICE MODIFICARE/STERFGE(COMENTAREA UNUI MODEL) TREBUIE
# SA RULATI CELE DOUA COMENZI PENTRU A SINCRONIZA BAZA DE DATE CU NOI MODIFICARI

# python manage.py makemigrations
# python manage.py migrate
