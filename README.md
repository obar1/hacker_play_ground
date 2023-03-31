# readme

> WIP

some snippet you can just run from main .py
```bash
python _tic_tac_toe.py
```

some others use a file for input/output

```bash

run_py () {
    echo "running #1 is $1 with ..."
    cat inputs.txt

    export OUTPUT_PATH='./tmp.txt'
    cat inputs.txt | python ./"$1"
    cat $OUTPUT_PATH
}

// opt - put in script and source it

```

and

```
run_py _big_sum.py
```

SORRY!
