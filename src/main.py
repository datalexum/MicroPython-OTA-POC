 from ota_update.main.ota_updater import OTAUpdater


 def download_and_install_update_if_available():
     o = OTAUpdater('url-to-your-github-project')
     o.install_update_if_available_after_boot('wifi-ssid', 'wifi-password')


 def start():
    print("test")


 def boot():
     download_and_install_update_if_available()
     start()


 boot()
