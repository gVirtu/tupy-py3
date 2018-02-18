import tupy.Interpreter
import re

def preprocess(inputString:str):
    lines = inputString.splitlines()
    parsedLines = []
    visibleLines = []
    # First pass: Find trace bars
    for i, line in enumerate(lines, 1):
        if line.lstrip().startswith("---"):
            tupy.Interpreter.Interpreter.traceBars.append(i)
        elif line.lstrip().startswith("~~~"):
            tupy.Interpreter.Interpreter.invisiBars.append(i)

    invisiBarCount = len(tupy.Interpreter.Interpreter.invisiBars)
    invisible = bool(invisiBarCount%2)
    currentInvisiBar = 0

    # Second pass: Determine what's visible
    for i, line in enumerate(lines, 1):
        if currentInvisiBar < invisiBarCount and \
           tupy.Interpreter.Interpreter.invisiBars[currentInvisiBar] == i:
            invisible = not invisible
            currentInvisiBar += 1

        if line.lstrip().startswith("---") or line.lstrip().startswith("~~~"):
            parsedLines.append("")
            visibleLines.append("<INVISIBLE>")
        elif line.rstrip().endswith(" ~~"):
            tupy.Interpreter.Interpreter.traceSquiggles.add(i)
            result = line.rstrip()[:-3]
            parsedLines.append(result)
            visibleLines.append("<INVISIBLE>")
        elif line.rstrip().endswith(" --"):
            tupy.Interpreter.Interpreter.traceSquiggles.add(i)
            result = line.rstrip()[:-3]
            parsedLines.append(result)
            visibleLines.append(result)
        else:
            parsedLines.append(line)
            if invisible:
                visibleLines.append("<INVISIBLE>")
            else:
                visibleLines.append(line)

    parsed = "{0}\n".format("\n".join(parsedLines))
    visible = "{0}\n".format("\n".join(visibleLines))
    return (parsed, visible)
