"""
Contains some fields as utilities
"""
from django import forms
from django.conf import settings
from django.forms.util import flatatt
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

class NullCheckboxWidget(forms.CheckboxInput):
    
    def render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(attrs, type='checkbox', name=name)
        try:
            result = self.check_test(value)
        except: # Silently catch exceptions
            result = False
        if result:
            final_attrs['checked'] = 'checked'
        if not (value is True or value is False or value is None or value == ''):
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = force_unicode(value)
        return mark_safe(u'<input%s />' % flatatt(final_attrs))

    def value_from_datadict(self, data, files, name):
        if name not in data:
            # A missing value means False because HTML form submission does not
            # send results for unselected checkboxes.
            return False
        value = data.get(name)
        # Translate true and false strings to boolean values.
        values =  {'on': True, 'false': False}
        if isinstance(value, basestring):
            value = values.get(value.lower(), value)
        return value

    def _has_changed(self, initial, data):
        # Sometimes data or initial could be None or u'' which should be the
        # same thing as False.
        return bool(initial) != bool(data)

class SubFKWidget(forms.Select):
    """
    This widget creates a formfield for a foreignkey but linked to its subclasses.
    sub_options parameter is a list of options for every subclass linked to the field with this widget.
    Every item of this list has these following parameters:
        - application: application's name
        - model: model's name
        - html: represents the html that you want insert in the popup's link
    refer_id: represents css id of object needs add button
    calling: represents object that calls createAddButton
    """
    def __init__(self,sub_options = [],refer_id = '',calling = '', *args, **kwargs):
        """
        Takes following parameters:
        sub_options: is a list of dictionaries. Each dictionary has application (lower application's name), model (lower model's name), html (html for add popup link),
        refer_id: represents css id of object needs add button,
        calling: represents object that calls createAddButton
        """
        self.sub_options = sub_options
        self.refer_id = refer_id
        self.calling = calling
        self.validate_sub_options()
        super(SubFKWidget, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):
        """
        Renders this widget
        """
        rendered = super(SubFKWidget, self).render(name, value, attrs)
        return rendered + mark_safe(u"%s" % self.createAddButton())

    def createAddButton(self):
        """
        Creates html to add to widget
        """
        buttons = u""
        for item in self.sub_options:
            application = item['application']
            model = item['model']
            html = item['html']
            buttons += '<span class = "add_custom_button"><a href="/admin/'+application+'/'+model+'/add/" class="add-another" id="add_'+self.refer_id+'" onclick="return showAddAnotherPopupCustom(this,\''+self.calling+'\');">'+html+'</a></span>';
        return buttons
    
    def validate_sub_options(self):
        """
        Validates sub_options parameter
        """
        if not self.sub_options or self.sub_options == []:
            raise ValueError("Error in upy.widgets.SubFKWidget: sub_options can't be empty or none. Check configurations in model")
        for item in self.sub_options:
            if not item.has_key('application'):
                raise ValueError("Error in upy.widgets.SubFKWidget: missing argument 'application' in sub_options")
            if not item.has_key('model'):
                raise ValueError("Error in upy.widgets.SubFKWidget: missing argument 'model' in sub_options")
            if not item.has_key('html'):
                raise ValueError("Error in upy.widgets.SubFKWidget: missing argument 'html' in sub_options")
    
    class Media:
        js = (settings.JQUERY_LIB,
              '/upy_static/js/sub_foreignkey.js',)
        css = {"all" : ("/upy_static/css/sub_foreignkey.css",)}