# from jinja2 import Environment, select_autoescape
# env = Environment(autoescape=select_autoescape(
#     enabled_extensions=('html', 'xml'),
#     default_for_string=True,
# ))



from jinja2 import Template
# template = Template('Hello {{name}}!').module
# template.render(name='John Doe')
#
# m = Template(u"{% set a, b = 'foo', 'föö' %}").module
# print(m.a)

'''

Environment
- compile_expression : return Boolean
- compile_templates : 템플릿 찾아서 컴파일 하고 디렉토리에 저장
- extend :

Template
- render(knights='that say nih')
- render_async : 비동기
- generate_async: 비동기 generate반
- modulemodule: 템플릿변수 접



select_autoescape : 자동저장기능

make_logging_undefined: 로즈저장


select_autoescape(enabled_extensions=('html', 'htm', 'xml'), disabled_extensions=(), default_for_string=True, default=False)
'''
t = Template('{% macro foo() %}42{% endmacro %}23')
print(str(t.module)) # 23
t.module.foo() == '42' # True


Template('Hello {{ name }}!').stream(name='foo').dump('hello.html')

