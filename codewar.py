import re
def to_camel_case(text):
    format = re.sub(r"[_|-]+", " ", text).title().replace(" ", "")
    return ''.join([format[0].lower(), format[1:]])


print(to_camel_case('hello-world_it-is_me'))
