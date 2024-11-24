from blog_app.models import Blog

blog1 = Blog.objects.create(title='Example1', content='Example', author='Admin')
blog2 = Blog.objects.create(title='Example2', content='Example', author='Admin')
blog3 = Blog.objects.create(title='Example3', content='Example', author='Admin')
blog4 = Blog.objects.create(title='Example4', content='Example', author='Admin')
blog5 = Blog.objects.create(title='Example5', content='Example', author='Admin')

blog = Blog.objects.get(id=1)

blog.title = 'Example1_edit'
blog.content = 'Example_edit'

blog.save()

all_blog = Blog.objects.all()

for _ in all_blog:
    print(f'Title: {_.title}, Content: {_.content}')

blog = Blog.objects.get(id=2)
blog.delete()

filter_blog = Blog.objects.filter(author='Admin')