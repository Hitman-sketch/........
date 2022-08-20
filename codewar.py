import re
def to_camel_case(text):
    s = re.sub(r"[_|-]+", " ", text).title().replace(" ", "")
    return ''.join([s[0].lower(), s[1:]])


print(to_camel_case('hello-world_it-is_me'))