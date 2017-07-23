from antlr4 import ParserRuleContext

def error(ex:Exception, message, ctx:ParserRuleContext):
    raise ex(message+" - Line : {0} / Col : {1}".format(ctx.start.line, ctx.start.column))

