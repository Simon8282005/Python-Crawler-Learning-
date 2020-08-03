### 第十四天
# 基于 BeautifulSoup 的 HTML 格式输出
**本课索引：如何让 HTML 格式的内容更加友善？**

这里说的友善不仅仅是让人更容易读，也指让程序更容易分析和解析。（这是本章节的主要目的 XD）

我们再拿 demo 页面来开刀
```
import requests as re
from bs4 import BeautifulSoup as bs

r = re.get("http://python123.io/ws/demo.html")
demo = r.text
soup = bs(demo, "html.parser")
```

# Prettify()
调用 prettify() 函数
```
>>> soup.prettify()
```
**Output:** 
```
'<html>\n <head>\n  <title>\n   This is a python demo page\n  </title>\n </head>\n <body>\n  <p class="title">\n   <b>\n    The demo python introduces several python courses.\n   </b>\n  </p>\n  <p class="course">\n   Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:\n   <a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">\n    Basic Python\n   </a>\n   and\n   <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">\n    Advanced Python\n   </a>\n   .\n  </p>\n </body>\n</html>'
```

这里我们可以看到 prettify() 函数在每个标签的后面加上了一个反斜杠n (\n), 我们接着使用 print() 函数将 prettify() 函数打印出来，看看结果会怎么样吧

```
>>> print(soup.prettify())
```
**Output:**
```
<html>
 <head>
  <title>
   This is a python demo page
  </title>
 </head>
 <body>
  <p class="title">
   <b>
    The demo python introduces several python courses.
   </b>
  </p>
  <p class="course">
   Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
   <a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">
    Basic Python
   </a>
   and
   <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">
    Advanced Python
   </a>
   .
  </p>
 </body>
</html>
```
是不是容易看多了？ 起码我这个只有一点点 HTML 基础的人能看的懂了 XD

prettify() 函数除了可以对全部的标签添加换行符，也能对单一的标签进行处理：
```
>>> print(soup.a.prettify())
```
**Output:**
```
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">
 Basic Python
</a>
```

我们能看到 `<a>` 标签被很清晰的显示出来了

# 单元小结
这一单元主要讲解了 BeautifulSoup 库的基本概念和使用方法，then让我们来复习一下吧（温故知心嘛 XD）

## BeaurifulSoup 是什么 ？
BeautifulSoup 是一个用来解析和遍历 HTML 代码的库

## 使用 BeaurifulSoup
```
from bs4 import BeautifulSoup
soup = ("<h1>HelloWorld</h1>", "html.parser")
```
## BeautifulSoup 五个基本类型
- Tag (`<Tag>`)
- Name (`<a>`)
- Attributes (标签的属性)
- NavigableString (标签之间的字符串)
- Comment (标签之间的注解)

## BeautifulSoup 基本的遍历方法
### 下行遍历：
(获得子孙节点的方法叫下行遍历)
- .contents
- .children (获得儿子节点)
- .descendants (获得子孙节点)

### 上行遍历：
(获得父亲和先辈节点的方法叫上行遍历)
- .parent (获得父亲节点)
- .parents (获得使用先辈节点)

### 平行遍历：
(获得在同一个父亲节点下的其他标签进行遍历叫平行遍历)
- .next_sibling
- .previous_sibling
- .next_siblings
- .previous_siblings

这些只是 BeautifulSoup 中的基本方法，但已经可以帮助我们很好的解析爬虫传输回来的数据，我们慢点会更深如的了解 BeautifulSoup 的其他更深入的方法 XD




