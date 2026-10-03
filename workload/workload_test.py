import requests
import time
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

URL = "http://localhost:5000/monitor"

WORKLOADS = [1, 2, 4, 8, 16]
REQUESTS_PER_LEVEL = 500

CONTAINERS = [
    "satellite-container",
    "image-container",
    "analysis-container"
]


def get_docker_stats():
    cpu_values = []
    memory_values = []

    for container in CONTAINERS:

        result = subprocess.run(
            [
                "docker",
                "stats",
                container,
                "--no-stream",
                "--format",
                "{{.CPUPerc}} {{.MemUsage}}"
            ],
            capture_output=True,
            text=True
        )

        output = result.stdout.strip()

        if output:
            parts = output.split()

            cpu = float(parts[0].replace("%", ""))

            memory_value = float(parts[1].replace("MiB", ""))

            cpu_values.append(cpu)
            memory_values.append(memory_value)

    average_cpu = sum(cpu_values) / len(cpu_values)
    average_memory = sum(memory_values) / len(memory_values)

    return average_cpu, average_memory


def send_request():

    data = {
        "satellite_id": "SAT-001",
        "location": "Karnataka"
    }

    start = time.perf_counter()

    try:

        response = requests.post(
            URL,
            json=data,
            timeout=10
        )

        end = time.perf_counter()

        return {
            "success": response.status_code == 201,
            "time": end - start
        }

    except Exception:

        end = time.perf_counter()

        return {
            "success": False,
            "time": end - start
        }


def run_workload(concurrency):

    print("\n======================================")
    print(f"Concurrency Level: {concurrency}")
    print("======================================")

    start_time = time.perf_counter()

    results = []

    with ThreadPoolExecutor(max_workers=concurrency) as executor:

        futures = [
            executor.submit(send_request)
            for _ in range(REQUESTS_PER_LEVEL)
        ]

        for future in as_completed(futures):
            results.append(future.result())

    end_time = time.perf_counter()

    total_time = end_time - start_time

    successful = sum(
        1 for r in results if r["success"]
    )

    failed = len(results) - successful

    response_times = [
        r["time"] for r in results
    ]

    average_response = (
        sum(response_times) / len(response_times)
    )

    throughput = len(results) / total_time

    cpu, memory = get_docker_stats()

    print(f"Total Requests     : {len(results)}")
    print(f"Successful Requests: {successful}")
    print(f"Failed Requests    : {failed}")
    print(f"Average Response   : {average_response * 1000:.2f} ms")
    print(f"Total Time         : {total_time:.2f} sec")
    print(f"Throughput         : {throughput:.2f} requests/sec")
    print(f"Average CPU        : {cpu:.2f}%")
    print(f"Average Memory     : {memory:.2f} MiB")


for concurrency in WORKLOADS:
    run_workload(concurrency)
