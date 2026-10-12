#!/usr/bin/env bash

# Скидання налаштувань фаєрвола за замовчуванням
ufw --force reset

# Політика за замовчуванням: вхідні заборонити, вихідні дозволити
ufw default deny incoming
ufw default allow outgoing

# HTTPS (443/tcp): заборонити конкретну адресу, для інших — дозволити
ufw deny from 198.51.100.77 to any port 443 proto tcp
ufw allow 443/tcp

# SSH (22/tcp): дозволено лише з офісної підмережі 192.0.2.0/24
ufw allow from 192.0.2.0/24 to any port 22 proto tcp

# PostgreSQL (5432/tcp): дозволено лише з підмережі застосунків 10.20.0.0/16
ufw allow from 10.20.0.0/16 to any port 5432 proto tcp

# Увімкнення UFW без підтвердження
ufw --force enable