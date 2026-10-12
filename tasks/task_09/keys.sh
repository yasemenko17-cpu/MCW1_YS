#!/usr/bin/env bash

# Створення каталогу .ssh з правильними правами
mkdir -p ~/.ssh
chmod 700 ~/.ssh

# Генерація ключа ed25519 без пароля
ssh-keygen -t ed25519 -N "" -C "bastion@lab" -f ~/.ssh/id_ed25519
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub

# Створення authorized_keys із захисними опціями
PUBKEY=$(cat ~/.ssh/id_ed25519.pub)
echo "from=\"203.0.113.0/24\",no-port-forwarding,no-X11-forwarding $PUBKEY" > ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys