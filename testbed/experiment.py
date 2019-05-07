#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import sys
import json

from benchmark_suites import *

############ BASEL GRID PARAMETER ############

# Load "infai" settings for partition and qos
partition="infai_2"
qos="normal"

# Gives the task's priority as a value between 0 (highest) and 2000 (lowest).
nice="2000"

# The email adress that receives an email when the experiment is finished
email = "my.name@unibas.ch"

############ FREIBURG GRID PARAMETER ############
# defines which queue to use for one task. Possible values are
# "athlon.q" and "athlon_core.q". The former value configures the use
# of a whole cpu, while the latter option configures the use of a
# single cpu core.
queue = "meta_core.q"

# defines the priority of the task. Possible values are [-1023,0], but the
# maximum of 0 should only be used for very urgent jobs.
priority = 0

############ OTHER PARAMETERS ############

# Set to true if you want to run the experiment in debug mode
run_debug = False

# Available options are "slurm" and "sge" (for sun grid engine)
grid_engine = "slurm"

# A list of domains that are used in this experiment. Each entry must correspond
# to a folder in testbed/benchmarks. See testbed/benchmark_suites.py for some
# predefined benchmark sets, such as IPPC2018 and IPPC_ALL.
benchmark= IPPC2011

# The search engine configurations that are started in this experiment.
# (each of these is run on each instance in the benchmark folder)
configs = [
    "IPPC2011",                                         # The configuration that participated at IPPC 2011
    "IPPC2014",                                         # The configuration that participated at IPPC 2014
#    "UCT -init [Single -h [RandomWalk]]",               # The configuration that is closest to "plain UCT"
#    "UCT -init [Expand -h [IDS]] -rec [MPA]",           # Best UCT configuration according to Keller's dissertation
#    "DP-UCT -init [Single -h [Uniform]]"                # A configuration that works well in wildfire and sysadmin
]

# The number of runs (30 in competition, should be higher (>=100) for
# papers and theses to obtain acceptable confidence intervalls
numRuns = "100"

# The current revision (used for appropriate naming only)
revision = "rev3b168b35"

# The timeout per task in hh:mm:ss
timeout = "4:00:00"

# The maximum amount of available memory per task. The value's format is
# either "<mem>M" or "<mem>G", where <mem> is an integer number, M
# stands for MByte and G for GByte. Note that PROST additionally has an
# internal memory management that makes sure that the used memory does
# not exceed a given value (see src/search/prost_planner.cc)
memout = "3872M"

############ (USUALLY) NO NEED TO CHANGE THE FOLLOWING ############

# The experiment's name
name = "prost_"+revision

# Directory results are written to
resultsDir = "results/"+revision+"/"

# Directory server logs are written to
serverLogDir = resultsDir+"serverLogs/"

# The file where stderr is directed to
errfile = "stderr.log"

# The file where stdout is directed to
logfile = "stdout.log"

# Template for the string that is executed for each job
TASK_TEMPLATE = "export LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH && " \
"mkdir -p %(resultsDir)s && " \
"mkdir -p %(resultsDir)s/%(run_batch)s && " \
"mkdir -p %(resultsDir)s/%(run_batch)s/%(run)s && " \
"./run-server benchmarks/%(benchmark)s %(port)s %(numRuns)s 0 1 0 %(serverLogDir)s 0 > %(resultsDir)s/%(run_batch)s/%(run)s/server.log 2> %(resultsDir)s/%(run_batch)s/%(run)s/server.err &" \
" sleep 45 &&" \
" ./%(resultsDir)s/prost %(instance)s -p %(port)s [PROST -s 1 -se [%(config)s]] > %(resultsDir)s/%(run_batch)s/%(run)s/run.log 2> %(resultsDir)s/%(run_batch)s/%(run)s/run.err &&" \
"cat > %(resultsDir)s/%(run_batch)s/%(run)s/driver.log" # TODO temporary just to avoid lab errors

SLURM_TEMPLATE = "#! /bin/bash -l\n" \
                 "### Set name.\n"\
                 "#SBATCH --job-name=%(name)s\n"\
                 "### Redirect stdout and stderr.\n"\
                 "#SBATCH --error=%(errfile)s\n"\
                 "#SBATCH --output=%(logfile)s\n"\
                 "### Set partition.\n"\
                 "#SBATCH --partition=%(partition)s\n"\
                 "### Set quality-of-service group.\n"\
                 "#SBATCH --qos=%(qos)s\n"\
                 "### Set memory limit\n"\
                 "#SBATCH --mem-per-cpu=%(memout)s\n"\
                 "### Set timeout\n"\
                 "#SBATCH -t %(timeout)s\n"\
                 "### Number of tasks.\n"\
                 "#SBATCH --array=1-%(num_tasks)s\n"\
                 "### Adjustment to priority ([-2147483645, 2147483645]).\n"\
                 "#SBATCH --nice=%(nice)s\n"\
                 "### Send mail? Mail type can be e.g. NONE, END, FAIL, ARRAY_TASKS.\n"\
                 "#SBATCH --mail-type=END\n"\
                 "#SBATCH --mail-user=%(email)s\n"\
                 "### Extra options.\n\n"

