#!/bin/bash

set -e

echo "Cloning the repository..."
git clone https://github.com/elizaos/eliza.git
cd eliza || exit

echo "Checking out the latest release..."
git checkout "$(git describe --tags --abbrev=0)" || git checkout "$(git describe --tags "$(git rev-list --tags --max-count=1)")"

echo "Copying environment configuration..."
cp .env.example .env

echo "Installing dependencies..."
pnpm install

echo "Building the project..."
pnpm build

echo "Installation complete!"
