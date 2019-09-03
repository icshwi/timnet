MRF hardware based network toolkit.
--

# Introduction
Each device in the timing system is given an unique identifier, the Topology ID. The master EVM is given ID 0x00000000. The downstream devices are given IDs with the least significant four bits representing the port number the device is connected to. Each EVM left shifts its own ID by four bits and assigns the downstream port number to the lowest four bits to form the topology ID for the downstream devices in the next level. The topolofgy IDs are represented above the devices in the example layout in ./doc/ figure.

# Capabilities
* To expose the timing network topology the states
* Background for an eventual timing network GUI development
* Maintenance checks after changes or shutdowns
* SAT and SIT purposes
* Timing network monitoring

# Usage
* Define the inventory.json
* python -m timnet -h
* Output inside ./json
* Plot ./json with https://vanya.jp.net/vtree/

# Examples
* Read the timing network distribution:

```
input: inventory.json
output: network.json
python -m timnet --net
```
* Plot the network

```
input: network.json
output: plot.json
python -m timnet --plot
```
* Check errors

```
input: check.json, network.json
output: console
python -m timnet --check
```
* All together

python -m timnet --net --plot --check
