#!/usr/bin/env python3


"""
Run this script to generate Qiskit assignments
"""

print("Loading modules...")
import otter
import subprocess as sp
from os.path import isfile


def main():
    if otter.__version__ != "4.2.1":
        otter_version_warning()
        return

    assignment_number, course_id, assignment_id = assignment_info_prompt()
    assignment_fp = f"./q{assignment_number}/q{assignment_number}.ipynb"
    assignment_dist_dir = f"./q{assignment_number}/q{assignment_number}-dist"

    if not isfile(assignment_fp):
        raise OSError(f"Expected to find the master notebook at {assignment_fp}, unable to locate")

    with open(assignment_fp, "r") as f:
        master_file_contents = f.readlines()

    new_master_file_contents = []
    for line in master_file_contents:
        if "assignment_id" in line:
            new_line = f"    \"    assignment_id: {assignment_id} # from Gradescope MANUAL assignment URL\\n\",\n"
            new_master_file_contents.append(new_line)
        elif "course_id" in line:
            new_line = f"    \"    course_id: {course_id} # from gradescope URL\\n\",\n"
            new_master_file_contents.append(new_line)
        else:
            new_master_file_contents.append(line)

    with open(assignment_fp, "w") as f:
        for line in new_master_file_contents:
            f.write(line)
        print(f"Updated master file written to {assignment_fp}")
    
    job = sp.run(f"otter assign {assignment_fp} {assignment_dist_dir}".split(" "))
    try:
        job.returncode
    except sp.CalledProcessError as e:
        print(e.output)
    else:
        print(f"Generated assignment successfully to {assignment_dist_dir}")



def otter_version_warning():
    # otter v1 necessary to generate assignments properly
    # anything > 4.2.1 is fine but please update this warning
    print("\tPlease check that your otter version is == 4.2.1")
    print("\tThis warning usually occurs when the course virtual environment is not active")
    print("\tTry running \"conda activate cse468\" before running this script")


def assignment_info_prompt():
    assignment_number = int(input("Which Qiskit assignment are you looking to generate? Enter (0-4) -> "))
    if assignment_number not in range(5):
        raise IndexError(f"Unexpected assignment number {assignment_number}, expected in range [0,4]")
    course_id = int(input("What is the Gradescope course id number for this semester? (Find this in the URL) -> "))
    assignment_id = int(input("What is the assignment id number for the *manual* portion of this assignment? (Find this in the URL) -> "))
    return (assignment_number, course_id, assignment_id)


if __name__ == "__main__":
    main()
