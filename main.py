# Print a variable's name in Python

site = 'bobbyhadz.com'

result = f'{site=}'
print(result)  # 👉️ site='bobbyhadz.com'

# ✅ print variable name using f-string
variable_name = f'{site=}'.split('=')[0]
print(variable_name)  # 👉️ 'site'