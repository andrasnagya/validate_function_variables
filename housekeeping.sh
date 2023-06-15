#!/bin/sh

# Housekeeping suggestion

linting(){
    ./housekeeping/lint.sh
}

typehinting(){
    ./housekeeping/typehint.sh
    }

testing(){
    ./housekeeping/test.sh
}

securing(){
    ./housekeeping/secure.sh
}

export_env(){
    conda env export > ./housekeeping/environment.yml
}

gener_callgraph(){
    pycallgraph graphviz -- ./decorators.py
}


main(){
    linting 1>> ./housekeeping.log 2>> ./housekeeping.err
    typehinting 1>> ./housekeeping.log 2>> ./housekeeping.err
    testing 1>> ./housekeeping.log 2>> ./housekeeping.err
    securing 1>> ./housekeeping.log 2>> ./housekeeping.err

    #export_env
    #gener_callgraph

}

main

