这是一个实现在线代码编辑器功能的xblock。基于codemirror实现在线代码编辑功能。

1.安装：

  1.1 把xblock-coedeeditor克隆到的open edx平台中。如我克隆到/home/zyn
  
      cd /home/zyn
      git clone https://github.com/jennyzhang8800/xblock-codeeditor
  1.2 安装xblock
  
      sudo -u edxapp /edx/bin/pip.edxapp install /home/zyn/xblock-codeeditor
      
      注意：/home/zyn/xblock-codeeditor是你在1.1中克隆的xblock-codeeditor所在的路径
      
  1.3 把static文件夹复制到/edx/app/edxapp/venvs/edxapp/local/lib/python2.7/site-packages/static/
  
      sudo cp -r static/* /edx/app/edxapp/venvs/edxapp/local/lib/python2.7/site-packages/static/
      
  1.4 把codeeditor文件夹复制到 /edx/var/edxapp/staticfiles/下
  
      sudo cp -r codeeditor /edx/var/edxapp/staticfiles/
      
2.使block可用：

   2.1在edx-platform/lms/envs/common.py中去掉注释：
   
        # from xmodule.x_module import prefer_xmodules
        # XBLOCK_SELECT_FUNCTION = prefer_xmodules
        
   2.2	在edx-platform/cms/envs/common.py,中去掉注释：
   
         # from xmodule.x_module import prefer_xmodules
        # XBLOCK_SELECT_FUNCTION = prefer_xmodules
        
   2.3	在edx-platform/cms/envs/common.py中把
   
         'ALLOW_ALL_ADVANCED_COMPONENTS': False,
         
       改成：
       
         'ALLOW_ALL_ADVANCED_COMPONENTS': True,

3.在Studio中把你的block添加到课程的高级设置中。

   1）登录到Studio,打开你的课程
   
   2）settings->Advanced Setting
   
   3)把键”advanced_modules”的值改为"codeeditor".
   
4.在studio中,把你的block添加到课程，

   1）Edit编辑一个单元
   
   2）Advanced->codeeditor
   


注意：如果把codeeditor文件夹放在其他位置。记得改/static/html/下的codeeditor_view.html中的src

 <iframe src="http://192.168.1.113/static/codeeditor/codemirror.html">
 
把"http://192.168.1.113/static/codeeditor/codemirror.html"换成你实际codeeditor文件夹所在位置。
  
  
