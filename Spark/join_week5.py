def split_show_views(line):
    show,views=line.split(",")
    return (show, views)


def split_show_channel(line):
    show,channel=line.split(",")
    return (show, channel)



def extract_channel_views(show_views_channel):
    _, (views, channel) = show_views_channel
    return channel, views



def some_function(a, b):
    a=int(a)
    b=int(b)
    return a+b


def unique_values(key_value):
    key = key_value[0]
    value = key_value[1]
    value = value.strip()
    values = value.split(',')
    unique_values = []
    for val in values:
        if not val in unique_values:
            unique_values.append(val)
    return_values = []
    for val in unique_values:
        return_values.append((key, val))
    return tuple(return_values)


if __name__ == '__main__':
    print unique_values(('PostModern_Cooking', 'DEF,CNO,CNO,NOX,MAN,MAN,XYZ,BAT,CAB,DEF'))
