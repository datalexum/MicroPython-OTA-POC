from libs.ota_updater import OTAUpdater
import secrets_config


def download_and_install_update_if_available():
    o = OTAUpdater('https://github.com/datalexum/MicroPython-OTA-POC', github_src_dir='src')
    o.install_update_if_available_after_boot(secrets_config.WIFI_SSID, secrets_config.WIFI_PASSWORD)


def start():
    import app.start


def boot():
    download_and_install_update_if_available()
    start()


boot()
