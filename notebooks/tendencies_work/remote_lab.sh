#!/bin/bash

module load python/3.7.12
module load conda
conda activate cenv
jupyter lab --no-browser --ip=`hostname` --port=8888

