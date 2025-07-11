import psutil
import threading
import time
from prometheus_client import Gauge

CPU_USAGE = Gauge('system_cpu_usage_percent', 'System CPU Usage Percent')
MEMORY_USAGE = Gauge('system_memory_usage_bytes', 'System Memory Usage Bytes')
FD_COUNT = Gauge('system_open_file_descriptors', 'System Open File Descriptors')
THREADS = Gauge('system_threads', 'Number of Threads')
UPTIME = Gauge('system_uptime_seconds', 'System Uptime seconds')

_start_time = time.time()

def collect_system_metrics():
    try:
        CPU_USAGE.set(psutil.cpu_percent())
        MEMORY_USAGE.set(psutil.virtual_memory().used)
        try:
            FD_COUNT.set(psutil.Process().num_fds())
        except AttributeError:
            FD_COUNT.set(0) # for windows
        THREADS.set(psutil.Process().num_threads())
        UPTIME.set(time.time() - _start_time)
    except Exception as e:
        pass

def metric_loop():
    while True:
        collect_system_metrics()
        time.sleep(5)

def start_system_metric_collector():
    thread = threading.Thread(target=metric_loop, daemon=True)
    thread.start()
