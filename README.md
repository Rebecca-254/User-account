#  Django User Management System

This is a Django project in progress. It will allow users to register, log in, verify their accounts, manage their profiles, and be managed by an admin.

---

##  Project Status

🛠 Work in progress — started on **July 7, 2025**

---

##  Planned Features

- User Registration & Login
- Email Verification 
- Profile View & Edit
- Change Password
- Admin Panel
- Unit Tests (models and views)

---

## 1. Project Setup 

so i started by by setting up my project by by the name user-mgmt and create an app and named it account. to ensure that django recognises the app, i added it in the installed apps in the user-mgmt/setting.py.


![Screenshot (10)](https://github.com/user-attachments/assets/fb03a423-b552-40e1-8773-f2859e15f3d7)



---
## 2. User Registration & Login

This project includes a simple user authentication system using Django's built-in tools.

### it What’s Implemented

- **User Registration**
  - Uses Django’s `UserCreationForm`
  - Allows users to register with a username, email, and password
  - Accessible at: `/accounts/register/`
   
![Screenshot (11)](https://github.com/user-attachments/assets/06c59fed-ba87-4d7b-b1e1-f938f68cbcb4)

- **User Login**
  - Uses Django’s built-in `LoginView`
  - Allows registered users to log in securely
  - Accessible at: `/accounts/login/`
 
    ![Screenshot (12)](https://github.com/user-attachments/assets/d142d04c-e623-4f4e-a1d1-e48020dd53ef)


- **Redirection**
  - Upon successful login, users are redirected to the home page (`/`)



---
## 3. Email Verification (Custom Django Feature)
## Description

This project implements **email verification** as part of the user registration process. After a user registers, a confirmation email is sent with a verification link. Only verified users are allowed to log in and access their account.

---

###  How It Works

1. **User Registers**
   - User submits the registration form via `/account/register/`.
   
2. **Verification Email Sent**
   - A unique verification link is sent to the user’s email using Django's `send_mail()` function and `default_token_generator`.

3. **User Verifies Account**
   - When the user clicks the link, their account is marked as verified.

4. **Login Enabled**
   - Only verified users can log in through `/account/login/`.

---

### Files Involved

- `views.py`  
  Handles registration, email sending, and token validation.
  
- `urls.py`  
  Maps verification URLs like `verify/<uidb64>/<token>/`.

- `register.html`  
  Registration form.

- `email_verification.html`  
  Template used for sending email content (if HTML email is used).

---

### 🛠️ Email Configuration (`settings.py`)

python
# Development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_FROM_EMAIL = 'noreply@example.com'

![Screenshot (13)](https://github.com/user-attachments/assets/42e16e65-af7f-45cb-888d-bedfe92df20c)

##  Profile Management

###  View & Edit Profile
- Logged-in users can view their personal profile page.
- Users can update their information (e.g., username, email, etc.).
- Form is prefilled with current data for easy editing.
- Upon successful update, a confirmation message is displayed.

![Screenshot (15)](https://github.com/user-attachments/assets/29ceabc8-5f50-4d4e-a9d9-61ea3b3b2945)


###  Change Password
- Users can change their password while logged in.
- Old password is required to ensure security.
- New password must meet Django’s password validation rules.
- After changing the password:
  - The user is immediately logged in with the new password.
  - A success message is shown.

###  Tech Used
- Django’s built-in `UserChangeForm`, `PasswordChangeForm`, and authentication views.
- `@login_required` decorator to restrict access to logged-in users only.


---
##  License

For educational use only.
