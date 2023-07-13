#!/usr/bin/env bash


typehinting(){
    script_path="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
    mypy --strict "$script_path"/../*.py
}

main(){
    typehinting
}

main