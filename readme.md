VNA Scheduler
=============

Installation
------------

### Clone directory

With SSH:

`git clone git@github.com:Terrabits/vnascheduler.git`

With HTTPS:
``

### Install python dependencies

`pip install -r requirements.txt`

Use
---

### Modify the following parameters in the `run.py` script:

- `interval_min`
- `duration_hr`
- `path`
- `vna_address`

### Execute

Run the `run.py` script to execute.


Results
-------

Every `interval_min` minutes for a duration of `duration_hr` hours this script will:

- Sweep each channel
- Save the full N-port S-parameter results for each channel to a touchstone file (`*.snp`).

Ports for the sweep and touchstone file are determined from the traces in the channel.

Script Modification
-------------------

The `schedule.run` method takes the following arguments:

- interval_min
- duration_hr
- action

The `action` input is a lambda function called every `interval_min` minutes. You can either modify `save.create_save_action` or otherwise provide your own lambda function to change the behavior of the script.

