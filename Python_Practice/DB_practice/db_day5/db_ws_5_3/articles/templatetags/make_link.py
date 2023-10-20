from django import template

# 유효한 tag library를 만들기 위한 모듈 레벨의 인스턴스 객체인 register 변수를 작성
register = template.Library()


@register.filter
def hashtag_link(word):
    content = word.content + ''
    hashtags = word.hashtags.all()
    for hashtag in hashtags:
        content = content.replace(hashtag.content + ' ', f'<a href="/articles/{hashtag.pk}/hashtag/">{hashtag.content}</a> ')
    return content # 원하는 문자열로 치환이 완료된 content 리턴

