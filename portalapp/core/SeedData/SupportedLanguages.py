from core.models import SupportedLanguage

class SupportedLanguages_SeedData:

    @staticmethod
    def seed_data(delete_old_data = False):

        print ("\nSupported Language")

        if delete_old_data:
            print ("Deleting old data....")
            SupportedLanguage.objects.all().delete()

        data =  [
                    {'description': 'Spanish', 'languageKey': 'es', 'flagPic': '\static\core\\flags\\spanish.png'},
                    {'description': 'Francais (CA)', 'languageKey': 'fr', 'flagPic': '\static\core\\flags\\french.png'},
                    {'description' : 'English (US)', 'languageKey': 'en-us', 'flagPic': '\static\core\\flags\\english.png'},
                ]
        print ("Adding new data...")

        for k in data:
            print (k['description'] + ":" + k['languageKey'].__str__()) 
            sl = SupportedLanguage()
            sl.description = k['description']
            sl.languageKey = k['languageKey']
            sl.flagPic = k['flagPic']

            sl.save()

        print ("First: " + SupportedLanguage.objects.first().__str__())