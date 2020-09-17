def set_browser_preference(driver,browser):
    if browser == 'Firefox':
        preference_option = driver.FirefoxProfile()
        preference_option.set_preference("browser.download.folderList", 2)
        preference_option.set_preference("browser.download.manager.showWhenStarting", False)
        preference_option.set_preference("browser.download.useDownloadDir", True)
        preference_option.set_preference("plugin.disable_full_page_plugin_for_types", "application/pdf")
        preference_option.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
        preference_option.set_preference("pdfjs.disabled", False)
        preference_option.set_preference("dom.disable_beforeunload", True)
        return preference_option