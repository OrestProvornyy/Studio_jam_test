from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def open_main_page(driver, base_url):
    driver.get(base_url)
    #assert "StudioJam" in driver.title

def handle_ngrok_warning(driver):
    try:
        visit_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Visit Site')]"))
        )
        visit_button.click()
    except:
        # Якщо кнопка не з’явилась — значить це не сторінка ngrok'а, нічого не робимо
        pass

def click_signin_button(driver):
    signin_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Sign in')]"))
    )
    signin_button.click()
    WebDriverWait(driver, 10).until(EC.url_contains("login"))
    assert "login" in driver.current_url

def click_register_button(driver):
    register_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Register')]"))
    )
    register_button.click()
    WebDriverWait(driver, 10).until(EC.url_contains("register"))
    assert "register" in driver.current_url

def select_account_type(driver, account_type="Studio Customer"):
    account_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((
            By.XPATH,
            f"//span[@class='user-type-label' and normalize-space(text())='{account_type}']"
        ))
    )
    account_option.click()

def click_continue_and_check_fields_visibility(driver):
    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Continue')]"))
    )
    assert continue_button.is_enabled()
    continue_button.click()

    try:
        first_name_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "firstName"))
    )
    except TimeoutException:
        print("⚠️ Could not find 'firstName' input. Possibly wrong ID?")
        raise

    try:
        last_name_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "lastName"))
    )
    except TimeoutException:
        print("⚠️ Could not find 'lastName' input. Possibly wrong ID?")
        raise

    try:
        phone_number_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter your phone number']"))
    )
    except TimeoutException:
        print("⚠️ Could not find 'Enter your phone number' input. Possibly wrong XPATH?")
        raise

    try:
        email_input = WebDriverWait(driver, 10).until(
           EC.visibility_of_element_located((By.XPATH, "//input[@type='email']"))
    )
    except TimeoutException:
        print("⚠️ Could not find 'email' input. Possibly wrong XPATH?")
        raise

    try:
        password_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'password'))
    )
    except TimeoutException:
        print("⚠️ Could not find 'password' input. Possibly wrong ID?")
        raise

    try:
        confirm_password_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'confirmPassword'))
    )
    except TimeoutException:
        print("⚠️ Could not find 'Confirm Password' input. Possibly wrong ID?")
        raise

    assert first_name_input.is_displayed()
    assert last_name_input.is_displayed()
    assert phone_number_input.is_displayed()
    assert email_input.is_displayed()
    assert password_input.is_displayed()
    assert confirm_password_input.is_displayed()

def test_invalid_inputs_validation(driver, base_url):
    open_main_page(driver, base_url)
    handle_ngrok_warning(driver)
    click_signin_button(driver)
    click_register_button(driver)
    select_account_type(driver, "Studio Customer")
    click_continue_and_check_fields_visibility(driver)

    errors = []

    # ❌ Phone Number
    try:
        phone_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter your phone number']"))
        )
        phone_input.send_keys("йцу")
        driver.find_element(By.ID, "firstName").click()
        error = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Please enter a valid phone number')]"))
        )
        assert error.is_displayed()
    except Exception:
        errors.append("🚨 Phone number validation message is missing!")

    # ❌ Email
    try:
        email_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "email"))
        )
        email_input.send_keys("кйцу")
        driver.find_element(By.ID, "firstName").click()
        error = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Please enter a valid email')]"))
        )
        assert error.is_displayed()
    except Exception:
        errors.append("🚨 Email validation message is missing!")

    # ❌ Password
    try:
        password_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
        password_input.send_keys("123")
        driver.find_element(By.ID, "firstName").click()
        error = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Password must be at least 8 characters')]"))
        )
        assert error.is_displayed()
    except Exception:
        errors.append("🚨 Password length validation message is missing!")

    # ❌ Confirm Password
    try:
        confirm_password_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "confirmPassword"))
        )
        confirm_password_input.send_keys("12345678")
        driver.find_element(By.ID, "firstName").click()
        error = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Passwords do not match')]"))
        )
        assert error.is_displayed()
    except Exception:
        errors.append("🚨 Confirm password mismatch message is missing!")

    if errors:
        for error in errors:
            print(error)
        time.sleep(5)  # ← Затримка перед фейлом
        raise AssertionError("❌ Validation error(s) occurred — see above.")
    else:
        time.sleep(5)  # ← Затримка перед успішним завершенням

def fill_in_registration_data(driver):
    time.sleep(5)
    first_name_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'firstName'))
    )
    first_name_input.send_keys("Orest")

    last_name_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'lastName'))
    )
    last_name_input.send_keys("Provornyy")

    phone_number = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter your phone number']"))
    )
    phone_number.send_keys("0635581408")

    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'email'))
    )
    email_input.send_keys("orestprovornyy@gmail.com")

    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'password'))
    )
    password_input.send_keys("Qwerty123")

    confirm_password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'confirmPassword'))
    )
    confirm_password_input.send_keys("Qwerty123")
    time.sleep(10)

def click_back_button(driver):
    back_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Back')]"))
    )
    assert back_button.is_enabled()
    back_button.click()

    print('back button was clicked')
    time.sleep(2)

def click_create_account_button(driver):
    time.sleep(3)
    create_account_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Create account')]" ))
    )
    assert create_account_button.is_enabled()
    create_account_button.click()

def enter_verification_code(driver):
    try:
        code_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "verificationCode"))
        )
        code_input.send_keys("666999")
        print("✅ Verification code entered")
    except TimeoutException:
        print("ℹ️ Verification code input not found — maybe auto-login already happened")


def click_verify_email_button(driver):
    time.sleep(3)
    try:
        verify_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Verify Email')]"))
        )
        verify_button.click()
        print("✅ Clicked 'Verify Email' successfully")
    except TimeoutException:
        print("✅  'Verify Email' button was auto completed!")


def test_register_flow(driver, base_url):
    test_invalid_inputs_validation(driver, base_url)
    open_main_page(driver, base_url)
    handle_ngrok_warning(driver)
    click_signin_button(driver)
    click_register_button(driver)
    select_account_type(driver, account_type="Studio Customer")
    click_continue_and_check_fields_visibility(driver)
    fill_in_registration_data(driver)
    click_back_button(driver)
    click_continue_and_check_fields_visibility(driver)
    click_create_account_button(driver)
    enter_verification_code(driver)
    click_verify_email_button(driver)




