#!/bin/bash
# Execute terraform destroy
cd /home/master/Projects/terravSphere
terraform destroy -var-file=~/Projects/terravSphere/Swarm/swarm.tfvars -var-file=~/Projects/terravSphere/DR.tfvars -state=~/Projects/terravSphere/Swarm/swarm.tfstate
