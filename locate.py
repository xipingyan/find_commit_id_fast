import os
import subprocess

def parse_log(log_outputs):
    for line in log_outputs:
        print(f"== line={line}")

# time format: 2024-07-27
def get_ranges_of_search(repos_path: str, start_tm=None, end_tm=None):
    os.chdir(repos_path)
    process = subprocess.run(["git", "log", "--pretty=reference", "--since", start_tm, "--before", end_tm], capture_output=True, text=True)
    output = process.stdout
    # parse_log(output)
    print("== git log:", output)

    return []

def clone_repos(repos, repos_name):
    if not os.path.exists(repos_name):
        print(f"== Start git clone: {repos}")
        process = subprocess.Popen(["git", "clone", repos], stdout=subprocess.PIPE)
        output = process.communicate()[0]
    else:
        print(f"== Repos:{repos} existed.")

    return repos_name

def main():
    repos='https://github.com/openvinotoolkit/openvino.git'
    repos_name='openvino'

    repos_path = clone_repos(repos, repos_name)
    commit_ids = get_ranges_of_search(repos_path=repos_path, start_tm='2024-07-27', end_tm='2024-08-01')

    print(f"commit_ids={commit_ids}")

main()