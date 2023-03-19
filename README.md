## Installation for my laptop

tbd

## Procedure

```bash
pip3 install -r requirements.txt

git clone https://github.com/gpanders/editorconfig.nvim ~/.config/nvim/pack/gpanders/start/editorconfig.nvim

sudo apt -yq install mlocate curl git neovim net-tools at atd ncdu whois nmap unzip fzf direnv
```

```bash
git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.11.2

for app in exa bat cilium-cli cilium-hubble eksctl helm istioctl kind k3d krew kubectl packer pulumi terraform velero docker-compose-v1 glab github-cli jq sops rclone trivy yq; do
    asdf plugin add $app
    asdf install $app latest
    asdf global $app latest
done

asdf reshim
```

```bash
curl https://www.virtualbox.org/download/oracle_vbox_2016.asc | gpg --dearmor > oracle_vbox_2016.gpg
curl https://www.virtualbox.org/download/oracle_vbox.asc | gpg --dearmor > oracle_vbox.gpg
sudo install -o root -g root -m 644 oracle_vbox_2016.gpg /etc/apt/trusted.gpg.d/
sudo install -o root -g root -m 644 oracle_vbox.gpg /etc/apt/trusted.gpg.d/

echo "deb [arch=amd64] http://download.virtualbox.org/virtualbox/debian $(lsb_release -sc) contrib" | sudo tee /etc/apt/sources.list.d/virtualbox.list

sudo apt update
sudo apt install -y linux-headers-$(uname -r) dkms
sudo apt install virtualbox-7.0 -y
```

```bash
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
```
