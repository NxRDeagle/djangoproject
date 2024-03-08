from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Модель профиля
class Profile(models.Model):
    # Расширяем модель профиля, прявязываем пользователя по связи один к одному, удаление - каскадное
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    
    # аватар пользователя, по умолчанию дефолтная ава, загр. в профиль
    avatar = models.ImageField(default = 'default_user_image.png', upload_to = 'profile_images')

    info = models.TextField()


    # Для объекта профиля возвр. строку с именем данного пользователя
    def __str__(self):
        return self.user.username
    
    # Функция сохранения автарки, если размер превышает 100x100 пикселей, то сжимаем ее
    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.avatar.path)
        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
