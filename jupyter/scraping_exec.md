

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
```


```python
try:
    html = urlopen('https://pythondojang.bitbucket.io/weather/observation/currentweather.html')
except HTTPError as he:
    print('http error')
except URLError as ue:
    print('urlerror')
else :
    soup = BeautifulSoup(html.read(), 'html.parser')
```


```python
soup
```




    
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    
    <html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">
    <head>
    <title>도시별 현재날씨 &gt; 지상관측자료 &gt; 관측자료 &gt; 날씨 &gt; 기상청 </title>
    <link href="http://www.kma.go.kr/favicon2.ico" rel="shortcut icon"/>
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
    <link href="/share/css/import.css?20160530" rel="stylesheet" type="text/css"/>
    <script src="/share/js/jquery-1.7.1.min.js" type="text/javascript"></script>
    <script src="/share/js/common.js?ver=20150417" type="text/javascript"></script>
    <link href="/share/css/warninglayer.css" rel="stylesheet" type="text/css"/>
    <!--[if gte IE 7]><link rel="stylesheet" type="text/css" href="/share/css/ie7.css" /><![endif]-->
    <meta content="기상청 " name="title"/>
    <meta content="기상청" name="author"/>
    <meta content="날씨, 기상청" name="keywords"/>
    <meta content="서울시 기상청 사이트입니다." name="description"/>
    <meta content="IE=EmulateIE7" http-equiv="X-UA-Compatible"/>
    <meta content="../../images/weather/observation/h4_1_1.gif" name="parent-image"/>
    <meta content="지상관측자료" name="parent-alt"/>
    <meta content="../../images/weather/observation/h5_1_1.gif" name="title-image"/>
    <meta content="도시별 현재날씨" name="title-alt"/>
    <meta content="/HELP/html/help_sfc001.jsp" name="help-url"/>
    <style type="text/css">
            .table_subheader .top_line{background:#dce6ef;font-weight:bold;border:1px solid #c8c8c8; color:#333;}
            .table_subheader .nm{background:#dce6ef;font-weight:bold;border:1px solid #c8c8c8; color:#333;}
        </style>
    </head>
    <body>
    <div id="header">
    <span class="gocontent"><a href="#content">본문 바로가기</a></span>
    <dl id="skip">
    <dt><strong class="hid">바로가기 메뉴</strong></dt>
    <dd><a class="golnb" href="#main_menu">메인메뉴 바로가기</a></dd>
    </dl>
    <div id="gnb">
    <ul id="area">
    <li><a href="http://www.kma.go.kr/index.jsp"><img alt="홈" src="/images/main/btn_home.gif"/></a></li>
    <li><a href="https://web.kma.go.kr/member/login.jsp?returnURL=http://www.kma.go.kr/weather/observation/currentweather.jsp"><img alt="로그인" src="/images/main/gm_login.gif"/></a></li>
    <li><a href="https://web.kma.go.kr/member/join.jsp"><img alt="회원가입" src="/images/main/gm_join.gif"/></a></li>
    <li class="sitemap"><a href="http://web.kma.go.kr/global/top/sitemap.jsp"><img alt="사이트맵" src="/images/main/gm_sitemap.gif"/></a></li>
    <li style="padding-left:5px !important; padding-right:3px !important;"><a href="http://web.kma.go.kr/eng/index.jsp" target="_blank" title="새창열림"><img alt="영어(english)" src="/images/main/icon_language_eng_1.gif" style="padding:2px; margin-top:-2px;"/></a></li>
    <li style="padding-right:3px !important;"><a href="http://web.kma.go.kr/jpn/index.jsp" target="_blank" title="새창열림"><img alt="일본어(japanese)" src="/images/main/icon_language_jpn_1.gif" style="padding:2px; margin-top:-2px;"/></a></li>
    <li><a href="http://web.kma.go.kr/chn/index.jsp" target="_blank" title="새창열림"><img alt="중국어(chinese)" src="/images/main/icon_language_chn_1.gif" style="padding:2px; margin-top:-2px;"/></a></li>
    <li class="sitemap"><img alt="글자크기" src="/images/main/gm_font.gif"/></li>
    <li class="pad3 global_btn"><a href="#" onclick="scaleFont(+1); return false;"><img alt="글자확대" src="/images/main/gm_fontplus.gif"/></a></li>
    <li class="pad global_btn"><a href="#" onclick="scaleFont(-1); return false;"><img alt="글자축소" src="/images/main/gm_fontminus.gif"/></a></li>
    <li class="padnone">
    <form action="http://web.kma.go.kr/search/kmaSearch.jsp" class="global_top_search" method="post" name="search_dictionary">
    <fieldset>
    <legend>통합 검색</legend>
    <p class="view">
    <input class="inputbase" id="input_keyword1" name="keyword" title="검색어 입력" type="text"/>
    <input alt="검색" src="/images/main/btn_global_search.gif" type="image"/>
    </p>
    </fieldset>
    </form>
    </li>
    </ul>
    </div>
    <div id="topMenu">
    <h1><a href="http://www.kma.go.kr/index.jsp"><img alt="기상청 " src="/images/common/logo_4.gif"/></a></h1>
    <div id="main_menu">
    <noscript>하위메뉴선택은 자바스크립트 기능이 있어야 선택하실 수 있습니다.</noscript>
    <a id="golnb" name="golnb"></a>
    <ul id="lnb">
    <li class="info_open" id="top-menu6"><a href="http://web.kma.go.kr/info_open/info/open.jsp" id="top-menu-head6"><img alt="정보공개" src="/images/main/mn12.gif"/></a>
    <ul id="top-sub-menu6" style="display:none;">
    <li id="top-6-1"><a href="http://web.kma.go.kr/info_open/info/open.jsp"><img alt="행정정보공개" src="/images/main/mn0_8.gif"/></a></li>
    <li id="top-6-2"><a href="http://web.kma.go.kr/info_open/public_data/guidepage.jsp"><img alt="기상자료 조회·발급" src="/images/main/mn0_9.gif"/></a></li>
    <li id="top-6-4"><a href="http://web.kma.go.kr/info_open/realname_plan.jsp"><img alt="정책실명제" src="/images/main/mn0_4.gif"/></a></li>
    <li id="top-6-5"><a href="http://web.kma.go.kr/info_open/cleango/gamsa03_list.jsp"><img alt="청렴자료공개" src="/images/main/mn0_5.gif"/></a></li>
    <li id="top-6-6"><a href="http://web.kma.go.kr/notify/information/law_status_list.jsp"><img alt="법령정보" src="/images/main/mn0_6.gif"/></a></li>
    </ul>
    </li>
    <li id="top-menu1"><a href="http://www.kma.go.kr/weather/main.jsp" id="top-menu-head1"><img alt="날씨" src="/images/main/mn1.gif"/></a>
    <ul id="top-sub-menu1" style="display:none;">
    <li id="top-1-1"><a href="http://www.kma.go.kr/weather/main.jsp"><img alt="날씨종합" src="/images/main/mn1_1.gif"/></a></li>
    <li id="top-1-2"><a href="http://www.kma.go.kr/weather/warning/status.jsp"><img alt="특보·예보" src="/images/main/mn1_2.gif"/></a></li>
    <li id="top-1-3"><a href="http://www.kma.go.kr/weather/images/rader_integrate.jsp"><img alt="날씨영상" src="/images/main/mn1_3.gif"/></a></li>
    <li id="top-1-10"><a href="http://www.kma.go.kr/mini/marine/marine_integrate.jsp"><img alt="바다날씨" src="/images/main/mn1_10.gif"/></a></li>
    <li id="top-1-4"><a href="http://www.kma.go.kr/weather/typoon/report.jsp"><img alt="태풍" src="/images/main/mn1_4.gif"/></a></li>
    <li id="top-1-5"><a href="http://www.kma.go.kr/weather/asiandust/density.jsp"><img alt="황사" src="/images/main/mn1_5.gif"/></a></li>
    <li id="top-1-6"><a href="http://www.kma.go.kr/weather/earthquake_volcano/report.jsp"><img alt="지진·화산" src="/images/main/mn1_11.gif"/></a></li>
    <li id="top-1-7"><a href="http://www.kma.go.kr/weather/observation/currentweather.jsp"><img alt="관측자료" src="/images/main/mn1_7.gif"/></a></li>
    <li id="top-1-8"><a href="http://www.kma.go.kr/weather/climate/average_south.jsp"><img alt="기후자료" src="/images/main/mn1_8.gif"/></a></li>
    <li id="top-1-9"><a href="http://www.kma.go.kr/weather/lifenindustry/life_jisu.jsp"><img alt="생활과 산업" src="/images/main/mn1_9.gif"/></a></li>
    </ul>
    </li>
    <li id="top-menu2"><a href="https://web.kma.go.kr/notify/epeople/e_qna.jsp#epeopleFrameFocus" id="top-menu-head2"><img alt="참여와소통" src="/images/main/mn10.gif"/></a>
    <ul id="top-sub-menu2" style="display:none;">
    <li id="top-2-8"><a href="https://web.kma.go.kr/notify/epeople/e_qna.jsp#epeopleFrameFocus"><img alt="국민참여마당" src="/images/main/mn6_8.gif"/></a></li>
    <li id="top-2-1"><a href="http://web.kma.go.kr/communication/community/discuss_list.jsp"><img alt="날씨이야기" src="/images/main/mn6_1.gif"/></a></li>
    <li id="top-2-2"><a href="http://web.kma.go.kr/communication/gallery/invite_prize_list.jsp"><img alt="기상사진전" src="/images/main/mn6_2.gif"/></a></li>
    <li id="top-2-4"><a href="http://web.kma.go.kr/communication/survey/list.jsp"><img alt="설문조사" src="/images/main/mn6_4.gif"/></a></li>
    </ul>
    </li>
    <li id="top-menu3"><a href="http://web.kma.go.kr/communication/encyclopedia/list.jsp" id="top-menu-head3"><img alt="지식과 배움" src="/images/main/mn2.gif"/></a>
    <ul id="top-sub-menu3" style="display:none;">
    <li id="top-3-10"><a href="http://web.kma.go.kr/communication/elearning/fct_trn_4.jsp"><img alt="예보기술" src="/images/main/mn2_10.gif"/></a></li>
    <li id="top-3-1"><a href="http://web.kma.go.kr/communication/encyclopedia/list.jsp"><img alt="기상백과" src="/images/main/mn2_1.gif"/></a></li>
    <li id="top-3-2"><a href="http://web.kma.go.kr/communication/webzine/skylove_list.jsp"><img alt="간행물" src="/images/main/mn2_2.gif"/></a></li>
    <li id="top-3-3"><a href="http://web.kma.go.kr/communication/knowledge/spring_list.jsp"><img alt="날씨배움터" src="/images/main/mn2_3.gif"/></a></li>
    <li id="top-3-4"><a href="http://www.kma.go.kr/child/main.jsp" target="_blank" title="새창으로 열립니다"><img alt="어린이기상교실" src="/images/main/mn2_4.gif"/></a></li>
    <li id="top-3-5"><a href="http://web.kma.go.kr/communication/visit/reservation_info.jsp"><img alt="기상청체험학습" src="/images/main/mn2_5.gif"/></a></li>
    <li id="top-3-6"><a href="http://metacademy.go.kr" target="_blank" title="새창으로 열립니다"><img alt="민간위탁교육훈련" src="/images/main/mn2_6.gif"/></a></li>
    </ul>
    </li>
    <li id="top-menu4"><a href="http://web.kma.go.kr/notify/focus/list.jsp" id="top-menu-head4"><img alt="행정과 정책" src="/images/main/mn3.gif"/></a>
    <ul id="top-sub-menu4" style="display:none;">
    <li id="top-4-2"><a href="http://web.kma.go.kr/notify/focus/list.jsp"><img alt="포토뉴스" src="/images/main/mn3_2.gif"/></a></li>
    <li id="top-4-1"><a href="http://web.kma.go.kr/notify/notice/list.jsp"><img alt="공지사항" src="/images/main/mn3_1.gif"/></a></li>
    <li id="top-4-3"><a href="http://web.kma.go.kr/notify/press/kma_list.jsp"><img alt="보도자료" src="/images/main/mn3_3.gif"/></a></li>
    <li id="top-4-4"><a href="http://web.kma.go.kr/notify/employ/list_01.jsp"><img alt="채용·인사" src="/images/main/mn3_4.gif"/></a></li>
    <li id="top-4-5"><a href="http://web.kma.go.kr/notify/work_plan1.jsp"><img alt="국정과제" src="/images/main/mn3_5_new.gif"/></a></li>
    <li id="top-4-6"><a href="http://web.kma.go.kr/notify/biz/biz_information.jsp"><img alt="날씨경영 도우미" src="/images/main/mn3_6.gif"/></a></li>
    </ul>
    </li>
    <li id="top-menu5"><a href="http://web.kma.go.kr/aboutkma/director/greeting.jsp" id="top-menu-head5"><img alt="기상청소개" src="/images/main/mn4.gif"/></a>
    <ul id="top-sub-menu5" style="display:none;">
    <li id="top-5-1"><a href="http://web.kma.go.kr/aboutkma/director/greeting.jsp"><img alt="청/차장 소개" src="/images/main/mn4_1.gif"/></a></li>
    <li id="top-5-2"><a href="http://web.kma.go.kr/aboutkma/mission/mission.jsp"><img alt="미션·비전" src="/images/main/mn4_2.gif"/></a></li>
    <li id="top-5-3"><a href="http://web.kma.go.kr/aboutkma/organization/quota.jsp"><img alt="조직·직원" src="/images/main/mn4_3.gif"/></a></li>
    <li id="top-5-4"><a href="http://web.kma.go.kr/aboutkma/biz/observation01.jsp"><img alt="주요업무" src="/images/main/mn4_4.gif"/></a></li>
    <li id="top-5-5"><a href="http://web.kma.go.kr/aboutkma/intro/regional_index.jsp"><img alt="소속·산하기관소개" src="/images/main/mn4_5.gif"/></a></li>
    <li id="top-5-6"><a href="http://web.kma.go.kr/aboutkma/publicity/catalog.jsp"><img alt="홍보실" src="/images/main/mn4_6.gif"/></a></li>
    <li id="top-5-7"><a href="http://web.kma.go.kr/aboutkma/location/map.jsp"><img alt="찾아오시는길" src="/images/main/mn4_7.gif"/></a></li>
    <li id="top-5-8"><a href="http://web.kma.go.kr/aboutkma/website/link_list.jsp"><img alt="관련사이트" src="/images/main/mn4_8.gif"/></a></li>
    </ul>
    </li>
    <li class="warning" id="warning">
    <a href="http://www.kma.go.kr/weather/warning/status.jsp">
    <img alt="기상특보" src="/images/main/img_issue_report_2.gif"/>
    </a>
    </li>
    </ul>
    </div>
    </div>
    <div class="allmenu">
    <h2><a href="#menuopen" id="menuopen_btn" onclick="showBx('menuopen'); return false;"><img alt="전체메뉴" src="/images/main/btn_allmenu.gif"/></a></h2>
    </div>
    <div id="menuopen">
    <ul class="mn1">
    <li class="sty0">
    <dl class="dlsty0">
    <dt><a href="http://web.kma.go.kr/info_open/info/open.jsp"><img alt="정보공개" src="/images/main/img_totalm_t0.gif"/></a></dt>
    <dd>
    <ul>
    <li><a href="http://web.kma.go.kr/info_open/info/open.jsp">행정정보공개</a></li>
    <li><a href="http://web.kma.go.kr/info_open/public_data/guidepage.jsp">기상자료 조회·발급</a></li>
    <li><a href="http://web.kma.go.kr/info_open/realname_plan.jsp">정책실명제</a></li>
    <li><a href="http://web.kma.go.kr/info_open/cleango/gamsa03_list.jsp">청렴자료공개</a></li>
    </ul>
    </dd>
    </dl>
    </li>
    <li class="sty1">
    <dl class="dlsty1">
    <dt><a href="http://www.kma.go.kr/weather/main.jsp"><img alt="날씨" src="/images/main/img_totalm_t1.gif"/></a></dt>
    <dd>
    <ul>
    <li><a href="http://www.kma.go.kr/weather/main.jsp">날씨종합</a></li>
    <li><a href="http://www.kma.go.kr/weather/warning/status.jsp">특보·예보</a></li>
    <li><a href="http://www.kma.go.kr/weather/images/rader_composite_ppi0.jsp">날씨영상</a></li>
    <li><a href="http://www.kma.go.kr/mini/marine/marine_integrate.jsp">바다날씨</a></li>
    <li><a href="http://www.kma.go.kr/weather/typoon/report.jsp">태풍</a></li>
    <li><a href="http://www.kma.go.kr/weather/asiandust/density.jsp">황사</a></li>
    <li><a href="http://www.kma.go.kr/weather/earthquake/report.jsp">지진/지진해일</a></li>
    <li><a href="http://www.kma.go.kr/weather/observation/currentweather.jsp">관측자료</a></li>
    <li><a href="http://www.kma.go.kr/weather/climate/average_south.jsp">기후자료</a></li>
    <li><a href="http://www.kma.go.kr/weather/lifenindustry/life_jisu.jsp">생활과 산업</a></li>
    </ul>
    </dd>
    </dl>
    </li>
    <li class="sty2">
    <dl class="dlsty2">
    <dt><a href="https://web.kma.go.kr/notify/epeople/e_qna.jsp#epeopleFrameFocus"><img alt="참여와 소통" src="/images/main/img_totalm_t2.gif"/></a></dt>
    <dd>
    <ul>
    <li><a href="https://web.kma.go.kr/notify/epeople/e_qna.jsp#epeopleFrameFocus">국민참여마당</a></li>
    <li><a href="http://web.kma.go.kr/communication/community/discuss_list.jsp">날씨이야기</a></li>
    <li><a href="http://web.kma.go.kr/communication/gallery/invite_prize_list.jsp">기상사진전</a></li>
    <li><a href="http://web.kma.go.kr/communication/survey/list.jsp">설문조사</a></li>
    </ul>
    </dd>
    </dl>
    </li>
    <li class="sty3">
    <dl class="dlsty2">
    <dt><a href="http://web.kma.go.kr/communication/encyclopedia/list.jsp"><img alt="지식과 배움" src="/images/main/img_totalm_t3.gif"/></a></dt>
    <dd>
    <ul>
    <li><a href="http://web.kma.go.kr/communication/elearning/fct_trn_4.jsp">예보기술</a></li>
    <li><a href="http://web.kma.go.kr/communication/encyclopedia/list.jsp">기상백과</a></li>
    <li><a href="http://web.kma.go.kr/communication/webzine/skylove_list.jsp">간행물</a></li>
    <li><a href="http://web.kma.go.kr/communication/knowledge/spring_list.jsp">날씨배움터</a></li>
    <li><a href="http://www.kma.go.kr/child/main.jsp" target="_blank" title="새창으로 열립니다">어린이기상교실</a></li>
    <li><a href="http://web.kma.go.kr/communication/visit/reservation_info.jsp">기상청체험학습</a></li>
    <li><a href="http://metacademy.go.kr" target="_blank" title="새창으로 열립니다">민간위탁교육훈련</a></li>
    </ul>
    </dd>
    </dl>
    </li>
    <li class="sty4">
    <dl class="dlsty2">
    <dt><a href="http://web.kma.go.kr/notify/focus/list.jsp"><img alt="행정과정책" src="/images/main/img_totalm_t4.gif"/></a></dt>
    <dd>
    <ul>
    <li><a href="http://web.kma.go.kr/notify/focus/list.jsp">포토뉴스</a></li>
    <li><a href="http://web.kma.go.kr/notify/notice/list.jsp">공지사항</a></li>
    <li><a href="http://web.kma.go.kr/notify/press/kma_list.jsp">보도자료</a></li>
    <li><a href="http://web.kma.go.kr/notify/employ/list_01.jsp">채용·인사</a></li>
    <li><a href="http://web.kma.go.kr/notify/work_plan1.jsp">국정과제</a></li>
    <li><a href="http://web.kma.go.kr/notify/biz/biz_information.jsp">날씨경영도우미</a></li>
    </ul>
    </dd>
    </dl>
    </li>
    <li class="sty5">
    <dl class="dlsty2">
    <dt><a href="http://web.kma.go.kr/aboutkma/director/greeting.jsp"><img alt="기상청소개" src="/images/main/img_totalm_t5.gif"/></a></dt>
    <dd>
    <ul>
    <li><a href="http://web.kma.go.kr/aboutkma/director/greeting.jsp">청/차장소개</a></li>
    <li><a href="http://web.kma.go.kr/aboutkma/mission/mission.jsp">미션·비전</a></li>
    <li><a href="http://web.kma.go.kr/aboutkma/organization/quota.jsp">조직·직원</a></li>
    <li><a href="http://web.kma.go.kr/aboutkma/biz/observation01.jsp">주요업무</a></li>
    <li><a href="http://web.kma.go.kr/aboutkma/intro/regional_index.jsp">소속·산하기관소개</a></li>
    <li><a href="http://web.kma.go.kr/aboutkma/publicity/catalog.jsp">홍보실</a></li>
    <li><a href="http://web.kma.go.kr/aboutkma/location/map.jsp">찾아오시는 길</a></li>
    <li><a href="http://web.kma.go.kr/aboutkma/website/link_list.jsp">관련사이트</a></li>
    </ul>
    </dd>
    </dl>
    </li>
    </ul>
    <p><a href="#issue_search" onclick="displayOff('menuopen'); return false;" onkeypress=""><img alt="전체메뉴닫기" src="/images/main/img_totalm_close.gif"/></a></p>
    </div>
    <script type="text/javascript">
    				  //content toggle
    				 function showBx(id)
    				 {
    					 var bx = document.getElementById(id);
    					 if (bx.style.display =='block')
    					 {
    						 bx.style.display='none';
    					 }
    					 else
    					 {
    						bx.style.display='block';
    					 }
    				 } 
    				</script>
    <div class="usermenu">
    <h2><a href="#usermenu" onclick="showUserMenu(); return false;"><img alt="사용자메뉴" src="/images/main/btn_usermenu.gif"/></a></h2>
    <div class="wrap_usermenu" id="usermenu" style="display:none;">
    <div class="usermenu_top">
    <h3><img alt="사용자메뉴" src="/images/main/h3_usemenu.gif"/></h3>
    <p class="btn"><a href="http://web.kma.go.kr/mypage/location.jsp"><img alt="사용자메뉴관리" src="/images/main/btn_usermenu_edit.gif"/></a> <a href="#usermenu" onclick="showUserMenu(); return false;"><img alt="닫기" src="/images/main/btn_usermenu_close.gif"/></a></p>
    </div>
    <p class="comment">기상청 홈페이지의 방대한 정보를 나만의 메뉴로 관리 해보세요.</p>
    <ul id="usermenu_list">
    <li>나만의 메뉴는 총 10개까지 등록하실 수 있습니다.</li>
    <li>각 페이지 상단의 ‘사용자메뉴추가’ 버튼을 이용, 추가되며 메뉴 순서는 등록 한 순서대로 제공됩니다.</li>
    <li>사용자 메뉴를 사용함으로써 나만의 메뉴로 원하시는 정보에 빠르게 접근할 수 있습니다. </li>
    </ul>
    </div>
    </div>
    </div>
    <hr/>
    <div id="container"><a id="gocontent" name="gocontent"></a>
    <div class="snb" id="sub-menu5">
    <h3><img alt="관측자료" src="/images/weather/common/snb_h3_5.gif"/></h3>
    <ul>
    <li id="menu5-1"><a href="http://www.kma.go.kr/weather/observation/currentweather.jsp"><img alt="지상관측자료" src="/images/weather/common/snb4_1.gif"/></a>
    <ul>
    <li id="menu5-1-1"><a class="on" href="http://www.kma.go.kr/weather/observation/currentweather.jsp">도시별 현재날씨</a></li>
    <li id="menu5-1-2"><a href="http://www.kma.go.kr/weather/observation/dashboard.jsp">날씨상황판</a></li>
    <li class="twoline" id="menu5-1-3"><a href="http://www.kma.go.kr/weather/observation/aws_table_popup.jsp" onclick="window.open(this.href, 'popName', 'width=1240,height=700,scrollbars=yes,resizable=yes'); return false;" title="새창 (팝업에서 열림)">지역별상세관측자료(AWS)</a></li>
    <!--<li id="menu5-1-3"><a href="/weather/observation/awos_popup.jsp" onclick="window.open(this.href, 'popName', 'width=1240,height=700,scrollbars=yes,resizable=yes'); return false;" title="새창 (팝업에서 열림)">유관기관관측자료</a></li>-->
    <li id="menu5-1-4"><a href="http://www.kma.go.kr/weather/climate/past_cal.jsp">과거자료</a></li>
    </ul>
    </li>
    <li id="menu5-3"><a href="http://web.kma.go.kr/weather/observation/flower_photo.jsp"><img alt="계절관측자료" src="/images/weather/common/snb4_3.gif"/></a>
    <ul>
    <li id="menu5-3-1" style="height:32px;line-height:normal;"><a href="http://web.kma.go.kr/weather/observation/flower_photo.jsp">봄꽃개화현황<br/>(벚꽃, 철쭉)</a></li>
    <!-- <li id="menu5-3-2"><a href="http://web.kma.go.kr/weather/observation/maple_photo.jsp">유명산 단풍현황</a></li> -->
    </ul>
    </li>
    <li id="menu5-2"><a href="http://www.kma.go.kr/weather/observation/marine_buoy.jsp"><img alt="바다관측자료" src="/images/weather/common/snb4_2.gif"/></a>
    <ul>
    <li id="menu5-2-1"><a href="http://www.kma.go.kr/weather/observation/marine_buoy.jsp">국내부이</a></li>
    <li id="menu5-2-11"><a href="http://www.kma.go.kr/weather/observation/marine_buoy_cosmos.jsp">파고부이</a></li>
    <li id="menu5-2-2"><a href="http://www.kma.go.kr/weather/observation/marine_beacon.jsp">국내등표</a></li>
    <!--<li id="menu5-2-3"><a href="http://www.kma.go.kr/weather/observation/marine_lighthouse.jsp">국내등대</a></li>
    					<li id="menu5-2-4"><a href="http://www.kma.go.kr/weather/observation/marine_asia.jsp">아시아연안</a></li>
    					<li id="menu5-2-5"><a href="http://www.kma.go.kr/weather/observation/marine_shipobserv.jsp">선박관측</a></li>
    					<li id="menu5-2-6"><a href="http://www.kma.go.kr/weather/observation/marine_onshorewind.jsp">위성관측</a></li>
    					<li id="menu5-2-7"><a href="http://www.kma.go.kr/weather/observation/marine_fax01.jsp">영역기상방송</a></li>
    					<li id="menu5-2-8"><a href="http://www.kma.go.kr/weather/observation/marine_information.jsp">항해안전정보</a></li>
    					<li id="menu5-2-9"><a href="http://www.kma.go.kr/weather/observation/marine_contents02.jsp">간만조정보</a></li>
    					<li id="menu5-2-10" class="twoline"><a href="http://www.kma.go.kr/weather/observation/marine_vos01.jsp">자원관측선박(VOS)제도</a></li> -->
    </ul>
    </li>
    </ul>
    </div>
    <hr/>
    <script type="text/javascript">initSubmenuByMenuId("1","7","1","1","");</script>
    <div class="width2" id="wrap_content">
    <p id="location"><a href="../../index.jsp">홈</a>
    
    	
    	
    		
    			 &gt;  <a href="/weather/main.jsp">날씨</a>
    		
    		
    	
    
    	
    	
    		
    			 &gt;  <a href="/weather/observation/currentweather.jsp">관측자료</a>
    		
    		
    	
    
    	
    	
    		
    			 &gt;  <a href="/weather/observation/currentweather.jsp">지상관측자료</a>
    		
    		
    	
    
    	
    	
    		
    		
    			 &gt;  <strong id="leaf-page-title">도시별 현재날씨</strong>
    <span id="location_text" style="display:none">|날씨|관측자료|지상관측자료|도시별 현재날씨</span>
    </p>
    <div id="title">
    <h4><img alt="지상관측자료" src="../../images/weather/observation/h4_1_1.gif"/></h4>
    <h5><img alt="도시별 현재날씨" src="../../images/weather/observation/h5_1_1.gif"/></h5>
    <script type="text/javascript">
    //<!--
    	
    		function goScrap(){
    			var scrapForm=document.scrapForm;
    			if(confirm("'"+scrapForm.title1.value+"'의 '"+scrapForm.title2.value+"' 페이지를 스크랩 하시겠습니까?")==true){
    				var scrapUrl = scrapForm.scrapUrl.value;
    				if (scrapUrl.indexOf("/weather/") == 0 )
    				{
    					scrapForm.scrapUrl.value = scrapUrl.replace("/weather/","http://www.kma.go.kr/weather/");
    				}
    				return true;
    			}else{
    				return false;
    			}
    		}
    	
    //-->
    </script>
    <ul class="button">
    <li class="print"><a href="#addUserMenu" onclick="addUserMenu(); return false;"><img alt="사용자메뉴추가" src="/images/common/btn_user_add.gif"/></a></li>
    <li class="print"><a href="/HELP/html/help_sfc001.jsp" onclick="window.open(this.href,'helpwindow','width=1000px, height=703px, scrollbars=no'); return false;" target="_blank" title="새 창 열림"><img alt="도움말" src="/images/common/btn_help.gif"/></a></li>
    <!-- 버튼추가시작 -->
    <!-- 버튼추가끝 -->
    <li class="print">
    <form action="http://web.kma.go.kr/mypage/favorite_action.jsp" method="post" name="scrapForm" onsubmit="return goScrap();">
    <input name="mode" type="hidden" value="write"/>
    <input name="title1" type="hidden" value="날씨"/>
    <input name="title2" type="hidden" value="도시별 현재날씨"/>
    <input name="scrapUrl" type="hidden" value="/weather/observation/currentweather.jsp"/>
    <input alt="스크랩하기" src="/images/common/btn_scrap.gif" type="image"/>
    </form>
    </li>
    <li><a href="/weather/observation/currentweather.jsp;jsessionid=uKCVm7S9d8AkQHDEp54iNhLgzXYTnGGv0faI7uPPquovofFk9MH5kAexIuw2paP8?printable=true&amp;amp;" onclick="window.open(this.href,'helpwindow','width=933px, height=703px, scrollbars=yes, resizable=yes'); return false;" target="_blank" title="새창에서 열림"><img alt="인쇄하기" src="/images/common/btn_print.gif"/></a></li>
    </ul>
    </div>
    <div id="content_weather"><a id="content" name="content"></a>
    <!-- content :Start -->
    <div class="comment_gray">
    <p>실황표로 정리되어 있는 기상청 각 지상관측 지점의 시간별 관측 실황자료를 조회하실 수 있습니다.</p>
    <dl>
    <dt>* 조회 시 참고사항</dt>
    <dd>해당 자료는 실시간 관측된 자료이며, 현지 사정에 의해 잘못된 값이 표출 될 수 있으므로, 증명자료로 사용 될 수 없습니다.</dd>
    <dd>지점명을 클릭하시면 시간별 현황을 확인할 수 있습니다.</dd>
    </dl>
    </div>
    <div class="distibution_search3">
    <form action="currentweather.jsp" method="get" name="distibution_search">
    <input name="auto_man" type="hidden" value="m"/>
    <fieldset>
    <legend>도시별 현재날씨 검색</legend>
    <p><img alt="선택" src="../../images/weather/observation/ti_choice.gif"/></p>
    <label class="hid" for="observation_select">시간자료, 일자료 검색 선택사항</label>
    <select id="observation_select" name="type">
    <option value="t99">&lt;시간자료&gt;</option>
    <option selected="selected" value="t99">종합</option>
    <option value="t11">기온</option>
    <option value="t12">이슬점</option>
    <option value="t13">상대습도</option>
    <option value="t48">일강수량</option>
    <option value="t19">신적설</option>
    <option value="t20">적설</option>
    <option value="t01">풍향</option>
    <option value="t02">풍속</option>
    <option value="t24">전운량</option>
    <option value="t08">해면기압</option>
    </select>
    <input alt="선택" class="btn" src="../../images/weather/forecast/btn_select.gif" type="image"/>
    <label class="hid" for="observation_text">시간대 입력</label>
    <input class="time" id="observation_text" name="tm" type="text" value="2017.05.17.14:00"/>
    <input alt="검색" class="btn" src="../../images/weather/forecast/btn_search.gif" type="image"/>
    </fieldset>
    <fieldset class="town_search">
    <legend>이전자료 검색</legend>
    <p><img alt="이전자료" src="../../images/weather/observation/ti_prev.gif"/></p>
    <ul class="ul_prev">
    <li class="bg_black"><a href="/weather/observation/currentweather.jsp;jsessionid=uKCVm7S9d8AkQHDEp54iNhLgzXYTnGGv0faI7uPPquovofFk9MH5kAexIuw2paP8?type=t99&amp;mode=0&amp;stn=0&amp;auto_man=m&amp;tm=2017.05.17.14:00&amp;dtm=-12">12시간 전</a></li>
    <li class="bg_black"><a href="/weather/observation/currentweather.jsp;jsessionid=uKCVm7S9d8AkQHDEp54iNhLgzXYTnGGv0faI7uPPquovofFk9MH5kAexIuw2paP8?type=t99&amp;mode=0&amp;stn=0&amp;auto_man=m&amp;tm=2017.05.17.14:00&amp;dtm=-3">3시간 전</a></li>
    <li class="bg_black"><a href="/weather/observation/currentweather.jsp;jsessionid=uKCVm7S9d8AkQHDEp54iNhLgzXYTnGGv0faI7uPPquovofFk9MH5kAexIuw2paP8?type=t99&amp;mode=0&amp;stn=0&amp;auto_man=m&amp;tm=2017.05.17.14:00&amp;dtm=-1">1시간 전</a></li>
    <li class="bg_orange"><a href="/weather/observation/currentweather.jsp;jsessionid=uKCVm7S9d8AkQHDEp54iNhLgzXYTnGGv0faI7uPPquovofFk9MH5kAexIuw2paP8?type=t99&amp;mode=0&amp;stn=0&amp;auto_man=a">현재</a></li>
    <li class="bg_black"><a href="/weather/observation/currentweather.jsp;jsessionid=uKCVm7S9d8AkQHDEp54iNhLgzXYTnGGv0faI7uPPquovofFk9MH5kAexIuw2paP8?type=t99&amp;mode=0&amp;stn=0&amp;auto_man=m&amp;tm=2017.05.17.14:00&amp;dtm=1">1시간 후</a></li>
    <li class="bg_black"><a href="/weather/observation/currentweather.jsp;jsessionid=uKCVm7S9d8AkQHDEp54iNhLgzXYTnGGv0faI7uPPquovofFk9MH5kAexIuw2paP8?type=t99&amp;mode=0&amp;stn=0&amp;auto_man=m&amp;tm=2017.05.17.14:00&amp;dtm=3">3시간 후</a></li>
    <li class="bg_black"><a href="/weather/observation/currentweather.jsp;jsessionid=uKCVm7S9d8AkQHDEp54iNhLgzXYTnGGv0faI7uPPquovofFk9MH5kAexIuw2paP8?type=t99&amp;mode=0&amp;stn=0&amp;auto_man=m&amp;tm=2017.05.17.14:00&amp;dtm=12">12시간 후</a></li>
    </ul>
    </fieldset>
    </form>
    </div>
    <p class="table_topinfo"><img alt="기상실황표" src="../../images/weather/observation/ic_current.gif"/>2017.05.17.14:00</p>
    <table class="table_develop3" summary="기상실황표로 지점, 날씨, 기온, 강수, 바람, 기압등을 안내한 표입니다.">
    <caption>기상실황표</caption>
    <colgroup>
    <col width="14%"/>
    <col width="12%"/>
    <col width="7%"/>
    <col width="5%"/>
    <col width="8%"/>
    <col width="5%"/>
    <col width="6%"/>
    <col width="5%"/>
    <col width="8%"/>
    <col width="5%"/>
    <col width="8%"/>
    <col width="6%"/>
    <col width="*%"/>
    </colgroup>
    <thead>
    <tr class="table_header" id="table_header1">
    <th class="top_line" rowspan="2" scope="col">
    		지점
    		</th>
    <th class="top_line" colspan="4" scope="col">날씨</th>
    <th class="top_line" colspan="3" scope="col">기온(℃)</th>
    <th class="top_line" colspan="2" scope="col">강수</th>
    <th class="top_line" colspan="2" scope="col">바람</th>
    <th class="top_line" scope="col">기압(hPa)</th>
    </tr>
    <tr class="table_header" id="table_header2">
    <th class="nm" scope="col">현재일기 </th>
    <th class="nm" scope="col">시정<br/>km</th>
    <th class="nm" scope="col">운량<br/>1/10</th>
    <th class="nm" scope="col">중하운량</th>
    <th class="nm" scope="col">현재<br/>기온</th>
    <th class="nm" scope="col">이슬점<br/>온도</th>
    <th class="nm" scope="col">불쾌<br/>지수</th>
    <th class="nm" scope="col">일강수<br/>mm</th>
    <th class="nm" scope="col">습도<br/>%</th>
    <th class="nm" scope="col">풍향 </th>
    <th class="nm" scope="col">풍속<br/>m/s</th>
    <th class="nm" scope="col">해면<br/>기압</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=108">서울</a></td>
    <td>맑음</td>
    <td>18.9</td>
    <td>1</td>
    <td>1</td>
    <td>25.6</td>
    <td>6.7</td>
    <td>70</td>
    <td> </td>
    <td>30</td>
    <td>서남서</td>
    <td>2.1</td>
    <td>1010.1</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=102">백령도</a></td>
    <td>구름조금</td>
    <td>19.8</td>
    <td>3</td>
    <td>0</td>
    <td>18.4</td>
    <td>10.9</td>
    <td>64</td>
    <td> </td>
    <td>62</td>
    <td>남서</td>
    <td>5.2</td>
    <td>1011.2</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=112">인천</a></td>
    <td>맑음</td>
    <td>20 이상</td>
    <td>0</td>
    <td>0</td>
    <td>20.8</td>
    <td>11.1</td>
    <td>67</td>
    <td> </td>
    <td>54</td>
    <td>서남서</td>
    <td>2.9</td>
    <td>1011.0</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=119">수원</a></td>
    <td>구름조금</td>
    <td>12.6</td>
    <td>3</td>
    <td>3</td>
    <td>25.0</td>
    <td>10.8</td>
    <td>71</td>
    <td> </td>
    <td>41</td>
    <td>북서</td>
    <td>2.4</td>
    <td>1010.6</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=98">동두천</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>24.9</td>
    <td>7.9</td>
    <td>70</td>
    <td> </td>
    <td>34</td>
    <td>서북서</td>
    <td>1.7</td>
    <td>1009.9</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=99">파주</a></td>
    <td> </td>
    <td>17.5</td>
    <td> </td>
    <td> </td>
    <td>25.1</td>
    <td>10.1</td>
    <td>71</td>
    <td> </td>
    <td>39</td>
    <td>서남서</td>
    <td>2.2</td>
    <td>1010.6</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=201">강화</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>20.0</td>
    <td>10.9</td>
    <td>66</td>
    <td> </td>
    <td>56</td>
    <td>서남서</td>
    <td>5.0</td>
    <td>1011.3</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=202">양평</a></td>
    <td> </td>
    <td>19.9</td>
    <td> </td>
    <td> </td>
    <td>25.5</td>
    <td>7.5</td>
    <td>70</td>
    <td> </td>
    <td>32</td>
    <td>서북서</td>
    <td>2.9</td>
    <td>1009.9</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=203">이천</a></td>
    <td> </td>
    <td>19.6</td>
    <td> </td>
    <td> </td>
    <td>25.6</td>
    <td>5.7</td>
    <td>70</td>
    <td> </td>
    <td>28</td>
    <td>북서</td>
    <td>2.9</td>
    <td>1010.0</td>
    </tr>
    <tr class="table_subheader">
    <th class="nm" scope="col">지점</th>
    <th class="nm" scope="col">현재일기</th>
    <th class="nm" scope="col">시정</th>
    <th class="nm" scope="col">운량</th>
    <th class="nm" scope="col">중하운량</th>
    <th class="nm" scope="col">현재기온</th>
    <th class="nm" scope="col">이슬점온도</th>
    <th class="nm" scope="col">불쾌지수</th>
    <th class="nm" scope="col">일강수</th>
    <th class="nm" scope="col">습도</th>
    <th class="nm" scope="col">풍향</th>
    <th class="nm" scope="col">풍속</th>
    <th class="nm" scope="col">해면기압</th>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=93">북춘천</a></td>
    <td>구름조금</td>
    <td>20 이상</td>
    <td>3</td>
    <td>3</td>
    <td>24.6</td>
    <td>8.5</td>
    <td>70</td>
    <td> </td>
    <td>36</td>
    <td>남남서</td>
    <td>3.4</td>
    <td>1008.9</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=104">북강릉</a></td>
    <td>맑음</td>
    <td>20 이상</td>
    <td>1</td>
    <td>1</td>
    <td>19.9</td>
    <td>10.8</td>
    <td>65</td>
    <td> </td>
    <td>56</td>
    <td>동</td>
    <td>3.1</td>
    <td>1010.3</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=115">울릉도</a></td>
    <td>구름많음</td>
    <td>20 이상</td>
    <td>7</td>
    <td>7</td>
    <td>16.8</td>
    <td>12.7</td>
    <td>62</td>
    <td> </td>
    <td>77</td>
    <td>동</td>
    <td>1.7</td>
    <td>1012.1</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=90">속초</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>19.1</td>
    <td>14.5</td>
    <td>65</td>
    <td> </td>
    <td>75</td>
    <td>남동</td>
    <td>2.9</td>
    <td>1010.4</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=95">철원</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>23.9</td>
    <td>8.3</td>
    <td>69</td>
    <td> </td>
    <td>37</td>
    <td>북북서</td>
    <td>2.2</td>
    <td>1009.5</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=100">대관령</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>17.9</td>
    <td>7.0</td>
    <td>62</td>
    <td> </td>
    <td>49</td>
    <td>동</td>
    <td>3.3</td>
    <td>1008.2</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=101">춘천</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>25.7</td>
    <td>10.6</td>
    <td>71</td>
    <td> </td>
    <td>39</td>
    <td>남서</td>
    <td>2.1</td>
    <td>1009.2</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=105">강릉</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>22.7</td>
    <td>8.7</td>
    <td>68</td>
    <td> </td>
    <td>41</td>
    <td>남남동</td>
    <td>2.1</td>
    <td>1010.3</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=106">동해</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>19.5</td>
    <td>15.3</td>
    <td>66</td>
    <td> </td>
    <td>77</td>
    <td>동남동</td>
    <td>3.6</td>
    <td>1010.7</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=114">원주</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>23.4</td>
    <td>7.4</td>
    <td>68</td>
    <td> </td>
    <td>36</td>
    <td>서</td>
    <td>1.6</td>
    <td>1008.8</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=121">영월</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>24.2</td>
    <td>7.3</td>
    <td>69</td>
    <td> </td>
    <td>34</td>
    <td>서남서</td>
    <td>3.1</td>
    <td>1008.2</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=211">인제</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>24.3</td>
    <td>6.0</td>
    <td>69</td>
    <td> </td>
    <td>31</td>
    <td>남남동</td>
    <td>2.7</td>
    <td>1008.3</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=212">홍천</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>25.4</td>
    <td>3.9</td>
    <td>70</td>
    <td> </td>
    <td>25</td>
    <td>서</td>
    <td>3.4</td>
    <td>1008.9</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=216">태백</a></td>
    <td> </td>
    <td>19.9</td>
    <td> </td>
    <td> </td>
    <td>19.6</td>
    <td>6.6</td>
    <td>64</td>
    <td> </td>
    <td>43</td>
    <td>북동</td>
    <td>3.6</td>
    <td>1007.9</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=217">정선군</a></td>
    <td> </td>
    <td>11.2</td>
    <td> </td>
    <td> </td>
    <td>23.0</td>
    <td>5.4</td>
    <td>68</td>
    <td> </td>
    <td>32</td>
    <td>북</td>
    <td>0.6</td>
    <td>1008.4</td>
    </tr>
    <tr class="table_subheader">
    <th class="nm" scope="col">지점</th>
    <th class="nm" scope="col">현재일기</th>
    <th class="nm" scope="col">시정</th>
    <th class="nm" scope="col">운량</th>
    <th class="nm" scope="col">중하운량</th>
    <th class="nm" scope="col">현재기온</th>
    <th class="nm" scope="col">이슬점온도</th>
    <th class="nm" scope="col">불쾌지수</th>
    <th class="nm" scope="col">일강수</th>
    <th class="nm" scope="col">습도</th>
    <th class="nm" scope="col">풍향</th>
    <th class="nm" scope="col">풍속</th>
    <th class="nm" scope="col">해면기압</th>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=129">서산</a></td>
    <td>맑음</td>
    <td>20 이상</td>
    <td>2</td>
    <td>2</td>
    <td>23.6</td>
    <td>12.2</td>
    <td>70</td>
    <td> </td>
    <td>49</td>
    <td>서남서</td>
    <td>2.0</td>
    <td>1011.6</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=131">청주</a></td>
    <td>구름조금</td>
    <td>20 이상</td>
    <td>4</td>
    <td>4</td>
    <td>24.3</td>
    <td>6.9</td>
    <td>69</td>
    <td> </td>
    <td>33</td>
    <td>북서</td>
    <td>2.7</td>
    <td>1010.0</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=133">대전</a></td>
    <td>맑음</td>
    <td>20 이상</td>
    <td>2</td>
    <td>2</td>
    <td>25.1</td>
    <td>9.3</td>
    <td>71</td>
    <td> </td>
    <td>37</td>
    <td>북북서</td>
    <td>1.8</td>
    <td>1010.5</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=127">충주</a></td>
    <td> </td>
    <td>18.5</td>
    <td> </td>
    <td> </td>
    <td>24.4</td>
    <td>6.6</td>
    <td>69</td>
    <td> </td>
    <td>32</td>
    <td>북서</td>
    <td>3.2</td>
    <td>1009.7</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=135">추풍령</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>23.0</td>
    <td>6.7</td>
    <td>68</td>
    <td> </td>
    <td>35</td>
    <td>서남서</td>
    <td>1.6</td>
    <td>1009.4</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=177">홍성(예)</a></td>
    <td> </td>
    <td> </td>
    <td> </td>
    <td> </td>
    <td>24.3</td>
    <td>11.9</td>
    <td>70</td>
    <td> </td>
    <td>46</td>
    <td>북동</td>
    <td>3.4</td>
    <td>1010.1</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=221">제천</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>24.2</td>
    <td>6.4</td>
    <td>69</td>
    <td> </td>
    <td>32</td>
    <td>남서</td>
    <td>3.6</td>
    <td>1007.8</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=226">보은</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>23.7</td>
    <td>4.0</td>
    <td>68</td>
    <td> </td>
    <td>28</td>
    <td>북</td>
    <td>2.9</td>
    <td>1009.8</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=232">천안</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>23.5</td>
    <td>7.1</td>
    <td>68</td>
    <td> </td>
    <td>35</td>
    <td>서</td>
    <td>3.2</td>
    <td>1010.3</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=235">보령</a></td>
    <td> </td>
    <td>19.4</td>
    <td> </td>
    <td> </td>
    <td>21.4</td>
    <td>12.2</td>
    <td>67</td>
    <td> </td>
    <td>56</td>
    <td>남서</td>
    <td>1.9</td>
    <td>1011.4</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=236">부여</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>23.9</td>
    <td>8.3</td>
    <td>69</td>
    <td> </td>
    <td>37</td>
    <td>남남동</td>
    <td>0.9</td>
    <td>1010.7</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=238">금산</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>23.7</td>
    <td>5.0</td>
    <td>68</td>
    <td> </td>
    <td>30</td>
    <td>북</td>
    <td>2.4</td>
    <td>1009.9</td>
    </tr>
    <tr class="table_subheader">
    <th class="nm" scope="col">지점</th>
    <th class="nm" scope="col">현재일기</th>
    <th class="nm" scope="col">시정</th>
    <th class="nm" scope="col">운량</th>
    <th class="nm" scope="col">중하운량</th>
    <th class="nm" scope="col">현재기온</th>
    <th class="nm" scope="col">이슬점온도</th>
    <th class="nm" scope="col">불쾌지수</th>
    <th class="nm" scope="col">일강수</th>
    <th class="nm" scope="col">습도</th>
    <th class="nm" scope="col">풍향</th>
    <th class="nm" scope="col">풍속</th>
    <th class="nm" scope="col">해면기압</th>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=146">전주</a></td>
    <td>구름조금</td>
    <td>19.2</td>
    <td>3</td>
    <td>3</td>
    <td>24.9</td>
    <td>11.8</td>
    <td>71</td>
    <td> </td>
    <td>44</td>
    <td>서북서</td>
    <td>2.0</td>
    <td>1010.4</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=156">광주</a></td>
    <td>구름조금</td>
    <td>20 이상</td>
    <td>5</td>
    <td>5</td>
    <td>24.0</td>
    <td>7.5</td>
    <td>69</td>
    <td> </td>
    <td>35</td>
    <td>동북동</td>
    <td>1.8</td>
    <td>1010.5</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=165">목포</a></td>
    <td>맑음</td>
    <td>20 이상</td>
    <td>0</td>
    <td>0</td>
    <td>22.8</td>
    <td>12.1</td>
    <td>69</td>
    <td> </td>
    <td>51</td>
    <td>북북서</td>
    <td>4.4</td>
    <td>1011.6</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=168">여수</a></td>
    <td>맑음</td>
    <td>20 이상</td>
    <td>1</td>
    <td>0</td>
    <td>22.8</td>
    <td>11.5</td>
    <td>69</td>
    <td> </td>
    <td>49</td>
    <td>남남서</td>
    <td>5.1</td>
    <td>1010.5</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=169">흑산도</a></td>
    <td>박무</td>
    <td>5.7</td>
    <td>0</td>
    <td>0</td>
    <td>19.2</td>
    <td>18.0</td>
    <td>66</td>
    <td> </td>
    <td>93</td>
    <td>북</td>
    <td>1.6</td>
    <td>1012.2</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=140">군산</a></td>
    <td> </td>
    <td>17.7</td>
    <td> </td>
    <td> </td>
    <td>21.8</td>
    <td>12.3</td>
    <td>68</td>
    <td> </td>
    <td>55</td>
    <td>서남서</td>
    <td>3.8</td>
    <td>1011.4</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=170">완도</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>23.2</td>
    <td>10.5</td>
    <td>69</td>
    <td> </td>
    <td>45</td>
    <td>동남동</td>
    <td>1.7</td>
    <td>1010.7</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=172">고창</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>22.7</td>
    <td>12.6</td>
    <td>69</td>
    <td> </td>
    <td>53</td>
    <td>북서</td>
    <td>5.8</td>
    <td>1011.4</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=174">순천</a></td>
    <td> </td>
    <td>18.5</td>
    <td> </td>
    <td> </td>
    <td>22.5</td>
    <td>8.2</td>
    <td>68</td>
    <td> </td>
    <td>40</td>
    <td>서</td>
    <td>2.7</td>
    <td>1009.4</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=175">진도(첨찰산)</a></td>
    <td> </td>
    <td> </td>
    <td> </td>
    <td> </td>
    <td>22.2</td>
    <td>10.6</td>
    <td>68</td>
    <td> </td>
    <td>48</td>
    <td>북북동</td>
    <td>3.4</td>
    <td>1010.0</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=243">부안</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>22.9</td>
    <td>9.9</td>
    <td>69</td>
    <td> </td>
    <td>44</td>
    <td>서북서</td>
    <td>3.3</td>
    <td>1011.7</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=244">임실</a></td>
    <td> </td>
    <td>15.3</td>
    <td> </td>
    <td> </td>
    <td>22.8</td>
    <td>8.4</td>
    <td>68</td>
    <td> </td>
    <td>40</td>
    <td>북</td>
    <td>1.3</td>
    <td>1010.0</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=245">정읍</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>23.8</td>
    <td>11.8</td>
    <td>70</td>
    <td> </td>
    <td>47</td>
    <td>북</td>
    <td>3.3</td>
    <td>1010.9</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=247">남원</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>23.8</td>
    <td>7.4</td>
    <td>69</td>
    <td> </td>
    <td>35</td>
    <td>서북서</td>
    <td>2.5</td>
    <td>1009.0</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=248">장수</a></td>
    <td> </td>
    <td>19.6</td>
    <td> </td>
    <td> </td>
    <td>22.0</td>
    <td>4.9</td>
    <td>67</td>
    <td> </td>
    <td>33</td>
    <td>북</td>
    <td>4.2</td>
    <td>1009.0</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=251">고창군</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>23.7</td>
    <td>12.0</td>
    <td>70</td>
    <td> </td>
    <td>48</td>
    <td>북서</td>
    <td>3.3</td>
    <td>1010.7</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=252">영광군</a></td>
    <td> </td>
    <td>18.8</td>
    <td> </td>
    <td> </td>
    <td>22.4</td>
    <td>8.1</td>
    <td>68</td>
    <td> </td>
    <td>40</td>
    <td>북</td>
    <td>5.3</td>
    <td>1011.4</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=254">순창군</a></td>
    <td> </td>
    <td>11.9</td>
    <td> </td>
    <td> </td>
    <td>23.5</td>
    <td>8.3</td>
    <td>69</td>
    <td> </td>
    <td>38</td>
    <td>북서</td>
    <td>3.1</td>
    <td>1010.3</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=258">보성군</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>23.7</td>
    <td>6.8</td>
    <td>69</td>
    <td> </td>
    <td>34</td>
    <td>남남동</td>
    <td>2.3</td>
    <td>1010.8</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=259">강진군</a></td>
    <td> </td>
    <td>12.4</td>
    <td> </td>
    <td> </td>
    <td>24.1</td>
    <td>6.8</td>
    <td>69</td>
    <td> </td>
    <td>33</td>
    <td>북북동</td>
    <td>4.2</td>
    <td>1011.1</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=260">장흥</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>25.5</td>
    <td>8.0</td>
    <td>71</td>
    <td> </td>
    <td>33</td>
    <td>북</td>
    <td>3.9</td>
    <td>1010.2</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=261">해남</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>24.6</td>
    <td>10.0</td>
    <td>70</td>
    <td> </td>
    <td>40</td>
    <td>북북서</td>
    <td>2.3</td>
    <td>1010.8</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=262">고흥</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>24.4</td>
    <td>7.5</td>
    <td>69</td>
    <td> </td>
    <td>34</td>
    <td>북북서</td>
    <td>1.1</td>
    <td>1010.1</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=266">광양시</a></td>
    <td> </td>
    <td>14.6</td>
    <td> </td>
    <td> </td>
    <td>24.6</td>
    <td>11.1</td>
    <td>71</td>
    <td> </td>
    <td>43</td>
    <td>남남서</td>
    <td>2.1</td>
    <td>1009.3</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=268">진도군</a></td>
    <td> </td>
    <td>14.8</td>
    <td> </td>
    <td> </td>
    <td>21.9</td>
    <td>13.2</td>
    <td>68</td>
    <td> </td>
    <td>58</td>
    <td>북북서</td>
    <td>2.9</td>
    <td>1011.2</td>
    </tr>
    <tr class="table_subheader">
    <th class="nm" scope="col">지점</th>
    <th class="nm" scope="col">현재일기</th>
    <th class="nm" scope="col">시정</th>
    <th class="nm" scope="col">운량</th>
    <th class="nm" scope="col">중하운량</th>
    <th class="nm" scope="col">현재기온</th>
    <th class="nm" scope="col">이슬점온도</th>
    <th class="nm" scope="col">불쾌지수</th>
    <th class="nm" scope="col">일강수</th>
    <th class="nm" scope="col">습도</th>
    <th class="nm" scope="col">풍향</th>
    <th class="nm" scope="col">풍속</th>
    <th class="nm" scope="col">해면기압</th>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=184">제주</a></td>
    <td>맑음</td>
    <td>20 이상</td>
    <td>2</td>
    <td>0</td>
    <td>20.7</td>
    <td>12.6</td>
    <td>67</td>
    <td> </td>
    <td>60</td>
    <td>서북서</td>
    <td>3.7</td>
    <td>1012.4</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=185">고산</a></td>
    <td> </td>
    <td>18.7</td>
    <td> </td>
    <td> </td>
    <td>19.1</td>
    <td>14.3</td>
    <td>65</td>
    <td> </td>
    <td>74</td>
    <td>북북서</td>
    <td>5.8</td>
    <td>1012.2</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=188">성산</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>23.1</td>
    <td>5.9</td>
    <td>68</td>
    <td> </td>
    <td>33</td>
    <td>서북서</td>
    <td>3.8</td>
    <td>1011.1</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=189">서귀포</a></td>
    <td> </td>
    <td>18.8</td>
    <td> </td>
    <td> </td>
    <td>24.0</td>
    <td>10.6</td>
    <td>70</td>
    <td> </td>
    <td>43</td>
    <td>남</td>
    <td>2.5</td>
    <td>1010.5</td>
    </tr>
    <tr class="table_subheader">
    <th class="nm" scope="col">지점</th>
    <th class="nm" scope="col">현재일기</th>
    <th class="nm" scope="col">시정</th>
    <th class="nm" scope="col">운량</th>
    <th class="nm" scope="col">중하운량</th>
    <th class="nm" scope="col">현재기온</th>
    <th class="nm" scope="col">이슬점온도</th>
    <th class="nm" scope="col">불쾌지수</th>
    <th class="nm" scope="col">일강수</th>
    <th class="nm" scope="col">습도</th>
    <th class="nm" scope="col">풍향</th>
    <th class="nm" scope="col">풍속</th>
    <th class="nm" scope="col">해면기압</th>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=136">안동</a></td>
    <td>구름많음</td>
    <td>20 이상</td>
    <td>6</td>
    <td>6</td>
    <td>25.0</td>
    <td>7.1</td>
    <td>70</td>
    <td> </td>
    <td>32</td>
    <td>북서</td>
    <td>2.9</td>
    <td>1008.8</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=138">포항</a></td>
    <td>구름많음</td>
    <td>20 이상</td>
    <td>7</td>
    <td>7</td>
    <td>19.0</td>
    <td>16.0</td>
    <td>65</td>
    <td>0.0</td>
    <td>83</td>
    <td>북북동</td>
    <td>1.9</td>
    <td>1011.3</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=143">대구</a></td>
    <td>구름많음</td>
    <td>19.9</td>
    <td>6</td>
    <td>6</td>
    <td>25.7</td>
    <td>7.2</td>
    <td>71</td>
    <td> </td>
    <td>31</td>
    <td>북서</td>
    <td>2.2</td>
    <td>1009.2</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=152">울산</a></td>
    <td>뇌전 끝</td>
    <td>20 이상</td>
    <td>7</td>
    <td>5</td>
    <td>19.7</td>
    <td>14.0</td>
    <td>66</td>
    <td>0.2</td>
    <td>70</td>
    <td>동남동</td>
    <td>3.8</td>
    <td>1010.7</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=155">창원</a></td>
    <td>구름조금</td>
    <td>20 이상</td>
    <td>4</td>
    <td>4</td>
    <td>20.6</td>
    <td>13.3</td>
    <td>67</td>
    <td>0.0</td>
    <td>63</td>
    <td>남남동</td>
    <td>4.7</td>
    <td>1010.3</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=159">부산</a></td>
    <td>구름많음</td>
    <td>14.5</td>
    <td>8</td>
    <td>8</td>
    <td>20.2</td>
    <td>13.6</td>
    <td>66</td>
    <td> </td>
    <td>66</td>
    <td>동남동</td>
    <td>3.5</td>
    <td>1011.2</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=130">울진</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>17.6</td>
    <td>14.8</td>
    <td>63</td>
    <td> </td>
    <td>84</td>
    <td>남동</td>
    <td>3.4</td>
    <td>1011.7</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=137">상주</a></td>
    <td> </td>
    <td>14.5</td>
    <td> </td>
    <td> </td>
    <td>25.0</td>
    <td>7.1</td>
    <td>70</td>
    <td> </td>
    <td>32</td>
    <td>남남서</td>
    <td>1.7</td>
    <td>1009.3</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=162">통영</a></td>
    <td> </td>
    <td>17.1</td>
    <td> </td>
    <td> </td>
    <td>20.0</td>
    <td>14.5</td>
    <td>66</td>
    <td>0.0</td>
    <td>71</td>
    <td>남남동</td>
    <td>5.3</td>
    <td>1010.8</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=192">진주</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>23.8</td>
    <td>5.1</td>
    <td>68</td>
    <td> </td>
    <td>30</td>
    <td>서남서</td>
    <td>1.4</td>
    <td>1009.9</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=253">김해시</a></td>
    <td> </td>
    <td>15.7</td>
    <td> </td>
    <td> </td>
    <td>21.9</td>
    <td>13.7</td>
    <td>68</td>
    <td> </td>
    <td>60</td>
    <td>남동</td>
    <td>3.8</td>
    <td>1011.3</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=255">북창원</a></td>
    <td> </td>
    <td>17.6</td>
    <td> </td>
    <td> </td>
    <td>22.8</td>
    <td>11.8</td>
    <td>69</td>
    <td>0.0</td>
    <td>50</td>
    <td>남남서</td>
    <td>1.2</td>
    <td>1009.9</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=257">양산시</a></td>
    <td> </td>
    <td>12.7</td>
    <td> </td>
    <td> </td>
    <td>21.4</td>
    <td>14.0</td>
    <td>68</td>
    <td> </td>
    <td>63</td>
    <td>남동</td>
    <td>2.6</td>
    <td>1011.7</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=263">의령군</a></td>
    <td> </td>
    <td>9.2</td>
    <td> </td>
    <td> </td>
    <td>25.1</td>
    <td>10.5</td>
    <td>71</td>
    <td> </td>
    <td>40</td>
    <td>동</td>
    <td>2.5</td>
    <td>1009.7</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=264">함양군</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>23.3</td>
    <td>8.1</td>
    <td>69</td>
    <td> </td>
    <td>38</td>
    <td>정온</td>
    <td>0.2</td>
    <td>1009.4</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=271">봉화</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>22.0</td>
    <td>7.0</td>
    <td>67</td>
    <td>0.0</td>
    <td>38</td>
    <td>동남동</td>
    <td>2.4</td>
    <td>1008.4</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=272">영주</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>23.0</td>
    <td>7.1</td>
    <td>68</td>
    <td> </td>
    <td>36</td>
    <td>북서</td>
    <td>3.9</td>
    <td>1008.4</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=273">문경</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>25.5</td>
    <td>4.5</td>
    <td>70</td>
    <td> </td>
    <td>26</td>
    <td>북북서</td>
    <td>2.6</td>
    <td>1009.0</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=276">청송군</a></td>
    <td> </td>
    <td>7.0</td>
    <td> </td>
    <td> </td>
    <td>17.9</td>
    <td>12.5</td>
    <td>63</td>
    <td>1.0</td>
    <td>71</td>
    <td>동북동</td>
    <td>2.3</td>
    <td>1010.1</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=277">영덕</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>19.4</td>
    <td>10.6</td>
    <td>65</td>
    <td> </td>
    <td>57</td>
    <td>동남동</td>
    <td>4.0</td>
    <td>1011.6</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=278">의성</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>25.7</td>
    <td>4.1</td>
    <td>70</td>
    <td> </td>
    <td>25</td>
    <td>서남서</td>
    <td>2.3</td>
    <td>1009.1</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=279">구미</a></td>
    <td> </td>
    <td> </td>
    <td> </td>
    <td> </td>
    <td>25.7</td>
    <td>7.7</td>
    <td>71</td>
    <td> </td>
    <td>32</td>
    <td>북서</td>
    <td>2.2</td>
    <td>1009.7</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=281">영천</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>21.8</td>
    <td>9.9</td>
    <td>67</td>
    <td>0.0</td>
    <td>47</td>
    <td>동</td>
    <td>3.3</td>
    <td>1009.9</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=283">경주시</a></td>
    <td> </td>
    <td>14.2</td>
    <td> </td>
    <td> </td>
    <td>23.8</td>
    <td>12.4</td>
    <td>70</td>
    <td>0.1</td>
    <td>49</td>
    <td>동</td>
    <td>2.2</td>
    <td>1010.3</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=284">거창</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>22.7</td>
    <td>7.6</td>
    <td>68</td>
    <td> </td>
    <td>38</td>
    <td>남남서</td>
    <td>1.5</td>
    <td>1008.6</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=285">합천</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>25.1</td>
    <td>7.2</td>
    <td>70</td>
    <td> </td>
    <td>32</td>
    <td>서남서</td>
    <td>1.0</td>
    <td>1009.7</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=288">밀양</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>24.7</td>
    <td>7.7</td>
    <td>70</td>
    <td>0.0</td>
    <td>34</td>
    <td>서북서</td>
    <td>1.2</td>
    <td>1009.6</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=289">산청</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>24.8</td>
    <td>10.6</td>
    <td>71</td>
    <td> </td>
    <td>41</td>
    <td>서북서</td>
    <td>1.5</td>
    <td>1009.4</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=294">거제</a></td>
    <td> </td>
    <td>19.1</td>
    <td> </td>
    <td> </td>
    <td>23.1</td>
    <td>14.1</td>
    <td>70</td>
    <td> </td>
    <td>57</td>
    <td>남남서</td>
    <td>2.7</td>
    <td>1010.4</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=295">남해</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>24.5</td>
    <td>10.0</td>
    <td>70</td>
    <td> </td>
    <td>40</td>
    <td>남남동</td>
    <td>1.8</td>
    <td>1010.3</td>
    </tr>
    </tbody>
    </table>
    <!-- content :End -->
    <!-- content :End -->
    </div>
    </div>
    <div id="relation">
    <h3><img alt="바로가기서비스" src="/images/weather/common/tl_quick.gif"/></h3>
    <ul class="list" id="relation_list">
    <li class="sty1"><a href="http://www.kma.go.kr/weather/observation/currentweather.jsp"><img alt="현재날씨" src="/images/weather/common/btn_quick1.gif"/></a></li>
    <li><a href="http://www.kma.go.kr/weather/observation/past_cal.jsp"><img alt="지난날씨" src="/images/weather/common/btn_quick2.gif"/></a></li>
    <li class="sty1"><a href="http://www.kma.go.kr/weather/lifenindustry/life_jisu.jsp"><img alt="생활과산업" src="/images/weather/common/btn_quick9.gif"/></a></li>
    <li><a href="http://www.kma.go.kr/mini/marine/marine_integrate.jsp"><img alt="바다날씨" src="/images/weather/common/btn_quick4.gif"/></a></li>
    <li class="sty1"><a href="http://www.kma.go.kr/weather/forecast/mountain_01.jsp"><img alt="산악날씨" src="/images/weather/common/btn_quick5.gif"/></a></li>
    <li><a href="http://www.kma.go.kr/weather/earthquake_volcano/report.jsp"><img alt="지진/해일" src="/images/weather/common/btn_quick6.gif"/></a></li>
    <li class="sty1"><a href="http://www.kma.go.kr/weather/forecast/weekend.jsp"><img alt="주말날씨" src="/images/weather/common/btn_quick3.gif"/></a></li>
    <li><a href="http://www.kma.go.kr/weather/lifenindustry/currentworld.jsp"><img alt="세계날씨" src="/images/weather/common/btn_quick8.gif"/></a></li>
    <li class="sty1"><a href="http://amo.kma.go.kr/new/html/main/main.jsp" target="_blank" title="새창으로 열립니다."><img alt="공항날씨" src="/images/weather/common/btn_quick7.gif"/></a></li>
    <li><a href="http://www.weather.kr/index.jsp" target="_blank" title="새창으로 열립니다."><img alt="날씨ON" src="/images/weather/common/btn_quick10.gif"/></a></li>
    </ul>
    <ul class="relation_new">
    <li><a href="http://typ.kma.go.kr/" target="_blank" title="새창으로 열립니다"><img alt="국가태풍센터" src="/images/weather/common/img_relation_banner_05.jpg"/></a></li>
    <li><a href="http://www.climate.go.kr/index.html" target="_blank" title="새창으로 열립니다"><img alt="기후정보포털" src="/images/weather/common/img_relation_banner_06.jpg"/></a></li>
    <li><a href="http://data.kma.go.kr" target="_blank" title="새창으로 열립니다"><img alt="국가기후자료센터 바로가기" src="/images/main/banner_climate_center_3.jpg"/></a></li>
    <li><a href="http://nmsc.kma.go.kr" target="_blank" title="새창으로 열립니다"><img alt="국가기상위성센터" src="/images/weather/common/img_relation_banner_07.jpg"/></a></li>
    <!-- <li><a href="http://www.kma.go.kr/wid/eastasia/kor/weather/eastasia_weather.jsp" title="새창으로 열립니다" target="_blank"><img src="/images/weather/common/img_relation_new_1.gif" alt="한중일 날씨정보 : 동북아 날씨를 한눈에" /></a></li> -->
    </ul>
    </div>
    </div>
    <hr/>
    <div id="footer"><a id="gofooter" name="gofooter"></a>
    <div class="wrap_site_link">
    <h3 class="blind">부속사이트 안내</h3>
    <fieldset class="sitelink">
    <legend class="blind">관련사이트 링크</legend>
    <form action="/sitelink.jsp" method="get" name="sitelink1" target="_blank">
    <label class="blind" for="sitelink1">기상청소속기관 링크</label>
    <select id="sitelink1" name="link">
    <option label="기상청소속기관" selected="selected" value="">기상청소속기관</option>
    <option value="수도권기상청">수도권기상청</option>
    <option value="부산지방기상청">부산지방기상청</option>
    <option value="광주지방기상청">광주지방기상청</option>
    <option value="대전지방기상청">대전지방기상청</option>
    <option value="강원지방기상청">강원지방기상청</option>
    <option value="제주지방기상청">제주지방기상청</option>
    <option value="청주기상지청">청주기상지청</option>
    <option value="전주기상지청">전주기상지청</option>
    <option value="대구기상지청">대구기상지청</option>
    <option value="국가기상위성센터">국가기상위성센터</option>
    <option value="항공기상청">항공기상청</option>
    <option value="국립기상과학원">국립기상과학원</option>
    <option value="기상레이더센터">기상레이더센터</option>
    <option value="국가태풍센터">국가태풍센터</option>
    <option value="국가기상슈퍼컴퓨터센터">국가기상슈퍼컴퓨터센터</option>
    </select>
    <input alt="이동" src="/images/main/btn_move.gif" title="선택한 홈페이지로 이동 새창에서 열림" type="image"/>
    </form>
    <form action="/sitelink.jsp" method="get" name="sitelink2" target="_blank">
    <label class="blind" for="sitelink2">주요행정기관 바로가기</label>
    <select id="sitelink2" name="link">
    <option label="주요행정기관" selected="selected" value="">주요행정기관</option>
    <option value="청와대">청와대</option>
    <option value="국무총리실">국무총리실</option>
    <option value="감사원">감사원</option>
    <option value="국가정보원">국가정보원</option>
    <option value="방송통신위원회">방송통신위원회</option>
    <option value="국가인권위원회">국가인권위원회</option>
    <option value="공정거래위원회">공정거래위원회</option>
    <option value="금융위원회">금융위원회</option>
    <option value="국민권익위원회">국민권익위원회</option>
    <option value="국회사무처">국회사무처</option>
    <option value="">17부-----------------&gt;</option>
    <option value="기획재정부">기획재정부</option>
    <option value="미래창조과학부">미래창조과학부</option>
    <option value="교육부">교육부</option>
    <option value="외교부">외교부</option>
    <option value="통일부">통일부</option>
    <option value="법무부">법무부</option>
    <option value="국방부">국방부</option>
    <option value="행정자치부">행정자치부</option>
    <option value="문화체육관광부">문화체육관광부</option>
    <option value="농림축산식품부">농림축산식품부</option>
    <option value="산업통상자원부">산업통상자원부</option>
    <option value="보건복지부">보건복지부</option>
    <option value="환경부">환경부</option>
    <option value="고용노동부">고용노동부</option>
    <option value="여성가족부">여성가족부</option>
    <option value="국토교통부">국토교통부</option>
    <option value="해양수산부">해양수산부</option>
    <option value="">5처------------------&gt;</option>
    <option value="국민안전처">국민안전처</option>
    <option value="인사혁신처">인사혁신처</option>
    <option value="법제처">법제처</option>
    <option value="국가보훈처">국가보훈처</option>
    <option value="식품의약품안전처">식품의약품안전처</option>
    <option value="">16청-----------------&gt;</option>
    <option value="국세청">국세청</option>
    <option value="관세청">관세청</option>
    <option value="조달청">조달청</option>
    <option value="통계청">통계청</option>
    <option value="검찰청">검찰청</option>
    <option value="병무청">병무청</option>
    <option value="방위사업청">방위사업청</option>
    <option value="경찰청">경찰청</option>
    <option value="문화재청">문화재청</option>
    <option value="농촌진흥청">농촌진흥청</option>
    <option value="산림청">산림청</option>
    <option value="중소기업청">중소기업청</option>
    <option value="특허청">특허청</option>
    <option value="기상청">기상청</option>
    <option value="행정중심복합도시건설청">행정중심복합도시건설청</option>
    <option value="새만금개발청">새만금개발청</option>
    </select>
    <input alt="이동" src="/images/main/btn_move.gif" title="선택한 홈페이지로 이동 새창에서 열림" type="image"/>
    </form>
    <form action="/sitelink.jsp" method="get" name="sitelink3" target="_blank">
    <label class="blind" for="sitelink3">방재유관기관 바로가기</label>
    <select id="sitelink3" name="link">
    <option label="방재유관기관" selected="selected" value="">방재유관기관</option>
    <option value="서울종합방재센터">서울종합방재센터</option>
    <option value="국립재난안전연구원">국립재난안전연구원</option>
    <option value="한강홍수통제소">한강홍수통제소</option>
    <option value="중앙재난안전대책본부">중앙재난안전대책본부</option>
    <option value="대기오염도실시간공개">대기오염도실시간공개</option>
    <option value="국가수자원관리종합정보시스템">국가수자원관리종합정보시스템</option>
    </select>
    <input alt="이동" src="/images/main/btn_move.gif" title="선택한 홈페이지로 이동 새창에서 열림" type="image"/>
    </form>
    <form action="/sitelink.jsp" method="get" name="sitelink4" target="_blank">
    <label class="blind" for="sitelink4">외국기상청 바로가기</label>
    <select id="sitelink4" name="link">
    <option label="외국기상청" selected="selected" value="">외국기상청</option>
    <option value="미국">미국</option>
    <option value="일본">일본</option>
    <option value="중국">중국</option>
    <option value="영국">영국</option>
    <option value="프랑스">프랑스</option>
    <option value="세계기상기구WMO">세계기상기구WMO</option>
    </select>
    <input alt="이동" src="/images/main/btn_move.gif" title="선택한 홈페이지로 이동 새창에서 열림" type="image"/>
    </form>
    <form action="/sitelink.jsp" class="last" method="get" name="sitelink5" target="_blank">
    <label class="blind" for="sitelink5">기상관련단체  바로가기</label>
    <select class="last" id="sitelink5" name="link">
    <option label="기상관련단체" selected="selected" value="">기상관련단체</option>
    <option value="한국기상산업진흥원">한국기상산업진흥원</option>
    <option value="APEC기후센터">APEC기후센터</option>
    <option value="기상기술개발원">기상기술개발원</option>
    <option value="한국형수치예보모델개발사업단">한국형수치예보모델개발사업단</option>
    </select>
    <input alt="이동" src="/images/main/btn_move.gif" title="선택한 홈페이지로 이동 새창에서 열림" type="image"/>
    </form>
    </fieldset>
    </div>
    <p class="logo"><img alt="기상청" src="/images/common/footer_logo_1.gif"/></p>
    <div class="footer_right">
    <h3 class="blind">사이트 도우미</h3>
    <ul class="site_helper">
    <li><a href="http://web.kma.go.kr/global/footer/privacy.jsp"><img alt="개인정보 처리방침" src="/images/common/footer_link_1.gif"/></a></li>
    <li><a href="http://web.kma.go.kr/global/footer/siteinfo.jsp"><img alt="이용안내" src="/images/common/footer_link_2.gif"/></a></li>
    <li><a href="http://web.kma.go.kr/global/footer/copyright.jsp"><img alt="저작권보호 및 정책" src="/images/common/footer_link_3.gif"/></a></li>
    <li><a href="http://web.kma.go.kr/global/footer/accessibility.jsp"><img alt="웹접근성정책" src="/images/common/footer_link_4.gif"/></a></li>
    <li><a href="http://web.kma.go.kr/global/footer/return.jsp"><img alt="홈페이지오류·건의" src="/images/common/footer_link_5.gif"/></a></li>
    <li><a href="http://web.kma.go.kr/global/footer/telephone_1.jsp"><img alt="전화번호안내" src="/images/common/footer_link_6.gif"/></a></li>
    <li><a href="http://web.kma.go.kr/aboutkma/organization/personnel_list.jsp?schParent=1360001"><img alt="부서·직원찾기" src="/images/common/footer_link_7.gif"/></a></li>
    <li><a href="http://web.kma.go.kr/global/footer/viewer.jsp"><img alt="뷰어다운로드" src="/images/common/footer_link_8.gif"/></a></li>
    </ul>
    <h3 class="blind">연락처 및 저작권</h3>
    <address>
    <p><img alt="우. 07062 서울시 동작구 여의대방로16길 61(신대방 2동 460-18) 대표전화 (02)2181-0900 (평일 9:00~18:00, 야간휴일은 당직실 연결)" src="/images/common/footer_copyright_6.gif"/> </p>
    <p><img alt="본 홈페이지에 게시된 이메일 주소가 자동 수집되는 것을 거부하며, 이를 위반시 정보통신망법에 의해 처벌됨을 유념하시기 바랍니다." src="/images/common/footer_copyright_2.gif"/></p>
    </address>
    <p class="copyright"><img alt="Copyright © 2009 KMA. All Rights RESERVED. E-mail: webmasterkma@kma.go.kr" src="/images/common/footer_copyright_3.gif"/></p>
    <p class="call_center"><a href="/aboutkma/intro/callcenter_greetion.jsp"><img alt="기상콜센터 전국 국번없이 131" src="/images/common/footer_call131.gif"/></a></p>
    <p style="float: left;margin-left:756px; margin-top: -76px; "><img alt="공공누리 공공저작물 자유이용허락" height="35" src="/images/common/KOGL.jpg" width="90"/></p>
    <p style="float: right;margin-top: -49px;margin-right: 170px;"><a href="http://web.kma.go.kr/notify/notice/list.jsp?bid=gongzi&amp;mode=view&amp;num=1191851&amp;page=1&amp;field=&amp;text="><img alt="웹 접근성 인증 마크" src="/images/mark_wa.png"/></a></p>
    </div>
    </div>
    <!--<script type="text/javascript" src="/share/js/warninglayer.js"></script>-->
    <!-- START OF LOGGER TRACKING SCRIPT -->
    <!--<script type="text/javascript" src="/share/js/logger.js"></script>
    <noscript><img  alt="로그" src="http://logger.kma.go.kr/tracker.tsp?u=7&amp;js=N" width="0" height="0" /></noscript>-->
    <!-- END OF LOGGER TRACKING SCRIPT -->
    </body>
    </html>




```python
table = soup.find('table', {'class' : 'table_develop3'})
table
```




    <table class="table_develop3" summary="기상실황표로 지점, 날씨, 기온, 강수, 바람, 기압등을 안내한 표입니다.">
    <caption>기상실황표</caption>
    <colgroup>
    <col width="14%"/>
    <col width="12%"/>
    <col width="7%"/>
    <col width="5%"/>
    <col width="8%"/>
    <col width="5%"/>
    <col width="6%"/>
    <col width="5%"/>
    <col width="8%"/>
    <col width="5%"/>
    <col width="8%"/>
    <col width="6%"/>
    <col width="*%"/>
    </colgroup>
    <thead>
    <tr class="table_header" id="table_header1">
    <th class="top_line" rowspan="2" scope="col">
    		지점
    		</th>
    <th class="top_line" colspan="4" scope="col">날씨</th>
    <th class="top_line" colspan="3" scope="col">기온(℃)</th>
    <th class="top_line" colspan="2" scope="col">강수</th>
    <th class="top_line" colspan="2" scope="col">바람</th>
    <th class="top_line" scope="col">기압(hPa)</th>
    </tr>
    <tr class="table_header" id="table_header2">
    <th class="nm" scope="col">현재일기 </th>
    <th class="nm" scope="col">시정<br/>km</th>
    <th class="nm" scope="col">운량<br/>1/10</th>
    <th class="nm" scope="col">중하운량</th>
    <th class="nm" scope="col">현재<br/>기온</th>
    <th class="nm" scope="col">이슬점<br/>온도</th>
    <th class="nm" scope="col">불쾌<br/>지수</th>
    <th class="nm" scope="col">일강수<br/>mm</th>
    <th class="nm" scope="col">습도<br/>%</th>
    <th class="nm" scope="col">풍향 </th>
    <th class="nm" scope="col">풍속<br/>m/s</th>
    <th class="nm" scope="col">해면<br/>기압</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=108">서울</a></td>
    <td>맑음</td>
    <td>18.9</td>
    <td>1</td>
    <td>1</td>
    <td>25.6</td>
    <td>6.7</td>
    <td>70</td>
    <td> </td>
    <td>30</td>
    <td>서남서</td>
    <td>2.1</td>
    <td>1010.1</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=102">백령도</a></td>
    <td>구름조금</td>
    <td>19.8</td>
    <td>3</td>
    <td>0</td>
    <td>18.4</td>
    <td>10.9</td>
    <td>64</td>
    <td> </td>
    <td>62</td>
    <td>남서</td>
    <td>5.2</td>
    <td>1011.2</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=112">인천</a></td>
    <td>맑음</td>
    <td>20 이상</td>
    <td>0</td>
    <td>0</td>
    <td>20.8</td>
    <td>11.1</td>
    <td>67</td>
    <td> </td>
    <td>54</td>
    <td>서남서</td>
    <td>2.9</td>
    <td>1011.0</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=119">수원</a></td>
    <td>구름조금</td>
    <td>12.6</td>
    <td>3</td>
    <td>3</td>
    <td>25.0</td>
    <td>10.8</td>
    <td>71</td>
    <td> </td>
    <td>41</td>
    <td>북서</td>
    <td>2.4</td>
    <td>1010.6</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=98">동두천</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>24.9</td>
    <td>7.9</td>
    <td>70</td>
    <td> </td>
    <td>34</td>
    <td>서북서</td>
    <td>1.7</td>
    <td>1009.9</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=99">파주</a></td>
    <td> </td>
    <td>17.5</td>
    <td> </td>
    <td> </td>
    <td>25.1</td>
    <td>10.1</td>
    <td>71</td>
    <td> </td>
    <td>39</td>
    <td>서남서</td>
    <td>2.2</td>
    <td>1010.6</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=201">강화</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>20.0</td>
    <td>10.9</td>
    <td>66</td>
    <td> </td>
    <td>56</td>
    <td>서남서</td>
    <td>5.0</td>
    <td>1011.3</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=202">양평</a></td>
    <td> </td>
    <td>19.9</td>
    <td> </td>
    <td> </td>
    <td>25.5</td>
    <td>7.5</td>
    <td>70</td>
    <td> </td>
    <td>32</td>
    <td>서북서</td>
    <td>2.9</td>
    <td>1009.9</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=203">이천</a></td>
    <td> </td>
    <td>19.6</td>
    <td> </td>
    <td> </td>
    <td>25.6</td>
    <td>5.7</td>
    <td>70</td>
    <td> </td>
    <td>28</td>
    <td>북서</td>
    <td>2.9</td>
    <td>1010.0</td>
    </tr>
    <tr class="table_subheader">
    <th class="nm" scope="col">지점</th>
    <th class="nm" scope="col">현재일기</th>
    <th class="nm" scope="col">시정</th>
    <th class="nm" scope="col">운량</th>
    <th class="nm" scope="col">중하운량</th>
    <th class="nm" scope="col">현재기온</th>
    <th class="nm" scope="col">이슬점온도</th>
    <th class="nm" scope="col">불쾌지수</th>
    <th class="nm" scope="col">일강수</th>
    <th class="nm" scope="col">습도</th>
    <th class="nm" scope="col">풍향</th>
    <th class="nm" scope="col">풍속</th>
    <th class="nm" scope="col">해면기압</th>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=93">북춘천</a></td>
    <td>구름조금</td>
    <td>20 이상</td>
    <td>3</td>
    <td>3</td>
    <td>24.6</td>
    <td>8.5</td>
    <td>70</td>
    <td> </td>
    <td>36</td>
    <td>남남서</td>
    <td>3.4</td>
    <td>1008.9</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=104">북강릉</a></td>
    <td>맑음</td>
    <td>20 이상</td>
    <td>1</td>
    <td>1</td>
    <td>19.9</td>
    <td>10.8</td>
    <td>65</td>
    <td> </td>
    <td>56</td>
    <td>동</td>
    <td>3.1</td>
    <td>1010.3</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=115">울릉도</a></td>
    <td>구름많음</td>
    <td>20 이상</td>
    <td>7</td>
    <td>7</td>
    <td>16.8</td>
    <td>12.7</td>
    <td>62</td>
    <td> </td>
    <td>77</td>
    <td>동</td>
    <td>1.7</td>
    <td>1012.1</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=90">속초</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>19.1</td>
    <td>14.5</td>
    <td>65</td>
    <td> </td>
    <td>75</td>
    <td>남동</td>
    <td>2.9</td>
    <td>1010.4</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=95">철원</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>23.9</td>
    <td>8.3</td>
    <td>69</td>
    <td> </td>
    <td>37</td>
    <td>북북서</td>
    <td>2.2</td>
    <td>1009.5</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=100">대관령</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>17.9</td>
    <td>7.0</td>
    <td>62</td>
    <td> </td>
    <td>49</td>
    <td>동</td>
    <td>3.3</td>
    <td>1008.2</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=101">춘천</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>25.7</td>
    <td>10.6</td>
    <td>71</td>
    <td> </td>
    <td>39</td>
    <td>남서</td>
    <td>2.1</td>
    <td>1009.2</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=105">강릉</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>22.7</td>
    <td>8.7</td>
    <td>68</td>
    <td> </td>
    <td>41</td>
    <td>남남동</td>
    <td>2.1</td>
    <td>1010.3</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=106">동해</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>19.5</td>
    <td>15.3</td>
    <td>66</td>
    <td> </td>
    <td>77</td>
    <td>동남동</td>
    <td>3.6</td>
    <td>1010.7</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=114">원주</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>23.4</td>
    <td>7.4</td>
    <td>68</td>
    <td> </td>
    <td>36</td>
    <td>서</td>
    <td>1.6</td>
    <td>1008.8</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=121">영월</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>24.2</td>
    <td>7.3</td>
    <td>69</td>
    <td> </td>
    <td>34</td>
    <td>서남서</td>
    <td>3.1</td>
    <td>1008.2</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=211">인제</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>24.3</td>
    <td>6.0</td>
    <td>69</td>
    <td> </td>
    <td>31</td>
    <td>남남동</td>
    <td>2.7</td>
    <td>1008.3</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=212">홍천</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>25.4</td>
    <td>3.9</td>
    <td>70</td>
    <td> </td>
    <td>25</td>
    <td>서</td>
    <td>3.4</td>
    <td>1008.9</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=216">태백</a></td>
    <td> </td>
    <td>19.9</td>
    <td> </td>
    <td> </td>
    <td>19.6</td>
    <td>6.6</td>
    <td>64</td>
    <td> </td>
    <td>43</td>
    <td>북동</td>
    <td>3.6</td>
    <td>1007.9</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=217">정선군</a></td>
    <td> </td>
    <td>11.2</td>
    <td> </td>
    <td> </td>
    <td>23.0</td>
    <td>5.4</td>
    <td>68</td>
    <td> </td>
    <td>32</td>
    <td>북</td>
    <td>0.6</td>
    <td>1008.4</td>
    </tr>
    <tr class="table_subheader">
    <th class="nm" scope="col">지점</th>
    <th class="nm" scope="col">현재일기</th>
    <th class="nm" scope="col">시정</th>
    <th class="nm" scope="col">운량</th>
    <th class="nm" scope="col">중하운량</th>
    <th class="nm" scope="col">현재기온</th>
    <th class="nm" scope="col">이슬점온도</th>
    <th class="nm" scope="col">불쾌지수</th>
    <th class="nm" scope="col">일강수</th>
    <th class="nm" scope="col">습도</th>
    <th class="nm" scope="col">풍향</th>
    <th class="nm" scope="col">풍속</th>
    <th class="nm" scope="col">해면기압</th>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=129">서산</a></td>
    <td>맑음</td>
    <td>20 이상</td>
    <td>2</td>
    <td>2</td>
    <td>23.6</td>
    <td>12.2</td>
    <td>70</td>
    <td> </td>
    <td>49</td>
    <td>서남서</td>
    <td>2.0</td>
    <td>1011.6</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=131">청주</a></td>
    <td>구름조금</td>
    <td>20 이상</td>
    <td>4</td>
    <td>4</td>
    <td>24.3</td>
    <td>6.9</td>
    <td>69</td>
    <td> </td>
    <td>33</td>
    <td>북서</td>
    <td>2.7</td>
    <td>1010.0</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=133">대전</a></td>
    <td>맑음</td>
    <td>20 이상</td>
    <td>2</td>
    <td>2</td>
    <td>25.1</td>
    <td>9.3</td>
    <td>71</td>
    <td> </td>
    <td>37</td>
    <td>북북서</td>
    <td>1.8</td>
    <td>1010.5</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=127">충주</a></td>
    <td> </td>
    <td>18.5</td>
    <td> </td>
    <td> </td>
    <td>24.4</td>
    <td>6.6</td>
    <td>69</td>
    <td> </td>
    <td>32</td>
    <td>북서</td>
    <td>3.2</td>
    <td>1009.7</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=135">추풍령</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>23.0</td>
    <td>6.7</td>
    <td>68</td>
    <td> </td>
    <td>35</td>
    <td>서남서</td>
    <td>1.6</td>
    <td>1009.4</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=177">홍성(예)</a></td>
    <td> </td>
    <td> </td>
    <td> </td>
    <td> </td>
    <td>24.3</td>
    <td>11.9</td>
    <td>70</td>
    <td> </td>
    <td>46</td>
    <td>북동</td>
    <td>3.4</td>
    <td>1010.1</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=221">제천</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>24.2</td>
    <td>6.4</td>
    <td>69</td>
    <td> </td>
    <td>32</td>
    <td>남서</td>
    <td>3.6</td>
    <td>1007.8</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=226">보은</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>23.7</td>
    <td>4.0</td>
    <td>68</td>
    <td> </td>
    <td>28</td>
    <td>북</td>
    <td>2.9</td>
    <td>1009.8</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=232">천안</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>23.5</td>
    <td>7.1</td>
    <td>68</td>
    <td> </td>
    <td>35</td>
    <td>서</td>
    <td>3.2</td>
    <td>1010.3</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=235">보령</a></td>
    <td> </td>
    <td>19.4</td>
    <td> </td>
    <td> </td>
    <td>21.4</td>
    <td>12.2</td>
    <td>67</td>
    <td> </td>
    <td>56</td>
    <td>남서</td>
    <td>1.9</td>
    <td>1011.4</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=236">부여</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>23.9</td>
    <td>8.3</td>
    <td>69</td>
    <td> </td>
    <td>37</td>
    <td>남남동</td>
    <td>0.9</td>
    <td>1010.7</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=238">금산</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>23.7</td>
    <td>5.0</td>
    <td>68</td>
    <td> </td>
    <td>30</td>
    <td>북</td>
    <td>2.4</td>
    <td>1009.9</td>
    </tr>
    <tr class="table_subheader">
    <th class="nm" scope="col">지점</th>
    <th class="nm" scope="col">현재일기</th>
    <th class="nm" scope="col">시정</th>
    <th class="nm" scope="col">운량</th>
    <th class="nm" scope="col">중하운량</th>
    <th class="nm" scope="col">현재기온</th>
    <th class="nm" scope="col">이슬점온도</th>
    <th class="nm" scope="col">불쾌지수</th>
    <th class="nm" scope="col">일강수</th>
    <th class="nm" scope="col">습도</th>
    <th class="nm" scope="col">풍향</th>
    <th class="nm" scope="col">풍속</th>
    <th class="nm" scope="col">해면기압</th>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=146">전주</a></td>
    <td>구름조금</td>
    <td>19.2</td>
    <td>3</td>
    <td>3</td>
    <td>24.9</td>
    <td>11.8</td>
    <td>71</td>
    <td> </td>
    <td>44</td>
    <td>서북서</td>
    <td>2.0</td>
    <td>1010.4</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=156">광주</a></td>
    <td>구름조금</td>
    <td>20 이상</td>
    <td>5</td>
    <td>5</td>
    <td>24.0</td>
    <td>7.5</td>
    <td>69</td>
    <td> </td>
    <td>35</td>
    <td>동북동</td>
    <td>1.8</td>
    <td>1010.5</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=165">목포</a></td>
    <td>맑음</td>
    <td>20 이상</td>
    <td>0</td>
    <td>0</td>
    <td>22.8</td>
    <td>12.1</td>
    <td>69</td>
    <td> </td>
    <td>51</td>
    <td>북북서</td>
    <td>4.4</td>
    <td>1011.6</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=168">여수</a></td>
    <td>맑음</td>
    <td>20 이상</td>
    <td>1</td>
    <td>0</td>
    <td>22.8</td>
    <td>11.5</td>
    <td>69</td>
    <td> </td>
    <td>49</td>
    <td>남남서</td>
    <td>5.1</td>
    <td>1010.5</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=169">흑산도</a></td>
    <td>박무</td>
    <td>5.7</td>
    <td>0</td>
    <td>0</td>
    <td>19.2</td>
    <td>18.0</td>
    <td>66</td>
    <td> </td>
    <td>93</td>
    <td>북</td>
    <td>1.6</td>
    <td>1012.2</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=140">군산</a></td>
    <td> </td>
    <td>17.7</td>
    <td> </td>
    <td> </td>
    <td>21.8</td>
    <td>12.3</td>
    <td>68</td>
    <td> </td>
    <td>55</td>
    <td>서남서</td>
    <td>3.8</td>
    <td>1011.4</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=170">완도</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>23.2</td>
    <td>10.5</td>
    <td>69</td>
    <td> </td>
    <td>45</td>
    <td>동남동</td>
    <td>1.7</td>
    <td>1010.7</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=172">고창</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>22.7</td>
    <td>12.6</td>
    <td>69</td>
    <td> </td>
    <td>53</td>
    <td>북서</td>
    <td>5.8</td>
    <td>1011.4</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=174">순천</a></td>
    <td> </td>
    <td>18.5</td>
    <td> </td>
    <td> </td>
    <td>22.5</td>
    <td>8.2</td>
    <td>68</td>
    <td> </td>
    <td>40</td>
    <td>서</td>
    <td>2.7</td>
    <td>1009.4</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=175">진도(첨찰산)</a></td>
    <td> </td>
    <td> </td>
    <td> </td>
    <td> </td>
    <td>22.2</td>
    <td>10.6</td>
    <td>68</td>
    <td> </td>
    <td>48</td>
    <td>북북동</td>
    <td>3.4</td>
    <td>1010.0</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=243">부안</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>22.9</td>
    <td>9.9</td>
    <td>69</td>
    <td> </td>
    <td>44</td>
    <td>서북서</td>
    <td>3.3</td>
    <td>1011.7</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=244">임실</a></td>
    <td> </td>
    <td>15.3</td>
    <td> </td>
    <td> </td>
    <td>22.8</td>
    <td>8.4</td>
    <td>68</td>
    <td> </td>
    <td>40</td>
    <td>북</td>
    <td>1.3</td>
    <td>1010.0</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=245">정읍</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>23.8</td>
    <td>11.8</td>
    <td>70</td>
    <td> </td>
    <td>47</td>
    <td>북</td>
    <td>3.3</td>
    <td>1010.9</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=247">남원</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>23.8</td>
    <td>7.4</td>
    <td>69</td>
    <td> </td>
    <td>35</td>
    <td>서북서</td>
    <td>2.5</td>
    <td>1009.0</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=248">장수</a></td>
    <td> </td>
    <td>19.6</td>
    <td> </td>
    <td> </td>
    <td>22.0</td>
    <td>4.9</td>
    <td>67</td>
    <td> </td>
    <td>33</td>
    <td>북</td>
    <td>4.2</td>
    <td>1009.0</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=251">고창군</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>23.7</td>
    <td>12.0</td>
    <td>70</td>
    <td> </td>
    <td>48</td>
    <td>북서</td>
    <td>3.3</td>
    <td>1010.7</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=252">영광군</a></td>
    <td> </td>
    <td>18.8</td>
    <td> </td>
    <td> </td>
    <td>22.4</td>
    <td>8.1</td>
    <td>68</td>
    <td> </td>
    <td>40</td>
    <td>북</td>
    <td>5.3</td>
    <td>1011.4</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=254">순창군</a></td>
    <td> </td>
    <td>11.9</td>
    <td> </td>
    <td> </td>
    <td>23.5</td>
    <td>8.3</td>
    <td>69</td>
    <td> </td>
    <td>38</td>
    <td>북서</td>
    <td>3.1</td>
    <td>1010.3</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=258">보성군</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>23.7</td>
    <td>6.8</td>
    <td>69</td>
    <td> </td>
    <td>34</td>
    <td>남남동</td>
    <td>2.3</td>
    <td>1010.8</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=259">강진군</a></td>
    <td> </td>
    <td>12.4</td>
    <td> </td>
    <td> </td>
    <td>24.1</td>
    <td>6.8</td>
    <td>69</td>
    <td> </td>
    <td>33</td>
    <td>북북동</td>
    <td>4.2</td>
    <td>1011.1</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=260">장흥</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>25.5</td>
    <td>8.0</td>
    <td>71</td>
    <td> </td>
    <td>33</td>
    <td>북</td>
    <td>3.9</td>
    <td>1010.2</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=261">해남</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>24.6</td>
    <td>10.0</td>
    <td>70</td>
    <td> </td>
    <td>40</td>
    <td>북북서</td>
    <td>2.3</td>
    <td>1010.8</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=262">고흥</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>24.4</td>
    <td>7.5</td>
    <td>69</td>
    <td> </td>
    <td>34</td>
    <td>북북서</td>
    <td>1.1</td>
    <td>1010.1</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=266">광양시</a></td>
    <td> </td>
    <td>14.6</td>
    <td> </td>
    <td> </td>
    <td>24.6</td>
    <td>11.1</td>
    <td>71</td>
    <td> </td>
    <td>43</td>
    <td>남남서</td>
    <td>2.1</td>
    <td>1009.3</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=268">진도군</a></td>
    <td> </td>
    <td>14.8</td>
    <td> </td>
    <td> </td>
    <td>21.9</td>
    <td>13.2</td>
    <td>68</td>
    <td> </td>
    <td>58</td>
    <td>북북서</td>
    <td>2.9</td>
    <td>1011.2</td>
    </tr>
    <tr class="table_subheader">
    <th class="nm" scope="col">지점</th>
    <th class="nm" scope="col">현재일기</th>
    <th class="nm" scope="col">시정</th>
    <th class="nm" scope="col">운량</th>
    <th class="nm" scope="col">중하운량</th>
    <th class="nm" scope="col">현재기온</th>
    <th class="nm" scope="col">이슬점온도</th>
    <th class="nm" scope="col">불쾌지수</th>
    <th class="nm" scope="col">일강수</th>
    <th class="nm" scope="col">습도</th>
    <th class="nm" scope="col">풍향</th>
    <th class="nm" scope="col">풍속</th>
    <th class="nm" scope="col">해면기압</th>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=184">제주</a></td>
    <td>맑음</td>
    <td>20 이상</td>
    <td>2</td>
    <td>0</td>
    <td>20.7</td>
    <td>12.6</td>
    <td>67</td>
    <td> </td>
    <td>60</td>
    <td>서북서</td>
    <td>3.7</td>
    <td>1012.4</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=185">고산</a></td>
    <td> </td>
    <td>18.7</td>
    <td> </td>
    <td> </td>
    <td>19.1</td>
    <td>14.3</td>
    <td>65</td>
    <td> </td>
    <td>74</td>
    <td>북북서</td>
    <td>5.8</td>
    <td>1012.2</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=188">성산</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>23.1</td>
    <td>5.9</td>
    <td>68</td>
    <td> </td>
    <td>33</td>
    <td>서북서</td>
    <td>3.8</td>
    <td>1011.1</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=189">서귀포</a></td>
    <td> </td>
    <td>18.8</td>
    <td> </td>
    <td> </td>
    <td>24.0</td>
    <td>10.6</td>
    <td>70</td>
    <td> </td>
    <td>43</td>
    <td>남</td>
    <td>2.5</td>
    <td>1010.5</td>
    </tr>
    <tr class="table_subheader">
    <th class="nm" scope="col">지점</th>
    <th class="nm" scope="col">현재일기</th>
    <th class="nm" scope="col">시정</th>
    <th class="nm" scope="col">운량</th>
    <th class="nm" scope="col">중하운량</th>
    <th class="nm" scope="col">현재기온</th>
    <th class="nm" scope="col">이슬점온도</th>
    <th class="nm" scope="col">불쾌지수</th>
    <th class="nm" scope="col">일강수</th>
    <th class="nm" scope="col">습도</th>
    <th class="nm" scope="col">풍향</th>
    <th class="nm" scope="col">풍속</th>
    <th class="nm" scope="col">해면기압</th>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=136">안동</a></td>
    <td>구름많음</td>
    <td>20 이상</td>
    <td>6</td>
    <td>6</td>
    <td>25.0</td>
    <td>7.1</td>
    <td>70</td>
    <td> </td>
    <td>32</td>
    <td>북서</td>
    <td>2.9</td>
    <td>1008.8</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=138">포항</a></td>
    <td>구름많음</td>
    <td>20 이상</td>
    <td>7</td>
    <td>7</td>
    <td>19.0</td>
    <td>16.0</td>
    <td>65</td>
    <td>0.0</td>
    <td>83</td>
    <td>북북동</td>
    <td>1.9</td>
    <td>1011.3</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=143">대구</a></td>
    <td>구름많음</td>
    <td>19.9</td>
    <td>6</td>
    <td>6</td>
    <td>25.7</td>
    <td>7.2</td>
    <td>71</td>
    <td> </td>
    <td>31</td>
    <td>북서</td>
    <td>2.2</td>
    <td>1009.2</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=152">울산</a></td>
    <td>뇌전 끝</td>
    <td>20 이상</td>
    <td>7</td>
    <td>5</td>
    <td>19.7</td>
    <td>14.0</td>
    <td>66</td>
    <td>0.2</td>
    <td>70</td>
    <td>동남동</td>
    <td>3.8</td>
    <td>1010.7</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=155">창원</a></td>
    <td>구름조금</td>
    <td>20 이상</td>
    <td>4</td>
    <td>4</td>
    <td>20.6</td>
    <td>13.3</td>
    <td>67</td>
    <td>0.0</td>
    <td>63</td>
    <td>남남동</td>
    <td>4.7</td>
    <td>1010.3</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=159">부산</a></td>
    <td>구름많음</td>
    <td>14.5</td>
    <td>8</td>
    <td>8</td>
    <td>20.2</td>
    <td>13.6</td>
    <td>66</td>
    <td> </td>
    <td>66</td>
    <td>동남동</td>
    <td>3.5</td>
    <td>1011.2</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=130">울진</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>17.6</td>
    <td>14.8</td>
    <td>63</td>
    <td> </td>
    <td>84</td>
    <td>남동</td>
    <td>3.4</td>
    <td>1011.7</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=137">상주</a></td>
    <td> </td>
    <td>14.5</td>
    <td> </td>
    <td> </td>
    <td>25.0</td>
    <td>7.1</td>
    <td>70</td>
    <td> </td>
    <td>32</td>
    <td>남남서</td>
    <td>1.7</td>
    <td>1009.3</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=162">통영</a></td>
    <td> </td>
    <td>17.1</td>
    <td> </td>
    <td> </td>
    <td>20.0</td>
    <td>14.5</td>
    <td>66</td>
    <td>0.0</td>
    <td>71</td>
    <td>남남동</td>
    <td>5.3</td>
    <td>1010.8</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=192">진주</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>23.8</td>
    <td>5.1</td>
    <td>68</td>
    <td> </td>
    <td>30</td>
    <td>서남서</td>
    <td>1.4</td>
    <td>1009.9</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=253">김해시</a></td>
    <td> </td>
    <td>15.7</td>
    <td> </td>
    <td> </td>
    <td>21.9</td>
    <td>13.7</td>
    <td>68</td>
    <td> </td>
    <td>60</td>
    <td>남동</td>
    <td>3.8</td>
    <td>1011.3</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=255">북창원</a></td>
    <td> </td>
    <td>17.6</td>
    <td> </td>
    <td> </td>
    <td>22.8</td>
    <td>11.8</td>
    <td>69</td>
    <td>0.0</td>
    <td>50</td>
    <td>남남서</td>
    <td>1.2</td>
    <td>1009.9</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=257">양산시</a></td>
    <td> </td>
    <td>12.7</td>
    <td> </td>
    <td> </td>
    <td>21.4</td>
    <td>14.0</td>
    <td>68</td>
    <td> </td>
    <td>63</td>
    <td>남동</td>
    <td>2.6</td>
    <td>1011.7</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=263">의령군</a></td>
    <td> </td>
    <td>9.2</td>
    <td> </td>
    <td> </td>
    <td>25.1</td>
    <td>10.5</td>
    <td>71</td>
    <td> </td>
    <td>40</td>
    <td>동</td>
    <td>2.5</td>
    <td>1009.7</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=264">함양군</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>23.3</td>
    <td>8.1</td>
    <td>69</td>
    <td> </td>
    <td>38</td>
    <td>정온</td>
    <td>0.2</td>
    <td>1009.4</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=271">봉화</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>22.0</td>
    <td>7.0</td>
    <td>67</td>
    <td>0.0</td>
    <td>38</td>
    <td>동남동</td>
    <td>2.4</td>
    <td>1008.4</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=272">영주</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>23.0</td>
    <td>7.1</td>
    <td>68</td>
    <td> </td>
    <td>36</td>
    <td>북서</td>
    <td>3.9</td>
    <td>1008.4</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=273">문경</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>25.5</td>
    <td>4.5</td>
    <td>70</td>
    <td> </td>
    <td>26</td>
    <td>북북서</td>
    <td>2.6</td>
    <td>1009.0</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=276">청송군</a></td>
    <td> </td>
    <td>7.0</td>
    <td> </td>
    <td> </td>
    <td>17.9</td>
    <td>12.5</td>
    <td>63</td>
    <td>1.0</td>
    <td>71</td>
    <td>동북동</td>
    <td>2.3</td>
    <td>1010.1</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=277">영덕</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>19.4</td>
    <td>10.6</td>
    <td>65</td>
    <td> </td>
    <td>57</td>
    <td>동남동</td>
    <td>4.0</td>
    <td>1011.6</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=278">의성</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>25.7</td>
    <td>4.1</td>
    <td>70</td>
    <td> </td>
    <td>25</td>
    <td>서남서</td>
    <td>2.3</td>
    <td>1009.1</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=279">구미</a></td>
    <td> </td>
    <td> </td>
    <td> </td>
    <td> </td>
    <td>25.7</td>
    <td>7.7</td>
    <td>71</td>
    <td> </td>
    <td>32</td>
    <td>북서</td>
    <td>2.2</td>
    <td>1009.7</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=281">영천</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>21.8</td>
    <td>9.9</td>
    <td>67</td>
    <td>0.0</td>
    <td>47</td>
    <td>동</td>
    <td>3.3</td>
    <td>1009.9</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=283">경주시</a></td>
    <td> </td>
    <td>14.2</td>
    <td> </td>
    <td> </td>
    <td>23.8</td>
    <td>12.4</td>
    <td>70</td>
    <td>0.1</td>
    <td>49</td>
    <td>동</td>
    <td>2.2</td>
    <td>1010.3</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=284">거창</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>22.7</td>
    <td>7.6</td>
    <td>68</td>
    <td> </td>
    <td>38</td>
    <td>남남서</td>
    <td>1.5</td>
    <td>1008.6</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=285">합천</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>25.1</td>
    <td>7.2</td>
    <td>70</td>
    <td> </td>
    <td>32</td>
    <td>서남서</td>
    <td>1.0</td>
    <td>1009.7</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=288">밀양</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>24.7</td>
    <td>7.7</td>
    <td>70</td>
    <td>0.0</td>
    <td>34</td>
    <td>서북서</td>
    <td>1.2</td>
    <td>1009.6</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=289">산청</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>24.8</td>
    <td>10.6</td>
    <td>71</td>
    <td> </td>
    <td>41</td>
    <td>서북서</td>
    <td>1.5</td>
    <td>1009.4</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=294">거제</a></td>
    <td> </td>
    <td>19.1</td>
    <td> </td>
    <td> </td>
    <td>23.1</td>
    <td>14.1</td>
    <td>70</td>
    <td> </td>
    <td>57</td>
    <td>남남서</td>
    <td>2.7</td>
    <td>1010.4</td>
    </tr>
    <tr>
    <td><a href="/weather/observation/currentweather.jsp?tm=2017.5.17.14:00&amp;type=t99&amp;mode=0&amp;auto_man=m&amp;stn=295">남해</a></td>
    <td> </td>
    <td>20 이상</td>
    <td> </td>
    <td> </td>
    <td>24.5</td>
    <td>10.0</td>
    <td>70</td>
    <td> </td>
    <td>40</td>
    <td>남남동</td>
    <td>1.8</td>
    <td>1010.3</td>
    </tr>
    </tbody>
    </table>




```python
# sample code
# tr = table.find_all('tr')
# tr
point_list = []
temp_list = []
humidity_list = []
data = []
for tr in table.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds:
        if td.find('a'):
            point = td.find('a').text
            # point_list.append(point)
            temp = tds[5].text
            # temp_list.append(temp)
            humidity = tds[9].text
            # humidity_list.append(humidity)
            data.append([point, temp, humidity])
