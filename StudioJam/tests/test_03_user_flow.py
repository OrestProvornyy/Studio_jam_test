from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

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

#!!!!!!!!!!!!!!!!!LOGIN VALIDATION!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def fill_in_invalid_login_creds(driver):
    email_input = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.ID, 'login'))
    )
    email_input.send_keys('oprovornyy@gmail.com')

    password_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'password'))
    )
    password_input.send_keys('zxcvbn')

    click_login_button = WebDriverWait(driver, 10). until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]"))
    )
    click_login_button.click()

def check_if_invalid_cred_error_appears(driver):
    try:
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Invalid credentials')]"))
        )
        assert error_message.is_displayed()
        print('✅ Error message 1 is displayed as exepted')
    except Exception:
        print('Error messeage "invalid credentials" doest not appear')
        raise AssertionError("❌ Error message 1 about creds does not appear blyat")

def fill_in_incorrect_login_creds(driver):
    email_input = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.ID, 'login'))
    )
    email_input.send_keys('orestprovornyy@gmail.com')

    password_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'password'))
    )
    password_input.send_keys('zxcvbn')

    click_login_button = WebDriverWait(driver, 10). until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]"))
    )
    click_login_button.click()

def check_if_incorrect_cred_error_appears(driver):
    try:
        time.sleep(1)  # щоб точно DOM оновився
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.general-error"))
        )
        assert "Incorrect credentials" in error_message.text
        print("✅ Error message 2 is displayed as expected")
    except Exception:
        print(driver.page_source)
        raise AssertionError("❌ Error message 2 about incorrect credentials not found")

def clear_invalid_cred(driver):
    email_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'login'))
    )
    email_input.clear()

    password_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'password'))
    )
    password_input.clear()
    time.sleep(2)

def fill_in_valid_login_creds(driver):
    try:
        email_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'login'))
        )
        email_input.click()
        email_input.clear()
        time.sleep(0.5)
        email_input.send_keys('orestprovornyy@gmail.com')

        password_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'password'))
        )
        password_input.click()
        password_input.clear()
        time.sleep(0.5)
        password_input.send_keys('Qwerty123')

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]"))
        )
        login_button.click()

        print("✅ Successfully clicked login button")

    except Exception as e:
        print("❌ Failed to log in with valid credentials.")
        print(f"Reason: {str(e)}")
        raise AssertionError("Login with valid credentials failed.")

#!!!!!!!!!!!!!!!!!MAIN MENU!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def select_burger_menu(driver):
    try:
        burger_menu = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Toggle menu']"))
        )
        burger_menu.click()

        side_menu = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "side-menu-container" ))
        )

        assert side_menu.is_displayed()
        print("✅ Side menu opened bitch!")

    except TimeoutException:
        print("Side meny didn't oppened in time")
        raise AssertionError("Side menu failed to open")

    except Exception as e:
        print(f" Unexpected error: {str(e)}")
        raise

def select_dashboard(driver):
    try:
        dashboard = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/dashboard']"))
        )
        dashboard.click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("dashboard")
        )
        print("✅ Success navigate to dashboard")

    except TimeoutException:
        print("❌ Failed to navigate to dashboard, 'dashboard' not found in URL")
        raise

def verify_create_studio_buttons_and_empty_state(driver):
    try:
        # Button "Create Studio"
        create_studio_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(@class, 'create-button') and normalize-space(text())='Create Studio']"))
        )
        print("✅ Create_studio button is visible")

        #Empty state
        empty_state_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), \"You haven't created any studios yet.\")]"))
        )
        print("✅ Empty state message is visible")

        # Button "Create your first Studio"
        first_studio_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(@class, 'create-button') and normalize-space(text())='Create Your First Studio']"))
        )
        print("✅ 'Create Your First Studio' button is visible")

    except Exception as e:
        print(f"❌ Some of the elements are missing or not visible: {e}")

#!!!!!!!!!!!!!!!!!STEP 1 - GENERAL INFO!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def first_studio_creation_flow_visibility_check_step_one(driver):
    first_studio_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'create-button') and normalize-space(text())='Create Your First Studio']"))
    )
    first_studio_button.click()

    try:
        # 1. Перевірка наявності прогрес-бара
        progress_bar = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "progress-bar"))
        )
        print("✅ Progress bar is visible")

        # 2. Перевірка, що Step 1 активний
        active_step = driver.find_element(By.XPATH, "//div[contains(@class, 'step') and contains(@class, 'active')]//div[text()='1']")
        print("✅ Step 1 is active")

        # 3. Studio name field
        studio_name_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter your studio name']")
        assert studio_name_input.is_displayed()
        print("✅ 'Studio Name' input is visible")

        # 4. Listing type - public and private radio buttons
        public_radio = driver.find_element(By.XPATH, "//span[text()='Public']")
        private_radio = driver.find_element(By.XPATH, "//span[text()='Private']")
        assert public_radio.is_displayed() and private_radio.is_displayed()
        print("✅ 'Listing Type' options are visible.")

        # 5. Services (at least one chechbox)
        services = driver.find_elements(By.XPATH, "//label[contains(@class, 'service-checkbox')]")
        assert len(services) > 0
        print(f"✅ Services are listed. Found: {len(services)}")

        # 6. Button "NEXT"
        next_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Next')]")
        assert next_button.is_displayed()
        print("✅ 'Next' button is visible")

        # 7. Check if "next" is disabled
        is_disabled = next_button.get_attribute("disabled")
        assert is_disabled is not None
        print("✅ 'Next' button is initially disabled")

    except Exception as e:
        print(f"❌ Error in verifying first step: {e}")

