### 第十八天

# 基于 bs4 库的 HTML 内容查找方法

`<>.find_all(name, attrs, recursive, string, **kwargs)`

find_all 返回的是一个列表类型

- name: 对列表名称的检索字符
- attrs: 对标签属性值搜索字符串，可标记属性检索
- recursive: 是否对子孙节点全部探索，默认为True
- string: <> ... </> 中字符串区域的探索字符串

# Name

```
soup.find_all("a")
```

**Output**:

`[<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>, <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>]`

```
soup.find_all(["a","b"])
```
**Output**:

`[<b>The demo python introduces several python courses.</b>, <a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>, <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>]`

```
for tag in soup.find_all(True):
	print(tag.name)
```

**Output**:

`html
head
title
body
p
b
p
a
a`

以上的列子需要我们很精确的知道标签的名字，但要是我们不知道名字或我们想要查找所有以 `b` 开头的标签名字要咋办呢？ 嘿嘿嘿，轮到正则表达式登场了，掌声！！！

# 正则表达式
`正则表达式，又称正则表示式、正则表示法、规则表达式、常规表示法，是计算机科学的一个概念。正则表达式使用单个字符串来描述、匹配一系列符合某个句法规则的字符串。在很多文本编辑器里，正则表达式通常被用来检索、替换那些符合某个模式的文本。 许多程序设计语言都支持利用正则表达式进行字符串操作。（摘自维基百科）`

要使用正则表达式要先导入 re 库

```
import re
soup.find_all(re.compile("b"))
```
**Output**:

`body b`

# Attrs

```
soup.find_all("p", "course")
```

**Output:**

`[<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>]`

```
soup.find_all(id="link1")
```

**Output:**

`[<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>]`

```
soup.find_all(id="link")
```

**Output:**

`[]`

```
soup.find_all(id="link2")
```

**Output:**

`[<a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>]`


```
soup.find_all(id = re.compile("link"))
```

**Output:**

`[<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>, <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>]`

# Recursive

```
soup.find_all("a", recursive = False)
```

**Output:**

`[]`

# String
```
soup.find_all(string = "Basic Python")
```

**Output:**

`['Basic Python']`

```
soup.find_all(string = re.compile("python"))
```

**Output:**

`['This is a python demo page', 'The demo python introduces several python courses.']`
