#### 项目的博客地址：
<a href="https://blog.csdn.net/happygjcd/article/details/104525443">大家可以先看看博客哈，这里附上博客地址</a>
#### 项目介绍
**这是一个适合初学Django的小白学习的Django项目，同时也比较适合运维人员入门运维开发，项目从基本的增删改查写起，到Django的缓存，分页，中间件，信号等不断进阶，相信我，搞懂这个一定受益匪浅！！！**
##### 1）功能介绍
* **添加管理账号（注册），包括账号，密码**
* **登陆功能的流程**
* **登陆后可以显示用户的所有主机（分页），并且可以查看 / 编辑主机详细信息，增加，删除主机。**
* **基于中间件做IP过滤。**
* **基于信号实现插入数据库数据的同时添加日志。**
* **基于缓存提高网站性能**
##### 2）运用的知识
* **数据库基本知识，一对多，多对多表关系，增删查看**
* **Django基础知识**
* **Django进阶**
 1. 分页器Paginator的使用
 2. 基于session完成用户登录
 3. 基于form组件生成表单
 4. Django信号，中间件的简单使用
* **少量前端知识（不影响理解此项目，fork我的代码就行）**
1. HTML，CSS，JavaScript
2. jQuery的简单使用，主要用来操作标签，ajax
3. boostrap，使用了boostrap的分页样式
##### 项目主要功能截图
###### 注册页面
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020030416102156.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2hhcHB5Z2pjZA==,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200304160946850.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2hhcHB5Z2pjZA==,size_16,color_FFFFFF,t_70)
###### 登录页面，（两周可免登录）
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200304161112548.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2hhcHB5Z2pjZA==,size_16,color_FFFFFF,t_70)
###### 登录成功跳转到主机页面
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200304161206466.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2hhcHB5Z2pjZA==,size_16,color_FFFFFF,t_70)
这里我已经使用Django的`bulk_create`批量插入数据库记录，否则无法进行分页效果，源码中有介绍
###### 查看详细的页面
可查看主机详细信息，也可以进行编辑
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200304161756381.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2hhcHB5Z2pjZA==,size_16,color_FFFFFF,t_70)
**点击编辑**
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200304162012430.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2hhcHB5Z2pjZA==,size_16,color_FFFFFF,t_70)
编辑成功使用ajax提交后alert()显示弹窗
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200304161951774.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2hhcHB5Z2pjZA==,size_16,color_FFFFFF,t_70)
若主机某一个信息为空，提示完善主机信息
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200304162133691.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2hhcHB5Z2pjZA==,size_16,color_FFFFFF,t_70)
