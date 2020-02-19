# import datetime

# from django.db import models
# from django.utils import timezone


# class Chat(models.Model):
#     name = models.CharField(max_length=200)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name

# class Post(models.Model):
#     chat = models.ForeignKey(Chat, related_name='posts', on_delete=models.CASCADE, blank=True)
#     language = models.CharField(max_length=20)
#     text = models.CharField(max_length=500)
#     created_at = models.DateTimeField(auto_now_add=True)


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#     def __str__(self):
#         return self.question_text
#     def was_published_recently(self):
#         now = timezone.now()
#         return now - datetime.timedelta(days=1) <= self.pub_date <= now 

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __str__(self):
#         return self.choice_text