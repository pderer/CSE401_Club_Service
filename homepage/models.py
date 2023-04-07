from django.db import models

# Create your models here.
class Notice(models.Model):
    ''' 전체 공지 '''
    title = models.CharField(max_length=200)
    information = models.TextField(default='')
    pub_date = models.DateTimeField('published')
    
    def __str__(self):
        return self.title

class Manual(models.Model):
    ''' 전체 메뉴얼 '''
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('published')
    information = models.TextField(default='')
    
    def __str__(self):
        return self.title

class Club(models.Model):
    ''' 클럽 정보 '''
    name = models.CharField(max_length=200)
    club_type = models.CharField(max_length=200) # "중앙", "자치", "일반"
    category = models.CharField(max_length=200) # "공연", "취미", "스포츠", "공부"
    num_members = models.IntegerField(default=0)
    budget = models.IntegerField(default=0)

    def __str__(self):
        return self.name   

class Calendar(models.Model):
    ''' 클럽 행사 정보 '''
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='calendar')
    title = models.CharField(max_length=200)
    information = models.TextField()
    start_day = models.DateField()
    finish_day = models.DateField()
    
    def __str__(self):
        return self.title
    
class Blog(models.Model):
    ''' 클럽 내부 페이지 '''
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='blog')
    title = models.CharField(max_length=200)
    information = models.TextField()
    update_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    view_count = models.IntegerField(default=0)
    image = models.ImageField(blank=True, upload_to='images/', null=True)
    
    def __str__(self):
        return self.title
    
class List(models.Model):
    ''' 클럽 돈 '''
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='list')
    title = models.CharField(max_length=200)
    information = models.TextField()
    due_date = models.DateField()
    money = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

class User(models.Model):
    user_id = models.CharField(max_length = 32, unique = True, verbose_name='유저 아이디')
    user_pw = models.CharField(max_length = 128, unique = True, verbose_name='유저 비밀번호')
    user_name = models.CharField(max_length = 16, unique = True, verbose_name='유저 이름')
    user_email = models.EmailField(max_length = 128, unique = True, verbose_name='유저 이메일')
    
    def __str__(self):
        return self.user_name
    
    class Meta:
        db_table = 'user'
        verbose_name = '유저'
        verbose_name_plural = '유저'