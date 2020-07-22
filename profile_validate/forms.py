from django import forms
from .models import UserBase, CheckStatus, UserStatus

class DoneForm(forms.ModelForm):
    confirmed = forms.CharField(required=False)
    denied = forms.CharField(required=False)
    class Meta:
        model = CheckStatus
        fields = ['confirmed', 'denied']

REASON_CHOICES = [(1, '실물인증 실패'),
                  (2, '얼굴확인 불가'),
                  (3, '영상 오류')]

class NoFilterDoneForm(forms.ModelForm):

    class Meta:
        model = UserStatus
        fields = ['reason']
        reason = forms.IntegerField(required=False, widget=forms.RadioSelect(choices=REASON_CHOICES))


class paperDetailDoneForm(forms.Form):
    btn = forms.CharField()