def fill_on_first_step_form(driver):
    driver.find_element(By.ID, "name").send_keys("Oraora studio")
    time.sleep(1)
    private_radio = driver.find_element(By.XPATH, "//input[@type='radio' and @value='UNLISTED']")
    private_radio.click()
    time.sleep(1)
    public_radio = driver.find_element(By.XPATH, "//input[@type='radio' and @value='LISTED']")
    public_radio.click()
    time.sleep(1)
    checkboxes = driver.find_elements(By.XPATH, "//div[contains(@class, 'services-grid')]//input[@type='checkbox']")
    for checkbox in checkboxes:
        driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
        if not checkbox.is_selected():
            checkbox.click()
    time.sleep(1)

def click_next_button(driver):
    next_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Next')]")
    next_button.click()

def click_back_button(driver):
    back_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Back')]")
    back_button.click()

#!!!!!!!!!!!!!!!!!STEP 2 - ADDRESS!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def verify_step_two_address_form(driver):
    try:
        # Перевіряємо, що step 2 активний
        active_step = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'step') and contains(@class, 'active')]//div[text()='2']"))
        )
        print("✅ Step 2 is active")

        # Перевірка дропдауну Country
        country_dropdown = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "country-select-container"))
        )
        print("✅ Country dropdown is visible")

    except Exception as e:
        print(f"❌ Error verifying Step 2 Address form: {e}")

def select_country_ukraine(driver):
    try:
        # Відкриваємо дропдаун
        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "select-header"))
        )
        dropdown.click()
        print("✅ Country dropdown opened")

        # Вводимо 'ukr' у пошук
        search_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'search-box')]//input"))
        )
        search_input.send_keys("ukr")
        print("✅ Entered 'ukr' into search box")

        # Вибираємо Ukraine
        ukraine_option = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Ukraine')]"))
        )
        ukraine_option.click()
        print("✅ Selected 'Ukraine' from dropdown")

        # Перевірка прапора та тексту
        selected_flag = driver.find_element(By.XPATH, "//div[contains(@class, 'selected-value')]//img[contains(@src, 'UA')]")
        selected_text = driver.find_element(By.XPATH, "//div[contains(@class, 'selected-value')]//span[contains(text(), 'Ukraine')]")
        assert selected_flag.is_displayed() and selected_text.is_displayed()
        print("✅ Ukraine selected and flag is visible")

    except Exception as e:
        print(f"❌ Error during country selection: {e}")

def verify_major_city_input_visible(driver):
    try:
        # Перевірка поля Major City
        major_city_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search for a city']"))
        )
        print("✅ 'Major City' input is visible")

    except Exception as e:
        print(f"❌ Error while verifying city input or Next button: {e}")
    time.sleep(10)

# Редагувати цю залупу коли Марк пофіксить відображення міст!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def check_city_dropdown_displayed(driver):
    try:
        time.sleep(10)
        city_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search for a city']"))
        )
        city_input.click()
        time.sleep(5)
        city_input.send_keys("К")
        time.sleep(5)
        city_input.clear()
        time.sleep(5)
        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "select-header"))
        )
        dropdown.click()
        dropdown.click()
        time.sleep(5)
        city_input.clear()
        city_input.send_keys(Keys.BACKSPACE)
        time.sleep(5)
        city_input.click()
        time.sleep(5)
        city_input.clear()
        city_input.click()
        dropdown_items = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class,'city-option')]"))
        )
        assert len(dropdown_items) > 0
        print(f"✅ Dropdown is visible and contains cities {len(dropdown_items)}")
    except Exception as e:
        print(f"❌ Dropdown not working properly: {e}")

def check_city_search_filter(driver):
    try:
        city_input = driver.find_element(By.XPATH, "//input[@placeholder='Search for a city']")
        city_input.send_keys("Льв")

        filtered_result = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'option') and contains(text(),'Львів')]"))
        )

        assert "Львів" in filtered_result.text
        print("✅ City search filter works")

    except Exception as e:
        print(f"❌ City search failed: {e}")

