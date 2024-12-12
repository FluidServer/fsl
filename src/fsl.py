# 📓 FluidServer .fsl Parser
# by clue <lost@biitle.nl>

def parse(data: str) -> dict:
    split = data.split('\n')

    fslVer = split[0].split(', ')[1].split('.')[0]

    settingsDict = {
        "Version": fslVer
    }

    for setting in split:
        pairs = setting.split('=')
        if setting.startswith((';', ':')):
            continue
        if len(pairs) < 2: 
            continue
        if len(pairs) > 2:
            continue
        settingsDict.update([pairs])

    print(".fsl parser: Read file.")
    print(" .fsl version "+fslVer)
    print(settingsDict)