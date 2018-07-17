from selenium.webdriver.common.by import By

# for maintainability we can seperate web objects by page name

class MainPageLocatars(object):
  LOGO          = (By.XPATH, '/html/body/div[2]/div[4]/div[2]/div/div[1]/div[1]/div/div/a/img')
  ACCOUNT       = (By.ID, 'nav-link-yourAccount')
  SIGNUP        = (By.CSS_SELECTOR, '#nav-flyout-ya-newCust > a')
  LOGIN         = (By.CSS_SELECTOR, '#nav-flyout-ya-signin > a')
  SEARCH        = (By.ID, 'search_input')
  SEARCH_LIST   = (By.ID, 's-results-list-atf')
  SEARCH_LUPA   = (By.XPATH, '/html/body/div[2]/div[4]/div[2]/div/div[1]/div[3]/div/div[1]/div/div/form/button')
  IMAGE_BATMAN  = (By.ID, 'det_img_94')
  BUTTON_CARRINHO = (By.ID, 'button_cart_94')

class LoginPageLocatars(object):
  EMAIL         = (By.ID, 'ap_email')
  PASSWORD      = (By.ID, 'ap_password')
  SUBMIT        = (By.ID, 'signInSubmit-input')
  ERROR_MESSAGE = (By.ID, 'message_error')