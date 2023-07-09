from pylenium.driver import Pylenium
from faker import Faker
import time 
import pytest

def test_compliting_profile(py: Pylenium):
    py.visit('https://sumoquoteweb-qa.azurewebsites.net/new-account')
    py.get('[class="v-tab"]').click()
    time.sleep(3)
    py.get('[name="email"]', timeout=3).type('cejol24734@fitwl.com') #I tryed to use timout, but works only with time.sleep
    py.get('[name="password"]').type('Qq!12345')
    py.get('[class="auth0-label-submit"]').click()
    time.sleep(5)
    # py.scroll_to(0,200)
    py.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    py.get('[class="btn btn-sumo-primary v-btn v-btn--has-bg theme--light elevation-0 v-size--default"]').scroll_into_view().click() #scroll_into??
    time.sleep(3)
    py.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # time.sleep(3)
    # py.get('[id="fileUploadForm"]').click() #Adding the file
    # py.get('[class="d-flex flex-row flex-nowrap justify-center align-center"]').click()
    time.sleep(3)
    py.get('[id="capabilities"]').type('Roofing, Gutters')
    py.get('[id="capabilities2"]').type('Residental')
    py.get('[class="btn-sumo-primary mt-8 v-btn v-btn--has-bg theme--light elevation-0 v-size--default"]').click()
    # time.sleep(3)
    # py.get('[src="/images/templates/Template2.png"]').click() #can't select
    time.sleep(5)
    py.get('[class="btn-sumo-primary float-right v-btn v-btn--has-bg theme--light elevation-0 v-size--default"]').click()
    time.sleep(3)
    # py.get('[class="v-responsive__content"]').click()
    # py.get('[class="fill-height d-flex flex-column pa-10 pb-5 text-center v-card v-card--link v-sheet theme--light"]').click() #Can't select the element on the pop-up
    # time.sleep(3)
    py.get('[class="fill-height d-flex flex-column pa-10 pb-5 text-center v-card v-card--link v-sheet theme--light"]').click()
    time.sleep(3)
    py.get('[class="btn-sumo-primary mt-2 v-btn v-btn--has-bg theme--light elevation-0 v-size--default"]').click()
    py.get('[class="btn-sumo-primary float-right v-btn v-btn--has-bg theme--light elevation-0 v-size--default"]').click()
    time.sleep(3)

    
    


