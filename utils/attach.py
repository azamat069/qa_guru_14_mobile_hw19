import requests
import allure
import os
from allure_commons.types import AttachmentType


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_xml(browser):
    xml_dump = browser.driver.page_source
    allure.attach(body=xml_dump,
                  name='XML screen',
                  attachment_type=AttachmentType.XML)


def add_video(session_id):
    browserstack_session = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(os.getenv('USER_NAME'), os.getenv('ACCESS_KEY'))
    ).json()
    video_url = browserstack_session['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='video recording',
        attachment_type=AttachmentType.HTML,
    )