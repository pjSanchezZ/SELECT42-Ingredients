1. 在html文档第一行插入 {% load static %}
2. CTRL-F replace [href="] -> [href="/]
3. replace [.html"] -> [/"]
4. replace [src="] -> [src="{% static ']
5. 拉至开头的一大段，将所有(大概7、8个左右)[href="/.../XX.css"] 或 [href="/.../XX.png"] 手动换成 [href="{% static '.../XX.css' %}"] 注意：地址中第一个'/'号一并替换掉
6. 搜索 [src="{% static '] 一共会有10几到20个，将它们的结尾由 ["] -> [' %}"]