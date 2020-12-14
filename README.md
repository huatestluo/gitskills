# gitskills
# 生成文件目录命令：django-admin startproject helloworld
# 这些目录和文件的用处是：
#    最外层的:helloworld: 项目的容器，可以随便命名。
#    manage.py: 一个让你用各种方式管理 Django 项目的命令行工具。
#    helloworld/__init__.py：一个空文件，告诉 Python 这个目录应该被认为是一个 Python 包。
#    helloworld/settings.py：Django 项目的配置文件。
#    helloworld/urls.py：Django 项目的 URL 声明，就像你网站的“目录”。
#    helloworld/wsgi.py：作为你的项目的运行在 WSGI 兼容的Web服务器上的入口。

# 启动命令 ： python manage.py runserver
# 默认端口 8000 切换端口命令：python manage.py runserver 8080
# url（）函数用法：
# def url(regex, view, kwargs=None, name=None):
#    return re_path(regex, view, kwargs, name)
# regex: 正则表达式，与之匹配的 URL 会执行对应的第二个参数 view。
# view: 用于执行与正则表达式匹配的 URL 请求。
# kwargs: 视图使用的字典类型的参数。
# name: 用来反向获取 URL。

# 新增目录 ：python manage.py startapp hello