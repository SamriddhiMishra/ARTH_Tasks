# ARTH - Task 19 👨🏻‍💻

## Task Description📄

📌Integrating Ansible with Kubernetes by setting up Multi-Node cluster over AWS Cloud, using Ansible roles📌

🔅 Create Ansible Playbook to launch 3 AWS EC2 Instance
🔅 Create Ansible Playbook to configure Docker over those instances.
🔅 Create Playbook to configure K8S Master, K8S Worker Nodes on the above created EC2 Instances using kubeadm.

#### There are four ansible roles here-
#### 1) aws_inst => To launch AWS instances and auto update the inventory with their IPs. Here default inventory is - /root/ip.txt
#### 2) docker_kubeadm => To install docker and kubeadm and start their services in nodes(both master and worker)
#### 3) master => It is used along with docker_kubeadm to initialize k8s cluster and configure master
#### 4) worker => To join worker node to the master of cluster

Link to Video- [here](https://www.linkedin.com/posts/activity-6764564296862101505-7nTf)
