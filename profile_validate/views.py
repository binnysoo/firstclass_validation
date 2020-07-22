from django.shortcuts import render, redirect, get_object_or_404
from .models import UserBase
from .models import UserInterview
from .models import UserStatus
from .models import UserProfile
from .models import UserImage, UserVideo
from .models import UserMark
from .models import ValidatedImage, ValidatedVideo, ValidatedProfile, BeautyScore
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView
from .forms import DoneForm, NoFilterDoneForm, paperDetailDoneForm
from django.db.models import Count, Max, Sum


def get_BaseStatus(passed, flag_type):
    if passed == False:
        BaseStatus = UserStatus.objects.filter(flag_type=flag_type) \
            .exclude(flag=1).exclude(flag=2).exclude(flag=5).select_related('user')
    else:
        BaseStatus = UserStatus.objects.filter(user__in=passed, flag_type=flag_type) \
            .exclude(flag=1).exclude(flag=2).exclude(flag=5).select_related('user')
    return BaseStatus


def get_BaseList(BaseStatus):
    BaseList = BaseStatus.values_list('user', flat=True)
    return BaseList


def get_imgsDict(BaseList, title, noFilter):
    SelectedImg = UserImage.objects.select_related('user').filter(user__user__in=BaseList, title=title, noFilter=noFilter)
    imgs = SelectedImg.values()
    print("imgs", SelectedImg)
    imgsDict = {}
    for i in range(len(SelectedImg)):
        key = SelectedImg[i].user.user.user.pk
        #print("#", key)
        #imgsDict[imgs[i]['user_id']] = imgsDict.get(imgs[i]['user_id'], []) + [SelectedImg[i]]
        imgsDict[key] = imgsDict.get(key, []) + [SelectedImg[i]]

    return imgsDict


def get_userInfo(BaseStatus, flag_type, passed):
    if passed:
        infoDict = {
            'male': BaseStatus.filter(user__sex='M'),
            'female': BaseStatus.filter(user__sex='F'),
            'male_new': UserStatus.objects.filter(user__in=passed, flag_type=flag_type, flag=0).select_related(
                'user').filter(user__sex="M"),
            'male_edit': UserStatus.objects.filter(user__in=passed, flag_type=flag_type, flag=3).select_related(
                'user').filter(user__sex="M"),
            'male_old': UserStatus.objects.filter(user__in=passed, flag_type=flag_type, flag=4).select_related(
                'user').filter(user__sex="M"),
            'female_new': UserStatus.objects.filter(user__in=passed, flag_type=flag_type, flag=0).select_related(
                'user').filter(user__sex="F"),
            'female_edit': UserStatus.objects.filter(user__in=passed, flag_type=flag_type, flag=3).select_related(
                'user').filter(user__sex="F"),
            'female_old': UserStatus.objects.filter(user__in=passed, flag_type=flag_type, flag=4).select_related(
                'user').filter(user__sex="F")
        }

    else:
        infoDict = {
            'male': BaseStatus.filter(user__sex='M'),
            'female': BaseStatus.filter(user__sex='F'),
            'male_new': UserStatus.objects.filter(flag_type=flag_type, flag=0).select_related('user').filter(
                user__sex="M"),
            'male_edit': UserStatus.objects.filter(flag_type=flag_type, flag=3).select_related('user').filter(
                user__sex="M"),
            'male_old': UserStatus.objects.filter(flag_type=flag_type, flag=4).select_related('user').filter(
                user__sex="M"),
            'female_new': UserStatus.objects.filter(flag_type=flag_type, flag=0).select_related('user').filter(
                user__sex="F"),
            'female_edit': UserStatus.objects.filter(flag_type=flag_type, flag=3).select_related('user').filter(
                user__sex="F"),
            'female_old': UserStatus.objects.filter(flag_type=flag_type, flag=4).select_related('user').filter(
                user__sex="F")
        }

    return infoDict


# Create your views here.

def base(request):
    return render(request, 'profile_validate/base.html')


