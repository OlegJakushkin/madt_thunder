
## 4-nodes Tendermint testnet using MADT network modelling system
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

*Say you have this lab folder "my" in "tutorials"*

3. Build image for 4 nodes in MADT 

Every node has 4 folders in it with initial data and config of all 4 starting  nodes

```
#open new terminal window
cd ~/madt
cd ./tutorials/my/nodes
make
```
4. Start the lab

```
cd ..
python3 ./lab.py
```

5. Open 127.0.0.1:80
6. login as `demo:demo`
7. Open lab ![image](https://user-images.githubusercontent.com/2915361/76143162-fe747180-606c-11ea-8b50-429b9067c62b.png)
8. Observe graph ![image2](https://user-images.githubusercontent.com/2915361/76143179-2368e480-606d-11ea-8d11-8ce5d360884e.png)
 in "my" folder

You can set 100% loss for one of nodes (you need 2/3 working nodes for consensus). 

## Adding local non-validator node

To see what's happening in realtime in your terminal, you can add one or more non-validator nodes with specified ports for listening, which fit to listening ports of validators. In my redaction it's 26657. So, to run localnode, you need:
1. Build nonvalidator image
```
cd nodes/nonvalidator
make
```
2. Run docker container

```
sudo docker run --name local_tender --privileged=True -p 26665:26656/tcp -p 26666:26657/tcp --env ID=4 "tendermint/nonvalidator"

```
Of course, you can add nonvalidator node in MADT too, but you need to start it at the same time with other nodes. Hence you need to add node by changing lab.py file (you can specify needed parameters as for local node, but in notation of MADT).

## Adding validator

To add validator, you need to specify it in genesis file of all nodes **before** starting testnet. This is not supported by us now.

## TODO
- [x] Add local nonvalidator
- [ ] Change docker image for nonvalidator
- [ ] Add more validators
- [ ] Add more business-logic
