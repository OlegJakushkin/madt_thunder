
## 7-nodes Tendermint testnet using MADT network modelling system
To run:

1. Download and start MADT
```
cd ~
git clone --recursive https://github.com/dltcspbu/madt/
mkdir ~/madt/labs && export MADT_LABS_DIR=$HOME/madt/labs
mkdir ~/madt/sockets && export MADT_LABS_SOCKETS_DIR=$HOME/madt/sockets

cd madt
sudo pip3 install -r ./requirements.txt
sudo make && sudo make install

sudo -HE env PYTHONPATH=$HOME/madt:$PYTHONPATH SSH_PWD=demo python3 madt_ui/main.py 80  
```
2. Downoload this repo 

*Say you now have this lab folder "madt_thunder" in "tutorials"*

3. Build images for 6 validators in MADT 

Every node has 6 folders in it with initial data and config of all 4 starting  nodes and tendermint binary.

```
#open new terminal window
cd ~/madt
cd ./tutorials/madt_thunder/nodes/
make build-validator
```
It will build image tendermint/validator

4. Build image for 1 nonvalidator
```
make build-nonvalidator
```
It will build image tendermint/nonvalidator

5. Start the lab

```
cd ..
python3 ./lab.py
```
lab.py will have such nodes for validators and nonvalidators:
```
# Validators
thunders.append(net.create_node('node'+str(x), 
                        privileged=True,
                        image="tendermint/validator",
                        ports={'26656/tcp': 26659+2*(x-1), '26657/tcp': 26660+2*(x-1)},
                        environment={'ID':str(x-1),'LOG':'${LOG:-tendermint.log}'},
                        ))

# Nonvalidators
thunders.append(net.create_node('node'+str(x), 
                        privileged=True,
                        image="tendermint/nonvalidator",
                        ports={'26656/tcp': 26659+2*(7-1), '26657/tcp': 26660+2*(x-1)},
                        environment={'ID':str(x-1),'LOG':'${LOG:-tendermint.log}'},
                        # entrypoint="sleep "+str(int(x>4)*x*10)
                        #entrypoint="sleep 100000",
                        ))
                      
```

5. Open 127.0.0.1:80
6. login as `demo:demo`
7. Open lab "my"
8. Observe graph

You can set 100% loss for two of nodes (you need 2/3 working nodes for consensus). If you set 100%loss for three nodes, you will get error messages and creating blocks will stop until one of nodes wakes up.

## Adding non-validator node

You can add one or more non-validator nodes with specified seeds for listening, which fit to adresses of validators. To create nonvalidator, you can just copy genesis.json to its folder (e.g. node 7) and change config file to specify seeds. No priv-key file or key-file needed! If seeds section contains no nodes, nonvalidator won't "see" anything. 

Of course, nonvalidator-nodes must be set up in lab.py **before** net starts.

## Adding validator

To add validator, you need to specify it in genesis file of all nodes **before** starting testnet. To be able to add it when other nodes
will be already working you need to add this node to lab.py in such way (entrypoint is different from others):
```
thunders.append(net.create_node('node'+str(x), 
                        privileged=True,
                        image="tendermint/validator",
                        ports={'26656/tcp': 26659+2*(x-1), '26657/tcp': 26660+2*(x-1)},
                        environment={'ID':str(x-1),'LOG':'${LOG:-tendermint.log}'},
                        # entrypoint="sleep "+str(int(x>4)*x*10)
                        entrypoint="sleep 100000",
                        ))
```
So it will sleep 100000 sec. To wake it up, you need to type in terminal [number_of_node] is placeholder to yours number of this node:
```
sudo docker exec MADT_my_node[number_of_node] sh -c 'until [ -e '/lab/lab.sock' ]; do sleep 3; done; "/usr/bin/wrapper.sh" "node" "--proxy_app" "kvstore"'
```

## TODO
- [x] Add local nonvalidator
- [x] Change docker image for nonvalidator
- [x] Add more validators
- [x] Add more business-logic
