import threading

local_data = threading.local()


def thread_id(*privat_data):
    print(threading.current_thread().name)
    local_data.privat = privat_data
    print(local_data.privat)


privat_data_array = ["private_data_1", "private_data_2", "private_data_3", "private_data_4"]
threads = []

for data in privat_data_array:
    thr = threading.Thread(target=thread_id, args=data)
    thr.start()
    threads.append(thr)

for thr in threads:
    thr.join()
