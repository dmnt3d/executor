#!/bin/bash
# Execute terraform
cd /home/master/Projects/terravSphere
terraform apply -var-file=~/Projects/terravSphere/Swarm/swarm.tfvars -var-file=~/Projects/terravSphere/DR.tfvars -state=~/Projects/terravSphere/Swarm/swarm.tfstate
# build ansible inventory 
python ~/Projects/executor/buildAnsibleInventory.py "/home/master/Projects/terravSphere/Swarm/swarm.tfvars"

# finalize build with ansible-playbook
cd ~/Projects/host-Config/
ansible-playbook -i ~/Projects/host-Config/inventory/inventory-swarm --private-key=/home/master/.ssh/id_rsa terra-final.yml
