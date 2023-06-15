#!/bin/sh

securing(){
    script_path="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
    bandit -r "$script_path"/../*.py
}

main(){
    securing
}

main