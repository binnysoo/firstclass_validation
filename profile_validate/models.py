from django.db import models
from django.utils import timezone

# Create your models here.
class UserBase(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    sex = models.CharField(max_length=200)  # M or W
    device = models.CharField(max_length=200)  # Android or iOS
    age = models.SmallIntegerField()
    blind = models.BooleanField(default=False)
    coin = models.IntegerField(default=0)
    birth = models.DateField(auto_now_add=True)
    joined_type = models.CharField(max_length=200)
    joined_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.name


class UserImage(models.Model):
   user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
   title = models.BooleanField(default=False)       #프로필사진
   noFilter = models.BooleanField(default=False)    #쌩얼인증
   image = models.ImageField(blank=True, upload_to='image/')
   validate = models.BooleanField(default=False)


# TODO Q. 비디오는 실물인증에만 쓰이니까 한 회원당 한 개의 object 만 가지고 있는 것이 맞는지 ??
class UserVideo(models.Model):
   user = models.ForeignKey('UserProfile', on_delete=models.CASCADE) #email
   video = models.FileField(upload_to='videos')
   validate =  models.BooleanField(default=False)


class UserProfile(models.Model):
    AREA_CHOICES = ((0, '서울'), (0, '경기'), (0, '인천'),
                    (1, '강원'),
                    (2, '충북'), (2, '세종'), (2, '충남'), (2, '대전'),
                    (3, '경북'), (3, '대구'), (3, '울산'), (3, '부산'), (3, '경남'),
                    (4, '전북'), (4, '전남'), (4, '광주'),
                    (5, '제주'),
                    (6, '해외'))
    user = models.ForeignKey('UserBase', on_delete=models.CASCADE)  # email
    nick = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    area = models.IntegerField(choices=AREA_CHOICES, default=0)  # 지역 카테고리화
    study = models.CharField(max_length=200)
    height = models.IntegerField()
    body = models.CharField(max_length=200)
    drink = models.CharField(max_length=200)
    smoke = models.CharField(max_length=200)
    religion = models.CharField(max_length=200)
    Character = models.CharField(max_length=200)

    def __str__(self):
       return self.nick


class UserInterview(models.Model):
   user = models.ForeignKey('UserProfile', on_delete=models.CASCADE) #email
   introduce = models.TextField()
   holiday = models.TextField()
   interest = models.TextField()
   trip = models.TextField()

   def __str__(self):
       return self.introduce

class UserMark(models.Model):
   user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)   #email
   type = models.CharField(max_length=200)
   one = models.ImageField(blank=True)
   two = models.ImageField(blank=True)

   def __str__(self):
       return self.type


class UserStatus(models.Model):
    TYPE_CHOICES = [(0, 'basic_profile'), (1, 'profile_photo'), (2, 'paper'),\
                    (3, 'beauty'), (4, 'noFilter')]
    REASON_CHOICES = [(0, '--선택해주세요--'),
                      (1, '실물인증 실패'),
                      (2, '얼굴확인 불가'),
                      (3, '영상 오류')]
    user = models.ForeignKey('UserBase', on_delete=models.CASCADE)
    flag = models.IntegerField(default=0) # 0: 신규, 1: 승인, 2: 반려, 3: 수정, 4: 변경, 5: 보류
    flag_type = models.IntegerField(choices=TYPE_CHOICES, default=0)
    admin = models.CharField(max_length=200, null=True, blank=True)
    reason = models.IntegerField(choices=REASON_CHOICES, default=0)


class CheckStatus(models.Model):
    confirmed = models.CharField(max_length=200)
    denied = models.CharField(max_length=200)


class ValidatedImage(models.Model):
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    title = models.BooleanField(default=False)  # 프로필사진
    noFilter = models.BooleanField(default=False)  # 쌩얼인증
    image = models.ImageField(blank=True, upload_to='image/')

class ValidatedVideo(models.Model):
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)  # email
    video = models.FileField(upload_to='videos')

class ValidatedProfile(models.Model):
    AREA_CHOICES = ((0, '서울'), (0, '경기'), (0, '인천'),
                    (1, '강원'),
                    (2, '충북'), (2, '세종'), (2, '충남'), (2, '대전'),
                    (3, '경북'), (3, '대구'), (3, '울산'), (3, '부산'), (3, '경남'),
                    (4, '전북'), (4, '전남'), (4, '광주'),
                    (5, '제주'),
                    (6, '해외'))
    user = models.ForeignKey('UserBase', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    sex = models.CharField(max_length=200)  # M or W
    device = models.CharField(max_length=200)  # Android or iOS
    age = models.SmallIntegerField()
    blind = models.BooleanField(default=False)
    coin = models.IntegerField(default=0)
    birth = models.DateField(auto_now_add=True)
    nick = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    area = models.IntegerField(choices=AREA_CHOICES, default=0)  # 지역 카테고리화
    study = models.CharField(max_length=200)
    height = models.IntegerField()
    body = models.CharField(max_length=200)
    drink = models.CharField(max_length=200)
    smoke = models.CharField(max_length=200)
    religion = models.CharField(max_length=200)
    Character = models.CharField(max_length=200)
    introduce = models.TextField()
    holiday = models.TextField()
    interest = models.TextField()
    trip = models.TextField()

class BeautyScore(models.Model):
    user = models.ForeignKey('UserBase', related_name='receiver', on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    scored_by = models.ForeignKey('UserBase', related_name='giver', on_delete=models.CASCADE)