def basic(request, random):
    # BaseStatus = UserStatus.objects.filter(flag_type=0).exclude(flag=1).exclude(flag=2).select_related('user')
    # UserBase 의 user 저장
    BaseStatus = get_BaseStatus(False, 0)
    #print("1.", BaseStatus)
    # BaseList = BaseStatus.values_list('user', flat=True)
    BaseList = get_BaseList(BaseStatus)
    TotalInfo_straight = UserInterview.objects.select_related('user__user').filter(user__user__in=BaseList)
    TotalInfo = TotalInfo_straight.order_by('user__user__joined_time')[:2]  # 10 elements per page
    #print("3.", TotalInfo)

    if random is 1:
        tmp = randomReload(TotalInfo_straight, 2)
        if tmp: TotalInfo = tmp

    infoDict = get_userInfo(BaseStatus, 0, False)

    form = DoneForm()
    return render(request, 'profile_validate/basic.html',
                  {'total_list': TotalInfo, 'base_list': BaseStatus, 'info': infoDict, 'form': form})


def photo(request, random):
    passed = UserStatus.objects.filter(flag_type=0, flag=1).values_list('user', flat=True)
    BaseStatus = get_BaseStatus(passed, 1)
    BaseList = get_BaseList(BaseStatus)
    TotalInfo_straight = UserProfile.objects.select_related('user').filter(user__in=BaseList)
    TotalInfo = TotalInfo_straight.order_by('user__joined_time')[:3]

    if random is 1:
        tmp = randomReload(TotalInfo_straight, 3)
        if tmp: TotalInfo = tmp

    imgsDict = get_imgsDict(BaseList, True, False)
    infoDict = get_userInfo(BaseStatus, 1, passed)
    form = DoneForm()

    #print("2:", TotalInfo[0].pk) # 11
    #print("1:", TotalInfo[0].user.pk) # 6
    #print("3:", TotalInfo[0].user.user.pk) # 12
    #print("4:", imgsDict)

    return render(request, 'profile_validate/photo.html',
                  {'total_list': TotalInfo, 'base_list': BaseStatus, 'imgs': imgsDict, 'info': infoDict, 'form': form})


def paper(request, random):
    passed1 = UserStatus.objects.filter(flag_type=0, flag=1).values_list('user', flat=True)
    passed = UserStatus.objects.filter(flag_type=1, flag=1, user__in=passed1).values_list('user', flat=True)
    BaseStatus = get_BaseStatus(passed, 2)
    BaseList = get_BaseList(BaseStatus)
    TotalInfo_straight = UserProfile.objects.filter(user__in=BaseList).select_related('user__user')
    TotalInfo = TotalInfo_straight.order_by('user__joined_time')[:3]

    if random is 3:
        tmp = randomReload(TotalInfo_straight, 3)
        if tmp: TotalInfo = tmp

    SelectedImg = UserImage.objects.filter(user__in=BaseList, title=False, noFilter=False)
    imgsDict = get_imgsDict(BaseList, False, False)
    # TODO 회원 한 명 생성될 때마다 여러개의 UserStatus 모델 생성
    infoDict = get_userInfo(BaseStatus, 2, passed)
    form = DoneForm()
    return render(request, 'profile_validate/paper.html',
                  {'total_list': TotalInfo, 'base_list': BaseStatus, 'imgs': imgsDict, 'info': infoDict ,'form': form})


def paper_detail(request, index):
    image = UserImage.objects.select_related('user__user').filter(user=index, title=False, noFilter=False)
    UserFull = UserInterview.objects.select_related('user__user').filter(user=index)
    mark = UserMark.objects.filter(user=index).values_list(flat=True)
    form = paperDetailDoneForm()
    return render(request, 'profile_validate/paper_detail.html',
                  {'imgs': image, 'user_full': UserFull[0], 'mark': mark, 'form': form})


