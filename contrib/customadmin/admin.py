from django.contrib import admin
from django import forms
from upy.contrib.customadmin.models import CustomAdmin, CustomApp, CustomLink, _,list_apps
from upy.contrib.image.admin import PositionImageOption
from upy.utils import upy_re_match



def cleaning_color_picker(form, fields):
    chk = True
    for field in fields:
        
        if form.cleaned_data[field] and not upy_re_match(r'^[0-9a-fA-F]+$',"%s" % form.cleaned_data[field]):
            chk = False
            form._errors[field] = form.error_class([_(u'You must compile this field with hexadecimal characters')])
        if form.cleaned_data[field] and len(form.cleaned_data[field]) != 6:
            chk = False
            form._errors[field] = form.error_class([_(u'You must compile this field with six hexadecimal characters')])
    return form, chk

class CustomAdminForm(forms.ModelForm):          
    def clean(self): 
        view_mode = self.cleaned_data['view_mode']
        autocomplete_app_list = self.cleaned_data['autocomplete_app_list']

        if view_mode and not autocomplete_app_list:
            try:
                CustomApp.objects.get(application__iexact="Customadmin")
            except CustomApp.DoesNotExist:
                msg_view_mode = _(u"You have to define Customadmin in your CustomApp if you use a custom view_mode...")
                msg_autocomplete_app_list= _(u"...or at least enable autocomplete_app_list which will include Customadmin too.")
                self._errors["view_mode"] = self.error_class([msg_view_mode])
                self._errors["autocomplete_app_list"] = self.error_class([msg_autocomplete_app_list])
    
                # These fields are no longer valid. Remove them from the
                # cleaned data.
                del self.cleaned_data["view_mode"]
                del self.cleaned_data["autocomplete_app_list"]
                #raise forms.ValidationError(_("You have to define Customadmin in your CustomApp if you use a custom view_mode without autocomplete_app_list"))
        
        self, chk = cleaning_color_picker(self, ['bg_header','table_title_bg','table_title_color','h2_color','h3_color','link_color','link_hover_color'])
        
        if not chk:
            raise forms.ValidationError(_("Some values are not hexadecimal string"))
        
        return self.cleaned_data 

class CustomAdminOption(admin.ModelAdmin):
    list_display = ('customization','branding','branding_link','is_default','view_mode','autocomplete_app_list')
    list_editable = ('branding','branding_link','is_default')
    fieldsets = ((_('Branding'), {'fields':
                                (('branding', 'branding_link'),('branding_image','is_default')),
                    },),
                 (_('View Option'), {'fields':
                                (('view_mode', 'autocomplete_app_list'),),
                    },),
                 (_('Style'), {'fields':
                                (('bg_header',), ('sitename_font','sitename_font_size',
                                 'sitename_font_weight'),('table_title_bg','table_title_color'),
                                 ('h2_color','h2_size'),('h3_color','h3_size'),
                                 ('link_color','link_hover_color'),
                                 ),
                    },),
                 (_('Code'), {'fields':
                                (('use_css_code',),('css_code',)),
                    },),
                 )
    form = CustomAdminForm
    save_on_top = True
    class Meta:
        model = CustomAdmin

 
class CustomAppForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super(CustomAppForm, self).__init__(*args, **kwargs)
        listapps = list_apps()
        if self.instance:
            listapps.append([self.instance.application]*2)
        print listapps
        self.fields['application'].widget = forms.Select(choices=listapps)
        
    class Meta:
        model = CustomApp
        
class CustomAppOption(PositionImageOption):
    list_display = ('position','application','verbose_app_name','show_models','admin_thumbnail_view',)
    list_editable = ['position','verbose_app_name',]
    list_display_links = ['application',]
    prepopulated_fields = {'verbose_app_name': ('application',)}    
    
    fieldsets = ((_('Icons'), {'fields':
                                (('application', 'verbose_app_name'),('original_image'),('show_models',),),
                    },),
                 )
    save_on_top = True
    form = CustomAppForm
    class Meta:
        model = CustomApp
        
class CustomLinkOption(PositionImageOption):
    list_display = ('position','link_url','verbose_url_name','admin_thumbnail_view',)
    list_editable = ['position','verbose_url_name',]
    list_display_links = ['link_url',]
    prepopulated_fields = {'verbose_url_name': ('link_url',)}    
    
    fieldsets = ((_('Icons'), {'fields':
                                (('link_url', 'verbose_url_name'),('original_image'),),
                    },),
                 )
    save_on_top = True
    class Meta:
        model = CustomLink

    
admin.site.register(CustomAdmin, CustomAdminOption)
admin.site.register(CustomApp, CustomAppOption)
admin.site.register(CustomLink, CustomLinkOption)
