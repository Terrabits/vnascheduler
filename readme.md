VNA Scheduler
=============

Installation
------------

### Clone directory

With SSH:

`git clone git@github.com:Terrabits/vnascheduler.git`

With HTTPS:
`git clone https://github.com/Terrabits/vnascheduler.git`

### Install python dependencies

`pip install -r requirements.txt`

Use
---

### Modify `settings.yaml` to your requirements:

- `interval (mins)`: Must be whole/integer number
- `duration (hrs)`: Must be whole/integer number
- `path`: Location where results will be saved. `~` character is expanded to user home.
- `vna address`: IP address of the VNA

### Execute

Run the `__main__.py` script to execute:

```shell
cd /path/to/vnascheduler
python .
```

Results
-------

Every `interval (mins)` for a duration of `duration (hrs)` this script will:

- Sweep each channel
- Save the full N-port S-parameter results for each channel to a touchstone file (`*.snp`).

Ports for the sweep and touchstone file are determined from the traces in the channel.

Script Modification
-------------------

The `schedule.run` method takes the following arguments:

- interval_min
- duration_hr
- action

The `action` input is a lambda function called every `interval (mins)`. You can either modify `save.create_save_action` or otherwise provide your own lambda function to change the behavior of the script.
