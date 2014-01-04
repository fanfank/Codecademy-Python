garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = "".join(x for x in garbled[ : : -1] if x != 'X')
print message