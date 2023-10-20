# views.py
def detail(request, __(a)__):
    article = get_object_or_404(Article, pk=article_pk)

    comment_form = CommentForm()

    # 여기에 comments 인스턴스를 하나 추가합니다. -> detail.html 에 사용
    # comments = article.comment_set.all()

    context_data = {
        'article': article,
        __(b)__,
    }
    return render(request, 'eithers/detail.html', __(c)__)


# (a) : article_pk
# (b) : 'comment_form' : comment_form, 'comments' : comments,
# (c) : context_data