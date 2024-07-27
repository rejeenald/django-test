from django.apps import AppConfig
from core import models as CORE_MODELS

#django method that registers the application
class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps_main'
    title = "DIY Property Management"
    site_name = "RenterMade"

#portalapp class where we configure the application settings
class ApplicationSettings:
    
    @staticmethod
    def load():
        #Enable supported languages
        print ("Enabling Supported Languages")
        CORE_MODELS.SupportedLanguage.enable_language('en-us')
        CORE_MODELS.SupportedLanguage.enable_language('fr')

        #Setup application setting values
        print ("Initializing Application Settings")
        
        MySettings =  [
                    {'setting_key': CORE_MODELS.ApplicationSetting.APP_TITLE, 'languageKey': 'en-us', 'setting_value': 'RenterMade.com'},
                    {'setting_key': CORE_MODELS.ApplicationSetting.APP_TITLE, 'languageKey': 'fr', 'setting_value': 'RenterMade.com'},

                    {'setting_key': CORE_MODELS.ApplicationSetting.APP_SLOGAN, 'languageKey': 'en-us', 'setting_value': 'Online DIY Property Management'},
                    {'setting_key': CORE_MODELS.ApplicationSetting.APP_SLOGAN, 'languageKey': 'fr', 'setting_value': 'Gestion immobilière de bricolage en ligne'},

                    {'setting_key': CORE_MODELS.ApplicationSetting.COPYRIGHT_STRING, 'languageKey': 'en-us', 'setting_value': '© BuzzerBoy.com'},
                    {'setting_key': CORE_MODELS.ApplicationSetting.COPYRIGHT_STRING, 'languageKey': 'fr', 'setting_value': '© BuzzerBoy.com'},

                    {'setting_key': CORE_MODELS.ApplicationSetting.PRIMARY_LOGO_URL, 'languageKey': 'en-us', 'setting_value': '/static/main/logos/primary-roundrect.png'},
                    {'setting_key': CORE_MODELS.ApplicationSetting.PRIMARY_LOGO_URL, 'languageKey': 'fr', 'setting_value': '/static/main/logos/primary-roundrect.png'},

                ]
        CORE_MODELS.ApplicationSetting.update_settings(MySettings)