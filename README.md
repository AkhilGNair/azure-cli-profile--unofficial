# Azure CLI profiles module

An unofficial Azure CLI module which just installs the `profile` commands on top of `azure-cli-core`
and adds a simple entrypoint to the program.

This is useful if you want access to `az login`, without having to install all the subpackages.

The command can be accessed via `azq`.
Or by symlinking `azq` to `az`, if you don't plan to install `azure-cli` at all for your need.

For production builds, I recommend the official package.
