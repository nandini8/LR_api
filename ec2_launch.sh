#!/bin/bash
aws ec2 run-instances --image-id ami-0c55b159cbfafe1f0 --count 1 --instance-type t2.micro --key-name ml_model --security-group-ids sg-02972ab9ea0bd13ea --subnet-id subnet-bc6cb0f0