```


```python
# print(point_list)
# print(temp_list)
# print(humidity_list)
data
```




    [['서울', '25.6', '30'],
     ['백령도', '18.4', '62'],
     ['인천', '20.8', '54'],
     ['수원', '25.0', '41'],
     ['동두천', '24.9', '34'],
     ['파주', '25.1', '39'],
     ['강화', '20.0', '56'],
     ['양평', '25.5', '32'],
     ['이천', '25.6', '28'],
     ['북춘천', '24.6', '36'],
     ['북강릉', '19.9', '56'],
     ['울릉도', '16.8', '77'],
     ['속초', '19.1', '75'],
     ['철원', '23.9', '37'],
     ['대관령', '17.9', '49'],
     ['춘천', '25.7', '39'],
     ['강릉', '22.7', '41'],
     ['동해', '19.5', '77'],
     ['원주', '23.4', '36'],
     ['영월', '24.2', '34'],
     ['인제', '24.3', '31'],
     ['홍천', '25.4', '25'],
     ['태백', '19.6', '43'],
     ['정선군', '23.0', '32'],
     ['서산', '23.6', '49'],
     ['청주', '24.3', '33'],
     ['대전', '25.1', '37'],
     ['충주', '24.4', '32'],
     ['추풍령', '23.0', '35'],
     ['홍성(예)', '24.3', '46'],
     ['제천', '24.2', '32'],
     ['보은', '23.7', '28'],
     ['천안', '23.5', '35'],
     ['보령', '21.4', '56'],
     ['부여', '23.9', '37'],
     ['금산', '23.7', '30'],
     ['전주', '24.9', '44'],
     ['광주', '24.0', '35'],
     ['목포', '22.8', '51'],
     ['여수', '22.8', '49'],
     ['흑산도', '19.2', '93'],
     ['군산', '21.8', '55'],
     ['완도', '23.2', '45'],
     ['고창', '22.7', '53'],
     ['순천', '22.5', '40'],
     ['진도(첨찰산)', '22.2', '48'],
     ['부안', '22.9', '44'],
     ['임실', '22.8', '40'],
     ['정읍', '23.8', '47'],
     ['남원', '23.8', '35'],
     ['장수', '22.0', '33'],
     ['고창군', '23.7', '48'],
     ['영광군', '22.4', '40'],
     ['순창군', '23.5', '38'],
     ['보성군', '23.7', '34'],
     ['강진군', '24.1', '33'],
     ['장흥', '25.5', '33'],
     ['해남', '24.6', '40'],
     ['고흥', '24.4', '34'],
     ['광양시', '24.6', '43'],
     ['진도군', '21.9', '58'],
     ['제주', '20.7', '60'],
     ['고산', '19.1', '74'],
     ['성산', '23.1', '33'],
     ['서귀포', '24.0', '43'],
     ['안동', '25.0', '32'],
     ['포항', '19.0', '83'],
     ['대구', '25.7', '31'],
     ['울산', '19.7', '70'],
     ['창원', '20.6', '63'],
     ['부산', '20.2', '66'],
     ['울진', '17.6', '84'],
     ['상주', '25.0', '32'],
     ['통영', '20.0', '71'],
     ['진주', '23.8', '30'],
     ['김해시', '21.9', '60'],
     ['북창원', '22.8', '50'],
     ['양산시', '21.4', '63'],
     ['의령군', '25.1', '40'],
     ['함양군', '23.3', '38'],
     ['봉화', '22.0', '38'],
     ['영주', '23.0', '36'],
     ['문경', '25.5', '26'],
     ['청송군', '17.9', '71'],
     ['영덕', '19.4', '57'],
     ['의성', '25.7', '25'],
     ['구미', '25.7', '32'],
     ['영천', '21.8', '47'],
     ['경주시', '23.8', '49'],
     ['거창', '22.7', '38'],
     ['합천', '25.1', '32'],
     ['밀양', '24.7', '34'],
     ['산청', '24.8', '41'],
     ['거제', '23.1', '57'],
     ['남해', '24.5', '40']]




```python
with open('python_weather.csv', 'w', encoding='utf-8') as file:
    for d in data :
        file.write('{}, {}, {} \n'.format(d[0], d[1], d[2]))
print('ok')
```

    ok
    


```python
import pandas as pd
weather_df = pd.DataFrame({
    'point' : point_list,
    'temp'  : temp_list,
    'humidity' : humidity_list
})
```


```python
weather_df.to_csv('weather_df.csv', mode='w', encoding='utf-8')
print('success')
```

    success
    
