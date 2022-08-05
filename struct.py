import re
class Option:
    NAME_OPTION_PATTERN = "\('\w+\',"
    TYPE_OPTION_PATTERN = "type\s*:\s*\'\w+\'"
    VALUE_OPTION_PATTERN = "value\s*:\s*'\w+\'"
    def __init__(self, line):
        self.is_option = False
        if len(line) == 0 or line[0] == "#" or not "option" in line: return
            
        result = re.findall(Option.NAME_OPTION_PATTERN, line)
        if result is None or len(result) == 0: return
        self.name = re.findall("\w+", result[0])[0]

        result = re.findall(Option.TYPE_OPTION_PATTERN, line)
        if result is None or len(result) == 0: return
        self.type = re.findall("\w+", result[0])[1]

        result = re.findall(Option.VALUE_OPTION_PATTERN, line)
        if result is None or  len(result) == 0: return
        self.value = re.findall("\w+", result[0])[1]
        
        self.is_option = True

    def __str__(self):
        return f'name: {self.name}, type: {self.type}, value: {self.value}'