# TODO 실물인증 초기 회원가입시부터 가능한지?
# TODO 실물인증 신청시 userstatus object 생성해야함 (flag = 0 으로 초기화 된 obj)
def noFilter(request, random):
    BaseStatus = get_BaseStatus(False, 4)
    BaseList = get_BaseList(BaseStatus)
    TotalInfo_straight = UserProfile.objects.filter(user__in=BaseList).select_related('user')
    TotalInfo = TotalInfo_straight.order_by('user__joined_time')[0]

    if random is 1:
        tmp = randomReload(TotalInfo_straight, 1)
        if tmp: TotalInfo = tmp

    infoDict = get_userInfo(BaseStatus, 4, False)
    imgsDict = get_imgsDict(BaseList, False, True)

    SelectedVideo = UserVideo.objects.filter(user__in=BaseList)
    videos = SelectedVideo.values()
    videoDict = {}
    for i in range(len(SelectedVideo)):
        videoDict[videos[i]['user_id']] = videoDict.get(videos[i]['user_id'], []) + [SelectedVideo[i]]

    print("User>>", TotalInfo.user)
    status = get_object_or_404(UserStatus, user=TotalInfo.user, flag_type=4)
    form = NoFilterDoneForm(instance=status)

    return render(request, 'profile_validate/nofilter.html',
                  {'target': TotalInfo, 'base_list': BaseStatus, 'imgs': imgsDict, 'video': videoDict, 'info': infoDict,
                   'form': form})


# TODO 실물인증 imgage 는 총 3개 / video 는 총 1개의 object 만 존재?
def beautyCheck(request):
    # BaseList = UserBase.objects.filter(joined_type='프로필심사').values_list('user', flat=True)
    BaseList = BeautyScore.objects.values_list('user', flat=True)
    print("1.", BaseList)
    BaseSet = set(BaseList)

    passed = UserStatus.objects.filter(flag_type=1, flag=1).values_list('user', flat=True)
    print("2.", passed)
    to_exclude = UserStatus.objects.filter(flag_type=3, flag=1).values_list('user', flat=True)
    TotalInfo = UserProfile.objects.filter(user__in=BaseSet).filter(user__in=passed).exclude(user__in=to_exclude)[:4]
    print("3.", TotalInfo)

    high_score = {}
    avg_score = {}
    progress = {}
    for user in TotalInfo.values_list('user', flat=True):
        scores = BeautyScore.objects.filter(user=user)
        sum = int(scores.aggregate(Sum('score')).get('score__sum'))
        high_num = len(scores.filter(score__gte=3))
        total_num = len(scores)
        high_score[user] = [high_num, total_num]
        avg_score[user] = sum / total_num
        progress[user] = total_num / 20 * 100

    imgsDict = get_imgsDict(BaseSet, True, False)
    print("4.", imgsDict)
    info_dict = {}
    info_dict['total'] = len(BaseSet)
    # info_dict['pass'] = BeautyScore.objects.
    # info_dict['fail'] =
    form = DoneForm()

    return render(request, 'profile_validate/beautycheck.html',
                  {'total_list': TotalInfo, 'high_score': high_score, 'avg_score': avg_score, 'progress': progress,
                   'imgs': imgsDict, 'form': form})


