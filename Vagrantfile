VAGRANTFILE_API_VERSION = "2"

$conda_installation = <<SCRIPT

if ! [ -d "miniconda3" ]; then
    curl https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o miniconda.sh || exit 1;
    bash miniconda.sh -bf || exit 1;
    rm miniconda.sh || exit 1;
fi
grep -q miniconda ~/.bashrc;
if [[ ${?} -ne 0 ]]; then
    echo "export PATH=\"${HOME}/miniconda3/bin:\${PATH}\"" >> ~/.bashrc
fi
source ~/.bashrc
SCRIPT

# Script to configure Jupyter notebook for external access
$jupyter_config = <<SCRIPT
rm /home/vagrant/.jupyter/jupyter_notebook_config.py
/home/vagrant/miniconda3/bin/jupyter notebook --generate-config
echo "
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.password = ''
c.NotebookApp.token = ''
" >> /home/vagrant/.jupyter/jupyter_notebook_config.py
SCRIPT

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.box = "ubuntu/trusty64"

    # Display the VirtualBox GUI when booting the machine
    config.vm.provider "virtualbox" do |vb|
        vb.gui = true
        vb.name = "teachingbox"
    end

    config.vm.provider "virtualbox" do |v|
        v.memory = 2048
        v.cpus = 2
    end

    config.vm.hostname = "vagrant-VM"
    # Forward jupyter port
    config.vm.network "forwarded_port", guest: 8888, host: 8889

    # Install lubuntu desktop and virtualbox additions
    config.vm.provision "shell", inline: "sudo apt-get update"
    config.vm.provision "shell", inline: "sudo apt-get install -y --no-install-recommends lubuntu-desktop virtualbox-guest-dkms virtualbox-guest-utils virtualbox-guest-x11"
    # Allow anyone to start the GUI
    config.vm.provision "shell", inline: "sudo sed -i 's/allowed_users=.*$/allowed_users=anybody/' /etc/X11/Xwrapper.config"
    # Run GUI from the start
    config.vm.provision "shell", inline: "echo '[[ -z $DISPLAY && $XDG_VTNR -eq 1 ]] && exec startx' > /home/vagrant/.bash_profile"

    # Conda installation, with necessary packages
    config.vm.provision "shell", inline: $conda_installation, privileged: false

    # Install other required conda packages
    config.vm.provision "shell", inline: "/home/vagrant/miniconda3/bin/conda install --yes --file '/vagrant/environment.yml'", privileged: false

    # Install pip packages (not available in conda)
    #config.vm.provision "shell", inline: "/home/vagrant/anaconda3/bin/pip install keras", privileged: false

    # Configure Jupyter notebook
    config.vm.provision "shell", inline: $jupyter_config, privileged: false
end
