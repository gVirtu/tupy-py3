import tupy.Interpreter
import re

def preprocess(inputString:str):
    lines = inputString.splitlines()
    parsedLines = []
    visibleLines = []
    for i, line in enumerate(lines, 1):
        if line.lstrip().startswith("~~"):
            tupy.Interpreter.Interpreter.traceSquiggles.add(i)
            result = re.sub(r'~~\s*', "", line, count=1)
            parsedLines.append(result)
            visibleLines.append("<INVISIBLE>")
        elif line.lstrip().startswith("~>"):
            tupy.Interpreter.Interpreter.traceSquiggles.add(i)
            result = re.sub(r'~>\s*', "", line, count=1)
            parsedLines.append(result)
            visibleLines.append(result)
        elif line.lstrip().startswith("---"):
            tupy.Interpreter.Interpreter.traceBars.append(i)
            visibleLines.append(line)
        else:
            parsedLines.append(line)
            visibleLines.append(line)
    parsed = "{0}\n".format("\n".join(parsedLines))
    visible = "{0}\n".format("\n".join(visibleLines))
    return (parsed, visible)
