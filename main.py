import sys, os, re
from struct import Option

if __name__ != "__main__" or len(sys.argv) < 2: exit()

meson_dir = sys.argv[1]

value = None
features = None
if len(sys.argv) > 2:
    value = sys.argv[2]

if len(sys.argv) > 3:
    features = sys.argv[3:]

def typeToValue(op, value):
    if value is None: return None 
    #print(op)
    return {
        op.type == "string": value if value == 'on' else '',
        op.type == "feature": 'enabled' if value == 'on' else 'disabled',  
        op.type == "boolean": 'true' if value == 'on' else 'false',
        op.type == "combo": None}[True]

for (dirpath, dirnames, filenames) in os.walk(meson_dir):
    if not "meson_options.txt" in filenames: continue
    print(dirpath)
    replacement = ''
    with open(os.path.join(dirpath, "meson_options.txt")) as f:
        for line in f:
            op = Option(line)
            if not op.is_option: 
                replacement += line
                continue
            if value is None:
                print(' '*len(dirpath), '|---', op)
                replacement += line
                continue
            if features is None or op.name in features:
                op.value = typeToValue(op, value)
                if op.value is None: 
                    replacement += line
                    continue
                replacement += re.sub("value\s*:\s*'\w+\'", f"value: '{op.value}'", line)
                print(' '*len(dirpath), '|---', op)
                continue
            
            replacement += line
    if value is None: continue
    with open(os.path.join(dirpath, "meson_options.txt"), "w") as f:
        f.write(replacement)
             
   # print(replacement)

            
    