SGE_TEMPLATE = "#! /bin/bash\n"\
               "## specifies the interpreting shell for this job file.\n"\
               "#$ -S /bin/bash\n"\
               "## Never send me an email.\n"\
               "#$ -m n\n"\
               "## Execute the job from the current working directory.\n"\
               "#$ -cwd\n"\
               "## stderr and stdout go here\n"\
               "#$ -e %(errfile)s\n"\
               "#$ -o %(logfile)s\n"\
               "## set time out\n"\
               "#$ -l h_cpu=%(timeout)s\n"\
               "## set memory out\n"\
               "#$ -l h_vmem=%(memout)s\n"\
               "## use this queue. \n"\
               "#$ -q %(queue)s\n"\
               "## the number of tasks is this job file\n"\
               "#$ -t 1-%(num_tasks)s\n"\
               "## the priority of this job.\n"\
               "#$ -p %(priority)s\n\n"

def isInstanceName(fileName):
    return fileName.count("inst") > 0

def copy_binaries():
    if run_debug:
        parser_name = "rddl-parser-debug"
        parser_file = "../builds/debug/rddl_parser/rddl-parser"
        search_file = "../builds/debug/search/search"
    else:
        parser_name = "rddl-parser-release"
        parser_file = "../builds/release/rddl_parser/rddl-parser"
        search_file = "../builds/release/search/search"

    shutil.copy2(parser_file, "./"+parser_name)
    shutil.copy2(search_file, "./"+resultsDir+"prost")

def create_tasks(filename, instances):
    port = 2000
    tasks = []
    domains_in_benchmark = set()
    for task in benchmark:
        # The path in benchmark_suites is the directory name.
        # We use this name to identify the domains instead of the RDDL domain file.
        domains_in_benchmark.add(task.path)
    
    # Create properties file of the whole experiment.
    properties = dict()
    properties["domains"] = list(domains_in_benchmark)
    properties["algorithms"] = configs
    properties["memory_limit"] = memout
    properties["name"] = name
    properties["num_runs"] = numRuns
    properties["partition"] = partition
    properties["revision"] = revision
    properties["run_debug"] = run_debug
    properties["time_limit"] = timeout
    props_path =  "/".join((resultsDir, "properties"))
    with open(props_path, 'w') as fp:
        json.dump(properties, fp, indent=2)

    task_id = 1
    lower = 1
    upper = 100
    for config in configs:
        for instance in sorted(instances):
            run_batch = "runs-{:0>5}-{:0>5}".format(lower, upper)
            run = "{:0>5}".format(task_id)
            run_dir = "/".join((resultsDir,
                                   run_batch, run))
            task = TASK_TEMPLATE % dict(config=config,
                                        benchmark =instance[0],
                                        instance=instance[1],
                                        port=port,
                                        numRuns = numRuns,
                                        resultsDir=resultsDir,
                                        run_batch=run_batch,
                                        run=run,
                                        serverLogDir=serverLogDir)

            if not os.path.exists(run_dir):
                os.makedirs(run_dir)
            # Create properties file of the run.
            # Lab requires at least the attributes with the names:
            # domain, problem and algorithm.
            properties = dict()
            properties["domain"] = instance[0]
            properties["algorithm"] = config
            properties["id"] = config, instance[0], instance[1]
            properties["problem"] = instance[1]
            properties["max_score"] = instance[3]
            properties["memory_limit"] = memout
            properties["min_score"] = instance[2]
            properties["numRuns"] = numRuns
            properties["revision"] = revision
            properties["run_dir"] = run_dir
            properties["time_limit"] = timeout
            props_path =  "/".join((run_dir, "static-properties"))
            with open(props_path, 'w') as fp:
                json.dump(properties, fp, indent=2)

            task_id += 1
            if task_id > upper:
                lower += 100
                upper += 100
            tasks.append(task)
            port = port + 1

    if grid_engine == "slurm":
        jobs = SLURM_TEMPLATE %dict(name=name,
                                    errfile=errfile,
                                    logfile=logfile,
                                    partition=partition,
                                    qos=qos,
                                    memout=memout,
                                    timeout=timeout,
                                    num_tasks=str(len(tasks)),
                                    nice=nice,
                                    email=email)

        for task_id,task in zip(range(1, len(tasks)+1), tasks):
            jobs += "if [ " + str(task_id) + " -eq $SLURM_ARRAY_TASK_ID ]; then\n"
            jobs += "    " + task + "\n"
            jobs += "    exit $?\n"
            jobs += "fi\n"
    elif grid_engine == "sge":
        jobs = SGE_TEMPLATE %dict(errfile=errfile,
                                  logfile=logfile,
                                  memout=memout,
                                  timeout=timeout,
                                  queue=queue,
                                  num_tasks=str(len(tasks)),
                                  priority=str(priority))

        for task_id,task in zip(range(1, len(tasks)+1), tasks):
            jobs += "if [ " + str(task_id) + " -eq $SGE_TASK_ID ]; then\n"
            jobs += "    " + task + "\n"
            jobs += "    exit $?\n"
            jobs += "fi\n"
    else:
        print "Invalid grid engine!"
        exit()

    f = file(filename, 'w')
    f.write(str(jobs))
    f.close()

def run_experiments(filename):
    if grid_engine == "slurm":
        os.system("sbatch " + filename + " &")
    elif grid_engine == "sge":
        os.system("qsub " + filename + " &")
    else:
        print "Invalid grid engine!"
        exit()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print >> sys.stderr, "Usage: create-jobs.py"
        exit()
    instances = []
    for instance in benchmark:
        domain_name = instance.path
        problem_name = instance.problem.replace('.rddl','')
        problem_min_score = instance.min_score
        problem_max_score = instance.max_score
        instances.append((domain_name, problem_name, problem_min_score, problem_max_score))
    os.system("mkdir -p " + resultsDir)
    os.system("mkdir -p " + serverLogDir)
    filename = resultsDir + "experiment_"+revision
    copy_binaries()
    create_tasks(filename, instances)
    run_experiments(filename)
