from stucampus.infor.models import Infor


def post_infor(request, cleaned_data):
    title = cleaned_data['title']
    content = cleaned_data['content']
    organization = cleaned_data['organization']
    author = request.user.student
    Infor.objects.create(title=title, content=content,
                         author=author, organization=organization)
