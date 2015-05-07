import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment

import os

class CodeeditorBlock(XBlock):
    """
    An XBlock providing code edit capabilities 
    """

    src = String(help="the directory of your code", default=None, scope=Scope.content)
    width = Integer(help="width of the frame", default=800, scope=Scope.content)
    height = Integer(help="height of the frame", default=900, scope=Scope.content)

    def student_view(self, context=None):
        """
        The primary view of the CodeeditorBlock, shown to students
        when viewing courses.
        """
       
	 # Load the HTML fragment from within the package and fill in the template
        html_str = pkg_resources.resource_string(__name__, "static/html/codeeditor_view.html")
	
        frag = Fragment(unicode(html_str).format(
		width=self.width, 
		height=self.height,
		
	))
        # Load CSS
        css_str = pkg_resources.resource_string(__name__, "static/css/codeeditor.css")
        frag.add_css(unicode(css_str))
	

        js_str = pkg_resources.resource_string(__name__, "static/js/src/codeeditor_view.js")
        frag.add_javascript(unicode(js_str))
        frag.initialize_js('CodeeditorViewBlock')

        return frag

    def studio_view(self, context):
        """
        Create a fragment used to display the edit view in the Studio.
        """
        html_str = pkg_resources.resource_string(__name__, "static/html/codeeditor_edit.html")
        src = self.src or ''
        frag = Fragment(unicode(html_str).format(width=self.width, height=self.height))

        js_str = pkg_resources.resource_string(__name__, "static/js/src/codeeditor_edit.js")
        frag.add_javascript(unicode(js_str))
        frag.initialize_js('CodeeditorEditBlock')

        return frag

    @XBlock.json_handler
    def studio_submit(self, data, suffix=''):
        """
        Called when submitting the form in Studio.
        """
        self.width = data.get('width')
        self.height = data.get('height')
        return {'result': 'success'}

    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("Code editor",
            """
            <vertical_demo>
            </vertical_demo>
            """)
        ]