#!/usr/bin/env python2
# -*- coding:utf-8 -*-

import os
import argparse
import glob
from functools import partial

import fontforge
import psMat
import source

opt_parser= argparse.ArgumentParser()

opt_parser.add_argument("--cjkv_info", type= str,
    help= u"the path of cjkv_info")
opt_parser.add_argument("--region", type= str,
    help= u"the region from where to select characters")
opt_parser.add_argument("--start", type= partial(int, base=16),
    help= u"the start point of unicode")
opt_parser.add_argument("--end", type= partial(int, base=16),
    help= u"the end point of unicode")
opt_parser.add_argument("--name", type= str,
    help= u"the name of the new font")
opt_parser.add_argument("--adjust", type= int,
    help= u"adjust the position of the outline")
opt_parser.add_argument("--output", type= str,
    help= u"the path and filename of the new font")

class Opts:
    def __init__(self):
        self.cjkv_info= "."
        self.region= "China"
        self.start= 0
        self.end= 0
        self.name= "my font"
        self.adjust= 0
        self.output= (".", "out.ttf")

def setup_opt():
    opts= Opts()
    args= opt_parser.parse_args()
    opts.cjkv_info= args.cjkv_info or opts.cjkv_info
    opts.region= args.region or opts.region
    opts.start= args.start or opts.start
    opts.end= args.end or opts.end
    opts.name= args.name or opts.name
    opts.adjust= args.adjust or opts.adjust
    if args.output:
        d= os.path.dirname(args.output) or opts.output[0]
        f= os.path.basename(args.output) or opts.output[1]
        opts.output= (d, f)
    try:
        os.mkdir(opts.output[0])
    except OSError:
        pass
    return opts

def get_code(path):
    basename= os.path.basename(path)
    (root, ext)= os.path.splitext(basename)
    code_tag= root.split("_")
    code= int(code_tag[0], 16)
    return code

def read_src(path):
    with open(path, "r") as f:
        src= f.readline()
        return src

def get_region(src):
    return source.rev.get(src.split("-")[0])

def is_region(region):
    return region == opts.region

def filter_src(path):
    code= get_code(path)
    if opts.start <= code and code <= opts.end:
        src= read_src(path)
        region= get_region(src)
        return is_region(region)
    else:
        return False

opts= setup_opt()

src_files= glob.glob(os.path.join(opts.cjkv_info, "*", "*.src"))
src_files= filter(filter_src, src_files)

newfont= fontforge.font()
newfont.em= 1024
newfont.fontname= opts.name

for src_file in src_files:
    code= get_code(src_file);
    glyph= newfont.createChar(code)
    (root, ext)= os.path.splitext(src_file)
    glyph.importOutlines(root + ".svg")
    glyph.transform(psMat.translate(0, opts.adjust))

newfont.generate(os.path.join(opts.output[0], opts.output[1]))

