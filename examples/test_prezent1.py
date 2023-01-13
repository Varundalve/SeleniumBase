"""Use SeleniumBase to test MyPrezent Application"""

from seleniumbase import BaseCase

BaseCase.main(__name__, __file__)


class MyPrezentTests(BaseCase):

    def login(self):
        self.open("https://prezent-livestaging.myprezent.com/signin")
        self.add_text("[id='username']", "intrvu_testuser_01.noreply@prezent.ai")
        self.click("[id='continue']")
        self.add_text("[id='password']", "kiqjemkh")
        self.click("[id='submit']")

    def test_verify_login_logout(self):
        self.login()
        self.click("div[name='profile-icon']", delay=2)
        self.click("//*[ text() = ' Sign Out ']")
        assert self.assert_url_contains("https://prezent-livestaging.myprezent.com/signin")

    def test_download_first_slide(self):
        self.login()
        self.click('a[id="v-step-2"]', delay=2)
        self.click("div[class='pl-1 download-actions icon']", delay=2)
        self.click("div[class*='download-from-new-present-list']")
        self.click("div[name='profile-icon']", delay=2)
        self.click("//*[ text() = ' Sign Out ']")
        assert self.assert_url_contains("https://prezent-livestaging.myprezent.com/signin")

    def test_fingerprint_tab(self):
        self.login()
        self.click("div[name='profile-icon']", delay=2)
        self.click("[id='fingerprint-tab']")   # fingerprint tab
        self.click('[class="btn-retake"]')     # retake fingerprint
        self.click('[id="discover"]')          # discover my fingerprint
        for i in range(6):
            self.click('[class="images-wrapper"] img')
            self.click('[class="v-btn__content"]')
        self.click('[class="selections"] div span[class="selection-title"]')
        self.click('span[class="v-btn__content"]')
        self.click('span[class="v-btn__content"]')
        text = self.get_text('[class="fingerprint-center-item"]')
        assert text == "Re-take fingerprint test"
