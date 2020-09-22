### 
#### **View**에서 화면 공유 방법

1. HttpResponse
2. render(request , templates , context) -> `templates`를 찾아서 context와 같이 넘겨주겠다. forward 방식
3. redirect() -> templates를 찾는게 아니라 **새로운** `url request` 요청할 수 있게 된다. 

### **static**이란?
- 서버에서 생성 된 HTML을 제외하고, 웹 어플리케이션은 일반적으로 전체 웹 페이지를 렌더링하는 데 필요한 추가 파일 — 예:이미지, JavaScript 또는 CSS — 을 제공해야합니다. Django에서는 이러한 파일을 "정적 파일" `static` 이라고 부릅니다.

#### **static** 파일을 한 곳으로 모을 때
- django는 하나의 web이 app들을 관리한다.
- djangoWEB이라는 전체 프로젝트 뼈대가 관리해야한다.
- djangoWEB에 static이 존재 해야한다.

> - python manage.py `collectstatic` : 프로젝트에 static 파일들 모아줄 때
>![](2020-09-21-09-45-02.png)
---
> - `{% load static %}` : 모은 static 파일들을 사용하고 싶을때
>![](2020-09-21-10-15-58.png)
---
- `login.html`에서 다른 url 로 넘어가는 링크 `{% url 'registerForm'}`는 `urls.py`에 `name="" ` 을 찾아간다.
```html
<a href="{% url 'registerForm'}" class="text-center">Register a new membership</a>
```
> ![](2020-09-21-16-33-12.png)
>
> ![](2020-09-21-10-24-28.png)
---
> - `user_id`, `user_name`, `user_pwd`는 테이블 `BbsUserRegister` 에 컬럼으로 만들어진다.
> ![](2020-09-21-10-38-28.png)
>
> ![](2020-09-21-16-34-56.png)
---
#### 지정된 **`header`**, **`footer`** 가져와서 사용하기.
- {% include 'header.html' %}
- {% include 'footer.html' %}

>`ex)`
> ```html 
> {% include 'header.html' %}
> {% block content %}
>   <section></section>
> {% endblock %}
> {% include 'footer.html' %}

#### Scope
- render 사용시 context에 데이터를 심으면 해당 데이터는 요청된 **`templates에서만`** 사용이 가능한 scope를 가지게 된다.
> ex) render(request, 'xxxx.html', `context`)

- 다른 `templates`에서도 데이터를 유지하고 싶을 때는 **`session`** 을 사용하고 session 자체를 context에 담아 넘겨준다.
> `ex) `
>```python
>   request.session['user_name_'] = user.user_name
>   context['userSession'] = reqeust.session['user_name']
> return render(request, 'home.html', context)
>```

#### 데이터 가져오기
- modelName.objects.filter() 를 사용하게 되면 return type 으로 Query_Set 리턴.

- modelName.objects.get() 으로 가져오면 해당 데이터 셋을 리턴.


#### logout session
##### session 삭제
- Django에서는 session을 DB에 저장한다.
- logout 을 하기위해서는 DB에 저장되어있는 session을 삭제해야 한다.

> ![](2020-09-21-14-29-49.png)

