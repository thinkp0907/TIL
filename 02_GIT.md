# 원격 저장소

- 팀원과 나의 공유 저장소

- 내 컴퓨터에서 `push` 로 원격 저장소에 원하는 폴더(파일)을 저장한다.

  ```shell
  $ git clone https://github.com/thinkp0907/wordchain.git
  ```

  > `git clone` 은 처음 프로젝트를 받을 때 만 사용한다. 그 이후에 차이점을 다운 받기 위해서는 `git pull` 로 받는다. 
  >
  > P.S. `git clone`실행 시 따로 `git remote add`를 해줄 필요 없음.

  

- 팀원이 나의 공유 저장소에 접속하고 차이점을 `push`하기 위해서는 나의 Manage Access 권한 허가가 필요하다.

  > Github 에서 `Settings` -> `Manage access` -> `invite a collaborator`
  >
  > 이후 팀원의 아이디 또는 이메일을 입력하여 초대장 전송. 



- 이전 commit 대비 변경 내용 보기.

  > `git diff [파일명]` 으로 이전 커밋 대비 현재 변경 내역 확인 가능.



## 협업 시나리오

### 1. Push & Pull

- 끝말잇기
- Synchronous 작업에만 가능



### 2. Branch

- Asynchronous 비동기적 작업 가능. (동시 작업)
- 원본에 영향 없이 테스트(실험) 가능. 



# Git Branch

## 원본 세상을 망치치 않고 새 세상에서 실험 가능



### (1) `git branch`

- 현재 저장소에 있는 **branch** 확인.

  ```
  * master
    test
  ```



### (2) `git branch [branchname]`

- 새로운 branch 생성



### (3) `git checkout [branchname]`

- 다른  branch로 넘어가는 방법.



### (4)` git branch -d [branchname]`

- branch 삭제



### (5) `git merge [합칠branchname]`

- 대상 브랜치를 병합
- **중요*** 주가 되는 브랜치로 이동
- mater가 test를 병합 -> master merges test
- master로 이동 ->  test로 병합
- `git checkout master` -> `git merge test`

> 다른 branch에 있던 파일들을 기존 branch(master) 로 합친다.
>
> 사실상 복사에 가깝다. test를 지우지 않는 한 자료가 남아있다.



### (6) `git cherry-pick`



## Github Pull-Request

- 각자의 branch 안에서의 변화를 master brance에 반영(Pull)시켜 달라는 요청(Request)
- `New pull request`
- Merge pull request 권한은 대체로 사수, 팀장, CTO, CEO  등이 가지고 있다.

> base : 주 브랜치 , compare :  병합을 할 브랜치
>
> ex) base : master  <-  compare : captain



## Fork & Pr model

- 강사 github 백일장 저장소 --> 나의 github 백일장 저장소로 만드는것을 `fork`라고 한다.
- 나의 github 백일장 저장소여야만 push 가능.