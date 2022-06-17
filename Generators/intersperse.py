def intersperse(iterator, separator):
    i = 0
    for item in iterator:
        if i > 0:
            yield separator
        yield item
        i += 1
