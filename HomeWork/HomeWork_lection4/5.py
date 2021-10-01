test_template = """
Hello, my name is {{name}}

{{name}} is {{age}} years old

{{age}} is very big
"""

test_data = {
    "name": "Vasya",
    "age": "100"
}


def templatator(template: str, data: dict):
    result = template
    for key, value in data.items():
        result = result.replace("{{" + key + "}}", value)
    return result


print(templatator(test_template, test_data))
