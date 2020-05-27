import time

memory_list = []

if __name__ == '__main__':
    print("start container")

    while True:
        key = str(int(time.time()))
        new_list = ["{}_{}".format(key, i) for i in range(100 * 10000)]
        memory_list.extend(new_list)
        print("memory len: {}".format(len(memory_list)))
        time.sleep(1)
