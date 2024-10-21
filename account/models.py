from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # 여기에 추가 필드를 정의할 수 있습니다.
    # 예: bio = models.TextField(blank=True)
    
    def __str__(self):
        return self.username