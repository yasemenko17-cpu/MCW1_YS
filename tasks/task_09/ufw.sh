#!/usr/bin/env bash

ufw --force reset
ufw default deny incoming
ufw default allow outgoing

# Повне блокування небезпечної адреси
ufw deny from 203.0.113.66

# Дозвіл порту 2200 лише з підмережі 203.0.113.0/24 з обмеженням частоти спроб
ufw limit from 203.0.113.0/24 to any port 2200 proto tcp

ufw --force enable