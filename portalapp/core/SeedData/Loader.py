from core.SeedData import SupportedLanguages
from core.SeedData.SupportedLanguages import SupportedLanguages_SeedData

class SeedDataLoader:

    @staticmethod
    def load(delete_old_data = True):

        #Delete old data if allowed. This may be required to preserve referrential integrity
        if delete_old_data:
            pass     

        #1. SupportedLanguages
        SupportedLanguages_SeedData.seed_data(delete_old_data)


