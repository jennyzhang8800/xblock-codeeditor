����һ��ʵ�����ߴ���༭�����ܵ�xblock������codemirrorʵ�����ߴ���༭���ܡ�
1.��װ��
  1.1 ��xblock-coedeeditor��¡����open edxƽ̨�С����ҿ�¡��/home/zyn
      cd /home/zyn
      git clone https://github.com/jennyzhang8800/xblock-codeeditor
  1.2 ��װxblock
      sudo -u edxapp /edx/bin/pip.edxapp install /home/zyn/xblock-codeeditor
      
      ע�⣺/home/zyn/xblock-codeeditor������1.1�п�¡��xblock-codeeditor���ڵ�·��
  1.3 ��static�ļ��и��Ƶ�/edx/app/edxapp/venvs/edxapp/local/lib/python2.7/site-packages/static/
      sudo cp -r static/* /edx/app/edxapp/venvs/edxapp/local/lib/python2.7/site-packages/static/
  1.4 ��codeeditor�ļ��и��Ƶ� /edx/var/edxapp/staticfiles/��
      sudo cp -r codeeditor /edx/var/edxapp/staticfiles/
2.ʹblock���ã�
1����edx-platform/lms/envs/common.py��ȥ��ע�ͣ�
# from xmodule.x_module import prefer_xmodules
# XBLOCK_SELECT_FUNCTION = prefer_xmodules
2��	��edx-platform/cms/envs/common.py,��ȥ��ע�ͣ�
# from xmodule.x_module import prefer_xmodules
# XBLOCK_SELECT_FUNCTION = prefer_xmodules
3��	��edx-platform/cms/envs/common.py�а�
'ALLOW_ALL_ADVANCED_COMPONENTS': False,
�ĳɣ�
'ALLOW_ALL_ADVANCED_COMPONENTS': True,

3.��Studio�а����block��ӵ��γ̵ĸ߼������С�
   1����¼��Studio,����Ŀγ�
   2��settings->Advanced Setting
   3)�Ѽ���advanced_modules����ֵ��Ϊ"codeeditor".
4.��studio��,�����block��ӵ��γ̣�
   1��Edit�༭һ����Ԫ
   2��Advanced->codeeditor


ע�⣺�����codeeditor�ļ��з�������λ�á��ǵø�/static/html/�µ�codeeditor_view.html�е�src
<iframe src="http://192.168.1.113/static/codeeditor/codemirror.html">
��"http://192.168.1.113/static/codeeditor/codemirror.html"������ʵ��codeeditor�ļ�������λ�á�
  
  