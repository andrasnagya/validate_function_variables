#!/usr/bin/env bash


linting(){
    script_path="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
    black "$script_path"/../*.py
    pylint "$script_path"/../*.py
}

main(){
    linting
}

main