from django import template
from .. import models


register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    return models.Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    return models.Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    # 别忘了在顶部引入 Category 类
    return models.Post.objects.raw('select a.id, b.name, a.category_id, count(a.category_id) as num '
                                   'from blog01_Post a left join blog01_Category b on a.category_id = b.id' 
                                   ' group by a.category_id')


@register.simple_tag
def get_tags():
    # 记得在顶部引入 Tag model
    return models.Tag.objects.raw('select a.id, c.name, a.tag_id, count(a.tag_id) as num '
                                  'from blog01_post_tags a'                                
                                  ' left join blog01_Post b on a.post_id=b.id'
                                  ' left join blog01_Tag c on a.tag_id = c.id'  
                                  ' group by a.tag_id'
                                  ' having num > 0 ')


@register.simple_tag
def get_nickname(aid):
    user_info = models.UserInfo.objects.get(user=aid)
    return user_info.nickname


