
name = 'Carlos'
last_name = 'Santana'

# Using f-strings (Python 3.6+)
full_name_fstring = f'{name} {last_name}'
print(full_name_fstring)
# Using str.format() method
full_name_format = '{} {}'.format(name, last_name)
print(full_name_format)
# Using % operator
full_name_percent = '%s %s' % (name, last_name)
print(full_name_percent)
# Using concatenation
full_name_concat = name + ' ' + last_name
print(full_name_concat)
# Using join() method
full_name_join = ' '.join([name, last_name])
print(full_name_join)
# Using template strings
from string import Template
template = Template('$name $last_name')
full_name_template = template.substitute(name=name, last_name=last_name)
print(full_name_template)

# String indexing and slicing
sample_text = 'Hello, World!'
first_char = sample_text[0]
print(first_char)  # H
substring = sample_text[0:5]
print(substring)  # Hello
stepover_substring = sample_text[::2]
print(stepover_substring)  # Hlo ol!
last_char = sample_text[-1]
print(last_char)  # '!'
length = len(sample_text)
print(length)  # 13
reversed_text = sample_text[::-1]
print(reversed_text)  # '!dlroW ,olleH
upper_text = sample_text.upper()
print(upper_text)  # 'HELLO, WORLD!'
lower_text = sample_text.lower()
print(lower_text)  # 'hello, world!'
capitalized_text = sample_text.capitalize()
print(capitalized_text)  # 'Hello, world!'
title_text = sample_text.title()
print(title_text)  # 'Hello, World!'
strip_text = '   Hello, World!   '.strip()
print(strip_text)  # 'Hello, World!'
replace_text = sample_text.replace('World', 'Python')
print(replace_text)  # 'Hello, Python!'
find_index = sample_text.find('World')
print(find_index)  # 7
split_text = sample_text.split(', ')
print(split_text)  # ['Hello', 'World!']
# Joining a list of strings
words = ['Hello', 'from', 'Python']
joined_text = ' '.join(words)
print(joined_text)  # 'Hello from Python'
# Multi-line string
multi_line = """This is line one.
This is line two."""
print(multi_line)
# Raw string
raw_string = r'C:\Users\Name\Documents'
print(raw_string)  # C:\Users\Name\Documents
# Unicode string
unicode_string = u'Hello, \u2602'
print(unicode_string)  # Hello, ☂
# Byte string
byte_string = b'Hello, World!'
print(byte_string)  # b'Hello, World!'
# Formatted string with specific width and precision
formatted_number = '{:.2f}'.format(3.14159)
print(formatted_number)  # 3.14
padded_string = '{:>10}'.format('Hi')
print(padded_string)  # '        Hi'  # 10 characters wide, right-aligned
padded_number = '{:^10}'.format(42)
print(padded_number)  # '    42    '  # 10 characters wide, centered
percent_format = '{:.2%}'.format(0.756)
print(percent_format)  # 75.60%  # 75.60%
scientific_format = '{:.2e}'.format(12345.6789)
print(scientific_format)  # 1.23e+04  # Scientific notation
# Escape sequences
escape_sequence = "First Line\nSecond Line\tTabbed"
print(escape_sequence)
# String membership test
membership_test = 'World' in sample_text
print(membership_test)  # True
# String repetition
repeated_string = 'Ha' * 3
print(repeated_string)  # HaHaHa
# String comparison
comparison_result = 'apple' < 'banana'
print(comparison_result)  # True
# String formatting with named placeholders
named_format = 'Hello, {first} {last}!'.format(first='John', last='Doe')
print(named_format)  # Hello, John Doe!
# String formatting with dictionary
data = {'first': 'Jane', 'last': 'Doe'}
dict_format = 'Hello, {first} {last}!'.format(**data)
print(dict_format)  # Hello, Jane Doe!
print(full_name_fstring)  # Carlos Santana
print(full_name_format)   # Carlos Santana
print(full_name_percent)  # Carlos Santana
print(full_name_concat)   # Carlos Santana
print(full_name_join)     # Carlos Santana
print(full_name_template) # Carlos Santana
print(first_char)         # H
print(substring)          # Hello
print(stepover_substring)  # Hlo ol!
print(last_char)          # '!
print(length)             # 13
print(reversed_text)      # '!dlroW ,olleH
print(upper_text)         # 'HELLO, WORLD!'
print(lower_text)         # 'hello, world!'
print(capitalized_text)   # 'Hello, world!'
print(title_text)         # 'Hello, World!'
print(strip_text)         # 'Hello, World!'
print(replace_text)       # 'Hello, Python!'
print(find_index)        # 7
print(split_text)        # ['Hello', 'World!']
print(joined_text)       # 'Hello from Python'
print(multi_line)
print(raw_string)        # C:\Users\Name\Documents
print(unicode_string)    # Hello, ☂
print(byte_string)       # b'Hello, World!'
print(formatted_number)  # 3.14
print(padded_string)     # '        Hi'
print(padded_number)     # '    42    '
print(percent_format)    # 75.60%
print(scientific_format)  # 1.23e+04
print(escape_sequence) 
print(membership_test)   # True
print(repeated_string)   # HaHaHa
print(comparison_result)  # True
print(named_format)      # Hello, John Doe!
print(dict_format)       # Hello, Jane Doe!
print('---------------------')