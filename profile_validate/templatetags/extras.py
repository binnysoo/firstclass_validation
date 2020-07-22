from django.template.defaulttags import register
...
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def get_list(list, index):
    if list == None:
        return None
    else:
        index = int(index)
        if index < len(list):
            return list[index]
        else: return None

@register.filter
def get_url(imgObj):
    if imgObj == None:
        return None
    return imgObj.image.url

@register.filter
def get_video_url(videoObj):
    if videoObj == None:
        return None
    return videoObj.video.url

@register.filter
def count(obj):
    if obj == None:
        return 0
    return obj.count()

@register.filter
def validate(obj):
    if obj == None:
        return False
    return obj.validate

@register.filter
def pk(obj):
    if obj == None:
        return False
    return obj.pk

