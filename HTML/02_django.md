
#### `models.py`
- 두개의 모델을 만든다?
    - 두개의 테이블을 만든다!
    ```python
    class Question(models.Model):
        question_text = models.CharField(max_length=50)
        # column의 형식들을 지정한다.
        regdate       = models.DateTimeField()
        
        def __str__(self):
            return self.question_text + " , " + self.regdate
    ```
    ```python
    class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE())
    choice_text = models.CharField(max_length=200)
    votes       = models.IntegerField(default=0)

    def __str__(self):
        return self.question + " , " + self.votes
    ```

- 기본키를 설정하지 않으면, 보이지 않지만 `id`컬럼이 자동으로 생성된다. 

#### `admin.py`

```python
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
```

### django ORM 활용 코드
#### ORM에서는 일반 SQL 사용 불가. 
#### select * from table ;
>-   -> modelName.`objects.all()`
    
#### select * from table where id = 1 ;
>-   -> modelName.`objects.filter(id = 1);`
    
#### select * from table where id = 1 and pwd = 1 ;
>-   -> modelName.`objects.filter(id = 1 , pwd = 1)`

#### select * from table where id = 1 or pwd = 1 ;
>-   -> modelName.`objects.filter(Q(id = 1) | Q(pwd = 1))`

#### select * from table where subject like'%공지%'
>-   -> modelName.`objects.filter(subject_icontains = '공지')`

#### select * from table where subject like'공지%'
>-   -> modelName.`objects.filter(subject_startwith = '공지')`

#### select * from table where subject like'%공지'
>-   -> modelName.`objects.filter(subject_endwith = '공지')`

#### insert into table values('')
>-   model(attr = value, atrr = value .... ) -> `model.save()`

#### delete * from table where id = 1 ;
>-   -> modelName.`objects.get(id=1).delete()`

#### update table set attr = value where id = 1
>-   obj = modelName.`objects.get(id = 1)`
>    obj.attr = '변경'
>    obj.save() -- commit



### GET 방식 받는 다른 방법
```python
def choice(request, q_id) :
    print('param q_id', str(q_id))
```    