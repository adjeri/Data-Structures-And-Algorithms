def serverLog(t,logs):
    if t == 0:
        return '-1'

    limit = None
    for i in range(len(logs)):
        log = logs[i]
        splitted = log.split(' ')
        if int(splitted[0]) >= t:
            limit = i
            break
    sliced = logs[:limit]

    struct = {}
    for i in range(len(sliced)-1, 0, -1):
        log = sliced[i]
        splitted = log.split(' ')
        if splitted[1] not in struct:
            struct[splitted[1]] = splitted[2]
    # print(struct)
    running = 0
    for element in struct:
        if struct[element] == 'running':
            # print('run +1 ')
            running += 1

    if running == 1:
        for element in struct:
            if struct[element] == 'running':
                return element
    else:
        return '-1'
