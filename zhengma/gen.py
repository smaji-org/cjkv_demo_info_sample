#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import argparse
import glob
from functools import partial
from typing import List

import source
import rime_zhengma

opt_parser= argparse.ArgumentParser()

opt_parser.add_argument("--cjkv_info", type= str,
    help= "the path of cjkv_info")
opt_parser.add_argument("--region", type= str,
    help= "the region from where to select characters")
opt_parser.add_argument("--start", type= partial(int, base=16),
    help= "the start point of unicode")
opt_parser.add_argument("--end", type= partial(int, base=16),
    help= "the end point of unicode")
opt_parser.add_argument("--name", type= str,
    help= "the name of the code table")
opt_parser.add_argument("--version", type= str,
    help= "the version of the code table")
opt_parser.add_argument("--output-dir", type= str,
    help= "the directory containing the new code table")

class Opts:
    def __init__(self):
        self.cjkv_info= "."
        self.region= "China"
        self.start= 0
        self.end= 0
        self.name= "zhengma"
        self.version= "0.1"
        self.output_dir= "."

def setup_opt() -> Opts:
    opts= Opts()
    args= opt_parser.parse_args()
    opts.cjkv_info= args.cjkv_info or opts.cjkv_info
    opts.region= args.region or opts.region
    opts.start= args.start or opts.start
    opts.end= args.end or opts.end
    opts.name= args.name or opts.name
    opts.version= args.version or opts.version
    opts.output_dir= args.output_dir or opts.output_dir
    try:
        os.mkdir(opts.output_dir)
    except OSError:
        pass
    return opts

def get_code(path: str) -> int:
    basename= os.path.basename(path)
    (root, ext)= os.path.splitext(basename)
    code_tag= root.split("_")
    code= int(code_tag[0], 16)
    return code

def read_zhengma(path: str) -> List[str]:
    with open(path, "r") as f:
        zhengma= f.read().splitlines()
        return zhengma

def read_src(path: str) -> str:
    with open(path, "r") as f:
        src= f.readline()
        return src

def get_region(src: str) -> str:
    return source.rev.get(src.split("-")[0])

def is_region(region: str) -> bool:
    return region == opts.region

def filter_src(path: str) -> bool:
    code= get_code(path)
    if opts.start <= code and code <= opts.end:
        src= read_src(path)
        region= get_region(src)
        return is_region(region)
    else:
        return False

def get_zhengma(src_file: str) -> List[str]:
    dirname= os.path.dirname(src_file)
    basename= os.path.basename(src_file)
    (root, ext)= os.path.splitext(basename)
    zhengma_file= os.path.join(dirname, "input_method", root + ".zhengma")
    if not os.path.exists(zhengma_file):
        code_tag= root.split("_")
        zhengma_file= os.path.join(
            dirname,
            "input_method",
            code_tag[0] + ".zhengma")
    return read_zhengma(zhengma_file)


opts= setup_opt()

src_files= glob.glob(os.path.join(opts.cjkv_info, "*", "*.src"))
src_files= filter(filter_src, src_files)

with open(os.path.join(opts.output_dir, "zhengma.dict.yaml"), "w") as output_file:
    output_file.write(rime_zhengma.header.format(opts.name, opts.version))

    for src_file in src_files:
        code= get_code(src_file)
        zhengma_l= get_zhengma(src_file)
        for zhengma in zhengma_l:
            item= "{}\t{}\n".format(chr(code), zhengma)
            output_file.write(item)

