def debug_in_out(func):
    def wrapped(*args, **kwargs):
        print "Enter {0}".format(func.__name__)
        ret = func(*args, **kwargs)
        print "Leave {0}".format(func.__name__)
        return ret
    return wrapped


