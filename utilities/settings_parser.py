import os
import json

from settings import Settings


class SettingsParse:
    SETTINGS_CONFIG: str = "etfbl-oglasi\settings.json"

    @staticmethod
    def save(settings: Settings):
        path = os.getenv('APPDATA')
        os.mkdir(path)

        json_object = vars(settings)
        with open(SettingsParse.SETTINGS_CONFIG, "w") as outfile:
            outfile.write(json_object)

    @staticmethod
    def read() -> Settings:
        if not os.path.exists(SettingsParse.SETTINGS_CONFIG):
            SettingsParse.save(Settings())

        with open(SettingsParse.SETTINGS_CONFIG) as infile:
            data = json.load(infile)
            return data