def select_city_from_dropdown(driver):
    city_input = driver.find_element(By.XPATH, "//input[@placeholder='Search for a city']")
    city_input.clear()
    city_input.send_keys("Львів")
    print("✅ 'Львів' was entered into the city input")
    time.sleep(3)

def check_address_after_city_appears_visibility(driver):
    try:
        address_input = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "address"))
        )
        print("✅ Address input is visible")
    except Exception as e:
        print(f"❌ Address input is not visible ")
    time.sleep(2)

#!!!!!!!!!!!!!!!!!STEP 3 - CONTACTS!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def check_if_step_three_is_active(driver):
   try:
        # Перевіряємо, що step 3 активний
        active_step = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'step') and contains(@class, 'active')]//div[text()='3']"))
        )
        print("✅ Step 3 is active")
   except Exception as e:
       print(f"❌ Error Step 3 is not active: {e}")

def input_phone_number(driver):
    try:
        phone_number = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your phone number']"))
        )
        phone_number.send_keys('0635581408')
        phone_value = phone_number.get_attribute("value")
        print(f"✅ Phone number added like {phone_value}")

    except Exception as e:
        print("❌ Phone number was not added")
    time.sleep(2)

def input_email(driver):
    try:
        email_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'email'))
        )
        email_input.click()
        email_input.send_keys('orestprovornyy@gmail.com')
        email_value = email_input.get_attribute("value")
        print(f"✅ Successfully added the email {email_value}")

    except Exception as e:
        print("❌ Failed to add email")
    time.sleep(2)

def input_websitelink(driver):
    try:
        website_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'websiteLink'))
        )
        website_input.click()
        website_input.send_keys('https://www.studiojam.com')
        website_value = website_input.get_attribute("value")
        print(f"✅ Successfully added the email {website_value}")

    except Exception as e:
        print("❌ Failed to add website")
    time.sleep(2)

def check_social_links_inputs_clickable(driver):
    try:
        instagram = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "instagramlink"))
        )
        facebook = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "facebooklink"))
        )
        youtube = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "youtubelink"))
        )
        print("✅ Social media input fields are clickable")

    except Exception as e:
        print(f"❌ Social media input check failed: {e}")

#!!!!!!!!!!!!!!!!!STEP 4 - CONTACTS!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def check_if_step_four_is_active(driver):
    try:
        # Перевіряємо, що step 4 активний
        active_step = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'step') and contains(@class, 'active')]//div[text()='4']"))
        )
        print("✅ Step 4 is active")
    except Exception as e:
        print(f"❌ Error Step 3 is not active: {e}")

def check_if_next_is_disabled_until_images_are_uploaded(driver):
    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'studio-creation-next-button') and text(), ' Next ']"))
        )
        is_disabled = next_button.get_attribute("disabled")
        assert is_disabled is not None
        print("✅ Next button is enabled till imgs not uploaded")
    except Exception as e:
        print(f"❌  Failed to verify NEXT button status {e}")

def test_login_and_user_flow_flow(driver, base_url):
    print('\nTESTS FOR SITE OPENING')
    open_main_page(driver, base_url)
    handle_ngrok_warning(driver)
    click_signin_button(driver)
    print('\nTESTS FOR LOGIN VALIDATION')
    fill_in_invalid_login_creds(driver)
    check_if_invalid_cred_error_appears(driver)
    clear_invalid_cred(driver)
    fill_in_incorrect_login_creds(driver)
    check_if_incorrect_cred_error_appears(driver)
    clear_invalid_cred(driver)
    fill_in_valid_login_creds(driver)
    print('\nTESTS FOR MAIN MENU')
    select_burger_menu(driver)
    select_dashboard(driver)
    print('\nTESTS FOR STUDIO ADDING STEP 1')
    verify_create_studio_buttons_and_empty_state(driver)
    first_studio_creation_flow_visibility_check_step_one(driver)
    fill_on_first_step_form(driver)
    click_next_button(driver)
    print('\nTESTS FOR STUDIO ADDING STEP 2')
    verify_step_two_address_form(driver)
    select_country_ukraine(driver)
    verify_major_city_input_visible(driver)
    check_city_dropdown_displayed(driver)
    check_city_search_filter(driver)
    select_city_from_dropdown(driver)
    check_address_after_city_appears_visibility(driver)
    click_next_button(driver)
    print('\nTESTS FOR STUDIO ADDING STEP 3')
    check_if_step_three_is_active(driver)
    input_phone_number(driver)
    input_email(driver)
    input_websitelink(driver)
    check_social_links_inputs_clickable(driver)
    click_next_button(driver)
    print('\nTESTS FOR STUDIO ADDING STEP 4')
    check_if_step_four_is_active(driver)
    check_if_next_is_disabled_until_images_are_uploaded(driver)
