

```python
import platform

from matplotlib import font_manager, rc
# plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~') 
```


```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
```


```python
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
```


```python
try:
    html = urlopen('http://www.pythonscraping.com/pages/page3.html')
except HTTPError as he:
    print('http error')
except URLError as ue:
    print('url error')
else : 
    soup = BeautifulSoup(html.read(), 'html.parser')
```


```python
table = soup.find('table',{'id':'giftList'})
table
```




    <table id="giftList">
    <tr><th>
    Item Title
    </th><th>
    Description
    </th><th>
    Cost
    </th><th>
    Image
    </th></tr>
    <tr class="gift" id="gift1"><td>
    Vegetable Basket
    </td><td>
    This vegetable basket is the perfect gift for your health conscious (or overweight) friends!
    <span class="excitingNote">Now with super-colorful bell peppers!</span>
    </td><td>
    $15.00
    </td><td>
    <img src="../img/gifts/img1.jpg"/>
    </td></tr>
    <tr class="gift" id="gift2"><td>
    Russian Nesting Dolls
    </td><td>
    Hand-painted by trained monkeys, these exquisite dolls are priceless! And by "priceless," we mean "extremely expensive"! <span class="excitingNote">8 entire dolls per set! Octuple the presents!</span>
    </td><td>
    $10,000.52
    </td><td>
    <img src="../img/gifts/img2.jpg"/>
    </td></tr>
    <tr class="gift" id="gift3"><td>
    Fish Painting
    </td><td>
    If something seems fishy about this painting, it's because it's a fish! <span class="excitingNote">Also hand-painted by trained monkeys!</span>
    </td><td>
    $10,005.00
    </td><td>
    <img src="../img/gifts/img3.jpg"/>
    </td></tr>
    <tr class="gift" id="gift4"><td>
    Dead Parrot
    </td><td>
    This is an ex-parrot! <span class="excitingNote">Or maybe he's only resting?</span>
    </td><td>
    $0.50
    </td><td>
    <img src="../img/gifts/img4.jpg"/>
    </td></tr>
    <tr class="gift" id="gift5"><td>
    Mystery Box
    </td><td>
    If you love suprises, this mystery box is for you! Do not place on light-colored surfaces. May cause oil staining. <span class="excitingNote">Keep your friends guessing!</span>
    </td><td>
    $1.50
    </td><td>
    <img src="../img/gifts/img6.jpg"/>
    </td></tr>
    </table>




```python
# data 담을 그릇
data = []
for tr in table.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds :
        title = tds[0].text.strip('\n')
        desc = tds[1].text.strip('\n')
        cost = tds[2].text.strip('\n')
        img_src = tds[3].find('img')['src']
        
    data.append([title, desc, cost, img_src])
```


```python
print(data)
```

    [['Mystery Box', 'If you love suprises, this mystery box is for you! Do not place on light-colored surfaces. May cause oil staining. Keep your friends guessing!', '$1.50', '../img/gifts/img6.jpg'], ['Vegetable Basket', 'This vegetable basket is the perfect gift for your health conscious (or overweight) friends!\nNow with super-colorful bell peppers!', '$15.00', '../img/gifts/img1.jpg'], ['Russian Nesting Dolls', 'Hand-painted by trained monkeys, these exquisite dolls are priceless! And by "priceless," we mean "extremely expensive"! 8 entire dolls per set! Octuple the presents!', '$10,000.52', '../img/gifts/img2.jpg'], ['Fish Painting', "If something seems fishy about this painting, it's because it's a fish! Also hand-painted by trained monkeys!", '$10,005.00', '../img/gifts/img3.jpg'], ['Dead Parrot', "This is an ex-parrot! Or maybe he's only resting?", '$0.50', '../img/gifts/img4.jpg'], ['Mystery Box', 'If you love suprises, this mystery box is for you! Do not place on light-colored surfaces. May cause oil staining. Keep your friends guessing!', '$1.50', '../img/gifts/img6.jpg']]
    


```python
with open('python_gifts.csv', 'w', encoding='utf-8') as file:
    # 컬럼 이름 추가
    file.write('Item, Description, Cost, Image\n')
    
    
    for d in data :
        file.write('{}, {}, {}, {}\n'.format(d[0], d[1], d[2], d[3]))
```


```python
%matplotlib inline
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_csv('./python_gifts.csv', encoding='utf-8')
df
```


    ---------------------------------------------------------------------------

    ParserError                               Traceback (most recent call last)

    <ipython-input-102-6794039dc65c> in <module>()
          4 import matplotlib.pyplot as plt
          5 
    ----> 6 df = pd.read_csv('./python_gifts.csv', encoding='utf-8')
          7 df
    

    ~\Anaconda3\lib\site-packages\pandas\io\parsers.py in parser_f(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, squeeze, prefix, mangle_dupe_cols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, dayfirst, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, escapechar, comment, encoding, dialect, tupleize_cols, error_bad_lines, warn_bad_lines, skipfooter, doublequote, delim_whitespace, low_memory, memory_map, float_precision)
        676                     skip_blank_lines=skip_blank_lines)
        677 
    --> 678         return _read(filepath_or_buffer, kwds)
        679 
        680     parser_f.__name__ = name
    

    ~\Anaconda3\lib\site-packages\pandas\io\parsers.py in _read(filepath_or_buffer, kwds)
        444 
        445     try:
    --> 446         data = parser.read(nrows)
        447     finally:
        448         parser.close()
    

    ~\Anaconda3\lib\site-packages\pandas\io\parsers.py in read(self, nrows)
       1034                 raise ValueError('skipfooter not supported for iteration')
       1035 
    -> 1036         ret = self._engine.read(nrows)
       1037 
       1038         # May alter columns / col_dict
    

    ~\Anaconda3\lib\site-packages\pandas\io\parsers.py in read(self, nrows)
       1846     def read(self, nrows=None):
       1847         try:
    -> 1848             data = self._reader.read(nrows)
       1849         except StopIteration:
       1850             if self._first_chunk:
    

    pandas\_libs\parsers.pyx in pandas._libs.parsers.TextReader.read()
    

    pandas\_libs\parsers.pyx in pandas._libs.parsers.TextReader._read_low_memory()
    

    pandas\_libs\parsers.pyx in pandas._libs.parsers.TextReader._read_rows()
    

    pandas\_libs\parsers.pyx in pandas._libs.parsers.TextReader._tokenize_rows()
    

    pandas\_libs\parsers.pyx in pandas._libs.parsers.raise_parser_error()
    

    ParserError: Error tokenizing data. C error: Expected 5 fields in line 5, saw 7
    

