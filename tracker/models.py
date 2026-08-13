from django.db import models

class Solution(models.Model):
    problem_name = models.CharField(max_length=200)
    language = models.CharField(max_length=50)
    code = models.TextField()
    solved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.problem_name} - {self.language}"