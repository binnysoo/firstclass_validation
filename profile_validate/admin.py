from django.contrib import admin

# Register your models here.
from .models import UserBase
from .models import UserImage
from .models import UserVideo
from .models import UserInterview
from .models import UserProfile
from .models import UserMark
from .models import UserStatus
from .models import ValidatedImage
from .models import BeautyScore
from .models import ValidatedProfile

admin.site.register(UserBase) #관리자 페이지에서 UserBase 모델을 관리
admin.site.register(UserImage)
admin.site.register(UserVideo)
admin.site.register(UserInterview)
admin.site.register(UserProfile)
admin.site.register(UserMark)
admin.site.register(UserStatus)
admin.site.register(ValidatedImage)
admin.site.register(BeautyScore)
admin.site.register(ValidatedProfile)