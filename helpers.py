def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')