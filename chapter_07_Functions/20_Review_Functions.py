def shut_down(s):
    if s == "Yes" or s == "yes" or s == "YES":
        return "Shutting down..."
    elif s == "No" or s == "no" or s == "NO":
        return "Shutdown aborted!"
    else:
        return "Sorry, I didn't understand you."