def in_dictionary(key, dict):
    if key in dict:
        return True
    return False

author = 'whitepride'
temp_message = {}
temp_message[author] = {}
data = '123'


if in_dictionary('message', temp_message[author]):
    temp_message[author]['message'].append(data)
else:
    temp_message[author]['message'] = []
if in_dictionary('counter', temp_message[author]):
    temp_message[author]['counter'] += 1
else:
    temp_message[author]['counter'] = 0
print(temp_message)
