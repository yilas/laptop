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
