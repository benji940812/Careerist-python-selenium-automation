# StackOverflow Create Account Page - Optimal XPaths

# Create your account
# $x("//h1[text()='Create your account']")
page_title = "//h1[text()='Create your account']"

# Terms and Privacy links
# $x("//form//a[text()='terms of service']")
terms_link = "//form//a[text()='terms of service']"
# $x("//form//a[text()='privacy policy']")
privacy_link = "//form//a[text()='privacy policy']"

# Email field
# $x("//input[@id='email']")
email_input = "//input[@id='email']"

# Password field
# $x("//input[@id='password']")
password_input = "//input[@id='password']"

# Password toggle icon
# $x("//*[contains(@class,'js-show-password')]")
password_toggle_icon = "//*[contains(@class,'js-show-password')]"

# Sign up
# $x("//button[@id='submit-button']")
sign_up_btn = "//button[@id='submit-button']"

# Sign up with Google
# $x("//button[@data-provider='google']")
google_btn = "//button[@data-provider='google']"

# Sign up with GitHub
# $x("//button[@data-provider='github']")
github_btn = "//button[@data-provider='github']"

# Stack Overflow for Teams
# $x("//a[contains(text(), 'Stack Overflow for Teams')]")
teams_link = "//a[contains(text(), 'Stack Overflow for Teams')]"
