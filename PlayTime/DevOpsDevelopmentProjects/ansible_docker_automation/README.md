# Ansible for Docker Deployments

Automate the deployment of Docker containers using Ansible.

## Project Walkthrough:

1. **Set up Ansible to install Docker**:
   - Install Docker on remote machines using Ansible.
   - Ensure Docker service is running.

2. **Deploy a Sample Web Application**:
   - Use a simple Go web application to print 'Hello, World!'.
   - Containerize the application with a Dockerfile.

3. **Use Ansible Roles to Structure the Playbook**:
   - Define a role with tasks for installing Docker, building the Go application, and running the container.

## Project Structure:

```
ansible-docker-project/
├── ansible.cfg
├── inventory.ini
├── deploy.yml  # Master playbook
├── build_image.yml  # Builds Docker Image
├── run_container.yml  # Runs the container
├── roles/
│   ├── app_deploy/
│   │   ├── tasks/
│   │   │   ├── main.yml  # Deprecated (We use run_container.yml now)
│   │   ├── files/
│   │   │   ├── Dockerfile
│   │   │   ├── main.go

```

## Run the Playbook:

`ansible-playbook deploy.yml --ask-become-pass -vvv`