def done(request, flag_type):
    if request.method == 'POST':
        form = DoneForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form = form.save(commit=False)
            makeConfirmList = form.confirmed.split('-')
            for i in makeConfirmList:
                if i is '': break
                tmp_pk = UserProfile.objects.filter(pk=i).select_related('user')
                tmp_pk = tmp_pk[0].user.pk
                print("#.", tmp_pk)
                status = UserStatus.objects.get(flag_type=flag_type, user=tmp_pk)
                print("STATUS", status)
                status.flag = 1
                status.save()
                # 승인된 신규 회원인 경우 새로운 object create
                # i => UserProfile 의 pk
                old_profile_profile = UserProfile.objects.get(user=tmp_pk)
                #print("**", old_profile_profile)
                #print("**", old_profile_profile.user.pk)
                old_profile_base = UserBase.objects.get(pk=tmp_pk)
                print("confirm:", old_profile_base.name)
                old_profile_interview = UserInterview.objects.select_related('user').get(user__user=tmp_pk)
                if i not in ValidatedProfile.objects.values_list('user', flat=True):
                    new_profile = ValidatedProfile.objects.create(
                        user=old_profile_base,
                        name=old_profile_base.name,
                        phone=old_profile_base.phone,
                        sex=old_profile_base.sex,  # M or W
                        device=old_profile_base.device,  # Android or iOS
                        age=old_profile_base.age,
                        blind=old_profile_base.blind,
                        coin=old_profile_base.coin,
                        birth=old_profile_base.birth,
                        nick=old_profile_profile.nick,
                        job=old_profile_profile.job,
                        area=old_profile_profile.area,  # 지역 카테고리화
                        study=old_profile_profile.study,
                        height=old_profile_profile.height,
                        body=old_profile_profile.body,
                        drink=old_profile_profile.drink,
                        smoke=old_profile_profile.smoke,
                        religion=old_profile_profile.religion,
                        Character=old_profile_profile.Character,
                        introduce=old_profile_interview.introduce,
                        holiday=old_profile_interview.holiday,
                        interest=old_profile_interview.interest,
                        trip=old_profile_interview.trip
                    ); new_profile.save()
                # 기존 회원의 수정 및 변경이 승인된 경우 부분 업데이트
                else:
                    new_profile = ValidatedProfile.objects.get(user=tmp_pk)
                    new_profile.update(
                        user=old_profile_base.user,
                        name=old_profile_base.name,
                        phone=old_profile_base.phone,
                        sex=old_profile_base.sex,  # M or W
                        device=old_profile_base.device,  # Android or iOS
                        age=old_profile_base.age,
                        blind=old_profile_base.blind,
                        coin=old_profile_base.coin,
                        birth=old_profile_base.birth,
                        nick=old_profile_profile.nick,
                        job=old_profile_profile.job,
                        area=old_profile_profile.area,  # 지역 카테고리화
                        study=old_profile_profile.study,
                        height=old_profile_profile.height,
                        body=old_profile_profile.body,
                        drink=old_profile_profile.drink,
                        smoke=old_profile_profile.smoke,
                        religion=old_profile_profile.religion,
                        Character=old_profile_profile.Character,
                        introduce=old_profile_interview.introduce,
                        holiday=old_profile_interview.holiday,
                        interest=old_profile_interview.interest,
                        trip=old_profile_interview.trip
                    ); new_profile.save()

            makeDenyList = form.denied.split('-')
            print("deny >>>", makeDenyList)
            for i in makeDenyList:
                if i is '': break
                tmp_pk = UserProfile.objects.filter(pk=i).select_related('user')
                tmp_pk = tmp_pk[0].user.pk
                status = UserStatus.objects.get(flag_type=flag_type, user=tmp_pk)
                print("denystatus:", status)
                status.flag = 2
                status.save()
        else:
            form = DoneForm()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def paperBeautyDone(request, flag_type):
    if request.method == 'POST':
        form = DoneForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            print(form.confirmed)
            makeConfirmList = form.confirmed.split('-')
            for i in makeConfirmList:
                if i is '': break
                tmp_pk = UserProfile.objects.filter(user__pk=i).select_related('user')
                tmp_pk = tmp_pk[0].user.pk
                print("#.", tmp_pk)
                status = UserStatus.objects.get(flag_type=flag_type, user=tmp_pk)
                print("STATUS", status)
                status.flag = 1
                status.save()
            makeDenyList = form.denied.split('-')
            print("deny >>>", makeDenyList)
            for i in makeDenyList:
                if i is '': break
                tmp_pk = UserProfile.objects.filter(user__pk=i).select_related('user')
                tmp_pk = tmp_pk[0].user.pk
                status = UserStatus.objects.get(flag_type=flag_type, user=tmp_pk)
                print("denystatus:", status)
                status.flag = 2
                status.save()
        else:
            form = DoneForm()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def profilePhotoDone(request):
    # image0-1,image1-1,... 의 형태로 form value 들어옴
    if request.method == 'POST':
        form = DoneForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            makeConfirmList = form.confirmed.split(',')
            confirm_dict = {}
            for i in makeConfirmList:
                if i is '': break
                imgNum = i.split('-')[0][5:]
                user = i.split('-')[1]
                confirm_dict[user] = confirm_dict.get(user, []) + [imgNum]
            for user in confirm_dict.keys():
                for pk in confirm_dict.get(user):
                    # 각 image 개별적으로 validate 속성 True 로 변경
                    ######################## user -> user__user
                    img = UserImage.objects.get(user__user=user, pk=pk)
                    img.validate = True
                    img.save()
                    # 승인된 이미지는 ValidateImg 모델에 새로운 object 로 복사
                    new_img = ValidatedImage.objects.create(
                        user=img.user,
                        title=True,
                        noFilter=False,
                        image=img.image
                    ); new_img.save()
                # 회원이 게시한 프로필 사진 중 3개 이상의 승인된 사진이 있으면 프로필 사진 status flag 1 로 변경
                ###################### user -> user__user
                validated_imgs = UserImage.objects.select_related('user').filter(user__user=user, title=True,
                                                                                 noFilter=False, validate=True)
                status = UserStatus.objects.get(flag_type=1, user=user)
                print("VAL: ", validated_imgs)
                if len(validated_imgs) >= 3:
                    status.flag = 1
                else:
                    status.flag = 2
                status.save()
            '''
            makeDenyList = form.denied.split(',')
            deny_dict = {}
            for i in makeDenyList:
                if i is '': break
                imgNum = i.split('-')[0][5:]
                user = i.split('-')[1]
                deny_dict[user] = deny_dict.get(user, []) + [imgNum]
            '''

        else:
            form = DoneForm()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def noFilterDone(request, index):
    status = get_object_or_404(UserStatus, user=index, flag_type=4)
    if request.method == 'POST':
        form = NoFilterDoneForm(request.POST, instance=status)
        if form.is_valid():
            form = form.save(commit=False)
            if form.reason == 0:
                form.flag = 1
                # UserImage, UserVideo validate 속성 True 로 변경
                image = UserImage.objects.filter(user=index, noFilter=True)[:3]
                video = UserVideo.objects.get(user=index)
                for i in range(3):
                    image[i].validate = True
                    image[i].save()
                    # 승인된 실물인증 이미지와 ValidatedImage 에 추가
                    validated_img = ValidatedImage.objects.create(
                        user=index,
                        title=False,
                        noFilter=True,
                        image=image[i].image
                    );
                    validated_img.save()
                # TODO Video validate 속성 삭제해도 될 것 같다!
                video.validate = True
                video.save()
                validate_video = ValidatedVideo.objects.create(
                    user=index,
                    video=video.video
                );
                validate_video.save()
            else:
                form.flag = 2
            form.save()
            return redirect('no-filter')
        else:
            form = NoFilterDoneForm(instance=status)
    return render(request, 'profile_validate/nofilter.html', {'form': form})


def paperDetailDone(request, index):
    if request.method == 'POST':
        form = paperDetailDoneForm(request.POST, request.FILES)
        if form.is_valid():
            status = UserStatus.objects.get(user=index, flag_type=2)
            print(status)
            flag_type = form.cleaned_data.get('btn')
            if flag_type == "승인": flag = 1
            elif flag_type == "보류": flag = 5
            elif flag_type == "반려": flag = 2
            status.flag = flag
            status.save()
    else:
        form = paperDetailDoneForm()
    return HttpResponse('<script type="text/javascript">window.close()</script>')


def randomReload(TotalInfo_straight, object_num):
    if (TotalInfo_straight is not None) and (len(TotalInfo_straight) >= object_num):
        if object_num == 1:
            random = TotalInfo_straight.order_by('?')[0]
        else:
            random = TotalInfo_straight.order_by('?')[:object_num]
    else:
        random = False
    return random
