#-------------------------------------------
# Buzzerboy Template Portal Application
# Developed by: Fahad Zain Jawaid (fjawaid@buzzerboy.com)
# This model file should be lite, it serves as Super classes for all 
# -----------------------------------------------
# Each model should have the following requirements:
# ---- 1) Audit Trail on each record (Created At, Created By, Last Updated At, Last Updated By)
# ---- 2) Some tables will be unilingual, and other tables will be multilingual, Multlingual tables
# ---------- will store a language key field to track what language the row is in. This way, multiple
#----------- rows of that table can together form a language specific value stream
#-------------------------------------------------
# All portals that are based on this template will have authentication (username/password), and 
# --- so core portal app will include that functionality. 
# All portals will also support multilingualism, so that functionalility will be part of the core 
# --- as well. This will include a table for SupportedLanguages
# All portals will have a tenant and team feature. This means more than one user can collaboratively 
# --- work on items in the portal
# -----------------------------------------------

#Necessary imports
from django.db import models
from django.contrib.auth.models import User
import uuid, os
from ckeditor.fields import RichTextField
from django.utils.crypto import get_random_string

#CORE MODELS
class SupportedLanguage(models.Model):
    languageKey = models.CharField(max_length=6)
    description = models.CharField(max_length=255)
    flagURL = models.TextField
    flagPic = models.ImageField(null=True, blank=True, default="", upload_to="settings/flags")
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.description + " (" + self.languageKey + ")"

    def flag_img (self):
        return "<img id=flag'" + self.id.__str__() + "' src='" + self.flag_url + "'/>"

    @staticmethod
    def enable_language(languageKey):
        sl = SupportedLanguage.objects.get(languageKey=languageKey)
        if sl:
            sl.enabled = True
        sl.save()

    @staticmethod
    def get_languages():
        sl = SupportedLanguage.objects.filter(enabled=True)
        return sl

    @property
    def flag_url(self):
	    if self.flagPic and hasattr(self.flagPic, 'url'):
		    return self.flagPic.url 


#INHERITABLE MODELS
class AuditableBaseModel(models.Model):

    @staticmethod
    def random_related_name():
        return get_random_string(10);        

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    last_updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)

    id = models.AutoField(primary_key=True)

    class Meta:
       abstract = True

class Address(AuditableBaseModel):

    #address fields
    street = models.CharField(max_length=255, blank=True)
    street1 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    postalcode = models.CharField(max_length=255, blank=True)
    telephone = models.CharField(max_length=40, blank=True)
    email = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.street + '\n' + self.street1 + '\n' + self.city + '\n' + self.country + '\n' + self.postalcode

class Tenant(AuditableBaseModel):
    tenant_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    companyName = models.CharField(max_length=255, blank=True)
    company_website = models.TextField(null=True, blank=True)
    logo = models.ImageField(null=True, blank=True, default="", upload_to="settings/flags")

    #addresses
    billing_address = models.OneToOneField(Address, on_delete=models.DO_NOTHING, null=True, related_name='billing_tenant', blank=True)
    shipping_address = models.OneToOneField(Address, on_delete=models.DO_NOTHING, null=True, related_name='shipping_tenant', blank=True)

    def __str__(self):
        return self.companyName

    def team_count(self):
        return self.team.count()

class TenantUser (AuditableBaseModel):

    def upload_profile_file_name (instance, filename):
       fname, fextension = os.path.splitext(filename)
       s = "u_" + instance.id.__str__() + "__t_".__str__() + instance.tenant.id.__str__() + fextension
       return os.path.join (".data",  instance.tenant.tenant_uuid.__str__(), "tenantUser", s)


    tenant = models.ForeignKey(Tenant, on_delete=models.DO_NOTHING, related_name="team")

#    userType = models.ForeignKey(UserType, on_delete=models.DO_NOTHING)

    userObject = models.OneToOneField(User, related_name="profile", on_delete=models.DO_NOTHING)

    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255,blank=True)
    postalcode = models.CharField(max_length=7, blank=True)
    telephone = models.CharField(max_length=25, blank=True)
    aboutme = RichTextField(blank=True)

    address = models.OneToOneField(Address, on_delete=models.DO_NOTHING, related_name="tenantuser_address")
    profilePicture = models.ImageField(null=True, blank=True, default="", upload_to=upload_profile_file_name)
    notes = models.TextField(blank = True)
    language = models.ForeignKey(SupportedLanguage, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
#        return self.userObject.username + " @ " + self.tenant.companyName + " (" + self.userType.description + ")"
        return self.userObject.username + " @ " + self.tenant.companyName

    def getTenant(self):
        return self.tenant.companyName


class MutlilingualBaseModel(AuditableBaseModel):
    language = models.ForeignKey(SupportedLanguage, on_delete=models.DO_NOTHING)
    obj_lang_uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True
        unique_together = ('id', 'language',)

#CORE MODELS
class ApplicationSetting(MutlilingualBaseModel):
    setting_key = models.CharField(max_length=40)
    setting_value = models.TextField(blank=True)

    #SETTING KEY CONSTANTS
    APP_TITLE = 'APP_TITLE'
    PRIMARY_LOGO_URL = 'PRIMARY_LOGO_URL'
    APP_SLOGAN = 'APP_SLOGAN'
    COPYRIGHT_STRING = 'COPYRIGHT_STRING'
    SETTING_KEY_CHOICES = [
        (APP_TITLE, 'Application Title'),
        (PRIMARY_LOGO_URL, 'Primary Logo URL'),
        (APP_SLOGAN, 'Application Slogan'),
        (COPYRIGHT_STRING, 'Copyright Text'),
    ]
    setting_key = models.CharField(
        max_length=40,
        choices=SETTING_KEY_CHOICES,
        default=APP_TITLE,
    )

    def update_settings(arr):
        ApplicationSetting.objects.all().delete()
        for item in arr:
            print(item.__str__())

            f = ApplicationSetting()
            f.setting_key = item['setting_key']
            f.setting_value = item['setting_value']
            f.language = SupportedLanguage.objects.get(languageKey=item['languageKey'])
            f.created_by = User.objects.first()
            f.last_updated_by = User.objects.first()
            f.save()

    def __str__(self):
        return self.setting_key + "(" + self.language.__str__() + ")"

    def load_settings(language):
        settings = ApplicationSetting.objects.filter(language=language)

        res = {}
        for s in settings:
            res[s.setting_key] = s.setting_value

        return res