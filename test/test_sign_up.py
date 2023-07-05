from pylenium.driver import Pylenium
from faker import Faker
import time 

def generate_accountName():
    fake = Faker()
    return fake.company()

def generate_firstName():
    fake = Faker()
    return fake.first_name()

def generate_lastName():
    fake = Faker()
    return fake.last_name()

def generate_email():
    fake = Faker()
    return fake.email()

def test_generate_email():
    email = generate_email()
    assert '@' in email  # Ensure that the generated email contains an '@' symbol
    assert '.' in email  # Ensure that the generated email contains an '.' symbol

def generate_canadian_phone_number():
    fake = Faker()
    return fake.phone_number()

def test_generate_canadian_phone_number():
    phone_number = generate_canadian_phone_number()
    assert phone_number.startswith("+1")  # Ensure that the generated phone number starts with "+1"
    assert len(phone_number) == 12  # Ensure that the generated phone number has a total length of 12 characters

def generate_password():
    fake = Faker()
    return fake.password(length=8, special_chars=True, digits=True, upper_case=True, lower_case=True)

    

def test_sign_up(py: Pylenium):
    py.visit('https://sumoquoteweb-qa.azurewebsites.net/new-account')
    organization_name = generate_accountName()
    py.get('[id="accountName"]').type(organization_name)
    first_name = generate_firstName()
    py.get('[id="firstName"]').type(first_name)
    last_name = generate_lastName()
    py.get('[id="lastName"]').type(last_name)
    email = generate_email()
    py.get('[id="emailAddress"]').type(email)
    phone_number = generate_canadian_phone_number()
    py.get('[id="phoneNumber"]').type(phone_number)
    password = generate_password()
    confirm_password = password  # Set the confirm password to be the same as the generated password
    py.get('[id="Password"]').type(password)
    py.get('[id="repeatPassword"]').type(confirm_password)
    py.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    py.get('[class="v-input__icon v-input__icon--append"]').click()
    time.sleep(1)
    py.get('[id="list-item-477-3"]').click()
    time.sleep(1)
    py.get('[class="v-input--selection-controls__ripple"]').click()
    py.get('[class="btn-sumo-primary v-btn v-btn--has-bg theme--light elevation-0 v-size--default"]').click()
    time.sleep(10)
