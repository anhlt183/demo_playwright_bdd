# Python Playwright BDD Hybrid Automation Framework

A robust, scalable test automation framework using **Python**, **Playwright**, **Behave (BDD)**, and the **Page Object Model (POM)** architecture.

---

## 🧱 Project Structure

```
hybrid_framwork_BDD/
│
├── features/
│   ├── login.feature                   # Login test scenarios (valid, invalid, outline)
│   ├── logout.feature                  # Logout scenarios
│   ├── sorting_product_list.feature    # Sorting product list scenario (by name, price)
│   ├── image_of_product.feature        # Image test scenarios (displaying, attribute, navigation)
│   ├── add_product_cart.feature        # Adding product to cart scenarios
│   ├── remove_product_cart.feature     # Removing product from cart scenarios
│   └── checkout.feature                # Check out scenarios   
│
├── pages/
│   ├── base_page.py            # Common page class
│   ├── login_page.py           # Page class for login and logout
│   ├── home_page.py            # Page class for home page
│   ├── product_detail_page.py  # Page class for product detail page
│   ├── cart_page.py            # Page class for cart page
│   ├── your_information_page.py  # Page class for checkout information page
│   ├── overview_page.py          # Page class for checkout overview page  
│   ├── complete_page.py          # Page class for checkout complete page  
│   └── locators/
│       ├── base_locators.py             # Locators for common page   
│       ├── login_locators.py            # Locators for login page
│       ├── home_locators.py             # Locators for home page
│       ├── product_detail_locators.py   # Locators for product detail page   
│       ├── cart_locators.py             # Locator for cart page   
│       ├── your_information_locators.py # Locator for checkout information page
│       ├── overview_locators.py         # Locator for checkout overview page
│       └── complete_locators.py         # Locator for checkout complete page
│
├── step_definations/
│   ├── common_steps.py                # contains step definitions that are used across multiple feature files    
│   ├── test_login.py                   # Step definitions for login
│   ├── test_logout.py                  # Step definitions for logout
│   ├── test_sorting_product_list.py    # Step definitions for sorting
│   ├── test_image_of_product.py
│   ├── test_add_product_cart.py
│   ├── test_remove_product_cart.py
│   └── test_checkout.py    
│
├── config/
│   └──config.py                # config URL,...      
│
├── myenv/                      # Python virtual environment
├── conftest.py                 # config to open and close browser  
├── pytest.ini                  # config key aspects of how pytest-bdd discovers and runs tests
├── README.md                   # Project documentation
└── requirements.txt            # List out all libraries and versions
```

---

## 🤖 Tech Stack

| Component       | Description                           |
|---------------  |---------------------------------------|
| **Python**      | Core programming language             |
| **Playwright**  | End-to-End Browser Automation         |
| **Pytest**      | Python testing framework              |
| **POM**         | Page Object Model for abstraction     |
| **Logging**     | `logging` module for step tracing     |

---

## 🌊 Features Covered

### **Login Functionality**

- Successful login with valid credentials  
- Login failure with invalid credentials  
- Scenario Outline for data-driven invalid login test cases  
- Form validation for blank fields

### **Logout Functionality**

- Log out from the Home page  
- Redirects back to login page  
- Login form remains visible after logout  

### **Sorting product list on Home page Functionality**

- Sorting product list with Name (A to Z) order 
- Sorting product list with Name (Z to A) order  
- Sorting product list with Price (low to high) order  
- Sorting product list with Price (high to low) order  

### **Product image validation on inventory page**

- Product images are displayed on inventory page
- Product images have valid src and alt attributes
- Product images navigation

### **Adding/Removing cart functionality**

- Adding product from inventory/product detail page
- Removing product from inventory/cart page

### **Checkout functionality**

- Checkout the product successfully
- Cancel checkout
---

## 🏃 How to run test  

### **Installation steps**

1. In Terminal, select the root folder project `cd hybrid_framwork_BDD`
2. Create virtual environment management directory `python -m venv myenv`
3. Activate virtual environment `myenv\Scripts\activate`
4. Install all project dependencies with `pip install -r requirements.txt`
5. Install Playwright for Python
```
pip install playwright
playwright install
```
6. Exports the current environment's installed packages into a requirements.txt `pip freeze > requirements.txt`

### **Run the test**

Run all test `pytest`  
Run specific feature file `pytest -v -k logout`  
Run specific scenarion in a feature file `pytest -v -k "successfull_logout_from_the_application"`  

### **Notes & Best Practices**

- Use `strip()` or default `''` for empty string handling in Scenario Outlines.
- Structure your Page classes well with locators, actions, and status checkers.

---

## 👨‍🚀 Author

**AnhLT183**  
_A QA Engineer.