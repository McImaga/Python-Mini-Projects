# 04 - Email Validator with Logging

A simple CLI tool to validate email addresses, clean input, and log user activity.

### **Features**
- Validates email format using regex
- Cleans input: strips spaces + converts to lowercase  
- Extracts username and domain name
- Logs all login attempts to `email_activity.log`

### **How to Run**
```bash
python email_validator.py