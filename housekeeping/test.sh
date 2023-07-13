#!/bin/sh

set -eux

unit_testing(){
    script_path="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
    python "$script_path"/../test_*
}

coverage_testing(){
    script_path="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
    coverage run "$script_path"/../decorators.py
}

main(){
    unit_testing
    coverage_testing 
}

main