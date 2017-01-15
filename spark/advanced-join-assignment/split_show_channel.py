def split_show_channel(line):
        show_channel = line.split(",")
        show = show_channel[0]
        channel = show_channel[1]
        return (show, channel)
