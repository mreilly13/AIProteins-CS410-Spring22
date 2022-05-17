#!/bin/bash

# Sample slurm submission script for the Chimera compute cluster
# Lines beginning with # are comments, and will be ignored by
# the interpreter.  Lines beginning with #SBATCH are directives
# to the scheduler.  These in turn can be commented out by
# adding a second # (e.g. ##SBATCH lines will not be processed
# by the scheduler).
#

#lines below edit is the lines edit from orgional

#
# set name of job
##SBATCH --job-name=slurm-sample

# edit
#SBATCH --job-name=AIPorteins

#
# set the number of processors/tasks needed
#SBATCH -n 2

#set an account to use
#if not used then default will be used
# for scavenger users, use this format:
##SBATCH --account=pi_first.last

#edit
#SBATCH --account=zihan.ma001

# for contributing users, use this format:
##SBATCH --account=<deptname|lastname>

# set max wallclock time  DD-HH:MM:SS
#SBATCH --time=00-10:00:00

# set a memory request
#SBATCH --mem=1gb

# Set filenames for stdout and stderr.  %j can be used for the jobid.
# see "filename patterns" section of the sbatch man page for
# additional options
#SBATCH --error=%x-%j.err
#SBATCH --output=%x-%j.out
#

# set the partition where the job will run.  Multiple partitions can
# be specified as a comma separated list
# Use command "sinfo" to get the list of partitions
#SBATCH --partition=Intel6240
##SBATCH --partition=Intel6240,Intel6248,DGXA100

#When submitting to the GPU node, these following three lines are needed:

##SBATCH --gres=gpu:1
##SBATCH --export=NONE
#. /etc/profile #there is a space after the period


#Optional
# mail alert at start, end and/or failure of execution
# see the sbatch man page for other options
##SBATCH --mail-type=ALL
# send mail to this address
##SBATCH --mail-user=first.last@umb.edu

# Put your job commands here, including loading any needed
# modules or diagnostic echos.

# this job simply reports the hostname and sleeps for two minutes

echo "using $SLURM_CPUS_ON_NODE CPUs"
echo `date`

hostname
sleep 120

# Diagnostic/Logging Information
echo "Finish Run"
echo "end time is `date`"
